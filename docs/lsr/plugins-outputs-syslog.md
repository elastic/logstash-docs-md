---
navigation_title: "syslog"
---

# Syslog output plugin [plugins-outputs-syslog]


* Plugin version: v3.0.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-syslog/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/output-syslog-index.md).

## Installation [_installation_49]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-output-syslog`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html) for more details.


## Getting help [_getting_help_115]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-syslog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_114]

Send events to a syslog server.

You can send messages compliant with RFC3164 or RFC5424 using either UDP or TCP as the transport protocol.

By default the contents of the `message` field will be shipped as the free-form message text part of the emitted syslog message. If your messages don’t have a `message` field or if you for some other reason want to change the emitted message, modify the `message` configuration option.


## Syslog Output Configuration Options [plugins-outputs-syslog-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-syslog.md#plugins-outputs-syslog-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`appname`](plugins-outputs-syslog.md#plugins-outputs-syslog-appname) | [string](introduction.md#string) | No |
| [`facility`](plugins-outputs-syslog.md#plugins-outputs-syslog-facility) | [string](introduction.md#string) | No |
| [`host`](plugins-outputs-syslog.md#plugins-outputs-syslog-host) | [string](introduction.md#string) | Yes |
| [`message`](plugins-outputs-syslog.md#plugins-outputs-syslog-message) | [string](introduction.md#string) | No |
| [`msgid`](plugins-outputs-syslog.md#plugins-outputs-syslog-msgid) | [string](introduction.md#string) | No |
| [`port`](plugins-outputs-syslog.md#plugins-outputs-syslog-port) | [number](introduction.md#number) | Yes |
| [`priority`](plugins-outputs-syslog.md#plugins-outputs-syslog-priority) | [string](introduction.md#string) | No |
| [`procid`](plugins-outputs-syslog.md#plugins-outputs-syslog-procid) | [string](introduction.md#string) | No |
| [`protocol`](plugins-outputs-syslog.md#plugins-outputs-syslog-protocol) | [string](introduction.md#string), one of `["tcp", "udp", "ssl-tcp"]` | No |
| [`reconnect_interval`](plugins-outputs-syslog.md#plugins-outputs-syslog-reconnect_interval) | [number](introduction.md#number) | No |
| [`rfc`](plugins-outputs-syslog.md#plugins-outputs-syslog-rfc) | [string](introduction.md#string), one of `["rfc3164", "rfc5424"]` | No |
| [`severity`](plugins-outputs-syslog.md#plugins-outputs-syslog-severity) | [string](introduction.md#string) | No |
| [`sourcehost`](plugins-outputs-syslog.md#plugins-outputs-syslog-sourcehost) | [string](introduction.md#string) | No |
| [`ssl_cacert`](plugins-outputs-syslog.md#plugins-outputs-syslog-ssl_cacert) | a valid filesystem path | No |
| [`ssl_cert`](plugins-outputs-syslog.md#plugins-outputs-syslog-ssl_cert) | a valid filesystem path | No |
| [`ssl_key`](plugins-outputs-syslog.md#plugins-outputs-syslog-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](plugins-outputs-syslog.md#plugins-outputs-syslog-ssl_key_passphrase) | [password](introduction.md#password) | No |
| [`ssl_verify`](plugins-outputs-syslog.md#plugins-outputs-syslog-ssl_verify) | [boolean](introduction.md#boolean) | No |
| [`use_labels`](plugins-outputs-syslog.md#plugins-outputs-syslog-use_labels) | [boolean](introduction.md#boolean) | No |

Also see [Common options](plugins-outputs-syslog.md#plugins-outputs-syslog-common-options) for a list of options supported by all output plugins.

 

### `appname` [plugins-outputs-syslog-appname]

* Value type is [string](introduction.md#string)
* Default value is `"LOGSTASH"`

application name for syslog message. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `facility` [plugins-outputs-syslog-facility]

* Value type is [string](introduction.md#string)
* Default value is `"user-level"`

facility label for syslog message default fallback to user-level as in rfc3164 The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `host` [plugins-outputs-syslog-host]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

syslog server address to connect to


### `message` [plugins-outputs-syslog-message]

* Value type is [string](introduction.md#string)
* Default value is `"%{{message}}"`

message text to log. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `msgid` [plugins-outputs-syslog-msgid]

* Value type is [string](introduction.md#string)
* Default value is `"-"`

message id for syslog message. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `port` [plugins-outputs-syslog-port]

* This is a required setting.
* Value type is [number](introduction.md#number)
* There is no default value for this setting.

syslog server port to connect to


### `priority` [plugins-outputs-syslog-priority]

* Value type is [string](introduction.md#string)
* Default value is `"%{{syslog_pri}}"`

syslog priority The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `procid` [plugins-outputs-syslog-procid]

* Value type is [string](introduction.md#string)
* Default value is `"-"`

process id for syslog message. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `protocol` [plugins-outputs-syslog-protocol]

* Value can be any of: `tcp`, `udp`, `ssl-tcp`
* Default value is `"udp"`

syslog server protocol. you can choose between udp, tcp and ssl/tls over tcp


### `reconnect_interval` [plugins-outputs-syslog-reconnect_interval]

* Value type is [number](introduction.md#number)
* Default value is `1`

when connection fails, retry interval in sec.


### `rfc` [plugins-outputs-syslog-rfc]

* Value can be any of: `rfc3164`, `rfc5424`
* Default value is `"rfc3164"`

syslog message format: you can choose between rfc3164 or rfc5424


### `severity` [plugins-outputs-syslog-severity]

* Value type is [string](introduction.md#string)
* Default value is `"notice"`

severity label for syslog message default fallback to notice as in rfc3164 The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `sourcehost` [plugins-outputs-syslog-sourcehost]

* Value type is [string](introduction.md#string)
* Default value is `"%{{host}}"`

source host for syslog message. The new value can include `%{{foo}}` strings to help you build a new value from other parts of the event.


### `ssl_cacert` [plugins-outputs-syslog-ssl_cacert]

* Value type is [path](introduction.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.


### `ssl_cert` [plugins-outputs-syslog-ssl_cert]

* Value type is [path](introduction.md#path)
* There is no default value for this setting.

SSL certificate path


### `ssl_key` [plugins-outputs-syslog-ssl_key]

* Value type is [path](introduction.md#path)
* There is no default value for this setting.

SSL key path


### `ssl_key_passphrase` [plugins-outputs-syslog-ssl_key_passphrase]

* Value type is [password](introduction.md#password)
* Default value is `nil`

SSL key passphrase


### `ssl_verify` [plugins-outputs-syslog-ssl_verify]

* Value type is [boolean](introduction.md#boolean)
* Default value is `false`

Verify the identity of the other end of the SSL connection against the CA.


### `use_labels` [plugins-outputs-syslog-use_labels]

* Value type is [boolean](introduction.md#boolean)
* Default value is `true`

use label parsing for severity and facility levels use priority field if set to false



## Common options [plugins-outputs-syslog-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](plugins-outputs-syslog.md#plugins-outputs-syslog-codec) | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](plugins-outputs-syslog.md#plugins-outputs-syslog-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-outputs-syslog.md#plugins-outputs-syslog-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

### `codec` [plugins-outputs-syslog-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [plugins-outputs-syslog-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-syslog-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 syslog outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  syslog {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




