---
navigation_title: "v4.7.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.7.0-plugins-filters-kv.html
---

# Kv filter plugin v4.7.0 [v4.7.0-plugins-filters-kv]


* Plugin version: v4.7.0
* Released on: 2022-03-04
* [Changelog](https://github.com/logstash-plugins/logstash-filter-kv/blob/v4.7.0/CHANGELOG.md)

For other versions, see the [overview list](filter-kv-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2052]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-kv). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2030]

This filter helps automatically parse messages (or specific event fields) which are of the `foo=bar` variety.

For example, if you have a log message which contains `ip=1.2.3.4 error=REFUSED`, you can parse those automatically by configuring:

```ruby
    filter {
      kv { }
    }
```

The above will result in a message of `ip=1.2.3.4 error=REFUSED` having the fields:

* `ip: 1.2.3.4`
* `error: REFUSED`

This is great for postfix, iptables, and other types of logs that tend towards `key=value` syntax.

You can configure any arbitrary strings to split your data on, in case your data is not structured using `=` signs and whitespace. For example, this filter can also be used to parse query parameters like `foo=bar&baz=fizz` by setting the `field_split` parameter to `&`.


## Event Metadata and the Elastic Common Schema (ECS) [v4.7.0-plugins-filters-kv-ecs_metadata]

The plugin behaves the same regardless of ECS compatibility, except giving a warning when ECS is enabled and `target` isn’t set.

::::{tip}
Set the `target` option to avoid potential schema conflicts.
::::



## Kv Filter Configuration Options [v4.7.0-plugins-filters-kv-options]

This plugin supports the following configuration options plus the [Common options](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`allow_duplicate_values`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-allow_duplicate_values) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`allow_empty_values`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-allow_empty_values) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`default_keys`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-default_keys) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`ecs_compatibility`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exclude_keys`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-exclude_keys) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`field_split`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-field_split) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field_split_pattern`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-field_split_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`include_brackets`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-include_brackets) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`include_keys`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-include_keys) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`prefix`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`recursive`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-recursive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_char_key`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-remove_char_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`remove_char_value`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-remove_char_value) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`source`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`target`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tag_on_failure`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`tag_on_timeout`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-tag_on_timeout) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`timeout_millis`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-timeout_millis) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`transform_key`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-transform_key) | [string](logstash://reference/configuration-file-structure.md#string), one of `["lowercase", "uppercase", "capitalize"]` | No |
| [`transform_value`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-transform_value) | [string](logstash://reference/configuration-file-structure.md#string), one of `["lowercase", "uppercase", "capitalize"]` | No |
| [`trim_key`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-trim_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`trim_value`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-trim_value) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`value_split`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-value_split) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`value_split_pattern`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-value_split_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`whitespace`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-whitespace) | [string](logstash://reference/configuration-file-structure.md#string), one of `["strict", "lenient"]` | No |

Also see [Common options](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-common-options) for a list of options supported by all filter plugins.

 

### `allow_duplicate_values` [v4.7.0-plugins-filters-kv-allow_duplicate_values]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

A bool option for removing duplicate key/value pairs. When set to false, only one unique key/value pair will be preserved.

For example, consider a source like `from=me from=me`. `[from]` will map to an Array with two elements: `["me", "me"]`. To only keep unique key/value pairs, you could use this configuration:

```ruby
    filter {
      kv {
        allow_duplicate_values => false
      }
    }
```


### `allow_empty_values` [v4.7.0-plugins-filters-kv-allow_empty_values]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

A bool option for explicitly including empty values. When set to true, empty values will be added to the event.

::::{note}
Parsing empty values typically requires [`whitespace => strict`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-whitespace).
::::



### `default_keys` [v4.7.0-plugins-filters-kv-default_keys]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

A hash specifying the default keys and their values which should be added to the event in case these keys do not exist in the source field being parsed.

```ruby
    filter {
      kv {
        default_keys => [ "from", "logstash@example.com",
                         "to", "default@dev.null" ]
      }
    }
```


### `ecs_compatibility` [v4.7.0-plugins-filters-kv-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: does not use ECS-compatible field names
    * `v1`: Elastic Common Schema compliant behavior (warns when `target` isn’t set)


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)](ecs://docs/reference/index.md)). See [Event Metadata and the Elastic Common Schema (ECS)](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-ecs_metadata) for detailed information.


### `exclude_keys` [v4.7.0-plugins-filters-kv-exclude_keys]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

An array specifying the parsed keys which should not be added to the event. By default no keys will be excluded.

For example, consider a source like `Hey, from=<abc>, to=def foo=bar`. To exclude `from` and `to`, but retain the `foo` key, you could use this configuration:

```ruby
    filter {
      kv {
        exclude_keys => [ "from", "to" ]
      }
    }
```


### `field_split` [v4.7.0-plugins-filters-kv-field_split]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `" "`

A string of characters to use as single-character field delimiters for parsing out key-value pairs.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

**Example with URL Query Strings**

For example, to split out the args from a url query string such as `?pin=12345~0&d=123&e=foo@bar.com&oq=bobo&ss=12345`:

```ruby
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


### `field_split_pattern` [v4.7.0-plugins-filters-kv-field_split_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A regex expression to use as field delimiter for parsing out key-value pairs. Useful to define multi-character field delimiters. Setting the `field_split_pattern` options will take precedence over the `field_split` option.

Note that you should avoid using captured groups in your regex and you should be cautious with lookaheads or lookbehinds and positional anchors.

For example, to split fields on a repetition of one or more colons `k1=v1:k2=v2::k3=v3:::k4=v4`:

```ruby
    filter { kv { field_split_pattern => ":+" } }
```

To split fields on a regex character that need escaping like the plus sign `k1=v1++k2=v2++k3=v3++k4=v4`:

```ruby
    filter { kv { field_split_pattern => "\\+\\+" } }
```


### `include_brackets` [v4.7.0-plugins-filters-kv-include_brackets]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

A boolean specifying whether to treat square brackets, angle brackets, and parentheses as value "wrappers" that should be removed from the value.

```ruby
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
* bracketstwo: [hello
* bracketsthree: <hello


### `include_keys` [v4.7.0-plugins-filters-kv-include_keys]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

An array specifying the parsed keys which should be added to the event. By default all keys will be added.

For example, consider a source like `Hey, from=<abc>, to=def foo=bar`. To include `from` and `to`, but exclude the `foo` key, you could use this configuration:

```ruby
    filter {
      kv {
        include_keys => [ "from", "to" ]
      }
    }
```


### `prefix` [v4.7.0-plugins-filters-kv-prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

A string to prepend to all of the extracted keys.

For example, to prepend arg_ to all keys:

```ruby
    filter { kv { prefix => "arg_" } }
```


### `recursive` [v4.7.0-plugins-filters-kv-recursive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

A boolean specifying whether to drill down into values and recursively get more key-value pairs from it. The extra key-value pairs will be stored as subkeys of the root key.

Default is not to recursive values.

```ruby
    filter {
      kv {
        recursive => "true"
      }
    }
```


### `remove_char_key` [v4.7.0-plugins-filters-kv-remove_char_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A string of characters to remove from the key.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Contrary to trim option, all characters are removed from the key, whatever their position.

For example, to remove `<` `>` `[` `]` and `,` characters from keys:

```ruby
    filter {
      kv {
        remove_char_key => "<>\[\],"
      }
    }
```


### `remove_char_value` [v4.7.0-plugins-filters-kv-remove_char_value]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A string of characters to remove from the value.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Contrary to trim option, all characters are removed from the value, whatever their position.

For example, to remove `<`, `>`, `[`, `]` and `,` characters from values:

```ruby
    filter {
      kv {
        remove_char_value => "<>\[\],"
      }
    }
```


### `source` [v4.7.0-plugins-filters-kv-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The field to perform `key=value` searching on

For example, to process the `not_the_message` field:

```ruby
    filter { kv { source => "not_the_message" } }
```


### `target` [v4.7.0-plugins-filters-kv-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the container to put all of the key-value pairs into.

If this setting is omitted, fields will be written to the root of the event, as individual fields.

For example, to place all keys into the event field kv:

```ruby
    filter { kv { target => "kv" } }
```


### `tag_on_failure` [v4.7.0-plugins-filters-kv-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* The default value for this setting is [`_kv_filter_error`].

When a kv operation causes a runtime exception to be thrown within the plugin, the operation is safely aborted without crashing the plugin, and the event is tagged with the provided values.


### `tag_on_timeout` [v4.7.0-plugins-filters-kv-tag_on_timeout]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* The default value for this setting is `_kv_filter_timeout`.

When timeouts are enabled and a kv operation is aborted, the event is tagged with the provided value (see: [`timeout_millis`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-timeout_millis)).


### `timeout_millis` [v4.7.0-plugins-filters-kv-timeout_millis]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* The default value for this setting is 30000 (30 seconds).
* Set to zero (`0`) to disable timeouts

Timeouts provide a safeguard against inputs that are pathological against the regular expressions that are used to extract key/value pairs. When parsing an event exceeds this threshold the operation is aborted and the event is tagged in order to prevent the operation from blocking the pipeline (see: [`tag_on_timeout`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-tag_on_timeout)).


### `transform_key` [v4.7.0-plugins-filters-kv-transform_key]

* Value can be any of: `lowercase`, `uppercase`, `capitalize`
* There is no default value for this setting.

Transform keys to lower case, upper case or capitals.

For example, to lowercase all keys:

```ruby
    filter {
      kv {
        transform_key => "lowercase"
      }
    }
```


### `transform_value` [v4.7.0-plugins-filters-kv-transform_value]

* Value can be any of: `lowercase`, `uppercase`, `capitalize`
* There is no default value for this setting.

Transform values to lower case, upper case or capitals.

For example, to capitalize all values:

```ruby
    filter {
      kv {
        transform_value => "capitalize"
      }
    }
```


### `trim_key` [v4.7.0-plugins-filters-kv-trim_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A string of characters to trim from the key. This is useful if your keys are wrapped in brackets or start with space.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Only leading and trailing characters are trimed from the key.

For example, to trim `<` `>` `[` `]` and `,` characters from keys:

```ruby
    filter {
      kv {
        trim_key => "<>\[\],"
      }
    }
```


### `trim_value` [v4.7.0-plugins-filters-kv-trim_value]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Constants used for transform check A string of characters to trim from the value. This is useful if your values are wrapped in brackets or are terminated with commas (like postfix logs).

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

Only leading and trailing characters are trimed from the value.

For example, to trim `<`, `>`, `[`, `]` and `,` characters from values:

```ruby
    filter {
      kv {
        trim_value => "<>\[\],"
      }
    }
```


### `value_split` [v4.7.0-plugins-filters-kv-value_split]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"="`

A non-empty string of characters to use as single-character value delimiters for parsing out key-value pairs.

These characters form a regex character class and thus you must escape special regex characters like `[` or `]` using `\`.

For example, to identify key-values such as `key1:value1 key2:value2`:

```ruby
    filter { kv { value_split => ":" } }
```


### `value_split_pattern` [v4.7.0-plugins-filters-kv-value_split_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A regex expression to use as value delimiter for parsing out key-value pairs. Useful to define multi-character value delimiters. Setting the `value_split_pattern` options will take precedence over the `value_split option`.

Note that you should avoid using captured groups in your regex and you should be cautious with lookaheads or lookbehinds and positional anchors.

See `field_split_pattern` for examples.


### `whitespace` [v4.7.0-plugins-filters-kv-whitespace]

* Value can be any of: `lenient`, `strict`
* Default value is `lenient`

An option specifying whether to be *lenient* or *strict* with the acceptance of unnecessary whitespace surrounding the configured value-split sequence.

By default the plugin is run in `lenient` mode, which ignores spaces that occur before or after the value-splitter. While this allows the plugin to make reasonable guesses with most input, in some situations it may be too lenient.

You may want to enable `whitespace => strict` mode if you have control of the input data and can guarantee that no extra spaces are added surrounding the pattern you have defined for splitting values. Doing so will ensure that a *field-splitter* sequence immediately following a *value-splitter* will be interpreted as an empty field.



## Common options [v4.7.0-plugins-filters-kv-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v4-7-0-plugins-filters-kv.md#v4.7.0-plugins-filters-kv-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v4.7.0-plugins-filters-kv-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      kv {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v4.7.0-plugins-filters-kv-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      kv {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      kv {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v4.7.0-plugins-filters-kv-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.7.0-plugins-filters-kv-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kv filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      kv {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v4.7.0-plugins-filters-kv-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v4.7.0-plugins-filters-kv-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      kv {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      kv {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v4.7.0-plugins-filters-kv-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      kv {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      kv {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



