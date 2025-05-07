---
navigation_title: "v3.1.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.5-plugins-outputs-graphite.html
---

# Graphite output plugin v3.1.5 [v3.1.5-plugins-outputs-graphite]


* Plugin version: v3.1.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-graphite/blob/v3.1.5/CHANGELOG.md)

For other versions, see the [overview list](output-graphite-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1282]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-graphite). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1275]

This output allows you to pull metrics from your logs and ship them to Graphite. Graphite is an open source tool for storing and graphing metrics.

An example use case: Some applications emit aggregated stats in the logs every 10 seconds. Using the grok filter and this output, it is possible to capture the metric values from the logs and emit them to Graphite.


## Graphite Output Configuration Options [v3.1.5-plugins-outputs-graphite-options]

This plugin supports the following configuration options plus the [Common options](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`exclude_metrics`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-exclude_metrics) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`fields_are_metrics`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-fields_are_metrics) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`host`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`include_metrics`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-include_metrics) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`metrics`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-metrics) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`metrics_format`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-metrics_format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`nested_object_separator`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-nested_object_separator) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`port`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`reconnect_interval`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-reconnect_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`resend_on_failure`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-resend_on_failure) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`timestamp_field`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-timestamp_field) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-common-options) for a list of options supported by all output plugins.

 

### `exclude_metrics` [v3.1.5-plugins-outputs-graphite-exclude_metrics]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["%{[^}]+}"]`

Exclude regex matched metric names, by default exclude unresolved `%{{field}}` strings.


### `fields_are_metrics` [v3.1.5-plugins-outputs-graphite-fields_are_metrics]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

An array indicating that these event fields should be treated as metrics and will be sent verbatim to Graphite. You may use either `fields_are_metrics` or `metrics`, but not both.


### `host` [v3.1.5-plugins-outputs-graphite-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

The hostname or IP address of the Graphite server.


### `include_metrics` [v3.1.5-plugins-outputs-graphite-include_metrics]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[".*"]`

Include only regex matched metric names.


### `metrics` [v3.1.5-plugins-outputs-graphite-metrics]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

The metric(s) to use. This supports dynamic strings like `%{{host}}` for metric names and also for values. This is a hash field with key being the metric name, value being the metric value. Example:

```ruby
    metrics => { "%{host}/uptime" => "%{uptime_1m}" }
```

The value will be coerced to a floating point value. Values which cannot be coerced will be set to zero (0). You may use either `metrics` or `fields_are_metrics`, but not both.


### `metrics_format` [v3.1.5-plugins-outputs-graphite-metrics_format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"*"`

Defines the format of the metric string. The placeholder *** will be replaced with the name of the actual metric.

```ruby
    metrics_format => "foo.bar.*.sum"
```

::::{note}
If no metrics_format is defined, the name of the metric will be used as fallback.
::::



### `nested_object_separator` [v3.1.5-plugins-outputs-graphite-nested_object_separator]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"."`

When hashes are passed in as values they are broken out into a dotted notation For instance if you configure this plugin with `metrics ⇒ "mymetrics` and "mymetrics" is a nested hash of *{a ⇒ 1, b ⇒ { c ⇒ 2 }}* this plugin will generate two metrics: a ⇒ 1, and b.c ⇒ 2 . If you’ve specified a *metrics_format* it will respect that, but you still may want control over the separator within these nested key names. This config setting changes the separator from the *.* default.


### `port` [v3.1.5-plugins-outputs-graphite-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2003`

The port to connect to on the Graphite server.


### `reconnect_interval` [v3.1.5-plugins-outputs-graphite-reconnect_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Interval between reconnect attempts to Carbon.


### `resend_on_failure` [v3.1.5-plugins-outputs-graphite-resend_on_failure]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Should metrics be resent on failure?


### `timestamp_field` [v3.1.5-plugins-outputs-graphite-timestamp_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"@timestamp"`

Use this field for the timestamp instead of *@timestamp* which is the default. Useful when backfilling or just getting more accurate data into graphite since you probably have a cache layer infront of Logstash.



## Common options [v3.1.5-plugins-outputs-graphite-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-5-plugins-outputs-graphite.md#v3.1.5-plugins-outputs-graphite-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.5-plugins-outputs-graphite-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.5-plugins-outputs-graphite-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.5-plugins-outputs-graphite-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 graphite outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  graphite {
    id => "my_plugin_id"
  }
}
```



