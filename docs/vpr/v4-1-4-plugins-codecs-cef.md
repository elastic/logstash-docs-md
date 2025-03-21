---
navigation_title: "v4.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.1.4-plugins-codecs-cef.html
---

# Cef codec plugin v4.1.4 [v4.1.4-plugins-codecs-cef]


* Plugin version: v4.1.4
* Released on: 2017-08-18
* [Changelog](https://github.com/logstash-plugins/logstash-codec-cef/blob/v4.1.4/CHANGELOG.md)

For other versions, see the [overview list](codec-cef-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2243]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-cef). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2221]

Implementation of a Logstash codec for the ArcSight Common Event Format (CEF) Based on Revision 20 of Implementing ArcSight CEF, dated from June 05, 2013 [https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf](https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf)

If this codec receives a payload from an input that is not a valid CEF message, then it will produce an event with the payload as the *message* field and a *_cefparsefailure* tag.


## Cef Codec Configuration Options [v4.1.4-plugins-codecs-cef-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`delimiter`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-delimiter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fields`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`name`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`product`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-product) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`severity`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-severity) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`signature`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-signature) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vendor`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-vendor) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version`](v4-1-4-plugins-codecs-cef.md#v4.1.4-plugins-codecs-cef-version) | [string](logstash://reference/configuration-file-structure.md#string) | No |

 

### `delimiter` [v4.1.4-plugins-codecs-cef-delimiter]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

If your input puts a delimiter between each CEF event, you’ll want to set this to be that delimiter.

For example, with the TCP input, you probably want to put this:

```
input {
  tcp {
    codec => cef { delimiter => "\r\n" }
    # ...
  }
}
```
This setting allows the following character sequences to have special meaning:

* `\\r` (backslash "r") - means carriage return (ASCII 0x0D)
* `\\n` (backslash "n") - means newline (ASCII 0x0A)


### `deprecated_v1_fields`  (DEPRECATED) [v4.1.4-plugins-codecs-cef-deprecated_v1_fields]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Set this flag if you want to have both v1 and v2 fields indexed at the same time. Note that this option will increase the index size and data stored in outputs like Elasticsearch This option is available to ease transition to new schema


### `fields` [v4.1.4-plugins-codecs-cef-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Fields to be included in CEV extension part as key/value pairs


### `name` [v4.1.4-plugins-codecs-cef-name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Name field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `product` [v4.1.4-plugins-codecs-cef-product]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Device product field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `sev`  (DEPRECATED) [v4.1.4-plugins-codecs-cef-sev]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Deprecated severity field for CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.

This field is used only if :severity is unchanged set to the default value.

Defined as field of type string to allow sprintf. The value will be validated to be an integer in the range from 0 to 10 (including). All invalid values will be mapped to the default of 6.


### `severity` [v4.1.4-plugins-codecs-cef-severity]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"6"`

Severity field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.

Defined as field of type string to allow sprintf. The value will be validated to be an integer in the range from 0 to 10 (including). All invalid values will be mapped to the default of 6.


### `signature` [v4.1.4-plugins-codecs-cef-signature]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Signature ID field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `vendor` [v4.1.4-plugins-codecs-cef-vendor]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Elasticsearch"`

Device vendor field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `version` [v4.1.4-plugins-codecs-cef-version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1.0"`

Device version field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.



