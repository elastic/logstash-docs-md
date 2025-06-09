---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-solr_http.html
---

# Solr_http output plugin v3.0.3 [v3.0.3-plugins-outputs-solr_http]

* Plugin version: v3.0.3
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-solr_http/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-solr_http-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1602]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-solr_http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1592]

This output lets you index\&store your logs in Solr. If you want to get started quickly you should use version 4.4 or above in schemaless mode, which will try and guess your fields automatically. To turn that on, you can use the example included in the Solr archive:

```
    tar zxf solr-4.4.0.tgz
    cd example
    mv solr solr_ #back up the existing sample conf
    cp -r example-schemaless/solr/ .  #put the schemaless conf in place
    java -jar start.jar   #start Solr
```

You can learn more at [the Solr home page](https://lucene.apache.org/solr/)

## Solr_http Output Configuration Options [v3.0.3-plugins-outputs-solr_http-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`document_id`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-document_id) | [string](/lsr/value-types.md#string) | No |
| [`flush_size`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-flush_size) | [number](/lsr/value-types.md#number) | No |
| [`idle_flush_time`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-idle_flush_time) | [number](/lsr/value-types.md#number) | No |
| [`solr_url`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-solr_url) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-common-options) for a list of options supported by all output plugins.

### `document_id` [v3.0.3-plugins-outputs-solr_http-document_id]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Solr document ID for events. You’d typically have a variable here, like *%{foo}* so you can assign your own IDs

### `flush_size` [v3.0.3-plugins-outputs-solr_http-flush_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `100`

Number of events to queue up before writing to Solr

### `idle_flush_time` [v3.0.3-plugins-outputs-solr_http-idle_flush_time]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

Amount of time since the last flush before a flush is done even if the number of buffered events is smaller than flush\_size

### `solr_url` [v3.0.3-plugins-outputs-solr_http-solr_url]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"http://localhost:8983/solr"`

URL used to connect to Solr

## Common options [v3.0.3-plugins-outputs-solr_http-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-solr_http.md#v3.0.3-plugins-outputs-solr_http-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-solr_http-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.3-plugins-outputs-solr_http-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-outputs-solr_http-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 solr\_http outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  solr_http {
    id => "my_plugin_id"
  }
}
```
