---
navigation_title: "v4.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.2-plugins-filters-kv.html
---

# Kv filter plugin v4.0.2 [v4.0.2-plugins-filters-kv]

* Plugin version: v4.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-kv/blob/v4.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-kv-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2097]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-kv). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2075]

This filter helps automatically parse messages (or specific event fields) which are of the `foo=bar` variety.

For example, if you have a log message which contains `ip=1.2.3.4 error=REFUSED`, you can parse those automatically by configuring:

```
    filter {
      kv { }
    }
```

The above will result in a message of `ip=1.2.3.4 error=REFUSED` having the fields:

* `ip: 1.2.3.4`
* `error: REFUSED`

This is great for postfix, iptables, and other types of logs that tend towards `key=value` syntax.

You can configure any arbitrary strings to split your data on, in case your data is not structured using `=` signs and whitespace. For example, this filter can also be used to parse query parameters like `foo=bar&baz=fizz` by setting the `field_split` parameter to `&`.

## Kv Filter Configuration Options [v4.0.2-plugins-filters-kv-options]

This plugin supports the following configuration options plus the [Common options](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`allow_duplicate_values`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-allow_duplicate_values) | [boolean](/lsr/value-types.md#boolean) | No |
| [`default_keys`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-default_keys) | [hash](/lsr/value-types.md#hash) | No |
| [`exclude_keys`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-exclude_keys) | [array](/lsr/value-types.md#array) | No |
| [`field_split`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-field_split) | [string](/lsr/value-types.md#string) | No |
| [`include_brackets`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-include_brackets) | [boolean](/lsr/value-types.md#boolean) | No |
| [`include_keys`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-include_keys) | [array](/lsr/value-types.md#array) | No |
| [`prefix`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-prefix) | [string](/lsr/value-types.md#string) | No |
| [`recursive`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-recursive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_char_key`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-remove_char_key) | [string](/lsr/value-types.md#string) | No |
| [`remove_char_value`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-remove_char_value) | [string](/lsr/value-types.md#string) | No |
| [`source`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-source) | [string](/lsr/value-types.md#string) | No |
| [`target`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-target) | [string](/lsr/value-types.md#string) | No |
| [`transform_key`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-transform_key) | [string](/lsr/value-types.md#string), one of `["lowercase", "uppercase", "capitalize"]` | No |
| [`transform_value`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-transform_value) | [string](/lsr/value-types.md#string), one of `["lowercase", "uppercase", "capitalize"]` | No |
| [`trim_key`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-trim_key) | [string](/lsr/value-types.md#string) | No |
| [`trim_value`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-trim_value) | [string](/lsr/value-types.md#string) | No |
| [`value_split`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-value_split) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-common-options) for a list of options supported by all filter plugins.

### `allow_duplicate_values` [v4.0.2-plugins-filters-kv-allow_duplicate_values]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

A bool option for removing duplicate key/value pairs. When set to false, only one unique key/value pair will be preserved.

For example, consider a source like `from=me from=me`. `[from]` will map to an Array with two elements: `["me", "me"]`. To only keep unique key/value pairs, you could use this configuration:

```
    filter {
      kv {
        allow_duplicate_values => false
      }
    }
```

### `default_keys` [v4.0.2-plugins-filters-kv-default_keys]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A hash specifying the default keys and their values which should be added to the event in case these keys do not exist in the source field being parsed.

```
    filter {
      kv {
        default_keys => [ "from", "logstash@example.com",
                         "to", "default@dev.null" ]
      }
    }
```

### `exclude_keys` [v4.0.2-plugins-filters-kv-exclude_keys]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

An array specifying the parsed keys which should not be added to the event. By default no keys will be excluded.

For example, consider a source like `Hey, from=<abc>, to=def foo=bar`. To exclude `from` and `to`, but retain the `foo` key, you could use this configuration:

```
    filter {
      kv {
        exclude_keys => [ "from", "to" ]
      }
    }
```

### `field_split` [v4.0.2-plugins-filters-kv-field_split]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `" "`

A string of characters to use as delimiters for parsing out key-value pairs.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

**Example with URL Query Strings**

For example, to split out the args from a url query string such as `?pin=12345~0&d=123&e=foo@bar.com&oq=bobo&ss=12345`:

```
    filter {
      kv {
        field_split => "&?"
      }
    }
```

The above splits on both `&` and `?` characters, giving you the following fields:

* `pin: 12345~0`
* `d: 123`
* `e: foo@bar.com`
* `oq: bobo`
* `ss: 12345`

### `include_brackets` [v4.0.2-plugins-filters-kv-include_brackets]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

A boolean specifying whether to treat square brackets, angle brackets, and parentheses as value "wrappers" that should be removed from the value.

```
    filter {
      kv {
        include_brackets => true
      }
    }
```

For example, the result of this line: `bracketsone=(hello world) bracketstwo=[hello world] bracketsthree=<hello world>`

will be:

* bracketsone: hello world
* bracketstwo: hello world
* bracketsthree: hello world

instead of:

* bracketsone: (hello
* bracketstwo: \[hello
* bracketsthree: \<hello

### `include_keys` [v4.0.2-plugins-filters-kv-include_keys]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

An array specifying the parsed keys which should be added to the event. By default all keys will be added.

For example, consider a source like `Hey, from=<abc>, to=def foo=bar`. To include `from` and `to`, but exclude the `foo` key, you could use this configuration:

```
    filter {
      kv {
        include_keys => [ "from", "to" ]
      }
    }
```

### `prefix` [v4.0.2-plugins-filters-kv-prefix]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

A string to prepend to all of the extracted keys.

For example, to prepend arg\_ to all keys:

```
    filter { kv { prefix => "arg_" } }
```

### `recursive` [v4.0.2-plugins-filters-kv-recursive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

A boolean specifying whether to drill down into values and recursively get more key-value pairs from it. The extra key-value pairs will be stored as subkeys of the root key.

Default is not to recursive values.

```
    filter {
      kv {
        recursive => "true"
      }
    }
```

### `remove_char_key` [v4.0.2-plugins-filters-kv-remove_char_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A string of characters to remove from the key.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Contrary to trim option, all characters are removed from the key, whatever their position.

For example, to remove `<` `>` `[` `]` and `,` characters from keys:

```
    filter {
      kv {
        remove_char_key => "<>\[\],"
      }
    }
```

### `remove_char_value` [v4.0.2-plugins-filters-kv-remove_char_value]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A string of characters to remove from the value.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Contrary to trim option, all characters are removed from the value, whatever their position.

For example, to remove `<`, `>`, `[`, `]` and `,` characters from values:

```
    filter {
      kv {
        remove_char_value => "<>\[\],"
      }
    }
```

### `source` [v4.0.2-plugins-filters-kv-source]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The field to perform `key=value` searching on

For example, to process the `not_the_message` field:

```
    filter { kv { source => "not_the_message" } }
```

### `target` [v4.0.2-plugins-filters-kv-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the container to put all of the key-value pairs into.

If this setting is omitted, fields will be written to the root of the event, as individual fields.

For example, to place all keys into the event field kv:

```
    filter { kv { target => "kv" } }
```

### `transform_key` [v4.0.2-plugins-filters-kv-transform_key]

* Value can be any of: `lowercase`, `uppercase`, `capitalize`
* There is no default value for this setting.

Transform keys to lower case, upper case or capitals.

For example, to lowercase all keys:

```
    filter {
      kv {
        transform_key => "lowercase"
      }
    }
```

### `transform_value` [v4.0.2-plugins-filters-kv-transform_value]

* Value can be any of: `lowercase`, `uppercase`, `capitalize`
* There is no default value for this setting.

Transform values to lower case, upper case or capitals.

For example, to capitalize all values:

```
    filter {
      kv {
        transform_value => "capitalize"
      }
    }
```

### `trim_key` [v4.0.2-plugins-filters-kv-trim_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A string of characters to trim from the key. This is useful if your keys are wrapped in brackets or start with space.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Only leading and trailing characters are trimed from the key.

For example, to trim `<` `>` `[` `]` and `,` characters from keys:

```
    filter {
      kv {
        trim_key => "<>\[\],"
      }
    }
```

### `trim_value` [v4.0.2-plugins-filters-kv-trim_value]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Constants used for transform check A string of characters to trim from the value. This is useful if your values are wrapped in brackets or are terminated with commas (like postfix logs).

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Only leading and trailing characters are trimed from the value.

For example, to trim `<`, `>`, `[`, `]` and `,` characters from values:

```
    filter {
      kv {
        trim_value => "<>\[\],"
      }
    }
```

### `value_split` [v4.0.2-plugins-filters-kv-value_split]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"="`

A non-empty string of characters to use as delimiters for identifying key-value relations.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

For example, to identify key-values such as `key1:value1 key2:value2`:

```
    filter { kv { value_split => ":" } }
```

## Common options [v4.0.2-plugins-filters-kv-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-0-2-plugins-filters-kv.md#v4.0.2-plugins-filters-kv-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.0.2-plugins-filters-kv-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      kv {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      kv {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.0.2-plugins-filters-kv-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      kv {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      kv {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.0.2-plugins-filters-kv-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.2-plugins-filters-kv-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kv filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      kv {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.0.2-plugins-filters-kv-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.0.2-plugins-filters-kv-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      kv {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      kv {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.0.2-plugins-filters-kv-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      kv {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      kv {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
