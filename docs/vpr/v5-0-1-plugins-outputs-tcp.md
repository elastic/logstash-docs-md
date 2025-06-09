---
navigation_title: "v5.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.1-plugins-outputs-tcp.html
---

# Tcp output plugin v5.0.1 [v5.0.1-plugins-outputs-tcp]

* Plugin version: v5.0.1
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-tcp/blob/v5.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1658]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1648]

Write events over a TCP socket.

Each event json is separated by a newline.

Can either accept connections from clients or connect to a server, depending on `mode`.

## Tcp Output Configuration Options [v5.0.1-plugins-outputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`host`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-host) | [string](/lsr/value-types.md#string) | Yes |
| [`mode`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`port`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-port) | [number](/lsr/value-types.md#number) | Yes |
| [`reconnect_interval`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-reconnect_interval) | [number](/lsr/value-types.md#number) | No |
| [`ssl_cacert`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_cacert) | a valid filesystem path | No |
| [`ssl_cert`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_cert) | a valid filesystem path | No |
| [`ssl_enable`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_enable) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_key`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verify`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-ssl_verify) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-common-options) for a list of options supported by all output plugins.

### `host` [v5.0.1-plugins-outputs-tcp-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.

### `mode` [v5.0.1-plugins-outputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"client"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.

### `port` [v5.0.1-plugins-outputs-tcp-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.

### `reconnect_interval` [v5.0.1-plugins-outputs-tcp-reconnect_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

When connect failed,retry interval in sec.

### `ssl_cacert` [v5.0.1-plugins-outputs-tcp-ssl_cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.

### `ssl_cert` [v5.0.1-plugins-outputs-tcp-ssl_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate path

### `ssl_enable` [v5.0.1-plugins-outputs-tcp-ssl_enable]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).

### `ssl_key` [v5.0.1-plugins-outputs-tcp-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key path

### `ssl_key_passphrase` [v5.0.1-plugins-outputs-tcp-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `nil`

SSL key passphrase

### `ssl_verify` [v5.0.1-plugins-outputs-tcp-ssl_verify]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.

## Common options [v5.0.1-plugins-outputs-tcp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-0-1-plugins-outputs-tcp.md#v5.0.1-plugins-outputs-tcp-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v5.0.1-plugins-outputs-tcp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.0.1-plugins-outputs-tcp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.0.1-plugins-outputs-tcp-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 tcp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  tcp {
    id => "my_plugin_id"
  }
}
```
