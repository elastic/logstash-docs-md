---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-filters-urldecode.html
---

# Urldecode filter plugin v3.0.4 [v3.0.4-plugins-filters-urldecode]

* Plugin version: v3.0.4
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-urldecode/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](filter-urldecode-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2209]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-urldecode). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2187]

The urldecode filter is for decoding fields that are urlencoded.

## Urldecode Filter Configuration Options [v3.0.4-plugins-filters-urldecode-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`all_fields`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-all_fields) | [boolean](/lsr/value-types.md#boolean) | No |
| [`charset`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-charset) | [string](/lsr/value-types.md#string), one of `["ASCII-8BIT", "UTF-8", "US-ASCII", "Big5", "Big5-HKSCS", "Big5-UAO", "CP949", "Emacs-Mule", "EUC-JP", "EUC-KR", "EUC-TW", "GB2312", "GB18030", "GBK", "ISO-8859-1", "ISO-8859-2", "ISO-8859-3", "ISO-8859-4", "ISO-8859-5", "ISO-8859-6", "ISO-8859-7", "ISO-8859-8", "ISO-8859-9", "ISO-8859-10", "ISO-8859-11", "ISO-8859-13", "ISO-8859-14", "ISO-8859-15", "ISO-8859-16", "KOI8-R", "KOI8-U", "Shift_JIS", "UTF-16BE", "UTF-16LE", "UTF-32BE", "UTF-32LE", "Windows-31J", "Windows-1250", "Windows-1251", "Windows-1252", "IBM437", "IBM737", "IBM775", "CP850", "IBM852", "CP852", "IBM855", "CP855", "IBM857", "IBM860", "IBM861", "IBM862", "IBM863", "IBM864", "IBM865", "IBM866", "IBM869", "Windows-1258", "GB1988", "macCentEuro", "macCroatian", "macCyrillic", "macGreek", "macIceland", "macRoman", "macRomania", "macThai", "macTurkish", "macUkraine", "CP950", "CP951", "IBM037", "stateless-ISO-2022-JP", "eucJP-ms", "CP51932", "EUC-JIS-2004", "GB12345", "ISO-2022-JP", "ISO-2022-JP-2", "CP50220", "CP50221", "Windows-1256", "Windows-1253", "Windows-1255", "Windows-1254", "TIS-620", "Windows-874", "Windows-1257", "MacJapanese", "UTF-7", "UTF8-MAC", "UTF-16", "UTF-32", "UTF8-DoCoMo", "SJIS-DoCoMo", "UTF8-KDDI", "SJIS-KDDI", "ISO-2022-JP-KDDI", "stateless-ISO-2022-JP-KDDI", "UTF8-SoftBank", "SJIS-SoftBank", "BINARY", "CP437", "CP737", "CP775", "IBM850", "CP857", "CP860", "CP861", "CP862", "CP863", "CP864", "CP865", "CP866", "CP869", "CP1258", "Big5-HKSCS:2008", "ebcdic-cp-us", "eucJP", "euc-jp-ms", "EUC-JISX0213", "eucKR", "eucTW", "EUC-CN", "eucCN", "CP936", "ISO2022-JP", "ISO2022-JP2", "ISO8859-1", "ISO8859-2", "ISO8859-3", "ISO8859-4", "ISO8859-5", "ISO8859-6", "CP1256", "ISO8859-7", "CP1253", "ISO8859-8", "CP1255", "ISO8859-9", "CP1254", "ISO8859-10", "ISO8859-11", "CP874", "ISO8859-13", "CP1257", "ISO8859-14", "ISO8859-15", "ISO8859-16", "CP878", "MacJapan", "ASCII", "ANSI_X3.4-1968", "646", "CP65000", "CP65001", "UTF-8-MAC", "UTF-8-HFS", "UCS-2BE", "UCS-4BE", "UCS-4LE", "CP932", "csWindows31J", "SJIS", "PCK", "CP1250", "CP1251", "CP1252", "external", "locale"]` | No |
| [`field`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-field) | [string](/lsr/value-types.md#string) | No |
| [`tag_on_failure`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-tag_on_failure) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-common-options) for a list of options supported by all filter plugins.

### `all_fields` [v3.0.4-plugins-filters-urldecode-all_fields]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Urldecode all fields

### `charset` [v3.0.4-plugins-filters-urldecode-charset]

* Value can be any of: `ASCII-8BIT`, `UTF-8`, `US-ASCII`, `Big5`, `Big5-HKSCS`, `Big5-UAO`, `CP949`, `Emacs-Mule`, `EUC-JP`, `EUC-KR`, `EUC-TW`, `GB2312`, `GB18030`, `GBK`, `ISO-8859-1`, `ISO-8859-2`, `ISO-8859-3`, `ISO-8859-4`, `ISO-8859-5`, `ISO-8859-6`, `ISO-8859-7`, `ISO-8859-8`, `ISO-8859-9`, `ISO-8859-10`, `ISO-8859-11`, `ISO-8859-13`, `ISO-8859-14`, `ISO-8859-15`, `ISO-8859-16`, `KOI8-R`, `KOI8-U`, `Shift_JIS`, `UTF-16BE`, `UTF-16LE`, `UTF-32BE`, `UTF-32LE`, `Windows-31J`, `Windows-1250`, `Windows-1251`, `Windows-1252`, `IBM437`, `IBM737`, `IBM775`, `CP850`, `IBM852`, `CP852`, `IBM855`, `CP855`, `IBM857`, `IBM860`, `IBM861`, `IBM862`, `IBM863`, `IBM864`, `IBM865`, `IBM866`, `IBM869`, `Windows-1258`, `GB1988`, `macCentEuro`, `macCroatian`, `macCyrillic`, `macGreek`, `macIceland`, `macRoman`, `macRomania`, `macThai`, `macTurkish`, `macUkraine`, `CP950`, `CP951`, `IBM037`, `stateless-ISO-2022-JP`, `eucJP-ms`, `CP51932`, `EUC-JIS-2004`, `GB12345`, `ISO-2022-JP`, `ISO-2022-JP-2`, `CP50220`, `CP50221`, `Windows-1256`, `Windows-1253`, `Windows-1255`, `Windows-1254`, `TIS-620`, `Windows-874`, `Windows-1257`, `MacJapanese`, `UTF-7`, `UTF8-MAC`, `UTF-16`, `UTF-32`, `UTF8-DoCoMo`, `SJIS-DoCoMo`, `UTF8-KDDI`, `SJIS-KDDI`, `ISO-2022-JP-KDDI`, `stateless-ISO-2022-JP-KDDI`, `UTF8-SoftBank`, `SJIS-SoftBank`, `BINARY`, `CP437`, `CP737`, `CP775`, `IBM850`, `CP857`, `CP860`, `CP861`, `CP862`, `CP863`, `CP864`, `CP865`, `CP866`, `CP869`, `CP1258`, `Big5-HKSCS:2008`, `ebcdic-cp-us`, `eucJP`, `euc-jp-ms`, `EUC-JISX0213`, `eucKR`, `eucTW`, `EUC-CN`, `eucCN`, `CP936`, `ISO2022-JP`, `ISO2022-JP2`, `ISO8859-1`, `ISO8859-2`, `ISO8859-3`, `ISO8859-4`, `ISO8859-5`, `ISO8859-6`, `CP1256`, `ISO8859-7`, `CP1253`, `ISO8859-8`, `CP1255`, `ISO8859-9`, `CP1254`, `ISO8859-10`, `ISO8859-11`, `CP874`, `ISO8859-13`, `CP1257`, `ISO8859-14`, `ISO8859-15`, `ISO8859-16`, `CP878`, `MacJapan`, `ASCII`, `ANSI_X3.4-1968`, `646`, `CP65000`, `CP65001`, `UTF-8-MAC`, `UTF-8-HFS`, `UCS-2BE`, `UCS-4BE`, `UCS-4LE`, `CP932`, `csWindows31J`, `SJIS`, `PCK`, `CP1250`, `CP1251`, `CP1252`, `external`, `locale`
* Default value is `"UTF-8"`

Thel character encoding used in this filter. Examples include `UTF-8` and `cp1252`

This setting is useful if your url decoded string are in `Latin-1` (aka `cp1252`) or in another character set other than `UTF-8`.

### `field` [v3.0.4-plugins-filters-urldecode-field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The field which value is urldecoded

### `tag_on_failure` [v3.0.4-plugins-filters-urldecode-tag_on_failure]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_urldecodefailure"]`

Append values to the `tags` field when an exception is thrown

## Common options [v3.0.4-plugins-filters-urldecode-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-4-plugins-filters-urldecode.md#v3.0.4-plugins-filters-urldecode-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.4-plugins-filters-urldecode-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      urldecode {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      urldecode {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.4-plugins-filters-urldecode-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      urldecode {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      urldecode {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.4-plugins-filters-urldecode-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.4-plugins-filters-urldecode-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 urldecode filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      urldecode {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.4-plugins-filters-urldecode-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.4-plugins-filters-urldecode-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      urldecode {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      urldecode {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.4-plugins-filters-urldecode-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      urldecode {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      urldecode {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
