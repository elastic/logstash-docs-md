---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-outputs-datadog_metrics.html
---

# Datadog_metrics output plugin v3.0.1 [v3.0.1-plugins-outputs-datadog_metrics]

* Plugin version: v3.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-datadog_metrics/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-datadog_metrics-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1099]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-datadog_metrics). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1092]

This output lets you send metrics to DataDogHQ based on Logstash events. Default `queue_size` and `timeframe` are low in order to provide near realtime alerting. If you do not use Datadog for alerting, consider raising these thresholds.

## Datadog_metrics Output Configuration Options [v3.0.1-plugins-outputs-datadog_metrics-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`api_key`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-api_key) | [string](/lsr/value-types.md#string) | Yes |
| [`dd_tags`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-dd_tags) | [array](/lsr/value-types.md#array) | No |
| [`device`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-device) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-host) | [string](/lsr/value-types.md#string) | No |
| [`metric_name`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-metric_name) | [string](/lsr/value-types.md#string) | No |
| [`metric_type`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-metric_type) | [string](/lsr/value-types.md#string), one of `["gauge", "counter", "%{metric_type}"]` | No |
| [`metric_value`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-metric_value) | <<,>> | No |
| [`queue_size`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-queue_size) | [number](/lsr/value-types.md#number) | No |
| [`timeframe`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-timeframe) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-common-options) for a list of options supported by all output plugins.

### `api_key` [v3.0.1-plugins-outputs-datadog_metrics-api_key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Your DatadogHQ API key. <https://app.datadoghq.com/account/settings#api>

### `dd_tags` [v3.0.1-plugins-outputs-datadog_metrics-dd_tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Set any custom tags for this event, default are the Logstash tags if any.

### `device` [v3.0.1-plugins-outputs-datadog_metrics-device]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{metric_device}"`

The name of the device that produced the metric.

### `host` [v3.0.1-plugins-outputs-datadog_metrics-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{host}"`

The name of the host that produced the metric.

### `metric_name` [v3.0.1-plugins-outputs-datadog_metrics-metric_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{metric_name}"`

The name of the time series.

### `metric_type` [v3.0.1-plugins-outputs-datadog_metrics-metric_type]

* Value can be any of: `gauge`, `counter`, `%{metric_type}`
* Default value is `"%{metric_type}"`

The type of the metric.

### `metric_value` [v3.0.1-plugins-outputs-datadog_metrics-metric_value]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{metric_value}"`

The value.

### `queue_size` [v3.0.1-plugins-outputs-datadog_metrics-queue_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

How many events to queue before flushing to Datadog prior to schedule set in `@timeframe`

### `timeframe` [v3.0.1-plugins-outputs-datadog_metrics-timeframe]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

How often (in seconds) to flush queued events to Datadog

## Common options [v3.0.1-plugins-outputs-datadog_metrics-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-1-plugins-outputs-datadog_metrics.md#v3.0.1-plugins-outputs-datadog_metrics-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.1-plugins-outputs-datadog_metrics-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.1-plugins-outputs-datadog_metrics-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.1-plugins-outputs-datadog_metrics-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 datadog\_metrics outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  datadog_metrics {
    id => "my_plugin_id"
  }
}
```
