---
navigation_title: "v3.1.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.5-plugins-outputs-statsd.html
---

# Statsd output plugin v3.1.5 [v3.1.5-plugins-outputs-statsd]

* Plugin version: v3.1.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-statsd/blob/v3.1.5/CHANGELOG.md)

For other versions, see the [overview list](output-statsd-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1629]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-statsd). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1619]

statsd is a network daemon for aggregating statistics, such as counters and timers, and shipping over UDP to backend services, such as Graphite or Datadog. The general idea is that you send metrics to statsd and every few seconds it will emit the aggregated values to the backend. Example aggregates are sums, average and maximum values, their standard deviation, etc. This plugin makes it easy to send such metrics based on data in Logstash events.

You can learn about statsd here:

* [Etsy blog post announcing statsd](https://codeascraft.com/2011/02/15/measure-anything-measure-everything/)
* [statsd on github](https://github.com/etsy/statsd)

Typical examples of how this can be used with Logstash include counting HTTP hits by response code, summing the total number of bytes of traffic served, and tracking the 50th and 95th percentile of the processing time of requests.

Each metric emitted to statsd has a dot-separated path, a type, and a value. The metric path is built from the `namespace` and `sender` options together with the metric name that’s picked up depending on the type of metric. All in all, the metric path will follow this pattern:

```
namespace.sender.metric
```

With regards to this plugin, the default namespace is "logstash", the default sender is the `host` field, and the metric name depends on what is set as the metric name in the `increment`, `decrement`, `timing`, `count`, `set` or `gauge` options. In metric paths, colons (":"), pipes ("|") and at signs ("@") are reserved and will be replaced by underscores ("\_").

Example:

```
output {
  statsd {
    host => "statsd.example.org"
    count => {
      "http.bytes" => "%{bytes}"
    }
  }
}
```

If run on a host named hal9000 the configuration above will send the following metric to statsd if the current event has 123 in its `bytes` field:

```
logstash.hal9000.http.bytes:123|c
```

## Statsd Output Configuration Options [v3.1.5-plugins-outputs-statsd-options]

This plugin supports the following configuration options plus the [Common options](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`count`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-count) | [hash](/lsr/value-types.md#hash) | No |
| [`decrement`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-decrement) | [array](/lsr/value-types.md#array) | No |
| [`gauge`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-gauge) | [hash](/lsr/value-types.md#hash) | No |
| [`host`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-host) | [string](/lsr/value-types.md#string) | No |
| [`increment`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-increment) | [array](/lsr/value-types.md#array) | No |
| [`namespace`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-namespace) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-port) | [number](/lsr/value-types.md#number) | No |
| [`sample_rate`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-sample_rate) | [number](/lsr/value-types.md#number) | No |
| [`sender`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-sender) | [string](/lsr/value-types.md#string) | No |
| [`set`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-set) | [hash](/lsr/value-types.md#hash) | No |
| [`timing`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-timing) | [hash](/lsr/value-types.md#hash) | No |

Also see [Common options](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-common-options) for a list of options supported by all output plugins.

### `count` [v3.1.5-plugins-outputs-statsd-count]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A count metric. `metric_name => count` as hash. `%{fieldname}` substitutions are allowed in the metric names.

### `decrement` [v3.1.5-plugins-outputs-statsd-decrement]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

A decrement metric. Metric names as array. `%{fieldname}` substitutions are allowed in the metric names.

### `gauge` [v3.1.5-plugins-outputs-statsd-gauge]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A gauge metric. `metric_name => gauge` as hash. `%{fieldname}` substitutions are allowed in the metric names.

### `host` [v3.1.5-plugins-outputs-statsd-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

The hostname or IP address of the statsd server.

### `increment` [v3.1.5-plugins-outputs-statsd-increment]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

An increment metric. Metric names as array. `%{fieldname}` substitutions are allowed in the metric names.

### `namespace` [v3.1.5-plugins-outputs-statsd-namespace]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

The statsd namespace to use for this metric. `%{fieldname}` substitutions are allowed.

### `port` [v3.1.5-plugins-outputs-statsd-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `8125`

The port to connect to on your statsd server.

### `sample_rate` [v3.1.5-plugins-outputs-statsd-sample_rate]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

The sample rate for the metric.

### `sender` [v3.1.5-plugins-outputs-statsd-sender]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{host}"`

The name of the sender. Dots will be replaced with underscores. `%{fieldname}` substitutions are allowed.

### `set` [v3.1.5-plugins-outputs-statsd-set]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A set metric. `metric_name => "string"` to append as hash. `%{fieldname}` substitutions are allowed in the metric names.

### `timing` [v3.1.5-plugins-outputs-statsd-timing]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A timing metric. `metric_name => duration` as hash. `%{fieldname}` substitutions are allowed in the metric names.

## Common options [v3.1.5-plugins-outputs-statsd-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-5-plugins-outputs-statsd.md#v3.1.5-plugins-outputs-statsd-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.1.5-plugins-outputs-statsd-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.5-plugins-outputs-statsd-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.5-plugins-outputs-statsd-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 statsd outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  statsd {
    id => "my_plugin_id"
  }
}
```
