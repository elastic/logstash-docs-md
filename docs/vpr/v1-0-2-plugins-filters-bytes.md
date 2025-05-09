---
navigation_title: "v1.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.2-plugins-filters-bytes.html
---

# Bytes filter plugin v1.0.2 [v1.0.2-plugins-filters-bytes]


* Plugin version: v1.0.2
* Released on: 2018-06-04
* [Changelog](https://github.com/logstash-plugins/logstash-filter-bytes/blob/v1.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-bytes-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1698]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-bytes). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1676]

Parse string representations of computer storage sizes, such as "123 MB" or "5.6gb", into their numeric value in bytes.

This plugin understands:

* bytes ("B")
* kilobytes ("KB" or "kB")
* megabytes ("MB", "mb", or "mB")
* gigabytes ("GB", "gb", or "gB")
* terabytes ("TB", "tb", or "tB")
* petabytes ("PB", "pb", or "pB")


## Examples [v1.0.2-plugins-filters-bytes-examples]

| Input string | Conversion method |
| --- | --- |
| Numeric value in bytes | 40 |
| `binary` or `metric` | 40 |
| 40B | `binary` or `metric` |
| 40 | 40 B |
| `binary` or `metric` | 40 |
| 40KB | `binary` |
| 40960 | 40kB |
| `binary` | 40960 |
| 40KB | `metric` |
| 40000 | 40.5KB |
| `binary` | 41472 |
| 40kb | `binary` |
| 5120 | 40Kb |
| `binary` | 5120 |
| 10 MB | `binary` |
| 10485760 | 10 mB |
| `binary` | 10485760 |
| 10 mb | `binary` |
| 10485760 | 10 Mb |
| `binary` | 1310720 |

```ruby
    filter {
      bytes {
        source => "my_bytes_string_field"
        target => "my_bytes_numeric_field"
      }
    }
```


## Bytes Filter Configuration Options [v1.0.2-plugins-filters-bytes-options]

This plugin supports the following configuration options plus the [Common options](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`source`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`target`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-target) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`conversion_method`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-conversion_method) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`source`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-decimal_separator) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-common-options) for a list of options supported by all filter plugins.

 

### `source` [v1.0.2-plugins-filters-bytes-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `message`

Name of the source field that contains the storage size


### `target` [v1.0.2-plugins-filters-bytes-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)

Name of the target field that will contain the storage size in bytes


### `conversion_method` [v1.0.2-plugins-filters-bytes-conversion_method]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Value can be any of: `binary`, `metric`
* Default value is `binary`

Which conversion method to use when converting to bytes. `binary` uses `1K = 1024B`. `metric` uses `1K = 1000B`.


### `source` [v1.0.2-plugins-filters-bytes-decimal_separator]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `.`

Separator, if any, used as the decimal. This value is only used if the plugin cannot guess the decimal separator by looking at the string in the `source` field.



## Common options [v1.0.2-plugins-filters-bytes-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v1-0-2-plugins-filters-bytes.md#v1.0.2-plugins-filters-bytes-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v1.0.2-plugins-filters-bytes-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      bytes {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      bytes {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v1.0.2-plugins-filters-bytes-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      bytes {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      bytes {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v1.0.2-plugins-filters-bytes-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.2-plugins-filters-bytes-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 bytes filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      bytes {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v1.0.2-plugins-filters-bytes-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v1.0.2-plugins-filters-bytes-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      bytes {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      bytes {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v1.0.2-plugins-filters-bytes-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      bytes {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      bytes {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



