---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-filters-punct.html
---

# Punct filter plugin v2.0.5 [v2.0.5-plugins-filters-punct]


* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-punct/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](filter-punct-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2115]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-punct). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2093]

Strip everything but punctuation from a field and store the remainder in the a separate field. This is often used for fingerprinting log events.


## Punct Filter Configuration Options [v2.0.5-plugins-filters-punct-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`source`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`target`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-common-options) for a list of options supported by all filter plugins.

 

### `source` [v2.0.5-plugins-filters-punct-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The field reference to use for punctuation stripping


### `target` [v2.0.5-plugins-filters-punct-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"punct"`

The field to store the result.



## Common options [v2.0.5-plugins-filters-punct-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v2-0-5-plugins-filters-punct.md#v2.0.5-plugins-filters-punct-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v2.0.5-plugins-filters-punct-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      punct {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      punct {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v2.0.5-plugins-filters-punct-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      punct {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      punct {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v2.0.5-plugins-filters-punct-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.5-plugins-filters-punct-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 punct filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      punct {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v2.0.5-plugins-filters-punct-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v2.0.5-plugins-filters-punct-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      punct {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      punct {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v2.0.5-plugins-filters-punct-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      punct {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      punct {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



