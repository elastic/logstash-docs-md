---
navigation_title: "v3.2.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.4-plugins-inputs-syslog.html
---

# Syslog input plugin v3.2.4 [v3.2.4-plugins-inputs-syslog]

* Plugin version: v3.2.4
* Released on: 2017-12-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-syslog/blob/v3.2.4/CHANGELOG.md)

For other versions, see the [overview list](input-syslog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_937]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-syslog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_930]

Read syslog messages as events over the network.

This input is a good choice if you already use syslog today. It is also a good choice if you want to receive logs from appliances and network devices where you cannot run your own log collector.

Of course, *syslog* is a very muddy term. This input only supports `RFC3164` syslog with some small modifications. The date format is allowed to be `RFC3164` style or `ISO8601`. Otherwise the rest of `RFC3164` must be obeyed. If you do not use `RFC3164`, do not use this input.

For more information see the [RFC3164 page](http://www.ietf.org/rfc/rfc3164.txt).

Note: This input will start listeners on both TCP and UDP.

## Syslog Input Configuration Options [v3.2.4-plugins-inputs-syslog-options]

This plugin supports the following configuration options plus the [Common options](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`facility_labels`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-facility_labels) | [array](/lsr/value-types.md#array) | No |
| [`host`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-host) | [string](/lsr/value-types.md#string) | No |
| [`locale`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-locale) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-port) | [number](/lsr/value-types.md#number) | No |
| [`proxy_protocol`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-proxy_protocol) | [boolean](/lsr/value-types.md#boolean) | No |
| [`severity_labels`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-severity_labels) | [array](/lsr/value-types.md#array) | No |
| [`timezone`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-timezone) | [string](/lsr/value-types.md#string) | No |
| [`use_labels`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-use_labels) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-common-options) for a list of options supported by all input plugins.

### `facility_labels` [v3.2.4-plugins-inputs-syslog-facility_labels]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["kernel", "user-level", "mail", "system", "security/authorization", "syslogd", "line printer", "network news", "UUCP", "clock", "security/authorization", "FTP", "NTP", "log audit", "log alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]`

Labels for facility levels. These are defined in RFC3164.

### `host` [v3.2.4-plugins-inputs-syslog-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The address to listen on.

### `locale` [v3.2.4-plugins-inputs-syslog-locale]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Specify a locale to be used for date parsing using either IETF-BCP47 or POSIX language tag. Simple examples are `en`,`en-US` for BCP47 or `en_US` for POSIX. If not specified, the platform default will be used.

The locale is mostly necessary to be set for parsing month names (pattern with MMM) and weekday names (pattern with EEE).

### `port` [v3.2.4-plugins-inputs-syslog-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `514`

The port to listen on. Remember that ports less than 1024 (privileged ports) may require root to use.

### `proxy_protocol` [v3.2.4-plugins-inputs-syslog-proxy_protocol]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time <http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt>

### `severity_labels` [v3.2.4-plugins-inputs-syslog-severity_labels]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["Emergency", "Alert", "Critical", "Error", "Warning", "Notice", "Informational", "Debug"]`

Labels for severity levels. These are defined in RFC3164.

### `timezone` [v3.2.4-plugins-inputs-syslog-timezone]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Specify a time zone canonical ID to be used for date parsing. The valid IDs are listed on the \[Joda.org available time zones page]\(<http://joda-time.sourceforge.net/timezones.html>). This is useful in case the time zone cannot be extracted from the value, and is not the platform default. If this is not specified the platform default will be used. Canonical ID is good as it takes care of daylight saving time for you For example, `America/Los_Angeles` or `Europe/France` are valid IDs.

### `use_labels` [v3.2.4-plugins-inputs-syslog-use_labels]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Use label parsing for severity and facility levels.

## Common options [v3.2.4-plugins-inputs-syslog-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-2-4-plugins-inputs-syslog.md#v3.2.4-plugins-inputs-syslog-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.2.4-plugins-inputs-syslog-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.2.4-plugins-inputs-syslog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.2.4-plugins-inputs-syslog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.2.4-plugins-inputs-syslog-id]

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

### `tags` [v3.2.4-plugins-inputs-syslog-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.2.4-plugins-inputs-syslog-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
