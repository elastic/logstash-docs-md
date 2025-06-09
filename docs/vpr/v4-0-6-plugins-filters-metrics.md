---
navigation_title: "v4.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.6-plugins-filters-metrics.html
---

# Metrics filter plugin v4.0.6 [v4.0.6-plugins-filters-metrics]

* Plugin version: v4.0.6
* Released on: 2019-02-05
* [Changelog](https://github.com/logstash-plugins/logstash-filter-metrics/blob/v4.0.6/CHANGELOG.md)

For other versions, see the [overview list](filter-metrics-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2115]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-metrics). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2093]

The metrics filter is useful for aggregating metrics.

Elasticsearch 2.0 no longer allows field names with dots. Version 3.0 of the metrics filter plugin changes behavior to use nested fields rather than dotted notation to avoid colliding with versions of Elasticsearch 2.0+. Please note the changes in the documentation (underscores and sub-fields used).

For example, if you have a field `response` that is a http response code, and you want to count each kind of response, you can do this:

```
    filter {
      metrics {
        meter => [ "http_%{response}" ]
        add_tag => "metric"
      }
    }
```

Metrics are flushed every 5 seconds by default or according to `flush_interval`. Metrics appear as new events in the event stream and go through any filters that occur after as well as outputs.

In general, you will want to add a tag to your metrics and have an output explicitly look for that tag.

The event that is flushed will include every *meter* and *timer* metric in the following way:

## `meter` values [_meter_values_2]

For a `meter => "thing"` you will receive the following fields:

* "\[thing]\[count]" - the total count of events
* "\[thing]\[rate\_1m]" - the per-second event rate in a 1-minute sliding window
* "\[thing]\[rate\_5m]" - the per-second event rate in a 5-minute sliding window
* "\[thing]\[rate\_15m]" - the per-second event rate in a 15-minute sliding window

## `timer` values [_timer_values_2]

For a `timer => { "thing" => "%{duration}" }` you will receive the following fields:

* "\[thing]\[count]" - the total count of events
* "\[thing]\[rate\_1m]" - the per-second average value in a 1-minute sliding window
* "\[thing]\[rate\_5m]" - the per-second average value in a 5-minute sliding window
* "\[thing]\[rate\_15m]" - the per-second average value in a 15-minute sliding window
* "\[thing]\[min]" - the minimum value seen for this metric
* "\[thing]\[max]" - the maximum value seen for this metric
* "\[thing]\[stddev]" - the standard deviation for this metric
* "\[thing]\[mean]" - the mean for this metric
* "\[thing]\[pXX]" - the XXth percentile for this metric (see `percentiles`)

The default lengths of the event rate window (1, 5, and 15 minutes) can be configured with the `rates` option.

## Example: Computing event rate [_example_computing_event_rate_2]

For a simple example, let’s track how many events per second are running through logstash:

```
    input {
      generator {
        type => "generated"
      }
    }

    filter {
      if [type] == "generated" {
        metrics {
          meter => "events"
          add_tag => "metric"
        }
      }
    }

    output {
      # only emit events with the 'metric' tag
      if "metric" in [tags] {
        stdout {
          codec => line {
            format => "rate: %{[events][rate_1m]}"
          }
        }
      }
    }
```

Running the above:

```
    % bin/logstash -f example.conf
    rate: 23721.983566819246
    rate: 24811.395722536377
    rate: 25875.892745934525
    rate: 26836.42375967113
```

We see the output includes our events' 1-minute rate.

In the real world, you would emit this to graphite or another metrics store, like so:

```
    output {
      graphite {
        metrics => [ "events.rate_1m", "%{[events][rate_1m]}" ]
      }
    }
```

## Metrics Filter Configuration Options [v4.0.6-plugins-filters-metrics-options]

This plugin supports the following configuration options plus the [Common options](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`clear_interval`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-clear_interval) | [number](/lsr/value-types.md#number) | No |
| [`flush_interval`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-flush_interval) | [number](/lsr/value-types.md#number) | No |
| [`ignore_older_than`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-ignore_older_than) | [number](/lsr/value-types.md#number) | No |
| [`meter`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-meter) | [array](/lsr/value-types.md#array) | No |
| [`percentiles`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-percentiles) | [array](/lsr/value-types.md#array) | No |
| [`rates`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-rates) | [array](/lsr/value-types.md#array) | No |
| [`timer`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-timer) | [hash](/lsr/value-types.md#hash) | No |

Also see [Common options](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-common-options) for a list of options supported by all filter plugins.

### `clear_interval` [v4.0.6-plugins-filters-metrics-clear_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `-1`

The clear interval, when all counters are reset.

If set to -1, the default value, the metrics will never be cleared. Otherwise, should be a multiple of 5s.

### `flush_interval` [v4.0.6-plugins-filters-metrics-flush_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

The flush interval, when the metrics event is created. Must be a multiple of 5s.

### `ignore_older_than` [v4.0.6-plugins-filters-metrics-ignore_older_than]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

Don’t track events that have `@timestamp` older than some number of seconds.

This is useful if you want to only include events that are near real-time in your metrics.

For example, to only count events that are within 10 seconds of real-time, you would do this:

```
filter {
  metrics {
    meter => [ "hits" ]
    ignore_older_than => 10
  }
}
```

### `meter` [v4.0.6-plugins-filters-metrics-meter]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

syntax: `meter => [ "name of metric", "name of metric" ]`

### `percentiles` [v4.0.6-plugins-filters-metrics-percentiles]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[1, 5, 10, 90, 95, 99, 100]`

The percentiles that should be measured and emitted for timer values.

### `rates` [v4.0.6-plugins-filters-metrics-rates]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[1, 5, 15]`

The rates that should be measured, in minutes. Possible values are 1, 5, and 15.

### `timer` [v4.0.6-plugins-filters-metrics-timer]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

syntax: `timer => [ "name of metric", "%{time_value}" ]`

## Common options [v4.0.6-plugins-filters-metrics-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-0-6-plugins-filters-metrics.md#v4.0.6-plugins-filters-metrics-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.0.6-plugins-filters-metrics-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      metrics {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      metrics {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.0.6-plugins-filters-metrics-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      metrics {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      metrics {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.0.6-plugins-filters-metrics-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.6-plugins-filters-metrics-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 metrics filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      metrics {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.0.6-plugins-filters-metrics-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.0.6-plugins-filters-metrics-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      metrics {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      metrics {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.0.6-plugins-filters-metrics-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      metrics {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      metrics {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
