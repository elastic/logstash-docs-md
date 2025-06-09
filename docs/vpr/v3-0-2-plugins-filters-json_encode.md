---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-filters-json_encode.html
---

# Json_encode filter plugin v3.0.2 [v3.0.2-plugins-filters-json_encode]

* Plugin version: v3.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-json_encode/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-json_encode-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2078]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-json_encode). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2056]

JSON encode filter. Takes a field and serializes it into JSON

If no target is specified, the source field is overwritten with the JSON text.

For example, if you have a field named `foo`, and you want to store the JSON encoded string in `bar`, do this:

```
    filter {
      json_encode {
        source => "foo"
        target => "bar"
      }
    }
```

## Json_encode Filter Configuration Options [v3.0.2-plugins-filters-json_encode-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`source`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-source) | [string](/lsr/value-types.md#string) | Yes |
| [`target`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-common-options) for a list of options supported by all filter plugins.

### `source` [v3.0.2-plugins-filters-json_encode-source]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field to convert to JSON.

### `target` [v3.0.2-plugins-filters-json_encode-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field to write the JSON into. If not specified, the source field will be overwritten.

## Common options [v3.0.2-plugins-filters-json_encode-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-2-plugins-filters-json_encode.md#v3.0.2-plugins-filters-json_encode-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.2-plugins-filters-json_encode-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      json_encode {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      json_encode {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.2-plugins-filters-json_encode-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      json_encode {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      json_encode {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.2-plugins-filters-json_encode-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.2-plugins-filters-json_encode-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 json\_encode filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      json_encode {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.2-plugins-filters-json_encode-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.2-plugins-filters-json_encode-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      json_encode {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      json_encode {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.2-plugins-filters-json_encode-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      json_encode {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      json_encode {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
