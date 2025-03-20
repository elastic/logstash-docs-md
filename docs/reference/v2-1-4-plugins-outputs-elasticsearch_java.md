---
navigation_title: "v2.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.1.4-plugins-outputs-elasticsearch_java.html
---

# Elasticsearch_java output plugin v2.1.4 [v2.1.4-plugins-outputs-elasticsearch_java]


* Plugin version: v2.1.4
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-elasticsearch_java/blob/v2.1.4/CHANGELOG.md)

For other versions, see the [overview list](output-elasticsearch_java-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1212]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-elasticsearch_java). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1205]

This output lets you store logs in Elasticsearch using the native *node* and *transport* protocols. It is highly recommended to use the regular *logstash-output-elasticsearch* output which uses HTTP instead. This output is, in-fact, sometimes slower, and never faster than that one. Additionally, upgrading your Elasticsearch cluster may require you to simultaneously update this plugin for any protocol level changes. The HTTP client may be easier to work with due to wider familiarity with HTTP.

**VERSION NOTE**: Your Elasticsearch cluster must be running Elasticsearch 1.0.0 or later.

If you want to set other Elasticsearch options that are not exposed directly as configuration options, there are two methods:

* Create an `elasticsearch.yml` file in the $PWD of the Logstash process
* Pass in es.* java properties (`java -Des.node.foo=` or `ruby -J-Des.node.foo=`)

With the default `protocol` setting ("node"), this plugin will join your Elasticsearch cluster as a client node, so it will show up in Elasticsearch’s cluster status.

You can learn more about Elasticsearch at [https://www.elastic.co/products/elasticsearch](https://www.elastic.co/products/elasticsearch)


## Operational Notes [_operational_notes_2]

If using the default `protocol` setting ("node"), your firewalls might need to permit port 9300 in **both** directions (from Logstash to Elasticsearch, and Elasticsearch to Logstash)


## Retry Policy [_retry_policy_129]

By default all bulk requests to ES are synchronous. Not all events in the bulk requests always make it successfully. For example, there could be events which are not formatted correctly for the index they are targeting (type mismatch in mapping). So that we minimize loss of events, we have a specific retry policy in place. We retry all events which fail to be reached by Elasticsearch for network related issues. We retry specific events which exhibit errors under a separate policy described below. Events of this nature are ones which experience ES error codes described as retryable errors.

**Retryable Errors:**

* 429, Too Many Requests (RFC6585)
* 503, The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.

Here are the rules of what is retried when:

* Block and retry all events in bulk response that experiences transient network exceptions until a successful submission is received by Elasticsearch.
* Retry subset of sent events which resulted in ES errors of a retryable nature which can be found in RETRYABLE_CODES
* For events which returned retryable error codes, they will be pushed onto a separate queue for retrying events. events in this queue will be retried a maximum of 5 times by default (configurable through :max_retries). The size of this queue is capped by the value set in :retry_max_items.
* Events from the retry queue are submitted again either when the queue reaches its max size or when the max interval time is reached, which is set in :retry_max_interval.
* Events which are not retryable or have reached their max retry count are logged to stderr.


## Elasticsearch_java Output Configuration Options [v2.1.4-plugins-outputs-elasticsearch_java-options]

This plugin supports the following configuration options plus the [Common options](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`action`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-action) | [string](logstash://reference/configuration-file-structure.md#string), one of `["index", "delete", "create", "update", "create_unless_exists"]` | No |
| [`cluster`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-cluster) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`doc_as_upsert`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-doc_as_upsert) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`document_id`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-document_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`document_type`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-document_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`hosts`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-hosts) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`index`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-index) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`manage_template`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-manage_template) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`network_host`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-network_host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`node_name`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-node_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`parent`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-parent) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pipeline`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-pipeline) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`protocol`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-protocol) | [string](logstash://reference/configuration-file-structure.md#string), one of `["node", "transport"]` | No |
| [`retry_initial_interval`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-retry_initial_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_max_interval`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-retry_max_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_on_conflict`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-retry_on_conflict) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`routing`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-routing) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-script) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script_lang`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-script_lang) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`script_type`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-script_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["inline", "indexed", "file"]` | No |
| [`script_var_name`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-script_var_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`scripted_upsert`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-scripted_upsert) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`sniffing`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-sniffing) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`template`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-template) | a valid filesystem path | No |
| [`template_name`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-template_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`template_overwrite`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-template_overwrite) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`transport_tcp_port`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-transport_tcp_port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`upsert`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-upsert) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version_type`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-version_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["internal", "external", "external_gt", "external_gte", "force"]` | No |

Also see [Common options](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-common-options) for a list of options supported by all output plugins.

 

### `action` [v2.1.4-plugins-outputs-elasticsearch_java-action]

* Value can be any of: `index`, `delete`, `create`, `update`, `create_unless_exists`
* Default value is `"index"`

The Elasticsearch action to perform. Valid actions are:

* index: indexes a document (an event from Logstash).
* delete: deletes a document by id (An id is required for this action)
* create: indexes a document, fails if a document by that id already exists in the index.
* update: updates a document by id. Update has a special case where you can upsert — update a document if not already present. See the `upsert` option
* create_unless_exists: create the document unless it already exists, in which case do nothing.

For more details on actions, check out the [Elasticsearch bulk API documentation](http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.md)


### `cluster` [v2.1.4-plugins-outputs-elasticsearch_java-cluster]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of your cluster if you set it on the Elasticsearch side. Useful for discovery when using `node` or `transport` protocols. By default, it looks for a cluster named *elasticsearch*. Equivalent to the Elasticsearch option *cluster.name*


### `doc_as_upsert` [v2.1.4-plugins-outputs-elasticsearch_java-doc_as_upsert]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable `doc_as_upsert` for update mode. Create a new document with source if `document_id` doesn’t exist in Elasticsearch


### `document_id` [v2.1.4-plugins-outputs-elasticsearch_java-document_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The document ID for the index. Useful for overwriting existing entries in Elasticsearch with the same ID.


### `document_type` [v2.1.4-plugins-outputs-elasticsearch_java-document_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The document type to write events to. Generally you should try to write only similar events to the same *type*. String expansion `%{{foo}}` works here. Unless you set *document_type*, the event *type* will be used if it exists otherwise the document type will be assigned the value of *logs*


### `flush_size`  (DEPRECATED) [v2.1.4-plugins-outputs-elasticsearch_java-flush_size]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.


### `hosts` [v2.1.4-plugins-outputs-elasticsearch_java-hosts]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* Default value is `[//127.0.0.1]`

Sets the host(s) of the remote instance. If given an array it will load balance requests across the hosts specified in the `hosts` parameter. Remember the `http` protocol uses the [http](http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.md#modules-http) address (eg. 9200, not 9300). `"127.0.0.1"` `["127.0.0.1:9200","127.0.0.2:9200"]` `["http://127.0.0.1"]` `["https://127.0.0.1:9200"]` `["https://127.0.0.1:9200/mypath"]` (If using a proxy on a subpath) It is important to exclude [dedicated master nodes](http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.md) from the `hosts` list to prevent LS from sending bulk requests to the master nodes.  So this parameter should only reference either data or client nodes in Elasticsearch.

Any special characters present in the URLs here MUST be URL escaped! This means `#` should be put in as `%23` for instance.


### `idle_flush_time`  (DEPRECATED) [v2.1.4-plugins-outputs-elasticsearch_java-idle_flush_time]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`


### `index` [v2.1.4-plugins-outputs-elasticsearch_java-index]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash-%{+YYYY.MM.dd}"`

The index to write events to. This can be dynamic using the `%{{foo}}` syntax. The default value will partition your indices by day so you can more easily delete old data or only search specific date ranges. Indexes may not contain uppercase characters. For weekly indexes ISO 8601 format is recommended, eg. logstash-%{+xxxx.ww}. LS uses Joda to format the index pattern from event timestamp. Joda formats are defined [here](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.md).


### `manage_template` [v2.1.4-plugins-outputs-elasticsearch_java-manage_template]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

From Logstash 1.3 onwards, a template is applied to Elasticsearch during Logstash’s startup if one with the name `template_name` does not already exist. By default, the contents of this template is the default template for `logstash-%{+YYYY.MM.dd}` which always matches indices based on the pattern `logstash-*`.  Should you require support for other index names, or would like to change the mappings in the template in general, a custom template can be specified by setting `template` to the path of a template file.

Setting `manage_template` to false disables this feature.  If you require more control over template creation, (e.g. creating indices dynamically based on field names) you should set `manage_template` to false and use the REST API to apply your templates manually.


### `max_inflight_requests`  (DEPRECATED) [v2.1.4-plugins-outputs-elasticsearch_java-max_inflight_requests]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`

This setting no longer does anything. It exists to keep config validation from failing. It will be removed in future versions.


### `network_host` [v2.1.4-plugins-outputs-elasticsearch_java-network_host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name/address of the host to bind to for Elasticsearch clustering. Equivalent to the Elasticsearch option *network.host* option. This MUST be set for either protocol to work (node or transport)! The internal Elasticsearch node will bind to this ip. This ip MUST be reachable by all nodes in the Elasticsearch cluster


### `node_name` [v2.1.4-plugins-outputs-elasticsearch_java-node_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The node name Elasticsearch will use when joining a cluster.

By default, this is generated internally by the ES client.


### `parent` [v2.1.4-plugins-outputs-elasticsearch_java-parent]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

For child documents, ID of the associated parent. This can be dynamic using the `%{{foo}}` syntax.


### `pipeline` [v2.1.4-plugins-outputs-elasticsearch_java-pipeline]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Set which ingest pipeline you wish to execute for an event. You can also use event dependent configuration here like `pipeline => "%{{INGEST_PIPELINE}}"`


### `protocol` [v2.1.4-plugins-outputs-elasticsearch_java-protocol]

* Value can be any of: `node`, `transport`
* Default value is `"transport"`

Choose the protocol used to talk to Elasticsearch.

The *node* protocol (default) will connect to the cluster as a normal Elasticsearch node (but will not store data). If you use the `node` protocol, you must permit bidirectional communication on the port 9300 (or whichever port you have configured).

If you do not specify the `host` parameter, it will use  multicast for [Elasticsearch discovery](docs-content://deploy-manage/distributed-architecture/discovery-cluster-formation.md).  While this may work in a test/dev environment where multicast is enabled in Elasticsearch, we strongly recommend [using unicast](http://www.elastic.co/guide/en/elasticsearch/guide/current/important-configuration-changes.md#unicast) in Elasticsearch.  To connect to an Elasticsearch cluster with unicast, you must include the `host` parameter (see relevant section above).

The *transport* protocol will connect to the host you specify and will not show up as a *node* in the Elasticsearch cluster. This is useful in situations where you cannot permit connections outbound from the Elasticsearch cluster to this Logstash server.

All protocols will use bulk requests when talking to Elasticsearch.


### `retry_initial_interval` [v2.1.4-plugins-outputs-elasticsearch_java-retry_initial_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Set initial interval in seconds between bulk retries. Doubled on each retry up to `retry_max_interval`


### `retry_max_interval` [v2.1.4-plugins-outputs-elasticsearch_java-retry_max_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `64`

Set max interval in seconds between bulk retries.


### `retry_on_conflict` [v2.1.4-plugins-outputs-elasticsearch_java-retry_on_conflict]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

The number of times Elasticsearch should internally retry an update/upserted document See the [partial updates](https://www.elastic.co/guide/en/elasticsearch/guide/current/partial-updates.html) for more info


### `routing` [v2.1.4-plugins-outputs-elasticsearch_java-routing]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A routing override to be applied to all processed events. This can be dynamic using the `%{{foo}}` syntax.


### `script` [v2.1.4-plugins-outputs-elasticsearch_java-script]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Set script name for scripted update mode


### `script_lang` [v2.1.4-plugins-outputs-elasticsearch_java-script_lang]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"painless"`

Set the language of the used script. If not set, this defaults to painless in ES 5.0


### `script_type` [v2.1.4-plugins-outputs-elasticsearch_java-script_type]

* Value can be any of: `inline`, `indexed`, `file`
* Default value is `["inline"]`

Define the type of script referenced by "script" variable inline : "script" contains inline script indexed : "script" contains the name of script directly indexed in elasticsearch file    : "script" contains the name of script stored in elasticseach’s config directory


### `script_var_name` [v2.1.4-plugins-outputs-elasticsearch_java-script_var_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"event"`

Set variable name passed to script (scripted update)


### `scripted_upsert` [v2.1.4-plugins-outputs-elasticsearch_java-scripted_upsert]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

if enabled, script is in charge of creating non-existent document (scripted update)


### `sniffing` [v2.1.4-plugins-outputs-elasticsearch_java-sniffing]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable cluster sniffing (transport only). Asks host for the list of all cluster nodes and adds them to the hosts list Equivalent to the Elasticsearch option *client.transport.sniff*


### `template` [v2.1.4-plugins-outputs-elasticsearch_java-template]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

You can set the path to your own template here, if you so desire. If not set, the included template will be used.


### `template_name` [v2.1.4-plugins-outputs-elasticsearch_java-template_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

This configuration option defines how the template is named inside Elasticsearch. Note that if you have used the template management features and subsequently change this, you will need to prune the old template manually, e.g.

`curl -XDELETE <http://localhost:9200/_template/OldTemplateName?pretty>`

where `OldTemplateName` is whatever the former setting was.


### `template_overwrite` [v2.1.4-plugins-outputs-elasticsearch_java-template_overwrite]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

The template_overwrite option will always overwrite the indicated template in Elasticsearch with either the one indicated by template or the included one. This option is set to false by default. If you always want to stay up to date with the template provided by Logstash, this option could be very useful to you. Likewise, if you have your own template file managed by puppet, for example, and you wanted to be able to update it regularly, this option could help there as well.

Please note that if you are using your own customized version of the Logstash template (logstash), setting this to true will make Logstash to overwrite the "logstash" template (i.e. removing all customized settings)


### `transport_tcp_port` [v2.1.4-plugins-outputs-elasticsearch_java-transport_tcp_port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

This sets the local port to bind to. Equivalent to the Elasticsrearch option *transport.tcp.port*


### `upsert` [v2.1.4-plugins-outputs-elasticsearch_java-upsert]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Set upsert content for update mode.s Create a new document with this parameter as json string if `document_id` doesn’t exists


### `version` [v2.1.4-plugins-outputs-elasticsearch_java-version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The version to use for indexing. Use sprintf syntax like `%{{my_version}}` to use a field value here. See [https://www.elastic.co/blog/elasticsearch-versioning-support](https://www.elastic.co/blog/elasticsearch-versioning-support).


### `version_type` [v2.1.4-plugins-outputs-elasticsearch_java-version_type]

* Value can be any of: `internal`, `external`, `external_gt`, `external_gte`, `force`
* There is no default value for this setting.

The version_type to use for indexing. See [https://www.elastic.co/blog/elasticsearch-versioning-support](https://www.elastic.co/blog/elasticsearch-versioning-support). See also [https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-create](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-create)



## Common options [v2.1.4-plugins-outputs-elasticsearch_java-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-1-4-plugins-outputs-elasticsearch_java.md#v2.1.4-plugins-outputs-elasticsearch_java-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v2.1.4-plugins-outputs-elasticsearch_java-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.1.4-plugins-outputs-elasticsearch_java-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.1.4-plugins-outputs-elasticsearch_java-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elasticsearch_java outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  elasticsearch_java {
    id => "my_plugin_id"
  }
}
```



