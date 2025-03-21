---
navigation_title: "metricize"
---

# Metricize filter plugin [plugins-filters-metricize]


* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-metricize/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/filter-metricize-index.md).

## Installation [_installation_63]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-filter-metricize`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html) for more details.


## Getting help [_getting_help_153]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-metricize). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_151]

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

## Metricize Filter Configuration Options [plugins-filters-metricize-options]

This plugin supports the following configuration options plus the [Common options](plugins-filters-metricize.md#plugins-filters-metricize-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`drop_original_event`](plugins-filters-metricize.md#plugins-filters-metricize-drop_original_event) | [boolean](introduction.md#boolean) | No |
| [`metric_field_name`](plugins-filters-metricize.md#plugins-filters-metricize-metric_field_name) | [string](introduction.md#string) | No |
| [`metrics`](plugins-filters-metricize.md#plugins-filters-metricize-metrics) | [array](introduction.md#array) | Yes |
| [`value_field_name`](plugins-filters-metricize.md#plugins-filters-metricize-value_field_name) | [string](introduction.md#string) | No |

Also see [Common options](plugins-filters-metricize.md#plugins-filters-metricize-common-options) for a list of options supported by all filter plugins.

 

### `drop_original_event` [plugins-filters-metricize-drop_original_event]

* Value type is [boolean](introduction.md#boolean)
* Default value is `false`

Flag indicating whether the original event should be dropped or not.


### `metric_field_name` [plugins-filters-metricize-metric_field_name]

* Value type is [string](introduction.md#string)
* Default value is `"metric"`

Name of the field the metric name will be written to.


### `metrics` [plugins-filters-metricize-metrics]

* This is a required setting.
* Value type is [array](introduction.md#array)
* There is no default value for this setting.

A new matrics event will be created for each metric field in this list. All fields in this list will be removed from generated events.


### `value_field_name` [plugins-filters-metricize-value_field_name]

* Value type is [string](introduction.md#string)
* Default value is `"value"`

Name of the field the metric value will be written to.



## Common options [plugins-filters-metricize-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](plugins-filters-metricize.md#plugins-filters-metricize-add_field) | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`add_tag`](plugins-filters-metricize.md#plugins-filters-metricize-add_tag) | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`enable_metric`](plugins-filters-metricize.md#plugins-filters-metricize-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-filters-metricize.md#plugins-filters-metricize-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`periodic_flush`](plugins-filters-metricize.md#plugins-filters-metricize-periodic_flush) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`remove_field`](plugins-filters-metricize.md#plugins-filters-metricize-remove_field) | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`remove_tag`](plugins-filters-metricize.md#plugins-filters-metricize-remove_tag) | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |

### `add_field` [plugins-filters-metricize-add_field]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      metricize {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [plugins-filters-metricize-add_tag]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      metricize {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      metricize {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [plugins-filters-metricize-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-filters-metricize-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 metricize filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      metricize {
        id => "ABC"
      }
    }
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::



### `periodic_flush` [plugins-filters-metricize-periodic_flush]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [plugins-filters-metricize-remove_field]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      metricize {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      metricize {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [plugins-filters-metricize-remove_tag]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      metricize {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      metricize {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



