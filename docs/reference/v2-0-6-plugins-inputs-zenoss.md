---
navigation_title: "v2.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.6-plugins-inputs-zenoss.html
---

# Zenoss input plugin v2.0.6 [v2.0.6-plugins-inputs-zenoss]


* Plugin version: v2.0.6
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-input-zenoss/blob/v2.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-zenoss-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1014]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-zenoss). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1007]

Read Zenoss events from the zenoss.zenevents fanout exchange.


## Zenoss Input Configuration Options [v2.0.6-plugins-inputs-zenoss-options]

This plugin supports the following configuration options plus the [Common options](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`ack`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-ack) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`arguments`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-arguments) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`auto_delete`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-auto_delete) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`automatic_recovery`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-automatic_recovery) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`connect_retry_interval`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-connect_retry_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`connection_timeout`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-connection_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`durable`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-durable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`exchange`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-exchange) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exchange_type`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-exchange_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exclusive`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-exclusive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`heartbeat`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-heartbeat) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_enabled`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-metadata_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`passive`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-passive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`password`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`prefetch_count`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-prefetch_count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`queue`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-queue) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate_password`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-ssl_certificate_password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_certificate_path`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-ssl_certificate_path) | a valid filesystem path | No |
| [`ssl_version`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-ssl_version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`subscription_retry_interval_seconds`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-subscription_retry_interval_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`threads`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`user`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vhost`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-vhost) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-common-options) for a list of options supported by all input plugins.

 

### `ack` [v2.0.6-plugins-inputs-zenoss-ack]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Enable message acknowledgements. With acknowledgements messages fetched by Logstash but not yet sent into the Logstash pipeline will be requeued by the server if Logstash shuts down. Acknowledgements will however hurt the message throughput.

This will only send an ack back every `prefetch_count` messages. Working in batches provides a performance boost here.


### `arguments` [v2.0.6-plugins-inputs-zenoss-arguments]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `{}`

Extra queue arguments as an array. To make a RabbitMQ queue mirrored, use: `{"x-ha-policy" => "all"}`


### `auto_delete` [v2.0.6-plugins-inputs-zenoss-auto_delete]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Should the queue be deleted on the broker when the last consumer disconnects? Set this option to `false` if you want the queue to remain on the broker, queueing up messages until a consumer comes along to consume them.


### `automatic_recovery` [v2.0.6-plugins-inputs-zenoss-automatic_recovery]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Set this to automatically recover from a broken connection. You almost certainly don’t want to override this!!!


### `connect_retry_interval` [v2.0.6-plugins-inputs-zenoss-connect_retry_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Time in seconds to wait before retrying a connection


### `connection_timeout` [v2.0.6-plugins-inputs-zenoss-connection_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The default connection timeout in milliseconds. If not specified the timeout is infinite.


### `durable` [v2.0.6-plugins-inputs-zenoss-durable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Is this queue durable? (aka; Should it survive a broker restart?)


### `exchange` [v2.0.6-plugins-inputs-zenoss-exchange]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"zenoss.zenevents"`

% Also broken in production
% The name of the exchange to bind the queue. This is analogous to the *rabbitmq output* config *name*

The name of the exchange to bind the queue. This is analogous to the *rabbitmq output* config *name*


### `exchange_type` [v2.0.6-plugins-inputs-zenoss-exchange_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The type of the exchange to bind to. Specifying this will cause this plugin to declare the exchange if it does not exist.


### `exclusive` [v2.0.6-plugins-inputs-zenoss-exclusive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Is the queue exclusive? Exclusive queues can only be used by the connection that declared them and will be deleted when it is closed (e.g. due to a Logstash restart).


### `heartbeat` [v2.0.6-plugins-inputs-zenoss-heartbeat]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Heartbeat delay in seconds. If unspecified no heartbeats will be sent


### `host` [v2.0.6-plugins-inputs-zenoss-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

Your rabbitmq server address


### `key` [v2.0.6-plugins-inputs-zenoss-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"zenoss.zenevent.#"`

The routing key to use. This is only valid for direct or fanout exchanges

* Routing keys are ignored on topic exchanges.
* Wildcards are not valid on direct exchanges.


### `metadata_enabled` [v2.0.6-plugins-inputs-zenoss-metadata_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable the storage of message headers and properties in `@metadata`. This may impact performance


### `passive` [v2.0.6-plugins-inputs-zenoss-passive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Passive queue creation? Useful for checking queue existance without modifying server state


### `password` [v2.0.6-plugins-inputs-zenoss-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `"zenoss"`

Your rabbitmq password


### `port` [v2.0.6-plugins-inputs-zenoss-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5672`

RabbitMQ port to connect on


### `prefetch_count` [v2.0.6-plugins-inputs-zenoss-prefetch_count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `256`

Prefetch count. If acknowledgements are enabled with the `ack` option, specifies the number of outstanding unacknowledged messages allowed.


### `queue` [v2.0.6-plugins-inputs-zenoss-queue]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Pull events from a [RabbitMQ](http://www.rabbitmq.com/) queue.

The default settings will create an entirely transient queue and listen for all messages by default. If you need durability or any other advanced settings, please set the appropriate options

This plugin uses the [March Hare](http://rubymarchhare.info/) library for interacting with the RabbitMQ server. Most configuration options map directly to standard RabbitMQ and AMQP concepts. The [AMQP 0-9-1 reference guide](https://www.rabbitmq.com/amqp-0-9-1-reference.md) and other parts of the RabbitMQ documentation are useful for deeper understanding.

The properties of messages received will be stored in the `[@metadata][rabbitmq_properties]` field if the `@metadata_enabled` setting is checked. Note that storing metadata may degrade performance. The following properties may be available (in most cases dependent on whether they were set by the sender):

* app-id
* cluster-id
* consumer-tag
* content-encoding
* content-type
* correlation-id
* delivery-mode
* exchange
* expiration
* message-id
* priority
* redeliver
* reply-to
* routing-key
* timestamp
* type
* user-id

For example, to get the RabbitMQ message’s timestamp property into the Logstash event’s `@timestamp` field, use the date filter to parse the `[@metadata][rabbitmq_properties][timestamp]` field:

```ruby
    filter {
      if [@metadata][rabbitmq_properties][timestamp] {
        date {
          match => ["[@metadata][rabbitmq_properties][timestamp]", "UNIX"]
        }
      }
    }
```

Additionally, any message headers will be saved in the `[@metadata][rabbitmq_headers]` field. The properties to extract from each message and store in a @metadata field.

Technically the exchange, redeliver, and routing-key properties belong to the envelope and not the message but we ignore that distinction here. However, we extract the headers separately via get_headers even though the header table technically is a message property.

Freezing all strings so that code modifying the event’s @metadata field can’t touch them.

If updating this list, remember to update the documentation above too. The default codec for this plugin is JSON. You can override this to suit your particular needs however. The name of the queue Logstash will consume events from. If left empty, a transient queue with an randomly chosen name will be created.


### `ssl` [v2.0.6-plugins-inputs-zenoss-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Enable or disable SSL. Note that by default remote certificate verification is off. Specify ssl_certificate_path and ssl_certificate_password if you need certificate verification


### `ssl_certificate_password` [v2.0.6-plugins-inputs-zenoss-ssl_certificate_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password for the encrypted PKCS12 (.p12) certificate file specified in ssl_certificate_path


### `ssl_certificate_path` [v2.0.6-plugins-inputs-zenoss-ssl_certificate_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to an SSL certificate in PKCS12 (.p12) format used for verifying the remote host


### `ssl_version` [v2.0.6-plugins-inputs-zenoss-ssl_version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"TLSv1.2"`

Version of the SSL protocol to use.


### `subscription_retry_interval_seconds` [v2.0.6-plugins-inputs-zenoss-subscription_retry_interval_seconds]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Amount of time in seconds to wait after a failed subscription request before retrying. Subscribes can fail if the server goes away and then comes back.


### `threads` [v2.0.6-plugins-inputs-zenoss-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`


### `tls_certificate_password`  (DEPRECATED) [v2.0.6-plugins-inputs-zenoss-tls_certificate_password]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

TLS certificate password


### `tls_certificate_path`  (DEPRECATED) [v2.0.6-plugins-inputs-zenoss-tls_certificate_path]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

TLS certifcate path


### `user` [v2.0.6-plugins-inputs-zenoss-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"zenoss"`

Your rabbitmq username


### `vhost` [v2.0.6-plugins-inputs-zenoss-vhost]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/zenoss"`

The vhost to use. If you don’t know what this is, leave the default.



## Common options [v2.0.6-plugins-inputs-zenoss-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v2-0-6-plugins-inputs-zenoss.md#v2.0.6-plugins-inputs-zenoss-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v2.0.6-plugins-inputs-zenoss-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v2.0.6-plugins-inputs-zenoss-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.6-plugins-inputs-zenoss-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.6-plugins-inputs-zenoss-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 zenoss inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  zenoss {
    id => "my_plugin_id"
  }
}
```


### `tags` [v2.0.6-plugins-inputs-zenoss-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v2.0.6-plugins-inputs-zenoss-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



