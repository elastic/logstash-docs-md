---
navigation_title: "v10.8.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v10.8.2-plugins-outputs-elasticsearch.html
---

# Elasticsearch output plugin v10.8.2 [v10.8.2-plugins-outputs-elasticsearch]


* Plugin version: v10.8.2
* Released on: 2021-01-19
* [Changelog](https://github.com/logstash-plugins/logstash-output-elasticsearch/blob/v10.8.2/CHANGELOG.md)

For other versions, see the [overview list](output-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1156]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1149]

If you plan to use the Kibana web interface to analyze data transformed by Logstash, use the Elasticsearch output plugin to get your data into Elasticsearch.

This output only speaks the HTTP protocol as it is the preferred protocol for interacting with Elasticsearch. In previous versions it was possible to communicate with Elasticsearch through the transport protocol, which is now reserved for internal cluster communication between nodes [communication between nodes](elasticsearch://reference/elasticsearch/configuration-reference/networking-settings.md). Using the transport protocol to communicate with the cluster has been deprecated in Elasticsearch 7.0.0 and will be removed in 8.0.0

You can [learn more about Elasticsearch](https://www.elastic.co/elasticsearch/) on the website landing page or in the [Elasticsearch documentation](docs-content://get-started/index.md).

::::{admonition} Compatibility Note
:class: note

When connected to Elasticsearch 7.x, modern versions of this plugin use the required `_doc` document-type when inserting documents.

If you are using an earlier version of Logstash and wish to connect to Elasticsearch 7.x, first upgrade Logstash to version 6.8 to ensure it picks up changes to the Elasticsearch index template.

If you are using a custom [`template`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template), ensure your template uses the `_doc` document-type before connecting to Elasticsearch 7.x.

::::


### Hosted {{es}} Service on Elastic Cloud [_hosted_es_service_on_elastic_cloud_59]

{{ess-leadin}}



## Compatibility with the Elastic Common Schema (ECS) [_compatibility_with_the_elastic_common_schema_ecs_73]

This plugin will persist events to Elasticsearch in the shape produced by your pipeline, and *cannot* be used to re-shape the event structure into a shape that complies with ECS. To produce events that fully comply with ECS, you will need to populate ECS-defined fields throughout your pipeline definition.

However, the Elasticsearch Index Templates it manages can be configured to be ECS-compatible by setting [`ecs_compatibility`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility). By having an ECS-compatible template in place, we can ensure that Elasticsearch is prepared to create and index fields in a way that is compatible with ECS, and will correctly reject events with fields that conflict and cannot be coerced.


## Writing to different indices: best practices [_writing_to_different_indices_best_practices_73]

::::{note}
You cannot use dynamic variable substitution when `ilm_enabled` is `true` and when using `ilm_rollover_alias`.

::::


If you’re sending events to the same Elasticsearch cluster, but you’re targeting different indices you can:

* use different Elasticsearch outputs, each one with a different value for the `index` parameter
* use one Elasticsearch output and use the dynamic variable substitution for the `index` parameter

Each Elasticsearch output is a new client connected to the cluster:

* it has to initialize the client and connect to Elasticsearch (restart time is longer if you have more clients)
* it has an associated connection pool

In order to minimize the number of open connections to Elasticsearch, maximize the bulk size and reduce the number of "small" bulk requests (which could easily fill up the queue), it is usually more efficient to have a single Elasticsearch output.

Example:

```ruby
    output {
      elasticsearch {
        index => "%{[some_field][sub_field]}-%{+YYYY.MM.dd}"
      }
    }
```

**What to do in case there is no field in the event containing the destination index prefix?**

You can use the `mutate` filter and conditionals to add a [`[@metadata](logstash://reference/event-dependent-configuration.md#metadata)` field] to set the destination index for each event. The `[@metadata]` fields will not be sent to Elasticsearch.

Example:

```ruby
    filter {
      if [log_type] in [ "test", "staging" ] {
        mutate { add_field => { "[@metadata][target_index]" => "test-%{+YYYY.MM}" } }
      } else if [log_type] == "production" {
        mutate { add_field => { "[@metadata][target_index]" => "prod-%{+YYYY.MM.dd}" } }
      } else {
        mutate { add_field => { "[@metadata][target_index]" => "unknown-%{+YYYY}" } }
      }
    }
    output {
      elasticsearch {
        index => "%{[@metadata][target_index]}"
      }
    }
```


## Retry Policy [_retry_policy_73]

The retry policy has changed significantly in the 8.1.1 release. This plugin uses the Elasticsearch bulk API to optimize its imports into Elasticsearch. These requests may experience either partial or total failures. The bulk API sends batches of requests to an HTTP endpoint. Error codes for the HTTP request are handled differently than error codes for individual documents.

HTTP requests to the bulk API are expected to return a 200 response code. All other response codes are retried indefinitely.

The following document errors are handled as follows:

* 400 and 404 errors are sent to the dead letter queue (DLQ), if enabled. If a DLQ is not enabled, a log message will be emitted, and the event will be dropped. See [DLQ Policy](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-dlq-policy) for more info.
* 409 errors (conflict) are logged as a warning and dropped.

Note that 409 exceptions are no longer retried. Please set a higher `retry_on_conflict` value if you experience 409 exceptions. It is more performant for Elasticsearch to retry these exceptions than this plugin.


## DLQ Policy [v10.8.2-plugins-outputs-elasticsearch-dlq-policy]

Mapping (404) errors from Elasticsearch can lead to data loss. Unfortunately mapping errors cannot be handled without human intervention and without looking at the field that caused the mapping mismatch. If the DLQ is enabled, the original events causing the mapping errors are stored in a file that can be processed at a later time. Often times, the offending field can be removed and re-indexed to Elasticsearch. If the DLQ is not enabled, and a mapping error happens, the problem is logged as a warning, and the event is dropped. See [dead-letter-queues](logstash://reference/dead-letter-queues.md) for more information about processing events in the DLQ.


## Index Lifecycle Management [v10.8.2-plugins-outputs-elasticsearch-ilm]

::::{note}
The Index Lifecycle Management feature requires plugin version `9.3.1` or higher.
::::


::::{note}
This feature requires an Elasticsearch instance of 6.6.0 or higher with at least a Basic license
::::


Logstash can use [Index Lifecycle Management](docs-content://manage-data/lifecycle/index-lifecycle-management.md) to automate the management of indices over time.

The use of Index Lifecycle Management is controlled by the `ilm_enabled` setting. By default, this setting detects whether the Elasticsearch instance supports ILM, and uses it if it is available. `ilm_enabled` can also be set to `true` or `false` to override the automatic detection, or disable ILM.

This will overwrite the index settings and adjust the Logstash template to write the necessary settings for the template to support index lifecycle management, including the index policy and rollover alias to be used.

Logstash will create a rollover alias for the indices to be written to, including a pattern for how the actual indices will be named, and unless an ILM policy that already exists has been specified, a default policy will also be created. The default policy is configured to rollover an index when it reaches either 50 gigabytes in size, or is 30 days old, whichever happens first.

The default rollover alias is called `logstash`, with a default pattern for the rollover index of `{now/d}-00001`, which will name indices on the date that the index is rolled over, followed by an incrementing number. Note that the pattern must end with a dash and a number that will be incremented.

See the [Rollover API documentation](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover) for more details on naming.

The rollover alias, ilm pattern and policy can be modified.

See config below for an example:

```ruby
    output {
      elasticsearch {
        ilm_rollover_alias => "custom"
        ilm_pattern => "000001"
        ilm_policy => "custom_policy"
      }
    }
```

::::{note}
Custom ILM policies must already exist on the Elasticsearch cluster before they can be used.
::::


::::{note}
If the rollover alias or pattern is modified, the index template will need to be overwritten as the settings `index.lifecycle.name` and `index.lifecycle.rollover_alias` are automatically written to the template
::::


::::{note}
If the index property is supplied in the output definition, it will be overwritten by the rollover alias.
::::



## Batch Sizes [_batch_sizes_73]

This plugin attempts to send batches of events to the [{{es}} Bulk API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk) as a single request. However, if a batch exceeds 20MB we break it up into multiple bulk requests. If a single document exceeds 20MB it is sent as a single request.


## DNS Caching [_dns_caching_73]

This plugin uses the JVM to lookup DNS entries and is subject to the value of [networkaddress.cache.ttl](https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html), a global setting for the JVM.

As an example, to set your DNS TTL to 1 second you would set the `LS_JAVA_OPTS` environment variable to `-Dnetworkaddress.cache.ttl=1`.

Keep in mind that a connection with keepalive enabled will not reevaluate its DNS value while the keepalive is in effect.


## HTTP Compression [_http_compression_73]

This plugin supports request and response compression. Response compression is enabled by default for HTTP and for Elasticsearch versions 5.0 and later.

You don’t have to set any configs in Elasticsearch for it to send back a compressed response. For versions before 5.0, or if HTTPS is enabled, `http.compression` must be set to `true` [in Elasticsearch](elasticsearch://reference/elasticsearch/configuration-reference/networking-settings.md) to take advantage of response compression when using this plugin.

For requests compression, regardless of the Elasticsearch version, enable the `http_compression` setting in the Logstash config file.


## Authentication [_authentication_84]

Authentication to a secure Elasticsearch cluster is possible using one of the `user`/`password`, `cloud_auth` or `api_key` options.


## Authorization [v10.8.2-plugins-outputs-elasticsearch-autz]

Authorization to a secure Elasticsearch cluster requires `read` permission at index level and `monitoring` permissions at cluster level. The `monitoring` permission at cluster level is necessary to perform periodic connectivity checks.


## Elasticsearch Output Configuration Options [v10.8.2-plugins-outputs-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`action`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-action) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`api_key`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`bulk_path`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-bulk_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`cacert`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-cacert) | a valid filesystem path | No |
| [`cloud_auth`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-cloud_auth) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`cloud_id`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-cloud_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`custom_headers`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-custom_headers) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`doc_as_upsert`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-doc_as_upsert) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`document_id`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-document_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`document_type`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-document_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ecs_compatibility`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`failure_type_logging_whitelist`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-failure_type_logging_whitelist) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`healthcheck_path`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-healthcheck_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`hosts`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-hosts) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`http_compression`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-http_compression) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ilm_enabled`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ilm_enabled) | [string](logstash://reference/configuration-file-structure.md#string), one of `["true", "false", "auto"]` | No |
| [`ilm_pattern`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ilm_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ilm_policy`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ilm_policy) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ilm_rollover_alias`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ilm_rollover_alias) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`index`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-index) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`keystore`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-keystore) | a valid filesystem path | No |
| [`keystore_password`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`manage_template`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-manage_template) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`parameters`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-parameters) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`parent`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-parent) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`path`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pipeline`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-pipeline) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pool_max`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-pool_max) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`pool_max_per_route`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-pool_max_per_route) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`proxy`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-proxy) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`resurrect_delay`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-resurrect_delay) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_initial_interval`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-retry_initial_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_max_interval`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-retry_max_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_on_conflict`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-retry_on_conflict) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`routing`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-routing) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-script) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script_lang`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-script_lang) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script_type`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-script_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["inline", "indexed", "file"]` | No |
| [`script_var_name`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-script_var_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`scripted_upsert`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-scripted_upsert) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`sniffing`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-sniffing) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`sniffing_delay`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-sniffing_delay) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`sniffing_path`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-sniffing_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate_verification`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ssl_certificate_verification) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`template`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template) | a valid filesystem path | No |
| [`template_name`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`template_overwrite`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template_overwrite) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`timeout`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`truststore`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-truststore) | a valid filesystem path | No |
| [`truststore_password`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`upsert`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-upsert) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`user`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`validate_after_inactivity`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-validate_after_inactivity) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`version`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version_type`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-version_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["internal", "external", "external_gt", "external_gte", "force"]` | No |

Also see [Common options](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-common-options) for a list of options supported by all output plugins.

 

### `action` [v10.8.2-plugins-outputs-elasticsearch-action]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"index"`

Protocol agnostic (i.e. non-http, non-java specific) configs go here Protocol agnostic methods The Elasticsearch action to perform. Valid actions are:

* index: indexes a document (an event from Logstash).
* delete: deletes a document by id (An id is required for this action)
* create: indexes a document, fails if a document by that id already exists in the index.
* update: updates a document by id. Update has a special case where you can upsert — update a document if not already present. See the `doc_as_upsert` option. NOTE: This does not work and is not supported in Elasticsearch 1.x. Please upgrade to ES 2.x or greater to use this feature with Logstash!
* A sprintf style string to change the action based on the content of the event. The value `%{[foo]}` would use the foo field for the action

For more details on actions, check out the [Elasticsearch bulk API documentation](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk).


### `api_key` [v10.8.2-plugins-outputs-elasticsearch-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Authenticate using Elasticsearch API key. Note that this option also requires enabling the `ssl` option.

Format is `id:api_key` where `id` and `api_key` are as returned by the Elasticsearch [Create API key API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key).


### `bulk_path` [v10.8.2-plugins-outputs-elasticsearch-bulk_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

HTTP Path to perform the _bulk requests to this defaults to a concatenation of the path parameter and "_bulk"


### `cacert` [v10.8.2-plugins-outputs-elasticsearch-cacert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The .cer or .pem file to validate the server’s certificate.


### `cloud_auth` [v10.8.2-plugins-outputs-elasticsearch-cloud_auth]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Cloud authentication string ("<username>:<password>" format) is an alternative for the `user`/`password` pair.

For more details, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `cloud_id` [v10.8.2-plugins-outputs-elasticsearch-cloud_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Cloud ID, from the Elastic Cloud web console. If set `hosts` should not be used.

For more details, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `doc_as_upsert` [v10.8.2-plugins-outputs-elasticsearch-doc_as_upsert]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable `doc_as_upsert` for update mode. Create a new document with source if `document_id` doesn’t exist in Elasticsearch.


### `document_id` [v10.8.2-plugins-outputs-elasticsearch-document_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The document ID for the index. Useful for overwriting existing entries in Elasticsearch with the same ID.


### `document_type` [v10.8.2-plugins-outputs-elasticsearch-document_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.
* This option is deprecated

::::{note}
This option is deprecated due to the [removal of types in Elasticsearch 6.0](https://www.elastic.co/guide/en/elasticsearch/reference/6.0/removal-of-types.html). It will be removed in the next major version of Logstash.
::::


::::{note}
This value is ignored and has no effect for Elasticsearch clusters `8.x`.
::::


This sets the document type to write events to. Generally you should try to write only similar events to the same *type*. String expansion `%{{foo}}` works here. If you don’t set a value for this option:

* for elasticsearch clusters 8.x: no value will be used;
* for elasticsearch clusters 7.x: the value of *_doc* will be used;
* for elasticsearch clusters 6.x: the value of *doc* will be used;
* for elasticsearch clusters 5.x and below: the event’s *type* field will be used, if the field is not present the value of *doc* will be used.


### `ecs_compatibility` [v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: does not provide ECS-compatible templates
    * `v1`: provides defaults that are compatible with v1 of the Elastic Common Schema

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`.


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)), including the installation of ECS-compatible index templates. The value of this setting affects the *default* values of:

* [`index`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-index)
* [`template_name`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template_name)
* [`ilm_rollover_alias`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ilm_rollover_alias)


### `failure_type_logging_whitelist` [v10.8.2-plugins-outputs-elasticsearch-failure_type_logging_whitelist]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Set the Elasticsearch errors in the whitelist that you don’t want to log. A useful example is when you want to skip all 409 errors which are `document_already_exists_exception`.


### `custom_headers` [v10.8.2-plugins-outputs-elasticsearch-custom_headers]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Pass a set of key value pairs as the headers sent in each request to an elasticsearch node. The headers will be used for any kind of request (_bulk request, template installation, health checks and sniffing). These custom headers will be overidden by settings like `http_compression`.


### `healthcheck_path` [v10.8.2-plugins-outputs-elasticsearch-healthcheck_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

HTTP Path where a HEAD request is sent when a backend is marked down the request is sent in the background to see if it has come back again before it is once again eligible to service requests. If you have custom firewall rules you may need to change this


### `hosts` [v10.8.2-plugins-outputs-elasticsearch-hosts]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* Default value is `[//127.0.0.1]`

Sets the host(s) of the remote instance. If given an array it will load balance requests across the hosts specified in the `hosts` parameter. Remember the `http` protocol uses the [http](elasticsearch://reference/elasticsearch/configuration-reference/networking-settings.md) address (eg. 9200, not 9300).

Examples:

```
`"127.0.0.1"`
`["127.0.0.1:9200","127.0.0.2:9200"]`
`["http://127.0.0.1"]`
`["https://127.0.0.1:9200"]`
`["https://127.0.0.1:9200/mypath"]` (If using a proxy on a subpath)
```
Exclude [dedicated master nodes](elasticsearch://reference/elasticsearch/configuration-reference/node-settings.md) from the `hosts` list to prevent Logstash from sending bulk requests to the master nodes. This parameter should reference only data or client nodes in Elasticsearch.

Any special characters present in the URLs here MUST be URL escaped! This means `#` should be put in as `%23` for instance.


### `http_compression` [v10.8.2-plugins-outputs-elasticsearch-http_compression]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable gzip compression on requests. Note that response compression is on by default for Elasticsearch v5.0 and beyond


### `ilm_enabled` [v10.8.2-plugins-outputs-elasticsearch-ilm_enabled]

* Value can be any of: `true`, `false`, `auto`
* Default value is `auto`

The default setting of `auto` will automatically enable [Index Lifecycle Management](docs-content://manage-data/lifecycle/index-lifecycle-management.md), if the Elasticsearch cluster is running Elasticsearch version `7.0.0` or higher with the ILM feature enabled, and disable it otherwise.

Setting this flag to `false` will disable the Index Lifecycle Management feature, even if the Elasticsearch cluster supports ILM. Setting this flag to `true` will enable Index Lifecycle Management feature, if the Elasticsearch cluster supports it. This is required to enable Index Lifecycle Management on a version of Elasticsearch earlier than version `7.0.0`.

::::{note}
This feature requires a Basic License or above to be installed on an Elasticsearch cluster version 6.6.0 or later.
::::



### `ilm_pattern` [v10.8.2-plugins-outputs-elasticsearch-ilm_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `{now/d}-000001`

Pattern used for generating indices managed by [Index Lifecycle Management](docs-content://manage-data/lifecycle/index-lifecycle-management.md). The value specified in the pattern will be appended to the write alias, and incremented automatically when a new index is created by ILM.

Date Math can be used when specifying an ilm pattern, see [Rollover API docs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover) for details.

::::{note}
Updating the pattern will require the index template to be rewritten.
::::


::::{note}
The pattern must finish with a dash and a number that will be automatically incremented when indices rollover.
::::


::::{note}
The pattern is a 6-digit string padded by zeros, regardless of prior index name. Example: 000001. See [Rollover path parameters API docs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover) for details.
::::



### `ilm_policy` [v10.8.2-plugins-outputs-elasticsearch-ilm_policy]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `logstash-policy`

Modify this setting to use a custom Index Lifecycle Management policy, rather than the default. If this value is not set, the default policy will be automatically installed into Elasticsearch

::::{note}
If this setting is specified, the policy must already exist in Elasticsearch cluster.
::::



### `ilm_rollover_alias` [v10.8.2-plugins-outputs-elasticsearch-ilm_rollover_alias]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: `logstash`
    * ECS Compatibility enabled: `ecs-logstash`


The rollover alias is the alias where indices managed using Index Lifecycle Management will be written to.

::::{note}
If both `index` and `ilm_rollover_alias` are specified, `ilm_rollover_alias` takes precedence.
::::


::::{note}
Updating the rollover alias will require the index template to be rewritten.
::::


::::{note}
`ilm_rollover_alias` does NOT support dynamic variable substitution as `index` does.
::::



### `index` [v10.8.2-plugins-outputs-elasticsearch-index]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: `"logstash-%{+yyyy.MM.dd}"`
    * ECS Compatibility enabled: `"ecs-logstash-%{+yyyy.MM.dd}"`


The index to write events to. This can be dynamic using the `%{{foo}}` syntax. The default value will partition your indices by day so you can more easily delete old data or only search specific date ranges. Indexes may not contain uppercase characters. For weekly indexes ISO 8601 format is recommended, eg. logstash-%{+xxxx.ww}. Logstash uses [Joda formats](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html) for the index pattern from event timestamp.


### `keystore` [v10.8.2-plugins-outputs-elasticsearch-keystore]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The keystore used to present a certificate to the server. It can be either .jks or .p12


### `keystore_password` [v10.8.2-plugins-outputs-elasticsearch-keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the keystore password


### `manage_template` [v10.8.2-plugins-outputs-elasticsearch-manage_template]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

From Logstash 1.3 onwards, a template is applied to Elasticsearch during Logstash’s startup if one with the name [`template_name`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-template_name) does not already exist. By default, the contents of this template is the default template for `logstash-%{+YYYY.MM.dd}` which always matches indices based on the pattern `logstash-*`.  Should you require support for other index names, or would like to change the mappings in the template in general, a custom template can be specified by setting `template` to the path of a template file.

Setting `manage_template` to false disables this feature.  If you require more control over template creation, (e.g. creating indices dynamically based on field names) you should set `manage_template` to false and use the REST API to apply your templates manually.


### `parameters` [v10.8.2-plugins-outputs-elasticsearch-parameters]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Pass a set of key value pairs as the URL query string. This query string is added to every host listed in the *hosts* configuration. If the *hosts* list contains urls that already have query strings, the one specified here will be appended.


### `parent` [v10.8.2-plugins-outputs-elasticsearch-parent]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

For child documents, ID of the associated parent. This can be dynamic using the `%{{foo}}` syntax.


### `password` [v10.8.2-plugins-outputs-elasticsearch-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password to authenticate to a secure Elasticsearch cluster


### `path` [v10.8.2-plugins-outputs-elasticsearch-path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

HTTP Path at which the Elasticsearch server lives. Use this if you must run Elasticsearch behind a proxy that remaps the root path for the Elasticsearch HTTP API lives. Note that if you use paths as components of URLs in the *hosts* field you may not also set this field. That will raise an error at startup


### `pipeline` [v10.8.2-plugins-outputs-elasticsearch-pipeline]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Set which ingest pipeline you wish to execute for an event. You can also use event dependent configuration here like `pipeline => "%{[@metadata][pipeline]}"`. The pipeline parameter won’t be set if the value resolves to empty string ("").


### `pool_max` [v10.8.2-plugins-outputs-elasticsearch-pool_max]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

While the output tries to reuse connections efficiently we have a maximum. This sets the maximum number of open connections the output will create. Setting this too low may mean frequently closing / opening connections which is bad.


### `pool_max_per_route` [v10.8.2-plugins-outputs-elasticsearch-pool_max_per_route]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100`

While the output tries to reuse connections efficiently we have a maximum per endpoint. This sets the maximum number of open connections per endpoint the output will create. Setting this too low may mean frequently closing / opening connections which is bad.


### `proxy` [v10.8.2-plugins-outputs-elasticsearch-proxy]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. This setting accepts only URI arguments to prevent leaking credentials. An empty string is treated as if proxy was not set. This is useful when using environment variables e.g. `proxy => '${LS_PROXY:}'`.


### `resurrect_delay` [v10.8.2-plugins-outputs-elasticsearch-resurrect_delay]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

How frequently, in seconds, to wait between resurrection attempts. Resurrection is the process by which backend endpoints marked *down* are checked to see if they have come back to life


### `retry_initial_interval` [v10.8.2-plugins-outputs-elasticsearch-retry_initial_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Set initial interval in seconds between bulk retries. Doubled on each retry up to `retry_max_interval`


### `retry_max_interval` [v10.8.2-plugins-outputs-elasticsearch-retry_max_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `64`

Set max interval in seconds between bulk retries.


### `retry_on_conflict` [v10.8.2-plugins-outputs-elasticsearch-retry_on_conflict]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

The number of times Elasticsearch should internally retry an update/upserted document.


### `routing` [v10.8.2-plugins-outputs-elasticsearch-routing]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A routing override to be applied to all processed events. This can be dynamic using the `%{{foo}}` syntax.


### `script` [v10.8.2-plugins-outputs-elasticsearch-script]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Set script name for scripted update mode

Example:

```ruby
    output {
      elasticsearch {
        script => "ctx._source.message = params.event.get('message')"
      }
    }
```


### `script_lang` [v10.8.2-plugins-outputs-elasticsearch-script_lang]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"painless"`

Set the language of the used script. When using indexed (stored) scripts on Elasticsearch 6.0 and higher, you must set this parameter to `""` (empty string).


### `script_type` [v10.8.2-plugins-outputs-elasticsearch-script_type]

* Value can be any of: `inline`, `indexed`, `file`
* Default value is `["inline"]`

Define the type of script referenced by "script" variable inline : "script" contains inline script indexed : "script" contains the name of script directly indexed in elasticsearch file    : "script" contains the name of script stored in elasticsearch’s config directory


### `script_var_name` [v10.8.2-plugins-outputs-elasticsearch-script_var_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"event"`

Set variable name passed to script (scripted update)


### `scripted_upsert` [v10.8.2-plugins-outputs-elasticsearch-scripted_upsert]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

if enabled, script is in charge of creating non-existent document (scripted update)


### `sniffing` [v10.8.2-plugins-outputs-elasticsearch-sniffing]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

This setting asks Elasticsearch for the list of all cluster nodes and adds them to the hosts list. For Elasticsearch 5.x and 6.x any nodes with `http.enabled` (on by default) will be added to the hosts list, excluding master-only nodes.


### `sniffing_delay` [v10.8.2-plugins-outputs-elasticsearch-sniffing_delay]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

How long to wait, in seconds, between sniffing attempts


### `sniffing_path` [v10.8.2-plugins-outputs-elasticsearch-sniffing_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

HTTP Path to be used for the sniffing requests the default value is computed by concatenating the path value and "_nodes/http" if sniffing_path is set it will be used as an absolute path do not use full URL here, only paths, e.g. "/sniff/_nodes/http"


### `ssl` [v10.8.2-plugins-outputs-elasticsearch-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Enable SSL/TLS secured communication to Elasticsearch cluster. Leaving this unspecified will use whatever scheme is specified in the URLs listed in *hosts*. If no explicit protocol is specified plain HTTP will be used. If SSL is explicitly disabled here the plugin will refuse to start if an HTTPS URL is given in *hosts*


### `ssl_certificate_verification` [v10.8.2-plugins-outputs-elasticsearch-ssl_certificate_verification]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Option to validate the server’s certificate. Disabling this severely compromises security. For more information on disabling certificate verification please read [https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf)


### `template` [v10.8.2-plugins-outputs-elasticsearch-template]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

You can set the path to your own template here, if you so desire. If not set, the included template will be used.


### `template_name` [v10.8.2-plugins-outputs-elasticsearch-template_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: `logstash`
    * ECS Compatibility enabled: `ecs-logstash`


This configuration option defines how the template is named inside Elasticsearch. Note that if you have used the template management features and subsequently change this, you will need to prune the old template manually, e.g.

`curl -XDELETE <http://localhost:9200/_template/OldTemplateName?pretty>`

where `OldTemplateName` is whatever the former setting was.


### `template_overwrite` [v10.8.2-plugins-outputs-elasticsearch-template_overwrite]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

The template_overwrite option will always overwrite the indicated template in Elasticsearch with either the one indicated by template or the included one. This option is set to false by default. If you always want to stay up to date with the template provided by Logstash, this option could be very useful to you. Likewise, if you have your own template file managed by puppet, for example, and you wanted to be able to update it regularly, this option could help there as well.

Please note that if you are using your own customized version of the Logstash template (logstash), setting this to true will make Logstash to overwrite the "logstash" template (i.e. removing all customized settings)


### `timeout` [v10.8.2-plugins-outputs-elasticsearch-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Set the timeout, in seconds, for network operations and requests sent Elasticsearch. If a timeout occurs, the request will be retried.


### `truststore` [v10.8.2-plugins-outputs-elasticsearch-truststore]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either .jks or .p12. Use either `:truststore` or `:cacert`.


### `truststore_password` [v10.8.2-plugins-outputs-elasticsearch-truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the truststore password


### `upsert` [v10.8.2-plugins-outputs-elasticsearch-upsert]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Set upsert content for update mode. Create a new document with this parameter as json string if `document_id` doesn’t exists


### `user` [v10.8.2-plugins-outputs-elasticsearch-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username to authenticate to a secure Elasticsearch cluster


### `validate_after_inactivity` [v10.8.2-plugins-outputs-elasticsearch-validate_after_inactivity]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

How long to wait before checking for a stale connection to determine if a keepalive request is needed. Consider setting this value lower than the default, possibly to 0, if you get connection errors regularly.

This client is based on Apache Commons. Here’s how the [Apache Commons documentation](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity(int)) describes this option: "Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool."


### `version` [v10.8.2-plugins-outputs-elasticsearch-version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The version to use for indexing. Use sprintf syntax like `%{{my_version}}` to use a field value here. See the [versioning support blog](https://www.elastic.co/blog/elasticsearch-versioning-support) for more information.


### `version_type` [v10.8.2-plugins-outputs-elasticsearch-version_type]

* Value can be any of: `internal`, `external`, `external_gt`, `external_gte`, `force`
* There is no default value for this setting.

The version_type to use for indexing. See the [versioning support blog](https://www.elastic.co/blog/elasticsearch-versioning-support) and [Version types](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-create) in the Elasticsearch documentation.



## Common options [v10.8.2-plugins-outputs-elasticsearch-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`enable_metric`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v10-8-2-plugins-outputs-elasticsearch.md#v10.8.2-plugins-outputs-elasticsearch-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `enable_metric` [v10.8.2-plugins-outputs-elasticsearch-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v10.8.2-plugins-outputs-elasticsearch-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elasticsearch outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  elasticsearch {
    id => "my_plugin_id"
  }
}
```
