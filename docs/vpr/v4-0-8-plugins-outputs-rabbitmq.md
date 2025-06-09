---
navigation_title: "v4.0.8"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.8-plugins-outputs-rabbitmq.html
---

# Rabbitmq output plugin v4.0.8 [v4.0.8-plugins-outputs-rabbitmq]

* Plugin version: v4.0.8
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-rabbitmq/blob/v4.0.8/CHANGELOG.md)

For other versions, see the [overview list](output-rabbitmq-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1511]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-rabbitmq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1501]

Push events to a RabbitMQ exchange. Requires RabbitMQ 2.x or later version (3.x is recommended).

Relevant links:

* [RabbitMQ](http://www.rabbitmq.com/)
* [March Hare](http://rubymarchhare.info)

## Rabbitmq Output Configuration Options [v4.0.8-plugins-outputs-rabbitmq-options]

This plugin supports the following configuration options plus the [Common options](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`arguments`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-arguments) | [array](/lsr/value-types.md#array) | No |
| [`automatic_recovery`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-automatic_recovery) | [boolean](/lsr/value-types.md#boolean) | No |
| [`connect_retry_interval`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-connect_retry_interval) | [number](/lsr/value-types.md#number) | No |
| [`connection_timeout`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-connection_timeout) | [number](/lsr/value-types.md#number) | No |
| [`durable`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-durable) | [boolean](/lsr/value-types.md#boolean) | No |
| [`exchange`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-exchange) | [string](/lsr/value-types.md#string) | Yes |
| [`exchange_type`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-exchange_type) | [string](/lsr/value-types.md#string), one of `["fanout", "direct", "topic", "x-consistent-hash", "x-modulus-hash"]` | Yes |
| [`heartbeat`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-heartbeat) | [number](/lsr/value-types.md#number) | No |
| [`host`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-host) | [string](/lsr/value-types.md#string) | Yes |
| [`key`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-key) | [string](/lsr/value-types.md#string) | No |
| [`passive`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-passive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`password`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-password) | [password](/lsr/value-types.md#password) | No |
| [`persistent`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-persistent) | [boolean](/lsr/value-types.md#boolean) | No |
| [`port`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-port) | [number](/lsr/value-types.md#number) | No |
| [`ssl`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_certificate_password`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-ssl_certificate_password) | [string](/lsr/value-types.md#string) | No |
| [`ssl_certificate_path`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-ssl_certificate_path) | a valid filesystem path | No |
| [`ssl_version`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-ssl_version) | [string](/lsr/value-types.md#string) | No |
| [`user`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-user) | [string](/lsr/value-types.md#string) | No |
| [`vhost`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-vhost) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-common-options) for a list of options supported by all output plugins.

### `arguments` [v4.0.8-plugins-outputs-rabbitmq-arguments]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `{}`

Extra queue arguments as an array. To make a RabbitMQ queue mirrored, use: `{"x-ha-policy" => "all"}`

### `automatic_recovery` [v4.0.8-plugins-outputs-rabbitmq-automatic_recovery]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Set this to automatically recover from a broken connection. You almost certainly don’t want to override this!!!

### `connect_retry_interval` [v4.0.8-plugins-outputs-rabbitmq-connect_retry_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

Time in seconds to wait before retrying a connection

### `connection_timeout` [v4.0.8-plugins-outputs-rabbitmq-connection_timeout]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

The default connection timeout in milliseconds. If not specified the timeout is infinite.

### `debug` (DEPRECATED) [v4.0.8-plugins-outputs-rabbitmq-debug]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable or disable logging

### `durable` [v4.0.8-plugins-outputs-rabbitmq-durable]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Is this exchange durable? (aka; Should it survive a broker restart?)

### `exchange` [v4.0.8-plugins-outputs-rabbitmq-exchange]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the exchange

### `exchange_type` [v4.0.8-plugins-outputs-rabbitmq-exchange_type]

* This is a required setting.
* Value can be any of: `fanout`, `direct`, `topic`, `x-consistent-hash`, `x-modulus-hash`
* There is no default value for this setting.

The exchange type (fanout, topic, direct)

### `heartbeat` [v4.0.8-plugins-outputs-rabbitmq-heartbeat]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

Heartbeat delay in seconds. If unspecified no heartbeats will be sent

### `host` [v4.0.8-plugins-outputs-rabbitmq-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Common functionality for the rabbitmq input/output RabbitMQ server address(es) host can either be a single host, or a list of hosts i.e. host ⇒ "localhost" or host ⇒ \["host01", "host02]

if multiple hosts are provided on the initial connection and any subsequent recovery attempts of the hosts is chosen at random and connected to. Note that only one host connection is active at a time.

### `key` [v4.0.8-plugins-outputs-rabbitmq-key]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

The default codec for this plugin is JSON. You can override this to suit your particular needs however. Key to route to by default. Defaults to *logstash*

* Routing keys are ignored on fanout exchanges.

### `passive` [v4.0.8-plugins-outputs-rabbitmq-passive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Passive queue creation? Useful for checking queue existance without modifying server state

### `password` [v4.0.8-plugins-outputs-rabbitmq-password]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `"guest"`

RabbitMQ password

### `persistent` [v4.0.8-plugins-outputs-rabbitmq-persistent]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Should RabbitMQ persist messages to disk?

### `port` [v4.0.8-plugins-outputs-rabbitmq-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5672`

RabbitMQ port to connect on

### `ssl` [v4.0.8-plugins-outputs-rabbitmq-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* There is no default value for this setting.

Enable or disable SSL. Note that by default remote certificate verification is off. Specify ssl\_certificate\_path and ssl\_certificate\_password if you need certificate verification

### `ssl_certificate_password` [v4.0.8-plugins-outputs-rabbitmq-ssl_certificate_password]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Password for the encrypted PKCS12 (.p12) certificate file specified in ssl\_certificate\_path

### `ssl_certificate_path` [v4.0.8-plugins-outputs-rabbitmq-ssl_certificate_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Path to an SSL certificate in PKCS12 (.p12) format used for verifying the remote host

### `ssl_version` [v4.0.8-plugins-outputs-rabbitmq-ssl_version]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"TLSv1.2"`

Version of the SSL protocol to use.

### `tls_certificate_password` (DEPRECATED) [v4.0.8-plugins-outputs-rabbitmq-tls_certificate_password]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

TLS certificate password

### `tls_certificate_path` (DEPRECATED) [v4.0.8-plugins-outputs-rabbitmq-tls_certificate_path]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

TLS certifcate path

### `user` [v4.0.8-plugins-outputs-rabbitmq-user]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"guest"`

RabbitMQ username

### `vhost` [v4.0.8-plugins-outputs-rabbitmq-vhost]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"/"`

The vhost (virtual host) to use. If you don’t know what this is, leave the default. With the exception of the default vhost ("/"), names of vhosts should not begin with a forward slash.

## Common options [v4.0.8-plugins-outputs-rabbitmq-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-8-plugins-outputs-rabbitmq.md#v4.0.8-plugins-outputs-rabbitmq-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v4.0.8-plugins-outputs-rabbitmq-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.8-plugins-outputs-rabbitmq-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.8-plugins-outputs-rabbitmq-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 rabbitmq outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  rabbitmq {
    id => "my_plugin_id"
  }
}
```
