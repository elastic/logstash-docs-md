---
navigation_title: "v3.5.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.5.6-plugins-filters-mutate.html
---

# Mutate filter plugin v3.5.6 [v3.5.6-plugins-filters-mutate]


* Plugin version: v3.5.6
* Released on: 2021-12-02
* [Changelog](https://github.com/logstash-plugins/logstash-filter-mutate/blob/v3.5.6/CHANGELOG.md)

For other versions, see the [overview list](filter-mutate-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2092]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-mutate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2070]

The mutate filter allows you to perform general mutations on fields. You can rename, replace, and modify fields in your events.

### Processing order [v3.5.6-plugins-filters-mutate-proc_order]

Mutations in a config file are executed in this order:

* coerce
* rename
* update
* replace
* convert
* gsub
* uppercase
* capitalize
* lowercase
* strip
* split
* join
* merge
* copy

::::{important}
Each mutation must be in its own code block if the sequence of operations needs to be preserved.
::::


Example:

```ruby
filter {
    mutate {
        split => { "hostname" => "." }
        add_field => { "shortHostname" => "%{[hostname][0]}" }
    }

    mutate {
        rename => {"shortHostname" => "hostname"}
    }
}
```



## Mutate Filter Configuration Options [v3.5.6-plugins-filters-mutate-options]

This plugin supports the following configuration options plus the [Common options](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`convert`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-convert) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`copy`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-copy) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`gsub`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-gsub) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`join`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-join) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`lowercase`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-lowercase) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`merge`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-merge) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`coerce`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-coerce) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`rename`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-rename) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`replace`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-replace) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`split`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-split) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`strip`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-strip) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`update`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-update) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`uppercase`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-uppercase) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`capitalize`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-capitalize) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`tag_on_failure`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-tag_on_failure) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-common-options) for a list of options supported by all filter plugins.

 

### `convert` [v3.5.6-plugins-filters-mutate-convert]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Convert a field’s value to a different type, like turning a string to an integer. If the field value is an array, all members will be converted. If the field is a hash no action will be taken.

::::{admonition} Conversion insights
:class: note

The values are converted using Ruby semantics. Be aware that using `float` and `float_eu` converts the value to a double-precision 64-bit IEEE 754 floating point decimal number. In order to maintain precision due to the conversion, you should use a `double` in the Elasticsearch mappings.

::::


Valid conversion targets, and their expected behaviour with different inputs are:

* `integer`:

    * strings are parsed; comma-separators are supported (e.g., the string `"1,000"` produces an integer with value of one thousand); when strings have decimal parts, they are *truncated*.
    * floats and decimals are *truncated* (e.g., `3.99` becomes `3`, `-2.7` becomes `-2`)
    * boolean true and boolean false are converted to `1` and `0` respectively

* `integer_eu`:

    * same as `integer`, except string values support dot-separators and comma-decimals (e.g., `"1.000"` produces an integer with value of one thousand)

* `float`:

    * integers are converted to floats
    * strings are parsed; comma-separators and dot-decimals are supported (e.g., `"1,000.5"` produces a float with value of one thousand and one half)
    * boolean true and boolean false are converted to `1.0` and `0.0` respectively

* `float_eu`:

    * same as `float`, except string values support dot-separators and comma-decimals (e.g., `"1.000,5"` produces a float with value of one thousand and one half)

* `string`:

    * all values are stringified and encoded with UTF-8

* `boolean`:

    * integer 0 is converted to boolean `false`
    * integer 1 is converted to boolean `true`
    * float 0.0 is converted to boolean `false`
    * float 1.0 is converted to boolean `true`
    * strings `"true"`, `"t"`, `"yes"`, `"y"`, `"1"`and `"1.0"` are converted to boolean `true`
    * strings `"false"`, `"f"`, `"no"`, `"n"`, `"0"` and `"0.0"` are converted to boolean `false`
    * empty strings are converted to boolean `false`
    * all other values pass straight through without conversion and log a warning message
    * for arrays each value gets processed separately using rules above


This plugin can convert multiple fields in the same document, see the example below.

Example:

```ruby
    filter {
      mutate {
        convert => {
          "fieldname" => "integer"
          "booleanfield" => "boolean"
        }
      }
    }
```


### `copy` [v3.5.6-plugins-filters-mutate-copy]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Copy an existing field to another field. Existing target field will be overriden.

Example:

```ruby
    filter {
      mutate {
         copy => { "source_field" => "dest_field" }
      }
    }
```


### `gsub` [v3.5.6-plugins-filters-mutate-gsub]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Match a regular expression against a field value and replace all matches with a replacement string. Only fields that are strings or arrays of strings are supported. For other kinds of fields no action will be taken.

This configuration takes an array consisting of 3 elements per field/substitution.

Be aware of escaping any backslash in the config file.

Example:

```ruby
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


### `join` [v3.5.6-plugins-filters-mutate-join]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Join an array with a separator character. Does nothing on non-array fields.

Example:

```ruby
   filter {
     mutate {
       join => { "fieldname" => "," }
     }
   }
```


### `lowercase` [v3.5.6-plugins-filters-mutate-lowercase]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Convert a string to its lowercase equivalent.

Example:

```ruby
    filter {
      mutate {
        lowercase => [ "fieldname" ]
      }
    }
```


### `merge` [v3.5.6-plugins-filters-mutate-merge]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Merge two fields of arrays or hashes. String fields will be automatically be converted into an array, so:

::::{admonition}
```
`array` + `string` will work
`string` + `string` will result in an 2 entry array in `dest_field`
`array` and `hash` will not work
```
::::


Example:

```ruby
    filter {
      mutate {
         merge => { "dest_field" => "added_field" }
      }
    }
```


### `coerce` [v3.5.6-plugins-filters-mutate-coerce]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Set the default value of a field that exists but is null

Example:

```ruby
    filter {
      mutate {
        # Sets the default value of the 'field1' field to 'default_value'
        coerce => { "field1" => "default_value" }
      }
    }
```


### `rename` [v3.5.6-plugins-filters-mutate-rename]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Rename one or more fields.

If the destination field already exists, its value is replaced.

If one of the source fields doesn’t exist, no action is performed for that field. (This is not considered an error; the `tag_on_failure` tag is not applied.)

When renaming multiple fields, the order of operations is not guaranteed.

Example:

```ruby
    filter {
      mutate {
        # Renames the 'HOSTORIP' field to 'client_ip'
        rename => { "HOSTORIP" => "client_ip" }
      }
    }
```


### `replace` [v3.5.6-plugins-filters-mutate-replace]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Replace the value of a field with a new value, or add the field if it doesn’t already exist. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.

Example:

```ruby
    filter {
      mutate {
        replace => { "message" => "%{source_host}: My new message" }
      }
    }
```


### `split` [v3.5.6-plugins-filters-mutate-split]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Split a field to an array using a separator character. Only works on string fields.

Example:

```ruby
    filter {
      mutate {
         split => { "fieldname" => "," }
      }
    }
```


### `strip` [v3.5.6-plugins-filters-mutate-strip]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Strip whitespace from field. NOTE: this only works on leading and trailing whitespace.

Example:

```ruby
    filter {
      mutate {
         strip => ["field1", "field2"]
      }
    }
```


### `update` [v3.5.6-plugins-filters-mutate-update]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Update an existing field with a new value. If the field does not exist, then no action will be taken.

Example:

```ruby
    filter {
      mutate {
        update => { "sample" => "My new message" }
      }
    }
```


### `uppercase` [v3.5.6-plugins-filters-mutate-uppercase]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Convert a string to its uppercase equivalent.

Example:

```ruby
    filter {
      mutate {
        uppercase => [ "fieldname" ]
      }
    }
```


### `capitalize` [v3.5.6-plugins-filters-mutate-capitalize]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Convert a string to its capitalized equivalent.

Example:

```ruby
    filter {
      mutate {
        capitalize => [ "fieldname" ]
      }
    }
```


### `tag_on_failure` [v3.5.6-plugins-filters-mutate-tag_on_failure]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* The default value for this setting is `_mutate_error`

If a failure occurs during the application of this mutate filter, the rest of the operations are aborted and the provided tag is added to the event.



## Common options [v3.5.6-plugins-filters-mutate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-5-6-plugins-filters-mutate.md#v3.5.6-plugins-filters-mutate-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.5.6-plugins-filters-mutate-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      mutate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.5.6-plugins-filters-mutate-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      mutate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      mutate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.5.6-plugins-filters-mutate-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.5.6-plugins-filters-mutate-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 mutate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      mutate {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.5.6-plugins-filters-mutate-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.5.6-plugins-filters-mutate-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      mutate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      mutate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.5.6-plugins-filters-mutate-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      mutate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      mutate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



