---
navigation_title: "v3.4.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.4.3-plugins-inputs-syslog.html
---

# Syslog input plugin v3.4.3 [v3.4.3-plugins-inputs-syslog]

* Plugin version: v3.4.3
* Released on: 2020-05-19
* [Changelog](https://github.com/logstash-plugins/logstash-input-syslog/blob/v3.4.3/CHANGELOG.md)

For other versions, see the [overview list](input-syslog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_932]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-syslog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_925]

Read syslog messages as events over the network.

This input is a good choice if you already use syslog today. It is also a good choice if you want to receive logs from appliances and network devices where you cannot run your own log collector.

Of course, *syslog* is a very muddy term. By default, this input only supports `RFC3164` syslog with some small modifications. However, some non-standard syslog formats can be read and parsed if a functional `grok_pattern` is provided. The date format is still only allowed to be `RFC3164` style or `ISO8601`.

For more information see the [RFC3164 page](http://www.ietf.org/rfc/rfc3164.txt).

Note: This input will start listeners on both TCP and UDP.

## Syslog Input Configuration Options [v3.4.3-plugins-inputs-syslog-options]

This plugin supports the following configuration options plus the [Common options](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`facility_labels`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-facility_labels) | [array](/lsr/value-types.md#array) | No |
| [`grok_pattern`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-grok_pattern) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-host) | [string](/lsr/value-types.md#string) | No |
| [`locale`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-locale) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-port) | [number](/lsr/value-types.md#number) | No |
| [`proxy_protocol`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-proxy_protocol) | [boolean](/lsr/value-types.md#boolean) | No |
| [`severity_labels`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-severity_labels) | [array](/lsr/value-types.md#array) | No |
| [`syslog_field`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-syslog_field) | [string](/lsr/value-types.md#string) | No |
| [`timezone`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-timezone) | [string](/lsr/value-types.md#string) | No |
| [`use_labels`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-use_labels) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-common-options) for a list of options supported by all input plugins.

### `facility_labels` [v3.4.3-plugins-inputs-syslog-facility_labels]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["kernel", "user-level", "mail", "system", "security/authorization", "syslogd", "line printer", "network news", "UUCP", "clock", "security/authorization", "FTP", "NTP", "log audit", "log alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]`

Labels for facility levels defined in RFC3164.

You can use this option to override the integer→label mapping for syslog inputs that behave differently than the RFCs.

Provide a zero-indexed array with all of your facility labels *in order*. If a log message contains a facility number with no corresponding entry, the facility\_label is not added to the event.

### `grok_pattern` [v3.4.3-plugins-inputs-syslog-grok_pattern]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"<%{POSINT:priority}>%{SYSLOGLINE}"`

The default value should read and properly parse syslog lines which are fully compliant with [RFC3164](http://www.ietf.org/rfc/rfc3164.txt).

You can override this value to parse non-standard lines with a valid grok pattern which will parse the received lines. If the line is unable to be parsed, the `_grokparsefailure_sysloginput` tag will be added.

The grok pattern must provide a `timestamp` field. If the `timestamp` field is omitted, or is unable to be parsed as `RFC3164` style or `ISO8601`, a `_dateparsefailure` tag will be added.

### `host` [v3.4.3-plugins-inputs-syslog-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The address to listen on.

### `locale` [v3.4.3-plugins-inputs-syslog-locale]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Specify a locale to be used for date parsing using either IETF-BCP47 or POSIX language tag. Simple examples are `en`,`en-US` for BCP47 or `en_US` for POSIX. If not specified, the platform default will be used.

The locale is mostly necessary to be set for parsing month names (pattern with MMM) and weekday names (pattern with EEE).

### `port` [v3.4.3-plugins-inputs-syslog-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `514`

The port to listen on. Remember that ports less than 1024 (privileged ports) may require root to use.

### `proxy_protocol` [v3.4.3-plugins-inputs-syslog-proxy_protocol]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time <http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt>

### `severity_labels` [v3.4.3-plugins-inputs-syslog-severity_labels]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["Emergency", "Alert", "Critical", "Error", "Warning", "Notice", "Informational", "Debug"]`

Labels for severity levels defined in RFC3164.

Provide a zero-indexed array with all of your severity labels *in order*. If a log message contains a severity label with no corresponding entry, the severity\_label is not added to the event.

### `syslog_field` [v3.4.3-plugins-inputs-syslog-syslog_field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

Codecs process the data before the rest of the data is parsed. Some codecs, like CEF, put the syslog data into another field after pre-processing the data. Use this option in conjunction with the `grok_pattern` configuration to allow the syslog input plugin to fully parse the syslog data in this case.

```
input {
  syslog {
    port => 12345
    codec => cef
    syslog_field => "syslog"
    grok_pattern => "<%{POSINT:priority}>%{SYSLOGTIMESTAMP:timestamp} CUSTOM GROK HERE"
  }
}
```

### `timezone` [v3.4.3-plugins-inputs-syslog-timezone]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Specify a time zone canonical ID to be used for date parsing. The valid IDs are listed on the \[Joda.org available time zones page]\(<http://joda-time.sourceforge.net/timezones.html>). This is useful in case the time zone cannot be extracted from the value, and is not the platform default. If this is not specified the platform default will be used. Canonical ID is good as it takes care of daylight saving time for you. For example, `America/Los_Angeles` or `Europe/Paris` are valid IDs.

### `use_labels` [v3.4.3-plugins-inputs-syslog-use_labels]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Use label parsing for severity and facility levels.

## Common options [v3.4.3-plugins-inputs-syslog-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-4-3-plugins-inputs-syslog.md#v3.4.3-plugins-inputs-syslog-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.4.3-plugins-inputs-syslog-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.4.3-plugins-inputs-syslog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.4.3-plugins-inputs-syslog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.4.3-plugins-inputs-syslog-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 syslog inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  syslog {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.4.3-plugins-inputs-syslog-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.4.3-plugins-inputs-syslog-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
