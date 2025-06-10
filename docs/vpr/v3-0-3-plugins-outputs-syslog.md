---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-syslog.html
---

# Syslog output plugin v3.0.3 [v3.0.3-plugins-outputs-syslog]

* Plugin version: v3.0.3
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-syslog/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-syslog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1643]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-syslog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1633]

Send events to a syslog server.

You can send messages compliant with RFC3164 or RFC5424 using either UDP or TCP as the transport protocol.

By default the contents of the `message` field will be shipped as the free-form message text part of the emitted syslog message. If your messages don’t have a `message` field or if you for some other reason want to change the emitted message, modify the `message` configuration option.

## Syslog Output Configuration Options [v3.0.3-plugins-outputs-syslog-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`appname`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-appname) | [string](/lsr/value-types.md#string) | No |
| [`facility`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-facility) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-host) | [string](/lsr/value-types.md#string) | Yes |
| [`message`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-message) | [string](/lsr/value-types.md#string) | No |
| [`msgid`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-msgid) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-port) | [number](/lsr/value-types.md#number) | Yes |
| [`priority`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-priority) | [string](/lsr/value-types.md#string) | No |
| [`procid`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-procid) | [string](/lsr/value-types.md#string) | No |
| [`protocol`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-protocol) | [string](/lsr/value-types.md#string), one of `["tcp", "udp", "ssl-tcp"]` | No |
| [`reconnect_interval`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-reconnect_interval) | [number](/lsr/value-types.md#number) | No |
| [`rfc`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-rfc) | [string](/lsr/value-types.md#string), one of `["rfc3164", "rfc5424"]` | No |
| [`severity`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-severity) | [string](/lsr/value-types.md#string) | No |
| [`sourcehost`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-sourcehost) | [string](/lsr/value-types.md#string) | No |
| [`ssl_cacert`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-ssl_cacert) | a valid filesystem path | No |
| [`ssl_cert`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-ssl_cert) | a valid filesystem path | No |
| [`ssl_key`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verify`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-ssl_verify) | [boolean](/lsr/value-types.md#boolean) | No |
| [`use_labels`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-use_labels) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-common-options) for a list of options supported by all output plugins.

### `appname` [v3.0.3-plugins-outputs-syslog-appname]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"LOGSTASH"`

application name for syslog message. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `facility` [v3.0.3-plugins-outputs-syslog-facility]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"user-level"`

facility label for syslog message default fallback to user-level as in rfc3164 The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `host` [v3.0.3-plugins-outputs-syslog-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

syslog server address to connect to

### `message` [v3.0.3-plugins-outputs-syslog-message]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{message}"`

message text to log. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `msgid` [v3.0.3-plugins-outputs-syslog-msgid]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"-"`

message id for syslog message. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `port` [v3.0.3-plugins-outputs-syslog-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

syslog server port to connect to

### `priority` [v3.0.3-plugins-outputs-syslog-priority]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{syslog_pri}"`

syslog priority The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `procid` [v3.0.3-plugins-outputs-syslog-procid]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"-"`

process id for syslog message. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `protocol` [v3.0.3-plugins-outputs-syslog-protocol]

* Value can be any of: `tcp`, `udp`, `ssl-tcp`
* Default value is `"udp"`

syslog server protocol. you can choose between udp, tcp and ssl/tls over tcp

### `reconnect_interval` [v3.0.3-plugins-outputs-syslog-reconnect_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

when connection fails, retry interval in sec.

### `rfc` [v3.0.3-plugins-outputs-syslog-rfc]

* Value can be any of: `rfc3164`, `rfc5424`
* Default value is `"rfc3164"`

syslog message format: you can choose between rfc3164 or rfc5424

### `severity` [v3.0.3-plugins-outputs-syslog-severity]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"notice"`

severity label for syslog message default fallback to notice as in rfc3164 The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `sourcehost` [v3.0.3-plugins-outputs-syslog-sourcehost]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"%{host}"`

source host for syslog message. The new value can include `%{foo}` strings to help you build a new value from other parts of the event.

### `ssl_cacert` [v3.0.3-plugins-outputs-syslog-ssl_cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.

### `ssl_cert` [v3.0.3-plugins-outputs-syslog-ssl_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate path

### `ssl_key` [v3.0.3-plugins-outputs-syslog-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key path

### `ssl_key_passphrase` [v3.0.3-plugins-outputs-syslog-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `nil`

SSL key passphrase

### `ssl_verify` [v3.0.3-plugins-outputs-syslog-ssl_verify]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Verify the identity of the other end of the SSL connection against the CA.

### `use_labels` [v3.0.3-plugins-outputs-syslog-use_labels]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

use label parsing for severity and facility levels use priority field if set to false

## Common options [v3.0.3-plugins-outputs-syslog-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-syslog.md#v3.0.3-plugins-outputs-syslog-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-syslog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.3-plugins-outputs-syslog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-outputs-syslog-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 syslog outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  syslog {
    id => "my_plugin_id"
  }
}
```
