---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-alter.html
---

# Alter filter plugin v3.0.3 [v3.0.3-plugins-filters-alter]

* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-alter/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-alter-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1709]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-alter). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1687]

The alter filter allows you to do general alterations to fields that are not included in the normal mutate filter.

The functionality provided by this plugin is likely to be merged into the *mutate* filter in future versions.

## Alter Filter Configuration Options [v3.0.3-plugins-filters-alter-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`coalesce`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-coalesce) | [array](/lsr/value-types.md#array) | No |
| [`condrewrite`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-condrewrite) | [array](/lsr/value-types.md#array) | No |
| [`condrewriteother`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-condrewriteother) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-common-options) for a list of options supported by all filter plugins.

### `coalesce` [v3.0.3-plugins-filters-alter-coalesce]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Sets the value of field\_name to the first nonnull expression among its arguments.

Example:

```
    filter {
      alter {
        coalesce => [
             "field_name", "value1", "value2", "value3", ...
        ]
      }
    }
```

### `condrewrite` [v3.0.3-plugins-filters-alter-condrewrite]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Change the content of the field to the specified value if the actual content is equal to the expected one.

Example:

```
    filter {
      alter {
        condrewrite => [
             "field_name", "expected_value", "new_value",
             "field_name2", "expected_value2", "new_value2",
             ....
           ]
      }
    }
```

### `condrewriteother` [v3.0.3-plugins-filters-alter-condrewriteother]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Change the content of the field to the specified value if the content of another field is equal to the expected one.

Example:

```
    filter {
      alter {
        condrewriteother => [
             "field_name", "expected_value", "field_name_to_change", "value",
             "field_name2", "expected_value2", "field_name_to_change2", "value2",
             ....
        ]
      }
    }
```

## Common options [v3.0.3-plugins-filters-alter-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-alter.md#v3.0.3-plugins-filters-alter-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-alter-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      alter {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      alter {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.3-plugins-filters-alter-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      alter {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      alter {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.3-plugins-filters-alter-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-filters-alter-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 alter filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      alter {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.3-plugins-filters-alter-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.3-plugins-filters-alter-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      alter {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      alter {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.3-plugins-filters-alter-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      alter {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      alter {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
