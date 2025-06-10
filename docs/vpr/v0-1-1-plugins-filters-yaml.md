---
navigation_title: "v0.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.1.1-plugins-filters-yaml.html
---

# Yaml filter plugin v0.1.1 [v0.1.1-plugins-filters-yaml]

* Plugin version: v0.1.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-yaml/blob/v0.1.1/CHANGELOG.md)

For other versions, see the [overview list](filter-yaml-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2242]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-yaml). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2220]

This is a YAML parsing filter. It takes an existing field which contains YAML and expands it into an actual data structure within the Logstash event.

By default it will place the parsed YAML in the root (top level) of the Logstash event, but this filter can be configured to place the YAML into any arbitrary event field, using the `target` configuration.

## Yaml Filter Configuration Options [v0.1.1-plugins-filters-yaml-options]

This plugin supports the following configuration options plus the [Common options](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`source`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-source) | [string](/lsr/value-types.md#string) | Yes |
| [`target`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-common-options) for a list of options supported by all filter plugins.

### `exclude_tags` (DEPRECATED) [v0.1.1-plugins-filters-yaml-exclude_tags]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Only handle events without any of these tags. Optional.

### `source` [v0.1.1-plugins-filters-yaml-source]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The configuration for the YAML filter:

```
    source => source_field
```

For example, if you have YAML data in the @message field:

```
    filter {
      yaml {
        source => "message"
      }
    }
```

The above would parse the yaml from the @message field

### `target` [v0.1.1-plugins-filters-yaml-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define the target field for placing the parsed data. If this setting is omitted, the YAML data will be stored at the root (top level) of the event.

For example, if you want the data to be put in the `doc` field:

```
    filter {
      yaml {
        target => "doc"
      }
    }
```

YAML in the value of the `source` field will be expanded into a data structure in the `target` field.

if the `target` field already exists, it will be overwritten!

## Common options [v0.1.1-plugins-filters-yaml-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v0-1-1-plugins-filters-yaml.md#v0.1.1-plugins-filters-yaml-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v0.1.1-plugins-filters-yaml-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      yaml {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      yaml {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v0.1.1-plugins-filters-yaml-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      yaml {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      yaml {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v0.1.1-plugins-filters-yaml-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v0.1.1-plugins-filters-yaml-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 yaml filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      yaml {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v0.1.1-plugins-filters-yaml-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v0.1.1-plugins-filters-yaml-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      yaml {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      yaml {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v0.1.1-plugins-filters-yaml-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      yaml {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      yaml {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
