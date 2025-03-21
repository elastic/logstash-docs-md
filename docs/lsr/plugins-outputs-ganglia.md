---
navigation_title: "ganglia"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash/current/plugins-outputs-ganglia.html
---

# Ganglia output plugin [plugins-outputs-ganglia]


* Plugin version: v3.0.6
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-ganglia/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/output-ganglia-index.md).

## Installation [_installation_27]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-output-ganglia`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html) for more details.


## Getting help [_getting_help_78]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-ganglia). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_77]

This output allows you to pull metrics from your logs and ship them to ganglia’s gmond. This is heavily based on the graphite output.


## Ganglia Output Configuration Options [plugins-outputs-ganglia-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-ganglia.md#plugins-outputs-ganglia-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`group`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-group) | [string](introduction.md#string) | No |
| [`host`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-host) | [string](introduction.md#string) | No |
| [`lifetime`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-lifetime) | [number](introduction.md#number) | No |
| [`max_interval`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-max_interval) | [number](introduction.md#number) | No |
| [`metric`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-metric) | [string](introduction.md#string) | Yes |
| [`metric_type`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-metric_type) | [string](introduction.md#string), one of `["string", "int8", "uint8", "int16", "uint16", "int32", "uint32", "float", "double"]` | No |
| [`port`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-port) | [number](introduction.md#number) | No |
| [`slope`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-slope) | [string](introduction.md#string), one of `["zero", "positive", "negative", "both", "unspecified"]` | No |
| [`units`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-units) | [string](introduction.md#string) | No |
| [`value`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-value) | [string](introduction.md#string) | Yes |

Also see [Common options](plugins-outputs-ganglia.md#plugins-outputs-ganglia-common-options) for a list of options supported by all output plugins.

 

### `group` [plugins-outputs-ganglia-group]

* Value type is [string](introduction.md#string)
* Default value is `""`

Metric group


### `host` [plugins-outputs-ganglia-host]

* Value type is [string](introduction.md#string)
* Default value is `"localhost"`

The address of the ganglia server.


### `lifetime` [plugins-outputs-ganglia-lifetime]

* Value type is [number](introduction.md#number)
* Default value is `300`

Lifetime in seconds of this metric


### `max_interval` [plugins-outputs-ganglia-max_interval]

* Value type is [number](introduction.md#number)
* Default value is `60`

Maximum time in seconds between gmetric calls for this metric.


### `metric` [plugins-outputs-ganglia-metric]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The metric to use. This supports dynamic strings like `%{{host}}`


### `metric_type` [plugins-outputs-ganglia-metric_type]

* Value can be any of: `string`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `float`, `double`
* Default value is `"uint8"`

The type of value for this metric.


### `port` [plugins-outputs-ganglia-port]

* Value type is [number](introduction.md#number)
* Default value is `8649`

The port to connect on your ganglia server.


### `slope` [plugins-outputs-ganglia-slope]

* Value can be any of: `zero`, `positive`, `negative`, `both`, `unspecified`
* Default value is `"both"`

Metric slope, represents metric behavior


### `units` [plugins-outputs-ganglia-units]

* Value type is [string](introduction.md#string)
* Default value is `""`

Gmetric units for metric, such as "kb/sec" or "ms" or whatever unit this metric uses.


### `value` [plugins-outputs-ganglia-value]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The value to use. This supports dynamic strings like `%{{bytes}}` It will be coerced to a floating point value. Values which cannot be coerced will zero (0)



## Common options [plugins-outputs-ganglia-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-codec) | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-outputs-ganglia.md#plugins-outputs-ganglia-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

### `codec` [plugins-outputs-ganglia-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [plugins-outputs-ganglia-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-ganglia-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 ganglia outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  ganglia {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




