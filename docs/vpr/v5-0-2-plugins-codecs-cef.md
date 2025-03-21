---
navigation_title: "v5.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.2-plugins-codecs-cef.html
---

# Cef codec plugin v5.0.2 [v5.0.2-plugins-codecs-cef]


* Plugin version: v5.0.2
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-codec-cef/blob/v5.0.2/CHANGELOG.md)

For other versions, see the [overview list](codec-cef-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2240]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-cef). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2218]

Implementation of a Logstash codec for the ArcSight Common Event Format (CEF) Based on Revision 20 of Implementing ArcSight CEF, dated from June 05, 2013 [https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf](https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf)

If this codec receives a payload from an input that is not a valid CEF message, then it will produce an event with the payload as the *message* field and a *_cefparsefailure* tag.


## Cef Codec Configuration Options [v5.0.2-plugins-codecs-cef-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`delimiter`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-delimiter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fields`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`name`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`product`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-product) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`severity`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-severity) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`signature`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-signature) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vendor`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-vendor) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version`](v5-0-2-plugins-codecs-cef.md#v5.0.2-plugins-codecs-cef-version) | [string](logstash://reference/configuration-file-structure.md#string) | No |

 

### `delimiter` [v5.0.2-plugins-codecs-cef-delimiter]

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


### `deprecated_v1_fields`  (OBSOLETE) [v5.0.2-plugins-codecs-cef-deprecated_v1_fields]

* OBSOLETE WARNING: This configuration item is obsolete and will prevent the pipeline from starting if used
* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.


### `fields` [v5.0.2-plugins-codecs-cef-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Fields to be included in CEV extension part as key/value pairs


### `name` [v5.0.2-plugins-codecs-cef-name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Name field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `product` [v5.0.2-plugins-codecs-cef-product]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Device product field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `sev`  (OBSOLETE) [v5.0.2-plugins-codecs-cef-sev]

* OBSOLETE WARNING: This configuration item is obsolete and will prevent the pipeline from starting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Obsolete severity field for CEF header use :severity instead.


### `severity` [v5.0.2-plugins-codecs-cef-severity]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"6"`

Severity field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.

Defined as field of type string to allow sprintf. The value will be validated to be an integer in the range from 0 to 10 (including). All invalid values will be mapped to the default of 6.


### `signature` [v5.0.2-plugins-codecs-cef-signature]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

Signature ID field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `vendor` [v5.0.2-plugins-codecs-cef-vendor]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Elasticsearch"`

Device vendor field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `version` [v5.0.2-plugins-codecs-cef-version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1.0"`

Device version field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.



