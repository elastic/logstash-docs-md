---
navigation_title: "v6.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.1.1-plugins-outputs-tcp.html
---

# Tcp output plugin v6.1.1 [v6.1.1-plugins-outputs-tcp]


* Plugin version: v6.1.1
* Released on: 2022-08-21
* [Changelog](https://github.com/logstash-plugins/logstash-output-tcp/blob/v6.1.1/CHANGELOG.md)

For other versions, see the [overview list](output-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1632]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1622]

Write events over a TCP socket.

Each event json is separated by a newline.

Can either accept connections from clients or connect to a server, depending on `mode`.


## Tcp Output Configuration Options [v6.1.1-plugins-outputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`mode`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["server", "client"]` | No |
| [`port`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`reconnect_interval`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-reconnect_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_cacert`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_cacert) | a valid filesystem path | No |
| [`ssl_cert`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_cert) | a valid filesystem path | No |
| [`ssl_enable`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_enable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_supported_protocols`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_supported_protocols) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_verify`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-ssl_verify) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-common-options) for a list of options supported by all output plugins.

 

### `host` [v6.1.1-plugins-outputs-tcp-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.


### `mode` [v6.1.1-plugins-outputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"client"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.


### `port` [v6.1.1-plugins-outputs-tcp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.


### `reconnect_interval` [v6.1.1-plugins-outputs-tcp-reconnect_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

When connect failed,retry interval in sec.


### `ssl_cacert` [v6.1.1-plugins-outputs-tcp-ssl_cacert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.


### `ssl_cert` [v6.1.1-plugins-outputs-tcp-ssl_cert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate path


### `ssl_enable` [v6.1.1-plugins-outputs-tcp-ssl_enable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).


### `ssl_key` [v6.1.1-plugins-outputs-tcp-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key path


### `ssl_key_passphrase` [v6.1.1-plugins-outputs-tcp-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

SSL key passphrase


### `ssl_supported_protocols` [v6.1.1-plugins-outputs-tcp-ssl_supported_protocols]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a secure connection.

::::{note}
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_verify` [v6.1.1-plugins-outputs-tcp-ssl_verify]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.



## Common options [v6.1.1-plugins-outputs-tcp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v6-1-1-plugins-outputs-tcp.md#v6.1.1-plugins-outputs-tcp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v6.1.1-plugins-outputs-tcp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v6.1.1-plugins-outputs-tcp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v6.1.1-plugins-outputs-tcp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 tcp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  tcp {
    id => "my_plugin_id"
  }
}
```



