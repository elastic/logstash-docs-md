---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-extractnumbers.html
---

# Extractnumbers filter plugin v3.0.3 [v3.0.3-plugins-filters-extractnumbers]


* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-extractnumbers/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-extractnumbers-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1848]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-extractnumbers). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1826]

This filter automatically extracts all numbers found inside a string

This is useful when you have lines that don’t match a grok pattern or use json but you still need to extract numbers.

Each numbers is returned in a `@fields.intX` or `@fields.floatX` field where X indicates the position in the string.

The fields produced by this filter are extra useful used in combination with kibana number plotting features.


## Extractnumbers Filter Configuration Options [v3.0.3-plugins-filters-extractnumbers-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`source`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-common-options) for a list of options supported by all filter plugins.

 

### `source` [v3.0.3-plugins-filters-extractnumbers-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The source field for the data. By default is message.



## Common options [v3.0.3-plugins-filters-extractnumbers-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-extractnumbers.md#v3.0.3-plugins-filters-extractnumbers-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-extractnumbers-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      extractnumbers {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      extractnumbers {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.3-plugins-filters-extractnumbers-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      extractnumbers {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      extractnumbers {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.3-plugins-filters-extractnumbers-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-filters-extractnumbers-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 extractnumbers filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      extractnumbers {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.3-plugins-filters-extractnumbers-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.3-plugins-filters-extractnumbers-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      extractnumbers {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      extractnumbers {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.3-plugins-filters-extractnumbers-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      extractnumbers {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      extractnumbers {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



