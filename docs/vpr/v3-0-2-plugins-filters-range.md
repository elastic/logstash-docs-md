---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-filters-range.html
---

# Range filter plugin v3.0.2 [v3.0.2-plugins-filters-range]


* Plugin version: v3.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-range/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-range-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2117]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-range). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2095]

This filter is used to check that certain fields are within expected size/length ranges. Supported types are numbers and strings. Numbers are checked to be within numeric value range. Strings are checked to be within string length range. More than one range can be specified for same fieldname, actions will be applied incrementally. When field value is within a specified range an action will be taken. Supported actions are drop event, add tag, or add field with specified value.

Example use cases are for histogram-like tagging of events or for finding anomaly values in fields or too big events that should be dropped.


## Range Filter Configuration Options [v3.0.2-plugins-filters-range-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`negate`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-negate) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ranges`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-ranges) | [array](logstash://reference/configuration-file-structure.md#array) | No |

Also see [Common options](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-common-options) for a list of options supported by all filter plugins.

 

### `negate` [v3.0.2-plugins-filters-range-negate]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Negate the range match logic, events should be outsize of the specified range to match.


### `ranges` [v3.0.2-plugins-filters-range-ranges]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

An array of field, min, max, action tuples. Example:

```ruby
    filter {
      range {
        ranges => [ "message", 0, 10, "tag:short",
                    "message", 11, 100, "tag:medium",
                    "message", 101, 1000, "tag:long",
                    "message", 1001, 1e1000, "drop",
                    "duration", 0, 100, "field:latency:fast",
                    "duration", 101, 200, "field:latency:normal",
                    "duration", 201, 1000, "field:latency:slow",
                    "duration", 1001, 1e1000, "field:latency:outlier",
                    "requests", 0, 10, "tag:too_few_%{host}_requests" ]
      }
    }
```

Supported actions are drop tag or field with specified value. Added tag names and field names and field values can have `%{{dynamic}}` values.



## Common options [v3.0.2-plugins-filters-range-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-2-plugins-filters-range.md#v3.0.2-plugins-filters-range-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.2-plugins-filters-range-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      range {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      range {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.2-plugins-filters-range-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      range {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      range {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.2-plugins-filters-range-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-filters-range-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 range filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      range {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.2-plugins-filters-range-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.2-plugins-filters-range-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      range {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      range {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.2-plugins-filters-range-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      range {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      range {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



