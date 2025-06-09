---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-ganglia.html
---

# Ganglia output plugin v3.0.6 [v3.0.6-plugins-outputs-ganglia]

* Plugin version: v3.0.6
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-ganglia/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-ganglia-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1242]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-ganglia). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1235]

This output allows you to pull metrics from your logs and ship them to ganglia’s gmond. This is heavily based on the graphite output.

## Ganglia Output Configuration Options [v3.0.6-plugins-outputs-ganglia-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`group`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-group) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-host) | [string](/lsr/value-types.md#string) | No |
| [`lifetime`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-lifetime) | [number](/lsr/value-types.md#number) | No |
| [`max_interval`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-max_interval) | [number](/lsr/value-types.md#number) | No |
| [`metric`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-metric) | [string](/lsr/value-types.md#string) | Yes |
| [`metric_type`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-metric_type) | [string](/lsr/value-types.md#string), one of `["string", "int8", "uint8", "int16", "uint16", "int32", "uint32", "float", "double"]` | No |
| [`port`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-port) | [number](/lsr/value-types.md#number) | No |
| [`slope`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-slope) | [string](/lsr/value-types.md#string), one of `["zero", "positive", "negative", "both", "unspecified"]` | No |
| [`units`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-units) | [string](/lsr/value-types.md#string) | No |
| [`value`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-value) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-common-options) for a list of options supported by all output plugins.

### `group` [v3.0.6-plugins-outputs-ganglia-group]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Metric group

### `host` [v3.0.6-plugins-outputs-ganglia-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

The address of the ganglia server.

### `lifetime` [v3.0.6-plugins-outputs-ganglia-lifetime]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `300`

Lifetime in seconds of this metric

### `max_interval` [v3.0.6-plugins-outputs-ganglia-max_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Maximum time in seconds between gmetric calls for this metric.

### `metric` [v3.0.6-plugins-outputs-ganglia-metric]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The metric to use. This supports dynamic strings like `%{host}`

### `metric_type` [v3.0.6-plugins-outputs-ganglia-metric_type]

* Value can be any of: `string`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `float`, `double`
* Default value is `"uint8"`

The type of value for this metric.

### `port` [v3.0.6-plugins-outputs-ganglia-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `8649`

The port to connect on your ganglia server.

### `slope` [v3.0.6-plugins-outputs-ganglia-slope]

* Value can be any of: `zero`, `positive`, `negative`, `both`, `unspecified`
* Default value is `"both"`

Metric slope, represents metric behavior

### `units` [v3.0.6-plugins-outputs-ganglia-units]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Gmetric units for metric, such as "kb/sec" or "ms" or whatever unit this metric uses.

### `value` [v3.0.6-plugins-outputs-ganglia-value]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The value to use. This supports dynamic strings like `%{bytes}` It will be coerced to a floating point value. Values which cannot be coerced will zero (0)

## Common options [v3.0.6-plugins-outputs-ganglia-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-ganglia.md#v3.0.6-plugins-outputs-ganglia-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-ganglia-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.6-plugins-outputs-ganglia-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.6-plugins-outputs-ganglia-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 ganglia outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  ganglia {
    id => "my_plugin_id"
  }
}
```
