---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-metricize.html
---

# Metricize filter plugin v3.0.3 [v3.0.3-plugins-filters-metricize]

* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-metricize/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-metricize-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2111]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-metricize). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2089]

The metricize filter takes complex events containing a number of metrics and splits these up into multiple events, each holding a single metric.

Example:

```
Assume the following filter configuration:
```

```
filter {
  metricize {
    metrics => [ "metric1", "metric2" ]
  }
}
```

```
Assuming the following event is passed in:
```

```
{
     type => "type A"
     metric1 => "value1"
     metric2 => "value2"
}
```

```
This will result in the following 2 events being generated in addition to the original event:
```

```
{                               {
    type => "type A"                type => "type A"
    metric => "metric1"             metric => "metric2"
    value => "value1"               value => "value2"
}                               }
```

## Metricize Filter Configuration Options [v3.0.3-plugins-filters-metricize-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`drop_original_event`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-drop_original_event) | [boolean](/lsr/value-types.md#boolean) | No |
| [`metric_field_name`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-metric_field_name) | [string](/lsr/value-types.md#string) | No |
| [`metrics`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-metrics) | [array](/lsr/value-types.md#array) | Yes |
| [`value_field_name`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-value_field_name) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-common-options) for a list of options supported by all filter plugins.

### `drop_original_event` [v3.0.3-plugins-filters-metricize-drop_original_event]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Flag indicating whether the original event should be dropped or not.

### `metric_field_name` [v3.0.3-plugins-filters-metricize-metric_field_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"metric"`

Name of the field the metric name will be written to.

### `metrics` [v3.0.3-plugins-filters-metricize-metrics]

* This is a required setting.
* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

A new matrics event will be created for each metric field in this list. All fields in this list will be removed from generated events.

### `value_field_name` [v3.0.3-plugins-filters-metricize-value_field_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"value"`

Name of the field the metric value will be written to.

## Common options [v3.0.3-plugins-filters-metricize-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-metricize.md#v3.0.3-plugins-filters-metricize-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-metricize-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      metricize {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      metricize {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.3-plugins-filters-metricize-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      metricize {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      metricize {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.3-plugins-filters-metricize-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-filters-metricize-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 metricize filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      metricize {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.3-plugins-filters-metricize-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.3-plugins-filters-metricize-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      metricize {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      metricize {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.3-plugins-filters-metricize-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      metricize {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      metricize {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
