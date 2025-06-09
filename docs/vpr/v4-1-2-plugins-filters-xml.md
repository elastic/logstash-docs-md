---
navigation_title: "v4.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.1.2-plugins-filters-xml.html
---

# Xml filter plugin v4.1.2 [v4.1.2-plugins-filters-xml]

* Plugin version: v4.1.2
* Released on: 2021-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-xml/blob/v4.1.2/CHANGELOG.md)

For other versions, see the [overview list](filter-xml-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2233]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-xml). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2211]

XML filter. Takes a field that contains XML and expands it into an actual datastructure.

## Xml Filter Configuration Options [v4.1.2-plugins-filters-xml-options]

This plugin supports the following configuration options plus the [Common options](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`force_array`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-force_array) | [boolean](/lsr/value-types.md#boolean) | No |
| [`force_content`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-force_content) | [boolean](/lsr/value-types.md#boolean) | No |
| [`namespaces`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-namespaces) | [hash](/lsr/value-types.md#hash) | No |
| [`parse_options`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-parse_options) | [string](/lsr/value-types.md#string) | No |
| [`remove_namespaces`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-remove_namespaces) | [boolean](/lsr/value-types.md#boolean) | No |
| [`source`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-source) | [string](/lsr/value-types.md#string) | Yes |
| [`store_xml`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-store_xml) | [boolean](/lsr/value-types.md#boolean) | No |
| [`suppress_empty`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-suppress_empty) | [boolean](/lsr/value-types.md#boolean) | No |
| [`target`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-target) | [string](/lsr/value-types.md#string) | No |
| [`xpath`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-xpath) | [hash](/lsr/value-types.md#hash) | No |

Also see [Common options](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-common-options) for a list of options supported by all filter plugins.

### `force_array` [v4.1.2-plugins-filters-xml-force_array]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

By default the filter will force single elements to be arrays. Setting this to false will prevent storing single elements in arrays.

### `force_content` [v4.1.2-plugins-filters-xml-force_content]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

By default the filter will expand attributes differently from content inside of tags. This option allows you to force text content and attributes to always parse to a hash value.

### `namespaces` [v4.1.2-plugins-filters-xml-namespaces]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

By default only namespaces declarations on the root element are considered. This allows to configure all namespace declarations to parse the XML document.

Example:

```
filter {
  xml {
    namespaces => {
      "xsl" => "http://www.w3.org/1999/XSL/Transform"
      "xhtml" => "http://www.w3.org/1999/xhtml"
    }
  }
}
```

### `parse_options` [v4.1.2-plugins-filters-xml-parse_options]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Setting XML parse options allows for more control of the parsing process. By default the parser is not strict and thus accepts some invalid content. Currently supported options are:

* `strict` - forces the parser to fail early instead of accumulating errors when content is not valid xml.

### `remove_namespaces` [v4.1.2-plugins-filters-xml-remove_namespaces]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Remove all namespaces from all nodes in the document. Of course, if the document had nodes with the same names but different namespaces, they will now be ambiguous.

### `source` [v4.1.2-plugins-filters-xml-source]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Config for xml to hash is:

```
    source => source_field
```

For example, if you have the whole XML document in your `message` field:

```
    filter {
      xml {
        source => "message"
      }
    }
```

The above would parse the XML from the `message` field.

### `store_xml` [v4.1.2-plugins-filters-xml-store_xml]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

By default the filter will store the whole parsed XML in the destination field as described above. Setting this to false will prevent that.

### `suppress_empty` [v4.1.2-plugins-filters-xml-suppress_empty]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

By default, output nothing if the element is empty. If set to `false`, empty element will result in an empty hash object.

### `target` [v4.1.2-plugins-filters-xml-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define target for placing the data

For example if you want the data to be put in the `doc` field:

```
    filter {
      xml {
        target => "doc"
      }
    }
```

XML in the value of the source field will be expanded into a datastructure in the `target` field. Note: if the `target` field already exists, it will be overridden. Required if `store_xml` is true (which is the default).

### `xpath` [v4.1.2-plugins-filters-xml-xpath]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

xpath will additionally select string values (non-strings will be converted to strings with Ruby’s `to_s` function) from parsed XML (using each source field defined using the method above) and place those values in the destination fields. Configuration:

```
xpath => [ "xpath-syntax", "destination-field" ]
```

Values returned by XPath parsing from `xpath-syntax` will be put in the destination field. Multiple values returned will be pushed onto the destination field as an array. As such, multiple matches across multiple source fields will produce duplicate entries in the field.

More on XPath: <http://www.w3schools.com/xml/xml_xpath.asp>

The XPath functions are particularly powerful: <http://www.w3schools.com/xsl/xsl_functions.asp>

## Common options [v4.1.2-plugins-filters-xml-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-1-2-plugins-filters-xml.md#v4.1.2-plugins-filters-xml-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.1.2-plugins-filters-xml-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      xml {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      xml {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.1.2-plugins-filters-xml-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      xml {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      xml {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.1.2-plugins-filters-xml-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.1.2-plugins-filters-xml-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 xml filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      xml {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.1.2-plugins-filters-xml-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.1.2-plugins-filters-xml-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      xml {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      xml {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.1.2-plugins-filters-xml-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      xml {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      xml {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
