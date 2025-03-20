---
navigation_title: "v1.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.2-plugins-filters-de_dot.html
---

# De_dot filter plugin v1.0.2 [v1.0.2-plugins-filters-de_dot]


* Plugin version: v1.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-de_dot/blob/v1.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-de_dot-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1745]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-de_dot). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1723]

This filter *appears* to rename fields by replacing `.` characters with a different separator.  In reality, it’s a somewhat expensive filter that has to copy the source field contents to a new destination field (whose name no longer contains dots), and then remove the corresponding source field.

It should only be used if no other options are available.


## De_dot Filter Configuration Options [v1.0.2-plugins-filters-de_dot-options]

This plugin supports the following configuration options plus the [Common options](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`fields`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`nested`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-nested) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`separator`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-separator) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-common-options) for a list of options supported by all filter plugins.

 

### `fields` [v1.0.2-plugins-filters-de_dot-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The `fields` array should contain a list of known fields to act on. If undefined, all top-level fields will be checked.  Sub-fields must be manually specified in the array.  For example: `["field.suffix","[foo][bar.suffix]"]` will result in "field_suffix" and nested or sub field ["foo"]["bar_suffix"]

::::{warning}
This is an expensive operation.
::::



### `nested` [v1.0.2-plugins-filters-de_dot-nested]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If `nested` is *true*, then create sub-fields instead of replacing dots with a different separator.


### `separator` [v1.0.2-plugins-filters-de_dot-separator]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_"`

Replace dots with this value.



## Common options [v1.0.2-plugins-filters-de_dot-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v1-0-2-plugins-filters-de_dot.md#v1.0.2-plugins-filters-de_dot-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v1.0.2-plugins-filters-de_dot-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      de_dot {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      de_dot {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v1.0.2-plugins-filters-de_dot-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      de_dot {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      de_dot {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v1.0.2-plugins-filters-de_dot-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.2-plugins-filters-de_dot-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 de_dot filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      de_dot {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v1.0.2-plugins-filters-de_dot-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v1.0.2-plugins-filters-de_dot-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      de_dot {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      de_dot {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v1.0.2-plugins-filters-de_dot-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      de_dot {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      de_dot {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



