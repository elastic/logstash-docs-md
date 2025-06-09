---
navigation_title: "v1.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.1.2-plugins-filters-dissect.html
---

# Dissect filter plugin v1.1.2 [v1.1.2-plugins-filters-dissect]

* Plugin version: v1.1.2
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-dissect/blob/v1.1.2/CHANGELOG.md)

For other versions, see the [overview list](filter-dissect-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1771]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-dissect). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1749]

The Dissect filter is a kind of split operation. Unlike a regular split operation where one delimiter is applied to the whole string, this operation applies a set of delimiters to a string value.\
Dissect does not use regular expressions and is very fast.\
However, if the structure of your text varies from line to line then Grok is more suitable.\
There is a hybrid case where Dissect can be used to de-structure the section of the line that is reliably repeated and then Grok can be used on the remaining field values with more regex predictability and less overall work to do.

A set of fields and delimiters is called a **dissection**.

The dissection is described using a set of `%{}` sections:

```
%{a} - %{b} - %{c}
```

A **field** is the text from `%` to `}` inclusive.

A **delimiter** is the text between a `}` and next `%{` characters.

Any set of characters that do not fit `%{`, `'not }'`, `}` pattern is a delimiter.

The config might look like this:

```
  filter {
    dissect {
      mapping => {
        "message" => "%{ts} %{+ts} %{+ts} %{src} %{} %{prog}[%{pid}]: %{msg}"
      }
    }
  }
```

When dissecting a string from left to right, text is captured upto the first delimiter - this captured text is stored in the first field. This is repeated for each field/# delimiter pair thereafter until the last delimiter is reached, then **the remaining text is stored in the last field**.

**The Key:**\
The key is the text between the `%{` and `}`, exclusive of the ?, +, & prefixes and the ordinal suffix.\
`%{?aaa}` - key is `aaa`\
`%{+bbb/3}` - key is `bbb`\
`%{&ccc}` - key is `ccc`

### Normal field notation [_normal_field_notation_3]

The found value is added to the Event using the key.\
`%{some_field}` - a normal field has no prefix or suffix

**Skip field notation:**\
The found value is stored internally but not added to the Event.\
The key, if supplied, is prefixed with a `?`.

`%{}` is an empty skip field.

`%{?foo}` is a named skip field.

### Append field notation [_append_field_notation_3]

The value is appended to another value or stored if its the first field seen.\
The key is prefixed with a `+`.\
The final value is stored in the Event using the key.

The delimiter found before the field is appended with the value.\
If no delimiter is found before the field, a single space character is used.

`%{+some_field}` is an append field.\
`%{+some_field/2}` is an append field with an order modifier.

An order modifier, `/digits`, allows one to reorder the append sequence.\
e.g. for a text of `1 2 3 go`, this `%{+a/2} %{+a/1} %{+a/4} %{+a/3}` will build a key/value of `a => 2 1 go 3`\
Append fields without an order modifier will append in declared order.\
e.g. for a text of `1 2 3 go`, this `%{a} %{b} %{+a}` will build two key/values of `a => 1 3 go, b => 2`

### Indirect field notation [_indirect_field_notation_3]

The found value is added to the Event using the found value of another field as the key.\
The key is prefixed with a `&`.\
`%{&some_field}` - an indirect field where the key is indirectly sourced from the value of `some_field`.\
e.g. for a text of `error: some_error, some_description`, this `error: %{?err}, %{&err}` will build a key/value of `some_error => some_description`.

for append and indirect field the key can refer to a field that already exists in the event before dissection.

use a Skip field if you do not want the indirection key/value stored.

e.g. for a text of `google: 77.98`, this `%{?a}: %{&a}` will build a key/value of `google => 77.98`.

append and indirect cannot be combined and will fail validation.\
`%{+&something}` - will add a value to the `&something` key, probably not the intended outcome.\
`%{&+something}` will add a value to the `+something` key, again probably unintended.

## Multiple Consecutive Delimiter Handling [_multiple_consecutive_delimiter_handling_8]

Starting from version 1.1.1 of this plugin, multiple found delimiter handling has changed. Now multiple consecutive delimiters will be seen as missing fields by default and not padding. If you are already using Dissect and your source text has fields padded with extra delimiters, you will need to change your config. Please read the section below.

### Empty data between delimiters [_empty_data_between_delimiters_8]

Given this text as the sample used to create a dissection:

```
John Smith,Big Oaks,Wood Lane,Hambledown,Canterbury,CB34RY
```

The created dissection, with 6 fields, is:

```
%{name},%{addr1},%{addr2},%{addr3},%{city},%{zip}
```

When a line like this is processed:

```
Jane Doe,4321 Fifth Avenue,,,New York,87432
```

Dissect will create an event with empty fields for `addr2 and addr3` like so:

```
{
  "name": "Jane Doe",
  "addr1": "4321 Fifth Avenue",
  "addr2": "",
  "addr3": "",
  "city": "New York"
  "zip": "87432"
}
```

### Delimiters used as padding to visually align fields [_delimiters_used_as_padding_to_visually_align_fields_8]

**Padding to the right hand side**

Given these texts as the samples used to create a dissection:

```
00000043 ViewReceive     machine-321
f3000a3b Calc            machine-123
```

The dissection, with 3 fields, is:

```
%{id} %{function->} %{server}
```

Note, above, the second field has a `->` suffix which tells Dissect to ignore padding to its right.\
Dissect will create these events:

```
{
  "id": "00000043",
  "function": "ViewReceive",
  "server": "machine-123"
}
{
  "id": "f3000a3b",
  "function": "Calc",
  "server": "machine-321"
}
```

Always add the `->` suffix to the field on the left of the padding.

**Padding to the left hand side (to the human eye)**

Given these texts as the samples used to create a dissection:

```
00000043     ViewReceive machine-321
f3000a3b            Calc machine-123
```

The dissection, with 3 fields, is now:

```
%{id->} %{function} %{server}
```

Here the `->` suffix moves to the `id` field because Dissect sees the padding as being to the right of the `id` field.

## Conditional processing [_conditional_processing_8]

You probably want to use this filter inside an `if` block.\
This ensures that the event contains a field value with a suitable structure for the dissection.

For example…

```
filter {
  if [type] == "syslog" or "syslog" in [tags] {
    dissect {
      mapping => {
        "message" => "%{ts} %{+ts} %{+ts} %{src} %{} %{prog}[%{pid}]: %{msg}"
      }
    }
  }
}
```

## Dissect Filter Configuration Options [v1.1.2-plugins-filters-dissect-options]

This plugin supports the following configuration options plus the [Common options](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`convert_datatype`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-convert_datatype) | [hash](/lsr/value-types.md#hash) | No |
| [`mapping`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-mapping) | [hash](/lsr/value-types.md#hash) | No |
| [`tag_on_failure`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-tag_on_failure) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-common-options) for a list of options supported by all filter plugins.

### `convert_datatype` [v1.1.2-plugins-filters-dissect-convert_datatype]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

With this setting `int` and `float` datatype conversions can be specified.\
These will be done after all `mapping` dissections have taken place.\
Feel free to use this setting on its own without a `mapping` section.

For example

```
filter {
  dissect {
    convert_datatype => {
      cpu => "float"
      code => "int"
    }
  }
}
```

### `mapping` [v1.1.2-plugins-filters-dissect-mapping]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A hash of dissections of `field => value`\
A later dissection can be done on values from a previous dissection or they can be independent.

For example

```
filter {
  dissect {
    mapping => {
      "message" => "%{field1} %{field2} %{description}"
      "description" => "%{field3} %{field4} %{field5}"
    }
  }
}
```

This is useful if you want to keep the field `description` but also dissect it some more.

### `tag_on_failure` [v1.1.2-plugins-filters-dissect-tag_on_failure]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_dissectfailure"]`

Append values to the `tags` field when dissection fails

## Common options [v1.1.2-plugins-filters-dissect-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-1-2-plugins-filters-dissect.md#v1.1.2-plugins-filters-dissect-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.1.2-plugins-filters-dissect-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      dissect {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      dissect {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.1.2-plugins-filters-dissect-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      dissect {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      dissect {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.1.2-plugins-filters-dissect-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.1.2-plugins-filters-dissect-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 dissect filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      dissect {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.1.2-plugins-filters-dissect-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.1.2-plugins-filters-dissect-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      dissect {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      dissect {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.1.2-plugins-filters-dissect-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      dissect {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      dissect {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
