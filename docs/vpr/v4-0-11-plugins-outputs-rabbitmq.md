---
navigation_title: "v4.0.11"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.11-plugins-outputs-rabbitmq.html
---

# Rabbitmq output plugin v4.0.11 [v4.0.11-plugins-outputs-rabbitmq]

* Plugin version: v4.0.11
* Released on: 2017-08-21
* [Changelog](https://github.com/logstash-plugins/logstash-output-rabbitmq/blob/v4.0.11/CHANGELOG.md)

For other versions, see the [overview list](output-rabbitmq-index.md "Versioned rabbitmq output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1506]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-rabbitmq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1496]

Push events to a RabbitMQ exchange. Requires RabbitMQ 2.x or later version (3.x is recommended).

Relevant links:

* [RabbitMQ](http://www.rabbitmq.com/)
* [March Hare](http://rubymarchhare.info)

### Rabbitmq Output Configuration Options [v4.0.11-plugins-outputs-rabbitmq-options]

This plugin supports the following configuration options plus the [Common options](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`arguments`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-arguments "arguments") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`automatic_recovery`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-automatic_recovery "automatic_recovery") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`connect_retry_interval`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-connect_retry_interval "connect_retry_interval") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`connection_timeout`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-connection_timeout "connection_timeout") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`durable`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-durable "durable") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`exchange`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-exchange "exchange") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`exchange_type`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-exchange_type "exchange_type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["fanout", "direct", "topic", "x-consistent-hash", "x-modulus-hash"]` | Yes |
| [`heartbeat`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-heartbeat "heartbeat") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`host`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-host "host") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`key`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-key "key") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`message_properties`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-message_properties "message_properties") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`passive`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-passive "passive") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`password`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-password "password") | [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password) | No |
| [`persistent`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-persistent "persistent") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`port`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-port "port") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`ssl`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-ssl "ssl") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`ssl_certificate_password`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-ssl_certificate_password "ssl_certificate_password") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`ssl_certificate_path`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-ssl_certificate_path "ssl_certificate_path") | a valid filesystem path | No |
| [`ssl_version`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-ssl_version "ssl_version") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`user`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-user "user") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`vhost`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-vhost "vhost") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

Also see [Common options](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-common-options "Common options") for a list of options supported by all output plugins.

 

#### `arguments` [v4.0.11-plugins-outputs-rabbitmq-arguments]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `{}`

Extra queue arguments as an array. To make a RabbitMQ queue mirrored, use: `{"x-ha-policy" => "all"}`

#### `automatic_recovery` [v4.0.11-plugins-outputs-rabbitmq-automatic_recovery]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Set this to automatically recover from a broken connection. You almost certainly don’t want to override this!!!

#### `connect_retry_interval` [v4.0.11-plugins-outputs-rabbitmq-connect_retry_interval]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `1`

Time in seconds to wait before retrying a connection

#### `connection_timeout` [v4.0.11-plugins-outputs-rabbitmq-connection_timeout]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

The default connection timeout in milliseconds. If not specified the timeout is infinite.

#### `debug` (DEPRECATED) [v4.0.11-plugins-outputs-rabbitmq-debug]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

Enable or disable logging

#### `durable` [v4.0.11-plugins-outputs-rabbitmq-durable]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Is this exchange durable? (aka; Should it survive a broker restart?)

#### `exchange` [v4.0.11-plugins-outputs-rabbitmq-exchange]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

The name of the exchange

#### `exchange_type` [v4.0.11-plugins-outputs-rabbitmq-exchange_type]

* This is a required setting.
* Value can be any of: `fanout`, `direct`, `topic`, `x-consistent-hash`, `x-modulus-hash`
* There is no default value for this setting.

The exchange type (fanout, topic, direct)

#### `heartbeat` [v4.0.11-plugins-outputs-rabbitmq-heartbeat]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

Heartbeat delay in seconds. If unspecified no heartbeats will be sent

#### `host` [v4.0.11-plugins-outputs-rabbitmq-host]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Common functionality for the rabbitmq input/output RabbitMQ server address(es) host can either be a single host, or a list of hosts i.e. host ⇒ "localhost" or host ⇒ \["host01", "host02]

if multiple hosts are provided on the initial connection and any subsequent recovery attempts of the hosts is chosen at random and connected to. Note that only one host connection is active at a time.

#### `key` [v4.0.11-plugins-outputs-rabbitmq-key]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"logstash"`

The default codec for this plugin is JSON. You can override this to suit your particular needs however. Key to route to by default. Defaults to *logstash*

* Routing keys are ignored on fanout exchanges.

#### `message_properties` [v4.0.11-plugins-outputs-rabbitmq-message_properties]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* Default value is `{}`

Add properties to be set per-message here, such as *Content-Type*, *Priority*

Example:

```
    message_properties => { "priority" => "1" }
```

#### `passive` [v4.0.11-plugins-outputs-rabbitmq-passive]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

Passive queue creation? Useful for checking queue existance without modifying server state

#### `password` [v4.0.11-plugins-outputs-rabbitmq-password]

* Value type is [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password)
* Default value is `"guest"`

RabbitMQ password

#### `persistent` [v4.0.11-plugins-outputs-rabbitmq-persistent]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Should RabbitMQ persist messages to disk?

#### `port` [v4.0.11-plugins-outputs-rabbitmq-port]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `5672`

RabbitMQ port to connect on

#### `ssl` [v4.0.11-plugins-outputs-rabbitmq-ssl]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* There is no default value for this setting.

Enable or disable SSL. Note that by default remote certificate verification is off. Specify ssl\_certificate\_path and ssl\_certificate\_password if you need certificate verification

#### `ssl_certificate_password` [v4.0.11-plugins-outputs-rabbitmq-ssl_certificate_password]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Password for the encrypted PKCS12 (.p12) certificate file specified in ssl\_certificate\_path

#### `ssl_certificate_path` [v4.0.11-plugins-outputs-rabbitmq-ssl_certificate_path]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

Path to an SSL certificate in PKCS12 (.p12) format used for verifying the remote host

#### `ssl_version` [v4.0.11-plugins-outputs-rabbitmq-ssl_version]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"TLSv1.2"`

Version of the SSL protocol to use.

#### `tls_certificate_password` (DEPRECATED) [v4.0.11-plugins-outputs-rabbitmq-tls_certificate_password]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

TLS certificate password

#### `tls_certificate_path` (DEPRECATED) [v4.0.11-plugins-outputs-rabbitmq-tls_certificate_path]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

TLS certifcate path

#### `user` [v4.0.11-plugins-outputs-rabbitmq-user]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"guest"`

RabbitMQ username

#### `vhost` [v4.0.11-plugins-outputs-rabbitmq-vhost]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"/"`

The vhost (virtual host) to use. If you don’t know what this is, leave the default. With the exception of the default vhost ("/"), names of vhosts should not begin with a forward slash.

### Common options [v4.0.11-plugins-outputs-rabbitmq-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v4-0-11-plugins-outputs-rabbitmq.md#v4.0.11-plugins-outputs-rabbitmq-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v4.0.11-plugins-outputs-rabbitmq-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v4.0.11-plugins-outputs-rabbitmq-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v4.0.11-plugins-outputs-rabbitmq-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 rabbitmq outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  rabbitmq {
    id => "my_plugin_id"
  }
}
```
