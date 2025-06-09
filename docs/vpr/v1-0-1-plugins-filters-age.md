---
navigation_title: "v1.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.1-plugins-filters-age.html
---

# Age filter plugin v1.0.1 [v1.0.1-plugins-filters-age]

* Plugin version: v1.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-age/blob/v1.0.1/CHANGELOG.md)

For other versions, see the [overview list](filter-age-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1694]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-age). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1684]

A simple filter for calculating the age of an event.

This filter calculates the age of an event by subtracting the event timestamp from the current timestamp. This allows you to drop Logstash events that are older than some threshold.

```
filter {
  age {}
```

```
  if [@metadata][age] > 86400 {
    drop {}
  }
}
```

## Age Filter Configuration Options [v1.0.1-plugins-filters-age-options]

This plugin supports the following configuration options plus the [Common options](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`target`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-common-options) for a list of options supported by all filter plugins.

### `target` [v1.0.1-plugins-filters-age-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"[@metadata][age]"`

Define the target field for the event age, in seconds.

## Common options [v1.0.1-plugins-filters-age-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-0-1-plugins-filters-age.md#v1.0.1-plugins-filters-age-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.0.1-plugins-filters-age-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      age {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      age {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.0.1-plugins-filters-age-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      age {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      age {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.0.1-plugins-filters-age-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.1-plugins-filters-age-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 age filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      age {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.0.1-plugins-filters-age-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.0.1-plugins-filters-age-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      age {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      age {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.0.1-plugins-filters-age-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      age {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      age {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
