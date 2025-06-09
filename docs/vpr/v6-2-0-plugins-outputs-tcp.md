---
navigation_title: "v6.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.2.0-plugins-outputs-tcp.html
---

# Tcp output plugin v6.2.0 [v6.2.0-plugins-outputs-tcp]

* Plugin version: v6.2.0
* Released on: 2023-12-19
* [Changelog](https://github.com/logstash-plugins/logstash-output-tcp/blob/v6.2.0/CHANGELOG.md)

For other versions, see the [overview list](output-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1649]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1639]

Write events over a TCP socket.

Each event json is separated by a newline.

Can either accept connections from clients or connect to a server, depending on `mode`.

## Tcp Output Configuration Options [v6.2.0-plugins-outputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`host`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-host) | [string](/lsr/value-types.md#string) | Yes |
| [`mode`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`port`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-port) | [number](/lsr/value-types.md#number) | Yes |
| [`reconnect_interval`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-reconnect_interval) | [number](/lsr/value-types.md#number) | No |
| [`ssl_cacert`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_cacert) | a valid filesystem path | *Deprecated* |
| [`ssl_cert`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_cert) | a valid filesystem path | *Deprecated* |
| [`ssl_certificate`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_cipher_suites`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_cipher_suites) | [string](/lsr/value-types.md#string) | No |
| [`ssl_client_authentication`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_client_authentication) | [string](/lsr/value-types.md#string), one of `["none", "optional", "required"]` | No |
| [`ssl_enable`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_enable) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`ssl_enabled`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_enabled) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_key`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_supported_protocols`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_supported_protocols) | [string](/lsr/value-types.md#string) | No |
| [`ssl_verification_mode`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_verification_mode) | [string](/lsr/value-types.md#string), one of `["full", "none"]` | No |
| [`ssl_verify`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_verify) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-common-options) for a list of options supported by all output plugins.

### `host` [v6.2.0-plugins-outputs-tcp-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.

### `mode` [v6.2.0-plugins-outputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"client"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.

### `port` [v6.2.0-plugins-outputs-tcp-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.

### `reconnect_interval` [v6.2.0-plugins-outputs-tcp-reconnect_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

When connect failed,retry interval in sec.

### `ssl_cacert` [v6.2.0-plugins-outputs-tcp-ssl_cacert]

Deprecated in 6.2.0.

Replaced by [`ssl_certificate_authorities`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate_authorities)

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.

### `ssl_cert` [v6.2.0-plugins-outputs-tcp-ssl_cert]

Deprecated in 6.2.0.

Replaced by [`ssl_certificate`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate)

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate path

### `ssl_certificate` [v6.2.0-plugins-outputs-tcp-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Path to certificate in PEM format. This certificate will be presented to the other part of the TLS connection.

### `ssl_certificate_authorities` [v6.2.0-plugins-outputs-tcp-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificate or certificate chain against these authorities. You can define multiple files. All the certificates will be read and added to the trust store. The system CA path is automatically included.

### `ssl_cipher_suites` [v6.2.0-plugins-outputs-tcp-ssl_cipher_suites]

* Value type is a list of [string](/lsr/value-types.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.

### `ssl_client_authentication` [v6.2.0-plugins-outputs-tcp-ssl_client_authentication]

* Value can be any of: `none`, `optional`, `required`
* Default value is `none`

Controls the server’s behavior in regard to requesting a certificate from client connections: `none` disables the client authentication. `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one.

When mutual TLS is enabled (`optional` or `required`), the certificate presented by the client must be signed by trusted [`ssl_certificate_authorities`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate_authorities) (CAs). Please note that the server does not validate the client certificate CN (Common Name) or SAN (Subject Alternative Name).

This setting can be used only if [`mode`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-mode) is `server` and [`ssl_certificate_authorities`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_certificate_authorities) is set.

### `ssl_enable` [v6.2.0-plugins-outputs-tcp-ssl_enable]

Deprecated in 6.2.0.

Replaced by [`ssl_enabled`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_enabled)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).

### `ssl_enabled` [v6.2.0-plugins-outputs-tcp-ssl_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).

### `ssl_key` [v6.2.0-plugins-outputs-tcp-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key path

### `ssl_key_passphrase` [v6.2.0-plugins-outputs-tcp-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `nil`

SSL key passphrase

### `ssl_supported_protocols` [v6.2.0-plugins-outputs-tcp-ssl_supported_protocols]

* Value type is [string](/lsr/value-types.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a secure connection.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_verification_mode` [v6.2.0-plugins-outputs-tcp-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another part in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not\_before and not\_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.

This setting can be used only if [`mode`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-mode) is `client`.

### `ssl_verify` [v6.2.0-plugins-outputs-tcp-ssl_verify]

Deprecated in 6.2.0.

Replaced by [`ssl_client_authentication`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_client_authentication) and [`ssl_verification_mode`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-ssl_verification_mode)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.

## Common options [v6.2.0-plugins-outputs-tcp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v6-2-0-plugins-outputs-tcp.md#v6.2.0-plugins-outputs-tcp-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v6.2.0-plugins-outputs-tcp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v6.2.0-plugins-outputs-tcp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v6.2.0-plugins-outputs-tcp-id]

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
