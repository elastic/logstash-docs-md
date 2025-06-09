---
navigation_title: "v5.2.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.2.2-plugins-inputs-tcp.html
---

# Tcp input plugin v5.2.2 [v5.2.2-plugins-inputs-tcp]

* Plugin version: v5.2.2
* Released on: 2019-03-09
* [Changelog](https://github.com/logstash-plugins/logstash-input-tcp/blob/v5.2.2/CHANGELOG.md)

For other versions, see the [overview list](input-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_983]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_976]

Read events over a TCP socket.

Like stdin and file inputs, each event is assumed to be one line of text.

Can either accept connections from clients or connect to a server, depending on `mode`.

### Accepting log4j2 logs [_accepting_log4j2_logs_43]

Log4j2 can send JSON over a socket, and we can use that combined with our tcp input to accept the logs.

First, we need to configure your application to send logs in JSON over a socket. The following log4j2.xml accomplishes this task.

Note, you will want to change the `host` and `port` settings in this configuration to match your needs.

```
<Configuration>
  <Appenders>
     <Socket name="Socket" host="localhost" port="12345">
       <JsonLayout compact="true" eventEol="true" />
    </Socket>
  </Appenders>
  <Loggers>
    <Root level="info">
      <AppenderRef ref="Socket"/>
    </Root>
  </Loggers>
</Configuration>
```

To accept this in Logstash, you will want tcp input and a date filter:

```
input {
  tcp {
    port => 12345
    codec => json
  }
}
```

and add a date filter to take log4j2’s `timeMillis` field and use it as the event timestamp

```
filter {
  date {
    match => [ "timeMillis", "UNIX_MS" ]
  }
}
```

## Tcp Input Configuration Options [v5.2.2-plugins-inputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`host`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-host) | [string](/lsr/value-types.md#string) | No |
| [`mode`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`port`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-port) | [number](/lsr/value-types.md#number) | Yes |
| [`proxy_protocol`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-proxy_protocol) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_cert`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_cert) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_enable`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_enable) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_extra_chain_certs`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_extra_chain_certs) | [array](/lsr/value-types.md#array) | No |
| [`ssl_key`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verify`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-ssl_verify) | [boolean](/lsr/value-types.md#boolean) | No |
| [`tcp_keep_alive`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-tcp_keep_alive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`dns_reverse_lookup_enabled`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-dns_reverse_lookup_enabled) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-common-options) for a list of options supported by all input plugins.

### `host` [v5.2.2-plugins-inputs-tcp-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.

### `mode` [v5.2.2-plugins-inputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.

### `port` [v5.2.2-plugins-inputs-tcp-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.

### `proxy_protocol` [v5.2.2-plugins-inputs-tcp-proxy_protocol]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time <http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt>

### `ssl_cert` [v5.2.2-plugins-inputs-tcp-ssl_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Path to certificate in PEM format. This certificate will be presented to the connecting clients.

### `ssl_certificate_authorities` [v5.2.2-plugins-inputs-tcp-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificate or certificate chain against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store.

### `ssl_enable` [v5.2.2-plugins-inputs-tcp-ssl_enable]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).

### `ssl_extra_chain_certs` [v5.2.2-plugins-inputs-tcp-ssl_extra_chain_certs]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

An Array of paths to extra X509 certificates. These are used together with the certificate to construct the certificate chain presented to the client.

### `ssl_key` [v5.2.2-plugins-inputs-tcp-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The path to the private key corresponding to the specified certificate (PEM format).

### `ssl_key_passphrase` [v5.2.2-plugins-inputs-tcp-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `nil`

SSL key passphrase for the private key.

### `ssl_verify` [v5.2.2-plugins-inputs-tcp-ssl_verify]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.

### `tcp_keep_alive` [v5.2.2-plugins-inputs-tcp-tcp_keep_alive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Instruct the socket to use TCP keep alives. Uses OS defaults for keep alive settings.

### `dns_reverse_lookup_enabled` [v5.2.2-plugins-inputs-tcp-dns_reverse_lookup_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

It is possible to avoid DNS reverse-lookups by disabling this setting. If disabled, the address metadata that is added to events will contain the source address as-specified at the TCP layer and IPs will not be resolved to hostnames.

## Common options [v5.2.2-plugins-inputs-tcp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v5-2-2-plugins-inputs-tcp.md#v5.2.2-plugins-inputs-tcp-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v5.2.2-plugins-inputs-tcp-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v5.2.2-plugins-inputs-tcp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"line"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.2.2-plugins-inputs-tcp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.2.2-plugins-inputs-tcp-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 tcp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  tcp {
    id => "my_plugin_id"
  }
}
```

### `tags` [v5.2.2-plugins-inputs-tcp-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v5.2.2-plugins-inputs-tcp-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
