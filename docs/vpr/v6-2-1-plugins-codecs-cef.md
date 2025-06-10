---
navigation_title: "v6.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.2.1-plugins-codecs-cef.html
---

# Cef codec plugin v6.2.1 [v6.2.1-plugins-codecs-cef]

* Plugin version: v6.2.1
* Released on: 2021-04-28
* [Changelog](https://github.com/logstash-plugins/logstash-codec-cef/blob/v6.2.1/CHANGELOG.md)

For other versions, see the [overview list](codec-cef-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2261]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-cef). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2239]

Implementation of a Logstash codec for the ArcSight Common Event Format (CEF) Based on Revision 20 of Implementing ArcSight CEF, dated from June 05, 2013 <https://community.saas.hpe.com/dcvta86296/attachments/dcvta86296/connector-documentation/1116/1/CommonEventFormatv23.pdf>

If this codec receives a payload from an input that is not a valid CEF message, then it will produce an event with the payload as the *message* field and a *\_cefparsefailure* tag.

## Compatibility with the Elastic Common Schema (ECS) [_compatibility_with_the_elastic_common_schema_ecs_94]

This plugin can be used to decode CEF events *into* the Elastic Common Schema, or to encode ECS-compatible events into CEF. It can also be used *without* ECS, encoding and decoding events using only CEF-defined field names and keys.

The ECS Compatibility mode for a specific plugin instance can be controlled by setting [`ecs_compatibility`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-ecs_compatibility) when defining the codec:

```
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

### Timestamps and ECS compatiblity [_timestamps_and_ecs_compatiblity_8]

When decoding in ECS Compatibility Mode, timestamp-type fields are parsed and normalized to specific points on the timeline.

Because the CEF format allows ambiguous timestamp formats, some reasonable assumptions are made:

* When the timestamp does not include a year, we assume it happened in the recent past (or *very* near future to accommodate out-of-sync clocks and timezone offsets).
* When the timestamp does not include UTC-offset information, we use the event’s timezone (`dtz` or `deviceTimeZone` field), or fall through to this plugin’s [`default_timezone`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-default_timezone).
* Localized timestamps are parsed using the provided [`locale`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-locale).

### Field mapping [v6.2.1-plugins-codecs-cef-field-mapping]

The header fields from each CEF payload is expanded to the following fields, depending on whether ECS is enabled.

### Header field mapping [v6.2.1-plugins-codecs-cef-header-field]

| ECS Disabled | ECS Field |
| :- | :- |
| `cefVersion` | `[cef][version]` |
| `deviceVendor` | `[observer][vendor]` |
| `deviceProduct` | `[observer][product]` |
| `deviceVersion` | `[observer][version]` |
| `deviceEventClassId` | `[event][code]` |
| `name` | `[cef][name]` |
| `severity` | `[event][severity]` |

When decoding CEF payloads with `ecs_compatibility => disabled`, the abbreviated CEF Keys found in extensions are expanded, and CEF Field Names are inserted at the root level of the event.

When decoding in an ECS Compatibility mode, the ECS Fields are populated from the corresponding CEF Field Names *or* CEF Keys found in the payload’s extensions.

The following is a mapping between these fields.

### Extension field mapping [v6.2.1-plugins-codecs-cef-ext-field]

| CEF Field Name (optional CEF Key) | ECS Field |
| :- | :- |
| `agentAddress` (`agt`) | `[agent][ip]` |
| `agentDnsDomain` | `[cef][agent][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *higher* priority. |
| `agentHostName` (`ahost`) | `[agent][name]` |
| `agentId` (`aid`) | `[agent][id]` |
| `agentMacAddress` (`amac`) | `[agent][mac]` |
| `agentNtDomain` | `[cef][agent][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *lower* priority. |
| `agentReceiptTime` (`art`) | `[event][created]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `agentTimeZone` (`atz`) | `[cef][agent][timezone]` |
| `agentTranslatedAddress` | `[cef][agent][nat][ip]` |
| `agentTranslatedZoneExternalID` | `[cef][agent][translated_zone][external_id]` |
| `agentTranslatedZoneURI` | `[cef][agent][translated_zone][uri]` |
| `agentType` (`at`) | `[agent][type]` |
| `agentVersion` (`av`) | `[agent][version]` |
| `agentZoneExternalID` | `[cef][agent][zone][external_id]` |
| `agentZoneURI` | `[cef][agent][zone][uri]` |
| `applicationProtocol` (`app`) | `[network][protocol]` |
| `baseEventCount` (`cnt`) | `[cef][base_event_count]` |
| `bytesIn` (`in`) | `[source,shell][bytes]` |
| `bytesOut` (`out`) | `[destination][bytes]` |
| `categoryDeviceType` (`catdt`) | `[cef][device_type]` |
| `customerExternalID` | `[organization][id]` |
| `customerURI` | `[organization][name]` |
| `destinationAddress` (`dst`) | `[destination][ip]` |
| `destinationDnsDomain` | `[destination][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *higher* priority. |
| `destinationGeoLatitude` (`dlat`) | `[destination][geo][location][lat]` |
| `destinationGeoLongitude` (`dlong`) | `[destination][geo][location][lon]` |
| `destinationHostName` (`dhost`) | `[destination][domain]` |
| `destinationMacAddress` (`dmac`) | `[destination][mac]` |
| `destinationNtDomain` (`dntdom`) | `[destination][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *lower* priority. |
| `destinationPort` (`dpt`) | `[destination][port]` |
| `destinationProcessId` (`dpid`) | `[destination][process][pid]` |
| `destinationProcessName` (`dproc`) | `[destination][process][name]` |
| `destinationServiceName` | `[destination][service][name]` |
| `destinationTranslatedAddress` | `[destination][nat][ip]` |
| `destinationTranslatedPort` | `[destination][nat][port]` |
| `destinationTranslatedZoneExternalID` | `[cef][destination][translated_zone][external_id]` |
| `destinationTranslatedZoneURI` | `[cef][destination][translated_zone][uri]` |
| `destinationUserId` (`duid`) | `[destination][user][id]` |
| `destinationUserName` (`duser`) | `[destination][user][name]` |
| `destinationUserPrivileges` (`dpriv`) | `[destination][user][group][name]` |
| `destinationZoneExternalID` | `[cef][destination][zone][external_id]` |
| `destinationZoneURI` | `[cef][destination][zone][uri]` |
| `deviceAction` (`act`) | `[event][action]` |
| `deviceAddress` (`dvc`) | `[observer][ip]`When plugin configured with `device => observer` |
| | `[host][ip]`When plugin configured with `device => host` |
| `deviceCustomFloatingPoint1` (`cfp1`) | `[cef][device_custom_floating_point_1][value]` |
| `deviceCustomFloatingPoint1Label` (`cfp1Label`) | `[cef][device_custom_floating_point_1][label]` |
| `deviceCustomFloatingPoint2` (`cfp2`) | `[cef][device_custom_floating_point_2][value]` |
| `deviceCustomFloatingPoint2Label` (`cfp2Label`) | `[cef][device_custom_floating_point_2][label]` |
| `deviceCustomFloatingPoint3` (`cfp3`) | `[cef][device_custom_floating_point_3][value]` |
| `deviceCustomFloatingPoint3Label` (`cfp3Label`) | `[cef][device_custom_floating_point_3][label]` |
| `deviceCustomFloatingPoint4` (`cfp4`) | `[cef][device_custom_floating_point_4][value]` |
| `deviceCustomFloatingPoint4Label` (`cfp4Label`) | `[cef][device_custom_floating_point_4][label]` |
| `deviceCustomIPv6Address1` (`c6a1`) | `[cef][device_custom_ipv6_address_1][value]` |
| `deviceCustomIPv6Address1Label` (`c6a1Label`) | `[cef][device_custom_ipv6_address_1][label]` |
| `deviceCustomIPv6Address2` (`c6a2`) | `[cef][device_custom_ipv6_address_2][value]` |
| `deviceCustomIPv6Address2Label` (`c6a2Label`) | `[cef][device_custom_ipv6_address_2][label]` |
| `deviceCustomIPv6Address3` (`c6a3`) | `[cef][device_custom_ipv6_address_3][value]` |
| `deviceCustomIPv6Address3Label` (`c6a3Label`) | `[cef][device_custom_ipv6_address_3][label]` |
| `deviceCustomIPv6Address4` (`c6a4`) | `[cef][device_custom_ipv6_address_4][value]` |
| `deviceCustomIPv6Address4Label` (`c6a4Label`) | `[cef][device_custom_ipv6_address_4][label]` |
| `deviceCustomNumber1` (`cn1`) | `[cef][device_custom_number_1][value]` |
| `deviceCustomNumber1Label` (`cn1Label`) | `[cef][device_custom_number_1][label]` |
| `deviceCustomNumber2` (`cn2`) | `[cef][device_custom_number_2][value]` |
| `deviceCustomNumber2Label` (`cn2Label`) | `[cef][device_custom_number_2][label]` |
| `deviceCustomNumber3` (`cn3`) | `[cef][device_custom_number_3][value]` |
| `deviceCustomNumber3Label` (`cn3Label`) | `[cef][device_custom_number_3][label]` |
| `deviceCustomString1` (`cs1`) | `[cef][device_custom_string_1][value]` |
| `deviceCustomString1Label` (`cs1Label`) | `[cef][device_custom_string_1][label]` |
| `deviceCustomString2` (`cs2`) | `[cef][device_custom_string_2][value]` |
| `deviceCustomString2Label` (`cs2Label`) | `[cef][device_custom_string_2][label]` |
| `deviceCustomString3` (`cs3`) | `[cef][device_custom_string_3][value]` |
| `deviceCustomString3Label` (`cs3Label`) | `[cef][device_custom_string_3][label]` |
| `deviceCustomString4` (`cs4`) | `[cef][device_custom_string_4][value]` |
| `deviceCustomString4Label` (`cs4Label`) | `[cef][device_custom_string_4][label]` |
| `deviceCustomString5` (`cs5`) | `[cef][device_custom_string_5][value]` |
| `deviceCustomString5Label` (`cs5Label`) | `[cef][device_custom_string_5][label]` |
| `deviceCustomString6` (`cs6`) | `[cef][device_custom_string_6][value]` |
| `deviceCustomString6Label` (`cs6Label`) | `[cef][device_custom_string_6][label]` |
| `deviceDirection` | `[network][direction]` |
| `deviceDnsDomain` | `[observer][registered_domain]`When plugin configured with `device => observer`. |
| | `[host][registered_domain]`When plugin configured with `device => host`. |
| `deviceEventCategory` (`cat`) | `[cef][category]` |
| `deviceExternalId` | `[observer][name]`When plugin configured with `device => observer`. |
| | `[host][id]`When plugin configured with `device => host`. |
| `deviceFacility` | `[log][syslog][facility][code]` |
| `deviceHostName` (`dvchost`) | `[observer][hostname]`When plugin configured with `device => observer`. |
| | `[host][name]`When plugin configured with `device => host`. |
| `deviceInboundInterface` | `[observer][ingress][interface][name]` |
| `deviceMacAddress` (`dvcmac`) | `[observer][mac]`When plugin configured with `device => observer`. |
| | `[host][mac]`When plugin configured with `device => host`. |
| `deviceNtDomain` | `[cef][nt_domain]` |
| `deviceOutboundInterface` | `[observer][egress][interface][name]` |
| `devicePayloadId` | `[cef][payload_id]` |
| `deviceProcessId` (`dvcpid`) | `[process][pid]` |
| `deviceProcessName` | `[process][name]` |
| `deviceReceiptTime` (`rt`) | `@timestamp`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `deviceTimeZone` (`dtz`) | `[event][timezone]` |
| `deviceTranslatedAddress` | `[host][nat][ip]` |
| `deviceTranslatedZoneExternalID` | `[cef][translated_zone][external_id]` |
| `deviceTranslatedZoneURI` | `[cef][translated_zone][uri]` |
| `deviceVersion` | `[observer][version]` |
| `deviceZoneExternalID` | `[cef][zone][external_id]` |
| `deviceZoneURI` | `[cef][zone][uri]` |
| `endTime` (`end`) | `[event][end]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `eventId` | `[event][id]` |
| `eventOutcome` (`outcome`) | `[event][outcome]` |
| `externalId` | `[cef][external_id]` |
| `fileCreateTime` | `[file][created]` |
| `fileHash` | `[file][hash]]` |
| `fileId` | `[file][inode]` |
| `fileModificationTime` | `[file][mtime]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `fileName` (`fname`) | `[file][name]` |
| `filePath` | `[file][path]` |
| `filePermission` | `[file][group]` |
| `fileSize` (`fsize`) | `[file][size]` |
| `fileType` | `[file][extension]` |
| `managerReceiptTime` (`mrt`) | `[event][ingested]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `message` (`msg`) | `[message]` |
| `oldFileCreateTime` | `[cef][old_file][created]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `oldFileHash` | `[cef][old_file][hash]` |
| `oldFileId` | `[cef][old_file][inode]` |
| `oldFileModificationTime` | `[cef][old_file][mtime]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `oldFileName` | `[cef][old_file][name]` |
| `oldFilePath` | `[cef][old_file][path]` |
| `oldFilePermission` | `[cef][old_file][group]` |
| `oldFileSize` | `[cef][old_file][size]` |
| `oldFileType` | `[cef][old_file][extension]` |
| `rawEvent` | `[event][original]` |
| `Reason` (`reason`) | `[event][reason]` |
| `requestClientApplication` | `[user_agent][original]` |
| `requestContext` | `[http][request][referrer]` |
| `requestCookies` | `[cef][request][cookies]` |
| `requestMethod` | `[http][request][method]` |
| `requestUrl` (`request`) | `[url][original]` |
| `sourceAddress` (`src`) | `[source,shell][ip]` |
| `sourceDnsDomain` | `[source,shell][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *higher* priority. |
| `sourceGeoLatitude` (`slat`) | `[source,shell][geo][location][lat]` |
| `sourceGeoLongitude` (`slong`) | `[source,shell][geo][location][lon]` |
| `sourceHostName` (`shost`) | `[source,shell][domain]` |
| `sourceMacAddress` (`smac`) | `[source,shell][mac]` |
| `sourceNtDomain` (`sntdom`) | `[source,shell][registered_domain]`Multiple possible CEF fields map to this ECS Field. When decoding, the last entry encountered wins. When encoding, this field has *lower* priority. |
| `sourcePort` (`spt`) | `[source,shell][port]` |
| `sourceProcessId` (`spid`) | `[source,shell][process][pid]` |
| `sourceProcessName` (`sproc`) | `[source,shell][process][name]` |
| `sourceServiceName` | `[source,shell][service][name]` |
| `sourceTranslatedAddress` | `[source,shell][nat][ip]` |
| `sourceTranslatedPort` | `[source,shell][nat][port]` |
| `sourceTranslatedZoneExternalID` | `[cef][source,shell][translated_zone][external_id]` |
| `sourceTranslatedZoneURI` | `[cef][source,shell][translated_zone][uri]` |
| `sourceUserId` (`suid`) | `[source,shell][user][id]` |
| `sourceUserName` (`suser`) | `[source,shell][user][name]` |
| `sourceUserPrivileges` (`spriv`) | `[source,shell][user][group][name]` |
| `sourceZoneExternalID` | `[cef][source,shell][zone][external_id]` |
| `sourceZoneURI` | `[cef][source,shell][zone][uri]` |
| `startTime` (`start`) | `[event][start]`This field contains a timestamp. In ECS Compatibility Mode, it is parsed to a specific point in time. |
| `transportProtocol` (`proto`) | `[network][transport]` |
| `type` | `[cef][type]` |

## Cef Codec Configuration Options [v6.2.1-plugins-codecs-cef-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`default_timezone`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-default_timezone) | [string](/lsr/value-types.md#string) | No |
| [`delimiter`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-delimiter) | [string](/lsr/value-types.md#string) | No |
| [`device`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-device) | [string](/lsr/value-types.md#string) | No |
| [`ecs_compatibility`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`fields`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-fields) | [array](/lsr/value-types.md#array) | No |
| [`locale`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-locale) | [string](/lsr/value-types.md#string) | No |
| [`name`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-name) | [string](/lsr/value-types.md#string) | No |
| [`product`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-product) | [string](/lsr/value-types.md#string) | No |
| [`reverse_mapping`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-reverse_mapping) | [boolean](/lsr/value-types.md#boolean) | No |
| [`severity`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-severity) | [string](/lsr/value-types.md#string) | No |
| [`signature`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-signature) | [string](/lsr/value-types.md#string) | No |
| [`vendor`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-vendor) | [string](/lsr/value-types.md#string) | No |
| [`version`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-version) | [string](/lsr/value-types.md#string) | No |

### `default_timezone` [v6.2.1-plugins-codecs-cef-default_timezone]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * [Timezone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (such as `Europe/Moscow`, `America/Argentina/Buenos_Aires`)
  * UTC Offsets (such as `-08:00`, `+03:00`)

* The default value is your system time zone

* This option has no effect when *encoding*.

When parsing timestamp fields in ECS mode and encountering timestamps that do not contain UTC-offset information, the `deviceTimeZone` (`dtz`) field from the CEF payload is used to interpret the given time. If the event does not include timezone information, this `default_timezone` is used instead.

### `delimiter` [v6.2.1-plugins-codecs-cef-delimiter]

* Value type is [string](/lsr/value-types.md#string)
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

* `\r` (backslash "r") - means carriage return (ASCII 0x0D)
* `\n` (backslash "n") - means newline (ASCII 0x0A)

### `device` [v6.2.1-plugins-codecs-cef-device]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `observer`: indicates that device-specific fields represent the device used to *observe* the event.
  * `host`: indicates that device-specific fields represent the device on which the event *occurred*.

* The default value for this setting is `observer`.

* Option has no effect when [`ecs_compatibility => disabled`](v6-2-1-plugins-codecs-cef.md#v6.2.1-plugins-codecs-cef-ecs_compatibility).

* Option has no effect when *encoding*

Defines a set of device-specific CEF fields as either representing the device on which an event *occurred*, or merely the device from which the event was *observed*. This causes the relevant fields to be routed to either the `host` or the `observer` top-level groupings.

If the codec handles data from a variety of sources, the ECS recommendation is to use `observer`.

### `ecs_compatibility` [v6.2.1-plugins-codecs-cef-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: uses CEF-defined field names in the event (e.g., `bytesIn`, `sourceAddress`)
  * `v1`: supports ECS-compatible event fields (e.g., `[source,shell][bytes]`, `[source,shell][ip]`)

* Default value depends on which version of Logstash is running:

  * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
  * Otherwise, the default value is `disabled`.

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current) (ECS)].

### `fields` [v6.2.1-plugins-codecs-cef-fields]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, a list of fields can be provided to be included in CEF extensions part as key/value pairs.

### `locale` [v6.2.1-plugins-codecs-cef-locale]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * Abbreviated language\_COUNTRY format (e.g., `en_GB`, `pt_BR`)
  * Valid [IETF BCP 47](https://tools.ietf.org/html/bcp47) language tag (e.g., `zh-cmn-Hans-CN`)

* The default value is your system locale

* Option has no effect when *encoding*

When parsing timestamp fields in ECS mode and encountering timestamps in a localized format, this `locale` is used to interpret locale-specific strings such as month abbreviations.

### `name` [v6.2.1-plugins-codecs-cef-name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the name field in the CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `product` [v6.2.1-plugins-codecs-cef-product]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device product field in CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `reverse_mapping` [v6.2.1-plugins-codecs-cef-reverse_mapping]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`
* Option has no effect when *decoding*

Set to true to adhere to the specifications and encode using the CEF key name (short name) for the CEF field names.

### `severity` [v6.2.1-plugins-codecs-cef-severity]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"6"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the severity field in CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

Defined as field of type string to allow sprintf. The value will be validated to be an integer in the range from 0 to 10 (including). All invalid values will be mapped to the default of 6.

### `signature` [v6.2.1-plugins-codecs-cef-signature]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Logstash"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the signature ID field in CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `vendor` [v6.2.1-plugins-codecs-cef-vendor]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Elasticsearch"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device vendor field in CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `version` [v6.2.1-plugins-codecs-cef-version]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"1.0"`
* Option has no effect when *decoding*

When this codec is used in an Output Plugin, this option can be used to specify the value of the device version field in CEF header. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.
