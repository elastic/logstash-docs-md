---
navigation_title: "v5.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.3-plugins-inputs-tcp.html
---

# Tcp input plugin v5.0.3 [v5.0.3-plugins-inputs-tcp]


* Plugin version: v5.0.3
* Released on: 2017-12-27
* [Changelog](https://github.com/logstash-plugins/logstash-input-tcp/blob/v5.0.3/CHANGELOG.md)

For other versions, see the [overview list](input-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_958]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_951]

Read events over a TCP socket.

Like stdin and file inputs, each event is assumed to be one line of text.

Can either accept connections from clients or connect to a server, depending on `mode`.

### Accepting log4j2 logs [_accepting_log4j2_logs_49]

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


## Tcp Input Configuration Options [v5.0.3-plugins-inputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`mode`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["server", "client"]` | No |
| [`port`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`proxy_protocol`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-proxy_protocol) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_cert`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_cert) | a valid filesystem path | No |
| [`ssl_enable`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_enable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_extra_chain_certs`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_extra_chain_certs) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_key`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verify`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-ssl_verify) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-common-options) for a list of options supported by all input plugins.

 

### `host` [v5.0.3-plugins-inputs-tcp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.


### `mode` [v5.0.3-plugins-inputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.


### `port` [v5.0.3-plugins-inputs-tcp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.


### `proxy_protocol` [v5.0.3-plugins-inputs-tcp-proxy_protocol]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time [http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt)


### `ssl_cert` [v5.0.3-plugins-inputs-tcp-ssl_cert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate path


### `ssl_enable` [v5.0.3-plugins-inputs-tcp-ssl_enable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).


### `ssl_extra_chain_certs` [v5.0.3-plugins-inputs-tcp-ssl_extra_chain_certs]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

An Array of extra X509 certificates to be added to the certificate chain. Useful when the CA chain is not necessary in the system store.


### `ssl_key` [v5.0.3-plugins-inputs-tcp-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key path


### `ssl_key_passphrase` [v5.0.3-plugins-inputs-tcp-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

SSL key passphrase


### `ssl_verify` [v5.0.3-plugins-inputs-tcp-ssl_verify]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.



## Common options [v5.0.3-plugins-inputs-tcp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v5-0-3-plugins-inputs-tcp.md#v5.0.3-plugins-inputs-tcp-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v5.0.3-plugins-inputs-tcp-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v5.0.3-plugins-inputs-tcp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v5.0.3-plugins-inputs-tcp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v5.0.3-plugins-inputs-tcp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 tcp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  tcp {
    id => "my_plugin_id"
  }
}
```


### `tags` [v5.0.3-plugins-inputs-tcp-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v5.0.3-plugins-inputs-tcp-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



