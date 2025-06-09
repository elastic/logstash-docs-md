---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-codecs-graphite.html
---

# Graphite codec plugin v3.0.3 [v3.0.3-plugins-codecs-graphite]

* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-graphite/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](codec-graphite-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2350]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-graphite). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2328]

This codec will encode and decode Graphite formated lines.

## Graphite Codec Configuration Options [v3.0.3-plugins-codecs-graphite-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`exclude_metrics`](v3-0-3-plugins-codecs-graphite.md#v3.0.3-plugins-codecs-graphite-exclude_metrics) | [array](/lsr/value-types.md#array) | No |
| [`fields_are_metrics`](v3-0-3-plugins-codecs-graphite.md#v3.0.3-plugins-codecs-graphite-fields_are_metrics) | [boolean](/lsr/value-types.md#boolean) | No |
| [`include_metrics`](v3-0-3-plugins-codecs-graphite.md#v3.0.3-plugins-codecs-graphite-include_metrics) | [array](/lsr/value-types.md#array) | No |
| [`metrics`](v3-0-3-plugins-codecs-graphite.md#v3.0.3-plugins-codecs-graphite-metrics) | [hash](/lsr/value-types.md#hash) | No |
| [`metrics_format`](v3-0-3-plugins-codecs-graphite.md#v3.0.3-plugins-codecs-graphite-metrics_format) | [string](/lsr/value-types.md#string) | No |

### `exclude_metrics` [v3.0.3-plugins-codecs-graphite-exclude_metrics]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["%{[^}]+}"]`

Exclude regex matched metric names, by default exclude unresolved %{field} strings

### `fields_are_metrics` [v3.0.3-plugins-codecs-graphite-fields_are_metrics]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Indicate that the event @fields should be treated as metrics and will be sent as is to graphite

### `include_metrics` [v3.0.3-plugins-codecs-graphite-include_metrics]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[".*"]`

Include only regex matched metric names

### `metrics` [v3.0.3-plugins-codecs-graphite-metrics]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

The metric(s) to use. This supports dynamic strings like `%{host}` for metric names and also for values. This is a hash field with key of the metric name, value of the metric value. Example:

```
    [ "%{host}/uptime", "%{uptime_1m}" ]
```

The value will be coerced to a floating point value. Values which cannot be coerced will zero (0)

### `metrics_format` [v3.0.3-plugins-codecs-graphite-metrics_format]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"*"`

Defines format of the metric string. The placeholder `*` will be replaced with the name of the actual metric. This supports dynamic strings like `%{host}`.

```
    metrics_format => "%{host}.foo.bar.*.sum"
```

If no metrics\_format is defined the name of the metric will be used as fallback.
