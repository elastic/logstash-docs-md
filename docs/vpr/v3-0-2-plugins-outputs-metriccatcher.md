---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-outputs-metriccatcher.html
---

# Metriccatcher output plugin v3.0.2 [v3.0.2-plugins-outputs-metriccatcher]

* Plugin version: v3.0.2
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-metriccatcher/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](output-metriccatcher-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1446]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-metriccatcher). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1436]

This output ships metrics to MetricCatcher, allowing you to utilize Coda Hale’s Metrics.

More info on MetricCatcher: <https://github.com/clearspring/MetricCatcher>

At Clearspring, we use it to count the response codes from Apache logs:

```
    metriccatcher {
        host => "localhost"
        port => "1420"
        type => "apache-access"
        fields => [ "response" ]
        meter => {
            "%{host}.apache.response.%{response}" => "1"
            }
    }
```

## Metriccatcher Output Configuration Options [v3.0.2-plugins-outputs-metriccatcher-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`biased`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-biased) | [hash](/lsr/value-types.md#hash) | No |
| [`counter`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-counter) | [hash](/lsr/value-types.md#hash) | No |
| [`gauge`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-gauge) | [hash](/lsr/value-types.md#hash) | No |
| [`host`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-host) | [string](/lsr/value-types.md#string) | No |
| [`meter`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-meter) | [hash](/lsr/value-types.md#hash) | No |
| [`port`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-port) | [number](/lsr/value-types.md#number) | No |
| [`timer`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-timer) | [hash](/lsr/value-types.md#hash) | No |
| [`uniform`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-uniform) | [hash](/lsr/value-types.md#hash) | No |

Also see [Common options](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-common-options) for a list of options supported by all output plugins.

### `biased` [v3.0.2-plugins-outputs-metriccatcher-biased]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value.

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `counter` [v3.0.2-plugins-outputs-metriccatcher-counter]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value. Example:

```
  counter => { "%{host}.apache.hits.%{response} => "1" }
```

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `gauge` [v3.0.2-plugins-outputs-metriccatcher-gauge]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value.

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `host` [v3.0.2-plugins-outputs-metriccatcher-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

The address of the MetricCatcher

### `meter` [v3.0.2-plugins-outputs-metriccatcher-meter]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value.

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `port` [v3.0.2-plugins-outputs-metriccatcher-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1420`

The port to connect on your MetricCatcher

### `timer` [v3.0.2-plugins-outputs-metriccatcher-timer]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like %{host} for metric names and also for values. This is a hash field with key of the metric name, value of the metric value. Example:

```
  timer => { "%{host}.apache.response_time => "%{response_time}" }
```

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `uniform` [v3.0.2-plugins-outputs-metriccatcher-uniform]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

The metrics to send. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value.

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

## Common options [v3.0.2-plugins-outputs-metriccatcher-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-2-plugins-outputs-metriccatcher.md#v3.0.2-plugins-outputs-metriccatcher-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.2-plugins-outputs-metriccatcher-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.2-plugins-outputs-metriccatcher-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.2-plugins-outputs-metriccatcher-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 metriccatcher outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  metriccatcher {
    id => "my_plugin_id"
  }
}
```
