---
navigation_title: "v7.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v7.3.0-plugins-outputs-rabbitmq.html
---

# Rabbitmq output plugin v7.3.0 [v7.3.0-plugins-outputs-rabbitmq]


* A component of the [rabbitmq integration plugin](integration-rabbitmq-index.md)
* Integration version: v7.3.0
* Released on: 2021-06-07
* [Changelog](https://github.com/logstash-plugins/logstash-integration-rabbitmq/blob/v7.3.0/CHANGELOG.md)

For other versions, see the [overview list](output-rabbitmq-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1483]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-rabbitmq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1473]

Push events to a RabbitMQ exchange. Requires RabbitMQ 2.x or later version (3.x is recommended).

Relevant links:

* [RabbitMQ](http://www.rabbitmq.com/)
* [March Hare](http://rubymarchhare.info)


## Rabbitmq Output Configuration Options [v7.3.0-plugins-outputs-rabbitmq-options]

This plugin supports the following configuration options plus the [Common options](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`arguments`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-arguments) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`automatic_recovery`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-automatic_recovery) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`connect_retry_interval`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-connect_retry_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`connection_timeout`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-connection_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`durable`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-durable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`exchange`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-exchange) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`exchange_type`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-exchange_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["fanout", "direct", "topic", "x-consistent-hash", "x-modulus-hash"]` | Yes |
| [`heartbeat`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-heartbeat) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`key`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`message_properties`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-message_properties) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`passive`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-passive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`password`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`persistent`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-persistent) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`port`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate_password`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-ssl_certificate_password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_certificate_path`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-ssl_certificate_path) | a valid filesystem path | No |
| [`ssl_version`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-ssl_version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`user`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vhost`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-vhost) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-common-options) for a list of options supported by all output plugins.

 

### `arguments` [v7.3.0-plugins-outputs-rabbitmq-arguments]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `{}`

Extra queue arguments as an array. To make a RabbitMQ queue mirrored, use: `{"x-ha-policy" => "all"}`


### `automatic_recovery` [v7.3.0-plugins-outputs-rabbitmq-automatic_recovery]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Set this to automatically recover from a broken connection. You almost certainly don’t want to override this!!!


### `connect_retry_interval` [v7.3.0-plugins-outputs-rabbitmq-connect_retry_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Time in seconds to wait before retrying a connection


### `connection_timeout` [v7.3.0-plugins-outputs-rabbitmq-connection_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The default connection timeout in milliseconds. If not specified the timeout is infinite.


### `durable` [v7.3.0-plugins-outputs-rabbitmq-durable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Is this exchange durable? (aka; Should it survive a broker restart?)


### `exchange` [v7.3.0-plugins-outputs-rabbitmq-exchange]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the exchange


### `exchange_type` [v7.3.0-plugins-outputs-rabbitmq-exchange_type]

* This is a required setting.
* Value can be any of: `fanout`, `direct`, `topic`, `x-consistent-hash`, `x-modulus-hash`
* There is no default value for this setting.

The exchange type (fanout, topic, direct)


### `heartbeat` [v7.3.0-plugins-outputs-rabbitmq-heartbeat]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Heartbeat delay in seconds. If unspecified no heartbeats will be sent


### `host` [v7.3.0-plugins-outputs-rabbitmq-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Common functionality for the rabbitmq input/output RabbitMQ server address(es) host can either be a single host, or a list of hosts i.e. host ⇒ "localhost" or host ⇒ ["host01", "host02]

if multiple hosts are provided on the initial connection and any subsequent recovery attempts of the hosts is chosen at random and connected to. Note that only one host connection is active at a time.


### `key` [v7.3.0-plugins-outputs-rabbitmq-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The default codec for this plugin is JSON. You can override this to suit your particular needs however. Key to route to by default. Defaults to *logstash*

* Routing keys are ignored on fanout exchanges.


### `message_properties` [v7.3.0-plugins-outputs-rabbitmq-message_properties]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add properties to be set per-message here, such as *content_type*, *priority*. Values can be [`sprintf` templates](logstash://reference/event-dependent-configuration.md#sprintf), whose value for each message will be populated from the event.

Example:

```ruby
    message_properties => {
      "content_type" => "application/json"
      "priority" => 1
    }
```


### `passive` [v7.3.0-plugins-outputs-rabbitmq-passive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Passive queue creation? Useful for checking queue existance without modifying server state


### `password` [v7.3.0-plugins-outputs-rabbitmq-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `"guest"`

RabbitMQ password


### `persistent` [v7.3.0-plugins-outputs-rabbitmq-persistent]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Should RabbitMQ persist messages to disk?


### `port` [v7.3.0-plugins-outputs-rabbitmq-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5672`

RabbitMQ port to connect on


### `ssl` [v7.3.0-plugins-outputs-rabbitmq-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Enable or disable SSL. Note that by default remote certificate verification is off. Specify ssl_certificate_path and ssl_certificate_password if you need certificate verification


### `ssl_certificate_password` [v7.3.0-plugins-outputs-rabbitmq-ssl_certificate_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password for the encrypted PKCS12 (.p12) certificate file specified in ssl_certificate_path


### `ssl_certificate_path` [v7.3.0-plugins-outputs-rabbitmq-ssl_certificate_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to an SSL certificate in PKCS12 (.p12) format used for verifying the remote host


### `ssl_version` [v7.3.0-plugins-outputs-rabbitmq-ssl_version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"TLSv1.2"`

Version of the SSL protocol to use.


### `user` [v7.3.0-plugins-outputs-rabbitmq-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"guest"`

RabbitMQ username


### `vhost` [v7.3.0-plugins-outputs-rabbitmq-vhost]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/"`

The vhost (virtual host) to use. If you don’t know what this is, leave the default. With the exception of the default vhost ("/"), names of vhosts should not begin with a forward slash.



## Common options [v7.3.0-plugins-outputs-rabbitmq-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v7-3-0-plugins-outputs-rabbitmq.md#v7.3.0-plugins-outputs-rabbitmq-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v7.3.0-plugins-outputs-rabbitmq-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v7.3.0-plugins-outputs-rabbitmq-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v7.3.0-plugins-outputs-rabbitmq-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 rabbitmq outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  rabbitmq {
    id => "my_plugin_id"
  }
}
```



