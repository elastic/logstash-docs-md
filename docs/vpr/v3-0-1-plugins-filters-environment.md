---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-filters-environment.html
---

# Environment filter plugin v3.0.1 [v3.0.1-plugins-filters-environment]

* Plugin version: v3.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-environment/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](filter-environment-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1871]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-environment). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1849]

This filter stores environment variables as subfields in the `@metadata` field. You can then use these values in other parts of the pipeline.

Adding environment variables is as easy as: filter { environment { add\_metadata\_from\_env ⇒ { "field\_name" ⇒ "ENV\_VAR\_NAME" } } }

Accessing stored environment variables is now done through the `@metadata` field:

```
["@metadata"]["field_name"]
```

This would reference field `field_name`, which in the above example references the `ENV_VAR_NAME` environment variable.

Previous versions of this plugin put the environment variables as fields at the root level of the event. Current versions make use of the `@metadata` field, as outlined. You have to change `add_field_from_env` in the older versions to `add_metadata_from_env` in the newer version.

## Environment Filter Configuration Options [v3.0.1-plugins-filters-environment-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_metadata_from_env`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-add_metadata_from_env) | [hash](/lsr/value-types.md#hash) | No |

Also see [Common options](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-common-options) for a list of options supported by all filter plugins.

### `add_metadata_from_env` [v3.0.1-plugins-filters-environment-add_metadata_from_env]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Specify a hash of field names and the environment variable name with the value you want imported into Logstash. For example:

```
add_metadata_from_env => { "field_name" => "ENV_VAR_NAME" }
```

or

```
add_metadata_from_env => {
  "field1" => "ENV1"
  "field2" => "ENV2"
  # "field_n" => "ENV_n"
}
```

## Common options [v3.0.1-plugins-filters-environment-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-1-plugins-filters-environment.md#v3.0.1-plugins-filters-environment-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.1-plugins-filters-environment-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      environment {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      environment {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.1-plugins-filters-environment-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      environment {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      environment {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.1-plugins-filters-environment-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.1-plugins-filters-environment-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 environment filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      environment {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.1-plugins-filters-environment-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.1-plugins-filters-environment-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      environment {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      environment {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.1-plugins-filters-environment-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      environment {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      environment {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
