---
navigation_title: "v7.3.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v7.3.3-plugins-inputs-rabbitmq.html
---

# Rabbitmq input plugin v7.3.3 [v7.3.3-plugins-inputs-rabbitmq]


* A component of the [rabbitmq integration plugin](integration-rabbitmq-index.md)
* Integration version: v7.3.3
* Released on: 2023-06-09
* [Changelog](https://github.com/logstash-plugins/logstash-integration-rabbitmq/blob/v7.3.3/CHANGELOG.md)

For other versions, see the [overview list](input-rabbitmq-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_737]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-rabbitmq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_730]

Pull events from a [RabbitMQ](http://www.rabbitmq.com/) queue.

The default settings will create an entirely transient queue and listen for all messages by default. If you need durability or any other advanced settings, please set the appropriate options

This plugin uses the [March Hare](http://rubymarchhare.info/) library for interacting with the RabbitMQ server. Most configuration options map directly to standard RabbitMQ and AMQP concepts. The [AMQP 0-9-1 reference guide](https://www.rabbitmq.com/amqp-0-9-1-reference.md) and other parts of the RabbitMQ documentation are useful for deeper understanding.

The properties of messages received will be stored in the `[@metadata][rabbitmq_properties]` field if the `@metadata_enabled` setting is enabled. Note that storing metadata may degrade performance. The following properties may be available (in most cases dependent on whether they were set by the sender):

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

Additionally, any message headers will be saved in the `[@metadata][rabbitmq_headers]` field.


## Rabbitmq Input Configuration Options [v7.3.3-plugins-inputs-rabbitmq-options]

This plugin supports the following configuration options plus the [Common options](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`ack`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-ack) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`arguments`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-arguments) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`auto_delete`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-auto_delete) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`automatic_recovery`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-automatic_recovery) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`connect_retry_interval`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-connect_retry_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`connection_timeout`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-connection_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`durable`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-durable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`exchange`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-exchange) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exchange_type`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-exchange_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exclusive`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-exclusive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`heartbeat`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-heartbeat) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`key`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_enabled`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-metadata_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`passive`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-passive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`password`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`prefetch_count`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-prefetch_count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`queue`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-queue) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate_password`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-ssl_certificate_password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_certificate_path`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-ssl_certificate_path) | a valid filesystem path | No |
| [`ssl_version`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-ssl_version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`subscription_retry_interval_seconds`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-subscription_retry_interval_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`threads`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`user`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`vhost`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-vhost) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-common-options) for a list of options supported by all input plugins.

 

### `ack` [v7.3.3-plugins-inputs-rabbitmq-ack]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Enable message acknowledgements. With acknowledgements messages fetched by Logstash but not yet sent into the Logstash pipeline will be requeued by the server if Logstash shuts down. Acknowledgements will however hurt the message throughput.

This will only send an ack back every `prefetch_count` messages. Working in batches provides a performance boost here.


### `arguments` [v7.3.3-plugins-inputs-rabbitmq-arguments]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `{}`

Optional queue arguments as an array.

Relevant RabbitMQ doc guides:

* [Optional queue arguments](https://www.rabbitmq.com/queues.md#optional-arguments)
* [Policies](https://www.rabbitmq.com/parameters.md#policies)
* [Quorum Queues](https://www.rabbitmq.com/quorum-queues.md)


### `auto_delete` [v7.3.3-plugins-inputs-rabbitmq-auto_delete]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Should the queue be deleted on the broker when the last consumer disconnects? Set this option to `false` if you want the queue to remain on the broker, queueing up messages until a consumer comes along to consume them.


### `automatic_recovery` [v7.3.3-plugins-inputs-rabbitmq-automatic_recovery]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Set this to [automatically recover](https://www.rabbitmq.com/connections.md#automatic-recovery) from a broken connection. You almost certainly don’t want to override this!


### `connect_retry_interval` [v7.3.3-plugins-inputs-rabbitmq-connect_retry_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Time in seconds to wait before retrying a connection


### `connection_timeout` [v7.3.3-plugins-inputs-rabbitmq-connection_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The default connection timeout in milliseconds. If not specified the timeout is infinite.


### `durable` [v7.3.3-plugins-inputs-rabbitmq-durable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Is this queue durable? (aka; Should it survive a broker restart?) If consuming directly from a queue you must set this value to match the existing queue setting, otherwise the connection will fail due to an inequivalent arg error.


### `exchange` [v7.3.3-plugins-inputs-rabbitmq-exchange]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the exchange to bind the queue to. Specify `exchange_type` as well to declare the exchange if it does not exist


### `exchange_type` [v7.3.3-plugins-inputs-rabbitmq-exchange_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The type of the exchange to bind to. Specifying this will cause this plugin to declare the exchange if it does not exist.


### `exclusive` [v7.3.3-plugins-inputs-rabbitmq-exclusive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Is the queue exclusive? Exclusive queues can only be used by the connection that declared them and will be deleted when it is closed (e.g. due to a Logstash restart).


### `heartbeat` [v7.3.3-plugins-inputs-rabbitmq-heartbeat]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

[Heartbeat timeout](https://www.rabbitmq.com/heartbeats.md) in seconds. If unspecified then heartbeat timeout of 60 seconds will be used.


### `host` [v7.3.3-plugins-inputs-rabbitmq-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Common functionality for the rabbitmq input/output RabbitMQ server address(es) host can either be a single host, or a list of hosts i.e. host ⇒ "localhost" or host ⇒ ["host01", "host02]

if multiple hosts are provided on the initial connection and any subsequent recovery attempts of the hosts is chosen at random and connected to. Note that only one host connection is active at a time.


### `key` [v7.3.3-plugins-inputs-rabbitmq-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The routing key to use when binding a queue to the exchange. This is only relevant for direct or topic exchanges.

* Routing keys are ignored on fanout exchanges.
* Wildcards are not valid on direct exchanges.


### `metadata_enabled` [v7.3.3-plugins-inputs-rabbitmq-metadata_enabled]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Accepted values are:

    * `none`: no metadata is added
    * `basic`: headers and properties are added
    * `extended`: headers, properties, and raw payload are added
    * `false`: deprecated alias for `none`
    * `true`: deprecated alias for `basic`

* Default value is `none`

Enable metadata about the RabbitMQ topic to be added to the event’s `@metadata` field, for availablity during pipeline processing. In general, most output plugins and codecs do not include `@metadata` fields. This may impact memory usage and performance.


### Metadata mapping [v7.3.3-plugins-inputs-rabbitmq-metadata_locations]

| category | location | type |
| --- | --- | --- |
| headers | `[@metadata][rabbitmq_headers]` | key/value map |
| properties | `[@metadata][rabbitmq_properties]` | key/value map |
| raw payload | `[@metadata][rabbitmq_payload]` | byte sequence |


### `passive` [v7.3.3-plugins-inputs-rabbitmq-passive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If true the queue will be passively declared, meaning it must already exist on the server. To have Logstash create the queue if necessary leave this option as false. If actively declaring a queue that already exists, the queue options for this plugin (durable etc) must match those of the existing queue.


### `password` [v7.3.3-plugins-inputs-rabbitmq-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `"guest"`

RabbitMQ password


### `port` [v7.3.3-plugins-inputs-rabbitmq-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5672`

RabbitMQ port to connect on


### `prefetch_count` [v7.3.3-plugins-inputs-rabbitmq-prefetch_count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `256`

Prefetch count. If acknowledgements are enabled with the `ack` option, specifies the number of outstanding unacknowledged messages allowed.


### `queue` [v7.3.3-plugins-inputs-rabbitmq-queue]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

The properties to extract from each message and store in a @metadata field.

Technically the exchange, redeliver, and routing-key properties belong to the envelope and not the message but we ignore that distinction here. However, we extract the headers separately via get_headers even though the header table technically is a message property.

Freezing all strings so that code modifying the event’s @metadata field can’t touch them.

If updating this list, remember to update the documentation above too. The default codec for this plugin is JSON. You can override this to suit your particular needs however. The name of the queue Logstash will consume events from. If left empty, a transient queue with an randomly chosen name will be created.


### `ssl` [v7.3.3-plugins-inputs-rabbitmq-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Enable or disable SSL. Note that by default remote certificate verification is off. Specify ssl_certificate_path and ssl_certificate_password if you need certificate verification


### `ssl_certificate_password` [v7.3.3-plugins-inputs-rabbitmq-ssl_certificate_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password for the encrypted PKCS12 (.p12) certificate file specified in ssl_certificate_path


### `ssl_certificate_path` [v7.3.3-plugins-inputs-rabbitmq-ssl_certificate_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to an SSL certificate in PKCS12 (.p12) format used for verifying the remote host


### `ssl_version` [v7.3.3-plugins-inputs-rabbitmq-ssl_version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"TLSv1.2"`

Version of the SSL protocol to use.


### `subscription_retry_interval_seconds` [v7.3.3-plugins-inputs-rabbitmq-subscription_retry_interval_seconds]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Amount of time in seconds to wait after a failed subscription request before retrying. Subscribes can fail if the server goes away and then comes back.


### `threads` [v7.3.3-plugins-inputs-rabbitmq-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`


### `user` [v7.3.3-plugins-inputs-rabbitmq-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"guest"`

RabbitMQ username


### `vhost` [v7.3.3-plugins-inputs-rabbitmq-vhost]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/"`

The vhost (virtual host) to use. If you don’t know what this is, leave the default. With the exception of the default vhost ("/"), names of vhosts should not begin with a forward slash.



## Common options [v7.3.3-plugins-inputs-rabbitmq-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v7-3-3-plugins-inputs-rabbitmq.md#v7.3.3-plugins-inputs-rabbitmq-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v7.3.3-plugins-inputs-rabbitmq-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v7.3.3-plugins-inputs-rabbitmq-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v7.3.3-plugins-inputs-rabbitmq-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v7.3.3-plugins-inputs-rabbitmq-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 rabbitmq inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  rabbitmq {
    id => "my_plugin_id"
  }
}
```


### `tags` [v7.3.3-plugins-inputs-rabbitmq-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v7.3.3-plugins-inputs-rabbitmq-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



