---
navigation_title: "v6.2.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.2.3-plugins-inputs-tcp.html
---

# Tcp input plugin v6.2.3 [v6.2.3-plugins-inputs-tcp]


* Plugin version: v6.2.3
* Released on: 2021-12-10
* [Changelog](https://github.com/logstash-plugins/logstash-input-tcp/blob/v6.2.3/CHANGELOG.md)

For other versions, see the [overview list](input-tcp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_926]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-tcp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_919]

Read events over a TCP socket.

Like stdin and file inputs, each event is assumed to be one line of text.

Can either accept connections from clients or connect to a server, depending on `mode`.

### Accepting log4j2 logs [_accepting_log4j2_logs_17]

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


## Event Metadata and the Elastic Common Schema (ECS) [v6.2.3-plugins-inputs-tcp-ecs_metadata]

In addition to decoding the events, this input will add metadata about the TCP connection itself to each event. This can be helpful when applications are configured to send events directly to this input’s TCP listener without including information about themselves.

Historically, this metadata was added to a variety of non-standard top-level fields, which had the potential to create confusion and schema conflicts downstream. With ECS compatibility mode, we can ensure a pipeline still has access to this metadata throughout the event’s lifecycle without polluting the top-level namespace.

| Metadata Group | ecs: `v1`, `v8` | ecs: `disabled` |
| --- | --- | --- |
| Source Metadata from the TCP connectionon which events are being received, includingthe sender’s name, ip, and outbound port. | [@metadata][input][tcp][source][name] | [host] |
| [@metadata][input][tcp][source][ip] | [@metadata][ip_address] |
| [@metadata][input][tcp][source][port] | [port] |
| Proxy Metadata from a proxied TCP connection.Available when receiving events by proxy and`proxy_protocol => true` | [@metadata][input][tcp][proxy][ip] | [proxy_host] |
| [@metadata][input][tcp][proxy][port] | [proxy_port] |
| SSL Subject Metadata from a secured TCPconnection. Available when `ssl_enable => true`AND `ssl_verify => true` | [@metadata][input][tcp][ssl][subject] | [sslsubject] |

For example, the Elastic Common Schema reserves the [top-level `host` field\]\(([^:]+)://reference/ecs-host.md) for information about the host on which the event happened. If an event is missing this metadata, it can be copied into place from the source TCP connection metadata that has been added to the event:

```txt
filter {
  if [@metadata][input][tcp][source] and not [host] {
    mutate {
      copy {
        "[@metadata][input][tcp][source][name]" => "[host][name]"
        "[@metadata][input][tcp][source][ip]"   => "[host][ip]"
      }
    }
  }
}
```


## Tcp Input Configuration Options [v6.2.3-plugins-inputs-tcp-options]

This plugin supports the following configuration options plus the [Common options](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`dns_reverse_lookup_enabled`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-dns_reverse_lookup_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ecs_compatibility`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`mode`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["server", "client"]` | No |
| [`port`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`proxy_protocol`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-proxy_protocol) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_cert`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_cert) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_certificate_authorities) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_enable`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_enable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_extra_chain_certs`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_extra_chain_certs) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_key`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verify`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ssl_verify) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`tcp_keep_alive`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-tcp_keep_alive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-common-options) for a list of options supported by all input plugins.

 

### `dns_reverse_lookup_enabled` [v6.2.3-plugins-inputs-tcp-dns_reverse_lookup_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

It is possible to avoid DNS reverse-lookups by disabling this setting. If disabled, the address metadata that is added to events will contain the source address as-specified at the TCP layer and IPs will not be resolved to hostnames.


### `ecs_compatibility` [v6.2.3-plugins-inputs-tcp-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: unstructured connection metadata added at root level
    * `v1`,`v8`: structured connection metadata added under `[@metadata][input][tcp]`

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`.


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). The value of this setting affects the [placement of a TCP connection’s metadata](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-ecs_metadata) on events.


### `host` [v6.2.3-plugins-inputs-tcp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.


### `mode` [v6.2.3-plugins-inputs-tcp-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.


### `port` [v6.2.3-plugins-inputs-tcp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.


### `proxy_protocol` [v6.2.3-plugins-inputs-tcp-proxy_protocol]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time [http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt)


### `ssl_cert` [v6.2.3-plugins-inputs-tcp-ssl_cert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to certificate in PEM format. This certificate will be presented to the connecting clients.


### `ssl_certificate_authorities` [v6.2.3-plugins-inputs-tcp-ssl_certificate_authorities]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Validate client certificate or certificate chain against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store.


### `ssl_enable` [v6.2.3-plugins-inputs-tcp-ssl_enable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).


### `ssl_extra_chain_certs` [v6.2.3-plugins-inputs-tcp-ssl_extra_chain_certs]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

An Array of paths to extra X509 certificates. These are used together with the certificate to construct the certificate chain presented to the client.


### `ssl_key` [v6.2.3-plugins-inputs-tcp-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The path to the private key corresponding to the specified certificate (PEM format).


### `ssl_key_passphrase` [v6.2.3-plugins-inputs-tcp-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

SSL key passphrase for the private key.


### `ssl_verify` [v6.2.3-plugins-inputs-tcp-ssl_verify]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.


### `tcp_keep_alive` [v6.2.3-plugins-inputs-tcp-tcp_keep_alive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Instruct the socket to use TCP keep alive. If it’s `true` then the underlying socket will use the OS defaults settings for keep alive. If it’s `false` it doesn’t configure any keep alive setting for the underlying socket.



## Common options [v6.2.3-plugins-inputs-tcp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v6-2-3-plugins-inputs-tcp.md#v6.2.3-plugins-inputs-tcp-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v6.2.3-plugins-inputs-tcp-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v6.2.3-plugins-inputs-tcp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"line"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v6.2.3-plugins-inputs-tcp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v6.2.3-plugins-inputs-tcp-id]

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


### `tags` [v6.2.3-plugins-inputs-tcp-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v6.2.3-plugins-inputs-tcp-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



