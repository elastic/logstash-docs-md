---
navigation_title: "v3.1.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.6-plugins-filters-split.html
---

# Split filter plugin v3.1.6 [v3.1.6-plugins-filters-split]

* Plugin version: v3.1.6
* Released on: 2017-12-11
* [Changelog](https://github.com/logstash-plugins/logstash-filter-split/blob/v3.1.6/CHANGELOG.md)

For other versions, see the [overview list](filter-split-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2164]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-split). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2142]

The split filter clones an event by splitting one of its fields and placing each value resulting from the split into a clone of the original event. The field being split can either be a string or an array.

An example use case of this filter is for taking output from the [exec input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-exec.html) which emits one event for the whole output of a command and splitting that output by newline - making each line an event.

Split filter can also be used to split array fields in events into individual events. A very common pattern in JSON & XML is to make use of lists to group data together.

For example, a json structure like this:

```
{ field1: ...,
 results: [
   { result ... },
   { result ... },
   { result ... },
   ...
] }
```

The split filter can be used on the above data to create separate events for each value of `results` field

```
filter {
 split {
   field => "results"
 }
}
```

The end result of each split is a complete copy of the event with only the current split section of the given field changed.

## Split Filter Configuration Options [v3.1.6-plugins-filters-split-options]

This plugin supports the following configuration options plus the [Common options](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`field`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-field) | [string](/lsr/value-types.md#string) | No |
| [`target`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-target) | [string](/lsr/value-types.md#string) | No |
| [`terminator`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-terminator) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-common-options) for a list of options supported by all filter plugins.

### `field` [v3.1.6-plugins-filters-split-field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The field which value is split by the terminator. Can be a multiline message or the ID of an array. Nested arrays are referenced like: "\[object\_id]\[array\_id]"

### `target` [v3.1.6-plugins-filters-split-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field within the new event which the value is split into. If not set, the target field defaults to split field name.

### `terminator` [v3.1.6-plugins-filters-split-terminator]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"\n"`

The string to split on. This is usually a line terminator, but can be any string. If you are splitting a JSON array into multiple events, you can ignore this field.

## Common options [v3.1.6-plugins-filters-split-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-1-6-plugins-filters-split.md#v3.1.6-plugins-filters-split-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.1.6-plugins-filters-split-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      split {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      split {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.1.6-plugins-filters-split-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      split {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      split {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.1.6-plugins-filters-split-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.6-plugins-filters-split-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 split filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      split {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.1.6-plugins-filters-split-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.1.6-plugins-filters-split-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      split {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      split {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.1.6-plugins-filters-split-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      split {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      split {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
