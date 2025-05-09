---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-outputs-opentsdb.html
---

# Opentsdb output plugin v3.1.3 [v3.1.3-plugins-outputs-opentsdb]


* Plugin version: v3.1.3
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-opentsdb/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](output-opentsdb-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1467]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-opentsdb). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1457]

This output allows you to pull metrics from your logs and ship them to opentsdb. Opentsdb is an open source tool for storing and graphing metrics.


## Opentsdb Output Configuration Options [v3.1.3-plugins-outputs-opentsdb-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metrics`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-metrics) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`port`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-common-options) for a list of options supported by all output plugins.

 

### `host` [v3.1.3-plugins-outputs-opentsdb-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

The address of the opentsdb server.


### `metrics` [v3.1.3-plugins-outputs-opentsdb-metrics]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The metric(s) to use. This supports dynamic strings like `%{{source_host}}` for metric names and also for values. This is an array field with key of the metric name, value of the metric value, and multiple tag,values . Example:

```ruby
    [
      "%{host}/uptime",
      %{uptime_1m} " ,
      "hostname" ,
      "%{host}
      "anotherhostname" ,
      "%{host}
    ]
```

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)


### `port` [v3.1.3-plugins-outputs-opentsdb-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `4242`

The port to connect on your graphite server.



## Common options [v3.1.3-plugins-outputs-opentsdb-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-3-plugins-outputs-opentsdb.md#v3.1.3-plugins-outputs-opentsdb-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.3-plugins-outputs-opentsdb-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.3-plugins-outputs-opentsdb-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.3-plugins-outputs-opentsdb-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 opentsdb outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  opentsdb {
    id => "my_plugin_id"
  }
}
```



