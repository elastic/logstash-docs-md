---
navigation_title: "v6.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.2.0-plugins-codecs-cef.html
---

# Cef codec plugin v6.2.0 [v6.2.0-plugins-codecs-cef]


* Plugin version: v6.2.0
* Released on: 2021-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-codec-cef/blob/v6.2.0/CHANGELOG.md)

For other versions, see the [overview list](codec-cef-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2230]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-cef). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2208]

Implementation of a Logstash codec for the ArcSight Common Event Format (CEF) Based on Revision 20 of Implementing ArcSight CEF, dated from June 05, 2013 [https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf](https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf)

If this codec receives a payload from an input that is not a valid CEF message, then it will produce an event with the payload as the *message* field and a *_cefparsefailure* tag.


## Compatibility with the Elastic Common Schema (ECS) [_compatibility_with_the_elastic_common_schema_ecs_94]

This plugin can be used to decode CEF events *into* the Elastic Common Schema, or to encode ECS-compatible events into CEF. It can also be used *without* ECS, encoding and decoding events using only CEF-defined field names and keys.

The ECS Compatibility mode for a specific plugin instance can be controlled by setting [`ecs_compatibility`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-ecs_compatibility) when defining the codec:

```sh
    input {
      tcp {
        # ...
        codec => cef {
          ecs_compatibility => v1
        }
      }
    }
```

If left unspecified, the value of the `pipeline.ecs_compatibility` setting is used.

### Timestamps and ECS Compatiblity [_timestamps_and_ecs_compatiblity_9]

When running in ECS Compatibility Mode, timestamp-type fields are parsed and normalized to specific points on the timeline.

Because the CEF format allows ambiguous timestamp formats, some reasonable assumptions are made:

* When the timestamp does not include a year, we assume it happened in the recent past (or *very* near future to accommodate out-of-sync clocks and timezone offsets).
* When the timestamp does not include UTC-offset information, we use the event’s timezone (`dtz` or `deviceTimeZone` field), or fall through to this plugin’s [`default_timezone`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-default_timezone).
* Localized timestamps are parsed using the provided [`locale`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-locale).



## Cef Codec Configuration Options [v6.2.0-plugins-codecs-cef-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`default_timezone`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-default_timezone) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`delimiter`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-delimiter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`device`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-device) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ecs_compatibility`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fields`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`locale`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-locale) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`name`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`product`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-product) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`reverse_mapping`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-reverse_mapping) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`severity`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-severity) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`signature`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-signature) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vendor`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-vendor) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`version`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-version) | [string](logstash://reference/configuration-file-structure.md#string) | No |

 

### `default_timezone` [v6.2.0-plugins-codecs-cef-default_timezone]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * [Timezone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (such as `Europe/Moscow`, `America/Argentina/Buenos_Aires`)
    * UTC Offsets (such as `-08:00`, `+03:00`)

* The default value is your system time zone
* This option has no effect when *encoding*.

When parsing timestamp fields in ECS mode and encountering timestamps that do not contain UTC-offset information, the `deviceTimeZone` (`dtz`) field from the CEF payload is used to interpret the given time. If the event does not include timezone information, this `default_timezone` is used instead.


### `delimiter` [v6.2.0-plugins-codecs-cef-delimiter]

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


### `device` [v6.2.0-plugins-codecs-cef-device]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `observer`: indicates that device-specific fields represent the device used to *observe* the event.
    * `host`: indicates that device-specific fields represent the device on which the event *occurred*.

* The default value for this setting is `observer`.
* Option has no effect when [`ecs_compatibility => disabled`](v6-2-0-plugins-codecs-cef.md#v6.2.0-plugins-codecs-cef-ecs_compatibility).
* Option has no effect when *encoding*

Defines a set of device-specific CEF fields as either representing the device on which an event *occurred*, or merely the device from which the event was *observed*. This causes the relevant fields to be routed to either the `host` or the `observer` top-level groupings.

If the codec handles data from a variety of sources, the ECS recommendation is to use `observer`.


### `ecs_compatibility` [v6.2.0-plugins-codecs-cef-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: uses CEF-defined field names in the event (e.g., `bytesIn`, `sourceAddress`)
    * `v1`: supports ECS-compatible event fields (e.g., `[source,shell][bytes]`, `[source,shell][ip]`)

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`.


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)](ecs://docs/reference/index.md)) (ECS)].


### `fields` [v6.2.0-plugins-codecs-cef-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, a list of fields can be provided to be included in CEF extensions part as key/value pairs.


### `locale` [v6.2.0-plugins-codecs-cef-locale]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * Abbreviated language_COUNTRY format (e.g., `en_GB`, `pt_BR`)
    * Valid [IETF BCP 47](https://tools.ietf.org/html/bcp47) language tag (e.g., `zh-cmn-Hans-CN`)

* The default value is your system locale
* Option has no effect when *encoding*

When parsing timestamp fields in ECS mode and encountering timestamps in a localized format, this `locale` is used to interpret locale-specific strings such as month abbreviations.


### `name` [v6.2.0-plugins-codecs-cef-name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the name field in the CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `product` [v6.2.0-plugins-codecs-cef-product]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device product field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `reverse_mapping` [v6.2.0-plugins-codecs-cef-reverse_mapping]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`
* Option has no effect when *decoding*

Set to true to adhere to the specifications and encode using the CEF key name (short name) for the CEF field names.


### `severity` [v6.2.0-plugins-codecs-cef-severity]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"6"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the severity field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.

Defined as field of type string to allow sprintf. The value will be validated to be an integer in the range from 0 to 10 (including). All invalid values will be mapped to the default of 6.


### `signature` [v6.2.0-plugins-codecs-cef-signature]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the signature ID field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `vendor` [v6.2.0-plugins-codecs-cef-vendor]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Elasticsearch"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device vendor field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `version` [v6.2.0-plugins-codecs-cef-version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1.0"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device version field in CEF header. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.



