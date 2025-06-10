---
navigation_title: "v10.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v10.1.0-plugins-outputs-elasticsearch.html
---

# Elasticsearch output plugin v10.1.0 [v10.1.0-plugins-outputs-elasticsearch]

* Plugin version: v10.1.0
* Released on: 2019-05-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-elasticsearch/blob/v10.1.0/CHANGELOG.md)

For other versions, see the [overview list](output-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1215]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1208]

Compatibility Note

Starting with Elasticsearch 5.3, there’s an [HTTP setting](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html) called `http.content_type.required`. If this option is set to `true`, and you are using Logstash 2.4 through 5.2, you need to update the Elasticsearch output plugin to version 6.2.5 or higher.

If you plan to use the Kibana web interface, use the Elasticsearch output plugin to get your log data into Elasticsearch.

You can run Elasticsearch on your own hardware, or use our [hosted Elasticsearch Service](https://www.elastic.co/cloud/elasticsearch-service) on Elastic Cloud. The Elasticsearch Service is available on both AWS and GCP. [Try the Elasticsearch Service for free](https://www.elastic.co/cloud/elasticsearch-service/signup).

This output only speaks the HTTP protocol. HTTP is the preferred protocol for interacting with Elasticsearch as of Logstash 2.0. We strongly encourage the use of HTTP over the node protocol for a number of reasons. HTTP is only marginally slower, yet far easier to administer and work with. When using the HTTP protocol one may upgrade Elasticsearch versions without having to upgrade Logstash in lock-step.

You can learn more about Elasticsearch at <https://www.elastic.co/products/elasticsearch>

## Template management for Elasticsearch 5.x [_template_management_for_elasticsearch_5_x_13]

Index template for this version (Logstash 5.0) has been changed to reflect Elasticsearch’s mapping changes in version 5.0. Most importantly, the subfield for string multi-fields has changed from `.raw` to `.keyword` to match ES default behavior.

**Users installing ES 5.x and LS 5.x**

This change will not affect you and you will continue to use the ES defaults.

**Users upgrading from LS 2.x to LS 5.x with ES 5.x**

LS will not force upgrade the template, if `logstash` template already exists. This means you will still use `.raw` for sub-fields coming from 2.x. If you choose to use the new template, you will have to reindex your data after the new template is installed.

## Retry Policy [_retry_policy_95]

The retry policy has changed significantly in the 8.1.1 release. This plugin uses the Elasticsearch bulk API to optimize its imports into Elasticsearch. These requests may experience either partial or total failures. The bulk API sends batches of requests to an HTTP endpoint. Error codes for the HTTP request are handled differently than error codes for individual documents.

HTTP requests to the bulk API are expected to return a 200 response code. All other response codes are retried indefinitely.

The following document errors are handled as follows:

* 400 and 404 errors are sent to the dead letter queue (DLQ), if enabled. If a DLQ is not enabled, a log message will be emitted, and the event will be dropped. See [DLQ Policy](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-dlq-policy) for more info.
* 409 errors (conflict) are logged as a warning and dropped.

Note that 409 exceptions are no longer retried. Please set a higher `retry_on_conflict` value if you experience 409 exceptions. It is more performant for Elasticsearch to retry these exceptions than this plugin.

## DLQ Policy [v10.1.0-plugins-outputs-elasticsearch-dlq-policy]

Mapping (404) errors from Elasticsearch can lead to data loss. Unfortunately mapping errors cannot be handled without human intervention and without looking at the field that caused the mapping mismatch. If the DLQ is enabled, the original events causing the mapping errors are stored in a file that can be processed at a later time. Often times, the offending field can be removed and re-indexed to Elasticsearch. If the DLQ is not enabled, and a mapping error happens, the problem is logged as a warning, and the event is dropped. See [dead-letter-queues](https://www.elastic.co/guide/en/logstash/current/dead-letter-queues.html) for more information about processing events in the DLQ.

## Index Lifecycle Management [v10.1.0-plugins-outputs-elasticsearch-ilm]

The Index Lifecycle Management feature requires plugin version `9.3.1` or higher.

This feature requires an Elasticsearch instance of 6.6.0 or higher with at least a Basic license

Logstash can use [Index Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html) to automate the management of indices over time.

The use of Index Lifecycle Management is controlled by the `ilm_enabled` setting. By default, this is will automatically detect whether the Elasticsearch instance supports ILM, and will use it if it is available. `ilm_enabled` can also be set to `true` or `false` to override the automatic detection, or disable ILM.

This will overwrite the index settings and adjust the Logstash template to write the necessary settings for the template to support index lifecycle management, including the index policy and rollover alias to be used.

Logstash will create a rollover alias for the indices to be written to, including a pattern for how the actual indices will be named, and unless an ILM policy that already exists has been specified, a default policy will also be created. The default policy is configured to rollover an index when it reaches either 50 gigabytes in size, or is 30 days old, whichever happens first.

The default rollover alias is called `logstash`, with a default pattern for the rollover index of `{now/d}-00001`, which will name indices on the date that the index is rolled over, followed by an incrementing number. Note that the pattern must end with a dash and a number that will be incremented.

See the [Rollover API documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-rollover-index.html#_using_date_math_with_the_rollover_api) for more details on naming.

The rollover alias, ilm pattern and policy can be modified.

See config below for an example:

```
    output {
      elasticsearch {
        ilm_rollover_alias => "custom"
        ilm_pattern => "000001"
        ilm_policy => "custom_policy"
      }
    }
```

Custom ILM policies must already exist on the Elasticsearch cluster before they can be used.

If the rollover alias or pattern is modified, the index template will need to be overwritten as the settings `index.lifecycle.name` and `index.lifecycle.rollover_alias` are automatically written to the template

If the index property is supplied in the output definition, it will be overwritten by the rollover alias.

## Batch Sizes [_batch_sizes_95]

This plugin attempts to send batches of events as a single request. However, if a request exceeds 20MB we will break it up into multiple batch requests. If a single document exceeds 20MB it will be sent as a single request.

## DNS Caching [_dns_caching_95]

This plugin uses the JVM to lookup DNS entries and is subject to the value of [networkaddress.cache.ttl](https://docs.oracle.com/javase/7/docs/technotes/guides/net/properties.html), a global setting for the JVM.

As an example, to set your DNS TTL to 1 second you would set the `LS_JAVA_OPTS` environment variable to `-Dnetworkaddress.cache.ttl=1`.

Keep in mind that a connection with keepalive enabled will not reevaluate its DNS value while the keepalive is in effect.

## HTTP Compression [_http_compression_95]

This plugin supports request and response compression. Response compression is enabled by default and for Elasticsearch versions 5.0 and later, the user doesn’t have to set any configs in Elasticsearch for it to send back compressed response. For versions before 5.0, `http.compression` must be set to `true` [in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html#modules-http) to take advantage of response compression when using this plugin

For requests compression, regardless of the Elasticsearch version, users have to enable `http_compression` setting in their Logstash config file.

## Elasticsearch Output Configuration Options [v10.1.0-plugins-outputs-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`action`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-action) | [string](/lsr/value-types.md#string) | No |
| [`bulk_path`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-bulk_path) | [string](/lsr/value-types.md#string) | No |
| [`cacert`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-cacert) | a valid filesystem path | No |
| [`custom_headers`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-custom_headers) | [hash](/lsr/value-types.md#hash) | No |
| [`doc_as_upsert`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-doc_as_upsert) | [boolean](/lsr/value-types.md#boolean) | No |
| [`document_id`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-document_id) | [string](/lsr/value-types.md#string) | No |
| [`document_type`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-document_type) | [string](/lsr/value-types.md#string) | No |
| [`failure_type_logging_whitelist`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-failure_type_logging_whitelist) | [array](/lsr/value-types.md#array) | No |
| [`healthcheck_path`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-healthcheck_path) | [string](/lsr/value-types.md#string) | No |
| [`hosts`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-hosts) | [uri](/lsr/value-types.md#uri) | No |
| [`http_compression`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-http_compression) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ilm_enabled`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ilm_enabled) | [string](/lsr/value-types.md#string), one of `["true", "false", "auto"]` | No |
| [`ilm_pattern`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ilm_pattern) | [string](/lsr/value-types.md#string) | No |
| [`ilm_policy`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ilm_policy) | [string](/lsr/value-types.md#string) | No |
| [`ilm_rollover_alias`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ilm_rollover_alias) | [string](/lsr/value-types.md#string) | No |
| [`index`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-index) | [string](/lsr/value-types.md#string) | No |
| [`keystore`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-keystore) | a valid filesystem path | No |
| [`keystore_password`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`manage_template`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-manage_template) | [boolean](/lsr/value-types.md#boolean) | No |
| [`parameters`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-parameters) | [hash](/lsr/value-types.md#hash) | No |
| [`parent`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-parent) | [string](/lsr/value-types.md#string) | No |
| [`password`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-password) | [password](/lsr/value-types.md#password) | No |
| [`path`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-path) | [string](/lsr/value-types.md#string) | No |
| [`pipeline`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-pipeline) | [string](/lsr/value-types.md#string) | No |
| [`pool_max`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-pool_max) | [number](/lsr/value-types.md#number) | No |
| [`pool_max_per_route`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-pool_max_per_route) | [number](/lsr/value-types.md#number) | No |
| [`proxy`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-proxy) | [uri](/lsr/value-types.md#uri) | No |
| [`resurrect_delay`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-resurrect_delay) | [number](/lsr/value-types.md#number) | No |
| [`retry_initial_interval`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-retry_initial_interval) | [number](/lsr/value-types.md#number) | No |
| [`retry_max_interval`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-retry_max_interval) | [number](/lsr/value-types.md#number) | No |
| [`retry_on_conflict`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-retry_on_conflict) | [number](/lsr/value-types.md#number) | No |
| [`routing`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-routing) | [string](/lsr/value-types.md#string) | No |
| [`script`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-script) | [string](/lsr/value-types.md#string) | No |
| [`script_lang`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-script_lang) | [string](/lsr/value-types.md#string) | No |
| [`script_type`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-script_type) | [string](/lsr/value-types.md#string), one of `["inline", "indexed", "file"]` | No |
| [`script_var_name`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-script_var_name) | [string](/lsr/value-types.md#string) | No |
| [`scripted_upsert`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-scripted_upsert) | [boolean](/lsr/value-types.md#boolean) | No |
| [`sniffing`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-sniffing) | [boolean](/lsr/value-types.md#boolean) | No |
| [`sniffing_delay`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-sniffing_delay) | [number](/lsr/value-types.md#number) | No |
| [`sniffing_path`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-sniffing_path) | [string](/lsr/value-types.md#string) | No |
| [`ssl`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_certificate_verification`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-ssl_certificate_verification) | [boolean](/lsr/value-types.md#boolean) | No |
| [`template`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-template) | a valid filesystem path | No |
| [`template_name`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-template_name) | [string](/lsr/value-types.md#string) | No |
| [`template_overwrite`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-template_overwrite) | [boolean](/lsr/value-types.md#boolean) | No |
| [`timeout`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-timeout) | [number](/lsr/value-types.md#number) | No |
| [`truststore`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-truststore) | a valid filesystem path | No |
| [`truststore_password`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`upsert`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-upsert) | [string](/lsr/value-types.md#string) | No |
| [`user`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-user) | [string](/lsr/value-types.md#string) | No |
| [`validate_after_inactivity`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-validate_after_inactivity) | [number](/lsr/value-types.md#number) | No |
| [`version`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-version) | [string](/lsr/value-types.md#string) | No |
| [`version_type`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-version_type) | [string](/lsr/value-types.md#string), one of `["internal", "external", "external_gt", "external_gte", "force"]` | No |

Also see [Common options](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-common-options) for a list of options supported by all output plugins.

### `action` [v10.1.0-plugins-outputs-elasticsearch-action]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"index"`

Protocol agnostic (i.e. non-http, non-java specific) configs go here Protocol agnostic methods The Elasticsearch action to perform. Valid actions are:

* index: indexes a document (an event from Logstash).
* delete: deletes a document by id (An id is required for this action)
* create: indexes a document, fails if a document by that id already exists in the index.
* update: updates a document by id. Update has a special case where you can upsert—update a document if not already present. See the `upsert` option. NOTE: This does not work and is not supported in Elasticsearch 1.x. Please upgrade to ES 2.x or greater to use this feature with Logstash!
* A sprintf style string to change the action based on the content of the event. The value `%{[foo]}` would use the foo field for the action

For more details on actions, check out the [Elasticsearch bulk API documentation](http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html)

### `bulk_path` [v10.1.0-plugins-outputs-elasticsearch-bulk_path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

HTTP Path to perform the \_bulk requests to this defaults to a concatenation of the path parameter and "\_bulk"

### `cacert` [v10.1.0-plugins-outputs-elasticsearch-cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The .cer or .pem file to validate the server’s certificate

### `doc_as_upsert` [v10.1.0-plugins-outputs-elasticsearch-doc_as_upsert]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable `doc_as_upsert` for update mode. Create a new document with source if `document_id` doesn’t exist in Elasticsearch

### `document_id` [v10.1.0-plugins-outputs-elasticsearch-document_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The document ID for the index. Useful for overwriting existing entries in Elasticsearch with the same ID.

### `document_type` [v10.1.0-plugins-outputs-elasticsearch-document_type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* This option is deprecated

Note: This option is deprecated due to the [removal of types in Elasticsearch 6.0](https://www.elastic.co/guide/en/elasticsearch/reference/6.0/removal-of-types.html). It will be removed in the next major version of Logstash. This sets the document type to write events to. Generally you should try to write only similar events to the same *type*. String expansion `%{foo}` works here. If you don’t set a value for this option:

* for elasticsearch clusters 6.x and above: the value of *doc* will be used;
* for elasticsearch clusters 5.x and below: the event’s *type* field will be used, if the field is not present the value of *doc* will be used.

### `failure_type_logging_whitelist` [v10.1.0-plugins-outputs-elasticsearch-failure_type_logging_whitelist]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Set the Elasticsearch errors in the whitelist that you don’t want to log. A useful example is when you want to skip all 409 errors which are `document_already_exists_exception`.

### `custom_headers` [v10.1.0-plugins-outputs-elasticsearch-custom_headers]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Pass a set of key value pairs as the headers sent in each request to an elasticsearch node. The headers will be used for any kind of request (\_bulk request, template installation, health checks and sniffing). These custom headers will be overidden by settings like `http_compression`.

### `healthcheck_path` [v10.1.0-plugins-outputs-elasticsearch-healthcheck_path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

HTTP Path where a HEAD request is sent when a backend is marked down the request is sent in the background to see if it has come back again before it is once again eligible to service requests. If you have custom firewall rules you may need to change this

### `hosts` [v10.1.0-plugins-outputs-elasticsearch-hosts]

* Value type is [uri](/lsr/value-types.md#uri)
* Default value is `[//127.0.0.1]`

Sets the host(s) of the remote instance. If given an array it will load balance requests across the hosts specified in the `hosts` parameter. Remember the `http` protocol uses the [http](http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html#modules-http) address (eg. 9200, not 9300). `"127.0.0.1"` `["127.0.0.1:9200","127.0.0.2:9200"]` `["http://127.0.0.1"]` `["https://127.0.0.1:9200"]` `["https://127.0.0.1:9200/mypath"]` (If using a proxy on a subpath) It is important to exclude [dedicated master nodes](http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html) from the `hosts` list to prevent LS from sending bulk requests to the master nodes. So this parameter should only reference either data or client nodes in Elasticsearch.

Any special characters present in the URLs here MUST be URL escaped! This means `#` should be put in as `%23` for instance.

### `http_compression` [v10.1.0-plugins-outputs-elasticsearch-http_compression]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable gzip compression on requests. Note that response compression is on by default for Elasticsearch v5.0 and beyond

### `ilm_enabled` [v10.1.0-plugins-outputs-elasticsearch-ilm_enabled]

* Value can be any of: `true`, `false`, `auto`
* Default value is `auto`

The default setting of `auto` will automatically enable the Index Lifecycle Management feature, if the Elasticsearch cluster is running Elasticsearch version `7.0.0` or higher with the ILM feature enabled, and disable it otherwise.

Setting this flag to `false` will disable the Index Lifecycle Management feature, even if the Elasticsearch cluster supports ILM. Setting this flag to `true` will enable Index Lifecycle Management feature, if the Elasticsearch cluster supports it. This is required to enable Index Lifecycle Management on a version of Elasticsearch earlier than version `7.0.0`.

This feature requires a Basic License or above to be installed on an Elasticsearch cluster version 6.6.0 or later

### `ilm_pattern` [v10.1.0-plugins-outputs-elasticsearch-ilm_pattern]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `{now/d}-000001`

Pattern used for generating indices managed by Index Lifecycle Management. The value specified in the pattern will be appended to the write alias, and incremented automatically when a new index is created by ILM.

Date Math can be used when specifying an ilm pattern, see [Rollover API docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-rollover-index.html#_using_date_math_with_the_rollover_api) for details

Updating the pattern will require the index template to be rewritten

The pattern must finish with a dash and a number that will be automatically incremented when indices rollover.

### `ilm_policy` [v10.1.0-plugins-outputs-elasticsearch-ilm_policy]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `logstash`

Modify this setting to use a custom Index Lifecycle Management policy, rather than the default. If this value is not set, the default policy will be automatically installed into Elasticsearch

If this setting is specified, the policy must already exist in Elasticsearch cluster.

### `ilm_rollover_alias` [v10.1.0-plugins-outputs-elasticsearch-ilm_rollover_alias]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `logstash`

The rollover alias is the alias where indices managed using Index Lifecycle Management will be written to.

If both `index` and `ilm_rollover_alias` are specified, `ilm_rollover_alias` takes precedence.

Updating the rollover alias will require the index template to be rewritten

### `index` [v10.1.0-plugins-outputs-elasticsearch-index]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash-%{+YYYY.MM.dd}"`

The index to write events to. This can be dynamic using the `%{foo}` syntax. The default value will partition your indices by day so you can more easily delete old data or only search specific date ranges. Indexes may not contain uppercase characters. For weekly indexes ISO 8601 format is recommended, eg. logstash-%{+xxxx.ww}. LS uses Joda to format the index pattern from event timestamp. Joda formats are defined [here](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html).

### `keystore` [v10.1.0-plugins-outputs-elasticsearch-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The keystore used to present a certificate to the server. It can be either .jks or .p12

### `keystore_password` [v10.1.0-plugins-outputs-elasticsearch-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the keystore password

### `manage_template` [v10.1.0-plugins-outputs-elasticsearch-manage_template]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

From Logstash 1.3 onwards, a template is applied to Elasticsearch during Logstash’s startup if one with the name `template_name` does not already exist. By default, the contents of this template is the default template for `logstash-%{+YYYY.MM.dd}` which always matches indices based on the pattern `logstash-*`. Should you require support for other index names, or would like to change the mappings in the template in general, a custom template can be specified by setting `template` to the path of a template file.

Setting `manage_template` to false disables this feature. If you require more control over template creation, (e.g. creating indices dynamically based on field names) you should set `manage_template` to false and use the REST API to apply your templates manually.

### `parameters` [v10.1.0-plugins-outputs-elasticsearch-parameters]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Pass a set of key value pairs as the URL query string. This query string is added to every host listed in the *hosts* configuration. If the *hosts* list contains urls that already have query strings, the one specified here will be appended.

### `parent` [v10.1.0-plugins-outputs-elasticsearch-parent]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

For child documents, ID of the associated parent. This can be dynamic using the `%{foo}` syntax.

### `password` [v10.1.0-plugins-outputs-elasticsearch-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to authenticate to a secure Elasticsearch cluster

### `path` [v10.1.0-plugins-outputs-elasticsearch-path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

HTTP Path at which the Elasticsearch server lives. Use this if you must run Elasticsearch behind a proxy that remaps the root path for the Elasticsearch HTTP API lives. Note that if you use paths as components of URLs in the *hosts* field you may not also set this field. That will raise an error at startup

### `pipeline` [v10.1.0-plugins-outputs-elasticsearch-pipeline]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Set which ingest pipeline you wish to execute for an event. You can also use event dependent configuration here like `pipeline => "%{INGEST_PIPELINE}"`

### `pool_max` [v10.1.0-plugins-outputs-elasticsearch-pool_max]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1000`

While the output tries to reuse connections efficiently we have a maximum. This sets the maximum number of open connections the output will create. Setting this too low may mean frequently closing / opening connections which is bad.

### `pool_max_per_route` [v10.1.0-plugins-outputs-elasticsearch-pool_max_per_route]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `100`

While the output tries to reuse connections efficiently we have a maximum per endpoint. This sets the maximum number of open connections per endpoint the output will create. Setting this too low may mean frequently closing / opening connections which is bad.

### `proxy` [v10.1.0-plugins-outputs-elasticsearch-proxy]

* Value type is [uri](/lsr/value-types.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. This used to accept hashes as arguments but now only accepts arguments of the URI type to prevent leaking credentials.

### `resurrect_delay` [v10.1.0-plugins-outputs-elasticsearch-resurrect_delay]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

How frequently, in seconds, to wait between resurrection attempts. Resurrection is the process by which backend endpoints marked *down* are checked to see if they have come back to life

### `retry_initial_interval` [v10.1.0-plugins-outputs-elasticsearch-retry_initial_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `2`

Set initial interval in seconds between bulk retries. Doubled on each retry up to `retry_max_interval`

### `retry_max_interval` [v10.1.0-plugins-outputs-elasticsearch-retry_max_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `64`

Set max interval in seconds between bulk retries.

### `retry_on_conflict` [v10.1.0-plugins-outputs-elasticsearch-retry_on_conflict]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

The number of times Elasticsearch should internally retry an update/upserted document See the [partial updates](https://www.elastic.co/guide/en/elasticsearch/guide/current/partial-updates.html) for more info

### `routing` [v10.1.0-plugins-outputs-elasticsearch-routing]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A routing override to be applied to all processed events. This can be dynamic using the `%{foo}` syntax.

### `script` [v10.1.0-plugins-outputs-elasticsearch-script]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Set script name for scripted update mode

Example:

```
    output {
      elasticsearch {
        script => "ctx._source.message = params.event.get('message')"
      }
    }
```

### `script_lang` [v10.1.0-plugins-outputs-elasticsearch-script_lang]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"painless"`

Set the language of the used script. If not set, this defaults to painless in ES 5.0. When using indexed (stored) scripts on Elasticsearch 6 and higher, you must set this parameter to `""` (empty string).

### `script_type` [v10.1.0-plugins-outputs-elasticsearch-script_type]

* Value can be any of: `inline`, `indexed`, `file`
* Default value is `["inline"]`

Define the type of script referenced by "script" variable inline : "script" contains inline script indexed : "script" contains the name of script directly indexed in elasticsearch file : "script" contains the name of script stored in elasticsearch’s config directory

### `script_var_name` [v10.1.0-plugins-outputs-elasticsearch-script_var_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"event"`

Set variable name passed to script (scripted update)

### `scripted_upsert` [v10.1.0-plugins-outputs-elasticsearch-scripted_upsert]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

if enabled, script is in charge of creating non-existent document (scripted update)

### `sniffing` [v10.1.0-plugins-outputs-elasticsearch-sniffing]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

This setting asks Elasticsearch for the list of all cluster nodes and adds them to the hosts list. For Elasticsearch 1.x and 2.x any nodes with `http.enabled` (on by default) will be added to the hosts list, including master-only nodes! For Elasticsearch 5.x and 6.x any nodes with `http.enabled` (on by default) will be added to the hosts list, excluding master-only nodes.

### `sniffing_delay` [v10.1.0-plugins-outputs-elasticsearch-sniffing_delay]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

How long to wait, in seconds, between sniffing attempts

### `sniffing_path` [v10.1.0-plugins-outputs-elasticsearch-sniffing_path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

HTTP Path to be used for the sniffing requests the default value is computed by concatenating the path value and "\_nodes/http" if sniffing\_path is set it will be used as an absolute path do not use full URL here, only paths, e.g. "/sniff/\_nodes/http"

### `ssl` [v10.1.0-plugins-outputs-elasticsearch-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* There is no default value for this setting.

Enable SSL/TLS secured communication to Elasticsearch cluster. Leaving this unspecified will use whatever scheme is specified in the URLs listed in *hosts*. If no explicit protocol is specified plain HTTP will be used. If SSL is explicitly disabled here the plugin will refuse to start if an HTTPS URL is given in *hosts*

### `ssl_certificate_verification` [v10.1.0-plugins-outputs-elasticsearch-ssl_certificate_verification]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Option to validate the server’s certificate. Disabling this severely compromises security. For more information on disabling certificate verification please read <https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf>

### `template` [v10.1.0-plugins-outputs-elasticsearch-template]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

You can set the path to your own template here, if you so desire. If not set, the included template will be used.

### `template_name` [v10.1.0-plugins-outputs-elasticsearch-template_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

This configuration option defines how the template is named inside Elasticsearch. Note that if you have used the template management features and subsequently change this, you will need to prune the old template manually, e.g.

`curl -XDELETE <http://localhost:9200/_template/OldTemplateName?pretty>`

where `OldTemplateName` is whatever the former setting was.

### `template_overwrite` [v10.1.0-plugins-outputs-elasticsearch-template_overwrite]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

The template\_overwrite option will always overwrite the indicated template in Elasticsearch with either the one indicated by template or the included one. This option is set to false by default. If you always want to stay up to date with the template provided by Logstash, this option could be very useful to you. Likewise, if you have your own template file managed by puppet, for example, and you wanted to be able to update it regularly, this option could help there as well.

Please note that if you are using your own customized version of the Logstash template (logstash), setting this to true will make Logstash to overwrite the "logstash" template (i.e. removing all customized settings)

### `timeout` [v10.1.0-plugins-outputs-elasticsearch-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Set the timeout, in seconds, for network operations and requests sent Elasticsearch. If a timeout occurs, the request will be retried.

### `truststore` [v10.1.0-plugins-outputs-elasticsearch-truststore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either .jks or .p12. Use either `:truststore` or `:cacert`.

### `truststore_password` [v10.1.0-plugins-outputs-elasticsearch-truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the truststore password

### `upsert` [v10.1.0-plugins-outputs-elasticsearch-upsert]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Set upsert content for update mode. Create a new document with this parameter as json string if `document_id` doesn’t exists

### `user` [v10.1.0-plugins-outputs-elasticsearch-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username to authenticate to a secure Elasticsearch cluster

### `validate_after_inactivity` [v10.1.0-plugins-outputs-elasticsearch-validate_after_inactivity]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000`

How long to wait before checking if the connection is stale before executing a request on a connection using keepalive. You may want to set this lower, if you get connection errors regularly Quoting the Apache commons docs (this client is based Apache Commmons): *Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool.* See [these docs for more info](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity\(int\))

### `version` [v10.1.0-plugins-outputs-elasticsearch-version]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The version to use for indexing. Use sprintf syntax like `%{my_version}` to use a field value here. See <https://www.elastic.co/blog/elasticsearch-versioning-support>.

### `version_type` [v10.1.0-plugins-outputs-elasticsearch-version_type]

* Value can be any of: `internal`, `external`, `external_gt`, `external_gte`, `force`
* There is no default value for this setting.

The version\_type to use for indexing. See <https://www.elastic.co/blog/elasticsearch-versioning-support>. See also <https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html#_version_types>

## Common options [v10.1.0-plugins-outputs-elasticsearch-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`enable_metric`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v10-1-0-plugins-outputs-elasticsearch.md#v10.1.0-plugins-outputs-elasticsearch-id) | [string](/lsr/value-types.md#string) | No |

### `enable_metric` [v10.1.0-plugins-outputs-elasticsearch-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v10.1.0-plugins-outputs-elasticsearch-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elasticsearch outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  elasticsearch {
    id => "my_plugin_id"
  }
}
```
