---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-inputs-zeromq.html
---

# Zeromq input plugin v3.0.5 [v3.0.5-plugins-inputs-zeromq]

* Plugin version: v3.0.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-zeromq/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-zeromq-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1051]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-zeromq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1044]

Read events over a 0MQ SUB socket.

You need to have the 0mq 2.1.x library installed to be able to use this input plugin.

The default settings will create a subscriber binding to `tcp://127.0.0.1:2120` waiting for connecting publishers.

## Zeromq Input Configuration Options [v3.0.5-plugins-inputs-zeromq-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`address`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-address) | [array](/lsr/value-types.md#array) | No |
| [`mode`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`sender`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-sender) | [string](/lsr/value-types.md#string) | No |
| [`sockopt`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-sockopt) | [hash](/lsr/value-types.md#hash) | No |
| [`topic`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-topic) | [array](/lsr/value-types.md#array) | No |
| [`topic_field`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-topic_field) | [string](/lsr/value-types.md#string) | No |
| [`topology`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-topology) | [string](/lsr/value-types.md#string), one of `["pushpull", "pubsub", "pair"]` | Yes |

Also see [Common options](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-common-options) for a list of options supported by all input plugins.

### `address` [v3.0.5-plugins-inputs-zeromq-address]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["tcp://*:2120"]`

0mq socket address to connect or bind Please note that `inproc://` will not work with logstash as each we use a context per thread. By default, inputs bind/listen and outputs connect

### `mode` [v3.0.5-plugins-inputs-zeromq-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

mode server mode binds/listens client mode connects

### `sender` [v3.0.5-plugins-inputs-zeromq-sender]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

sender overrides the sender to set the source of the event default is `zmq+topology://type/`

### `sockopt` [v3.0.5-plugins-inputs-zeromq-sockopt]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"ZMQ::RCVTIMEO"=>"1000"}`

0mq socket options This exposes `zmq_setsockopt` for advanced tuning see <http://api.zeromq.org/2-1:zmq-setsockopt> for details

This is where you would set values like:

* `ZMQ::HWM` - high water mark
* `ZMQ::IDENTITY` - named queues
* `ZMQ::SWAP_SIZE` - space for disk overflow

Example:

```
    sockopt => {
       "ZMQ::HWM" => 50
       "ZMQ::IDENTITY"  => "my_named_queue"
    }
```

defaults to: `sockopt => { "ZMQ::RCVTIMEO" => "1000" }`, which has the effect of "interrupting" the recv operation at least once every second to allow for properly shutdown handling.

### `topic` [v3.0.5-plugins-inputs-zeromq-topic]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

0mq topic This is used for the `pubsub` topology only On inputs, this allows you to filter messages by topic On outputs, this allows you to tag a message for routing NOTE: ZeroMQ does subscriber side filtering. NOTE: All topics have an implicit wildcard at the end You can specify multiple topics here

### `topic_field` [v3.0.5-plugins-inputs-zeromq-topic_field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"topic"`

Event topic field This is used for the `pubsub` topology only When a message is received on a topic, the topic name on which the message was received will saved in this field.

### `topology` [v3.0.5-plugins-inputs-zeromq-topology]

* This is a required setting.
* Value can be any of: `pushpull`, `pubsub`, `pair`
* There is no default value for this setting.

0mq topology The default logstash topologies work as follows:

* pushpull - inputs are pull, outputs are push
* pubsub - inputs are subscribers, outputs are publishers
* pair - inputs are clients, inputs are servers

If the predefined topology flows don’t work for you, you can change the `mode` setting

## Common options [v3.0.5-plugins-inputs-zeromq-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-5-plugins-inputs-zeromq.md#v3.0.5-plugins-inputs-zeromq-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.5-plugins-inputs-zeromq-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.5-plugins-inputs-zeromq-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.5-plugins-inputs-zeromq-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.5-plugins-inputs-zeromq-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 zeromq inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  zeromq {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.5-plugins-inputs-zeromq-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.5-plugins-inputs-zeromq-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
