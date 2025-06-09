---
navigation_title: "v3.1.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.6-plugins-filters-mutate.html
---

# Mutate filter plugin v3.1.6 [v3.1.6-plugins-filters-mutate]

* Plugin version: v3.1.6
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-mutate/blob/v3.1.6/CHANGELOG.md)

For other versions, see the [overview list](filter-mutate-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2134]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-mutate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2112]

The mutate filter allows you to perform general mutations on fields. You can rename, remove, replace, and modify fields in your events.

## Mutate Filter Configuration Options [v3.1.6-plugins-filters-mutate-options]

This plugin supports the following configuration options plus the [Common options](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`convert`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-convert) | [hash](/lsr/value-types.md#hash) | No |
| [`copy`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-copy) | [hash](/lsr/value-types.md#hash) | No |
| [`gsub`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-gsub) | [array](/lsr/value-types.md#array) | No |
| [`join`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-join) | [hash](/lsr/value-types.md#hash) | No |
| [`lowercase`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-lowercase) | [array](/lsr/value-types.md#array) | No |
| [`merge`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-merge) | [hash](/lsr/value-types.md#hash) | No |
| [`rename`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-rename) | [hash](/lsr/value-types.md#hash) | No |
| [`replace`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-replace) | [hash](/lsr/value-types.md#hash) | No |
| [`split`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-split) | [hash](/lsr/value-types.md#hash) | No |
| [`strip`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-strip) | [array](/lsr/value-types.md#array) | No |
| [`update`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-update) | [hash](/lsr/value-types.md#hash) | No |
| [`uppercase`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-uppercase) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-common-options) for a list of options supported by all filter plugins.

### `convert` [v3.1.6-plugins-filters-mutate-convert]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Convert a field’s value to a different type, like turning a string to an integer. If the field value is an array, all members will be converted. If the field is a hash, no action will be taken.

If the conversion type is `boolean`, the acceptable values are:

* **True:** `true`, `t`, `yes`, `y`, and `1`
* **False:** `false`, `f`, `no`, `n`, and `0`

If a value other than these is provided, it will pass straight through and log a warning message.

Valid conversion targets are: integer, float, string, and boolean.

Example:

```
    filter {
      mutate {
        convert => { "fieldname" => "integer" }
      }
    }
```

### `copy` [v3.1.6-plugins-filters-mutate-copy]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Copy an existing field to another field. Existing target field will be overriden.

Example:

```
    filter {
      mutate {
         copy => { "source_field" => "dest_field" }
      }
    }
```

### `gsub` [v3.1.6-plugins-filters-mutate-gsub]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Match a regular expression against a field value and replace all matches with a replacement string. Only fields that are strings or arrays of strings are supported. For other kinds of fields no action will be taken.

This configuration takes an array consisting of 3 elements per field/substitution.

Be aware of escaping any backslash in the config file.

Example:

```
    filter {
      mutate {
        gsub => [
          # replace all forward slashes with underscore
          "fieldname", "/", "_",
          # replace backslashes, question marks, hashes, and minuses
          # with a dot "."
          "fieldname2", "[\\?#-]", "."
        ]
      }
    }
```

### `join` [v3.1.6-plugins-filters-mutate-join]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Join an array with a separator character. Does nothing on non-array fields.

Example:

```
   filter {
     mutate {
       join => { "fieldname" => "," }
     }
   }
```

### `lowercase` [v3.1.6-plugins-filters-mutate-lowercase]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Convert a string to its lowercase equivalent.

Example:

```
    filter {
      mutate {
        lowercase => [ "fieldname" ]
      }
    }
```

### `merge` [v3.1.6-plugins-filters-mutate-merge]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Merge two fields of arrays or hashes. String fields will be automatically be converted into an array, so:

```
`array` + `string` will work
`string` + `string` will result in an 2 entry array in `dest_field`
`array` and `hash` will not work
```

Example:

```
    filter {
      mutate {
         merge => { "dest_field" => "added_field" }
      }
    }
```

### `rename` [v3.1.6-plugins-filters-mutate-rename]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Rename one or more fields.

Example:

```
    filter {
      mutate {
        # Renames the 'HOSTORIP' field to 'client_ip'
        rename => { "HOSTORIP" => "client_ip" }
      }
    }
```

### `replace` [v3.1.6-plugins-filters-mutate-replace]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Replace a field with a new value. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

Example:

```
    filter {
      mutate {
        replace => { "message" => "%{source_host}: My new message" }
      }
    }
```

### `split` [v3.1.6-plugins-filters-mutate-split]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Split a field to an array using a separator character. Only works on string fields.

Example:

```
    filter {
      mutate {
         split => { "fieldname" => "," }
      }
    }
```

### `strip` [v3.1.6-plugins-filters-mutate-strip]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Strip whitespace from field. NOTE: this only works on leading and trailing whitespace.

Example:

```
    filter {
      mutate {
         strip => ["field1", "field2"]
      }
    }
```

### `update` [v3.1.6-plugins-filters-mutate-update]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Update an existing field with a new value. If the field does not exist, then no action will be taken.

Example:

```
    filter {
      mutate {
        update => { "sample" => "My new message" }
      }
    }
```

### `uppercase` [v3.1.6-plugins-filters-mutate-uppercase]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Convert a string to its uppercase equivalent.

Example:

```
    filter {
      mutate {
        uppercase => [ "fieldname" ]
      }
    }
```

## Common options [v3.1.6-plugins-filters-mutate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-1-6-plugins-filters-mutate.md#v3.1.6-plugins-filters-mutate-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.1.6-plugins-filters-mutate-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      mutate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      mutate {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.1.6-plugins-filters-mutate-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      mutate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      mutate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.1.6-plugins-filters-mutate-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.6-plugins-filters-mutate-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 mutate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      mutate {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.1.6-plugins-filters-mutate-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.1.6-plugins-filters-mutate-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      mutate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      mutate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.1.6-plugins-filters-mutate-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      mutate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      mutate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
