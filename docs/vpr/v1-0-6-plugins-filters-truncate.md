---
navigation_title: "v1.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.6-plugins-filters-truncate.html
---

# Truncate filter plugin v1.0.6 [v1.0.6-plugins-filters-truncate]

* Plugin version: v1.0.6
* Released on: 2023-05-10
* [Changelog](https://github.com/logstash-plugins/logstash-filter-truncate/blob/v1.0.6/CHANGELOG.md)

For other versions, see the [overview list](filter-truncate-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2199]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-truncate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2177]

Allows you to truncate fields longer than a given length.

This truncates on bytes values, not character count. In practice, this should mean that the truncated length is somewhere between `length_bytes` and `length_bytes - 6` (UTF-8 supports up to 6-byte characters).

## Truncate Filter Configuration Options [v1.0.6-plugins-filters-truncate-options]

This plugin supports the following configuration options plus the [Common options](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`fields`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-fields) | [string](/lsr/value-types.md#string) | No |
| [`length_bytes`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-length_bytes) | [number](/lsr/value-types.md#number) | Yes |

Also see [Common options](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-common-options) for a list of options supported by all filter plugins.

### `fields` [v1.0.6-plugins-filters-truncate-fields]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A list of fieldrefs to truncate if they are too long.

If not specified, the default behavior will be to attempt truncation on all strings in the event. This default behavior could be computationally expensive, so if you know exactly which fields you wish to truncate, it is advised that you be specific and configure the fields you want truncated.

Special behaviors for non-string fields:

* Numbers: No action
* Array: this plugin will attempt truncation on all elements of that array.
* Hash: truncate will try all values of the hash (recursively, if this hash contains other hashes).

### `length_bytes` [v1.0.6-plugins-filters-truncate-length_bytes]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

Fields over this length will be truncated to this length.

Truncation happens from the end of the text (the start will be kept).

As an example, if you set `length_bytes => 10` and a field contains "hello world, how are you?", then this field will be truncated and have this value: "hello worl"

## Common options [v1.0.6-plugins-filters-truncate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-0-6-plugins-filters-truncate.md#v1.0.6-plugins-filters-truncate-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.0.6-plugins-filters-truncate-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      truncate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      truncate {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.0.6-plugins-filters-truncate-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      truncate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      truncate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.0.6-plugins-filters-truncate-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.6-plugins-filters-truncate-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 truncate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      truncate {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.0.6-plugins-filters-truncate-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.0.6-plugins-filters-truncate-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      truncate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      truncate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.0.6-plugins-filters-truncate-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      truncate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      truncate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
