---
navigation_title: "v3.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.1-plugins-outputs-zeromq.html
---

# Zeromq output plugin v3.1.1 [v3.1.1-plugins-outputs-zeromq]

* Plugin version: v3.1.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-zeromq/blob/v3.1.1/CHANGELOG.md)

For other versions, see the [overview list](output-zeromq-index.md "Versioned zeromq output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1691]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-zeromq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1681]

Write events to a 0MQ PUB socket.

You need to have the 0mq 2.1.x library installed to be able to use this output plugin.

The default settings will create a publisher connecting to a subscriber bound to tcp\://127.0.0.1:2120

### Zeromq Output Configuration Options [v3.1.1-plugins-outputs-zeromq-options]

This plugin supports the following configuration options plus the [Common options](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`address`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-address "address") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`mode`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-mode "mode") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["server", "client"]` | No |
| [`sockopt`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-sockopt "sockopt") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`topic`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-topic "topic") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`topology`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-topology "topology") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["pushpull", "pubsub", "pair"]` | Yes |

Also see [Common options](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-common-options "Common options") for a list of options supported by all output plugins.

 

#### `address` [v3.1.1-plugins-outputs-zeromq-address]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `["tcp://127.0.0.1:2120"]`

This will be a performance bottleneck. Someone needs to upgrade this to concurrency :shared and make sure there is no breakage 0mq socket address to connect or bind. Please note that `inproc://` will not work with logstashi. For each we use a context per thread. By default, inputs bind/listen and outputs connect.

#### `mode` [v3.1.1-plugins-outputs-zeromq-mode]

* Value can be any of: `server`, `client`
* Default value is `"client"`

Server mode binds/listens. Client mode connects.

#### `sockopt` [v3.1.1-plugins-outputs-zeromq-sockopt]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* There is no default value for this setting.

This exposes zmq\_setsockopt for advanced tuning. See <http://api.zeromq.org/2-1:zmq-setsockopt> for details.

This is where you would set values like:

* ZMQ::HWM - high water mark
* ZMQ::IDENTITY - named queues
* ZMQ::SWAP\_SIZE - space for disk overflow

Example:

```
    sockopt => {
       "ZMQ::HWM" => 50
       "ZMQ::IDENTITY"  => "my_named_queue"
    }
```

#### `topic` [v3.1.1-plugins-outputs-zeromq-topic]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `""`

This is used for the *pubsub* topology only. On inputs, this allows you to filter messages by topic. On outputs, this allows you to tag a message for routing. NOTE: ZeroMQ does subscriber-side filtering NOTE: Topic is evaluated with `event.sprintf` so macros are valid here.

#### `topology` [v3.1.1-plugins-outputs-zeromq-topology]

* This is a required setting.
* Value can be any of: `pushpull`, `pubsub`, `pair`
* There is no default value for this setting.

The default logstash topologies work as follows:

* pushpull - inputs are pull, outputs are push
* pubsub - inputs are subscribers, outputs are publishers
* pair - inputs are clients, outputs are servers

If the predefined topology flows don’t work for you, you can change the *mode* setting

### Common options [v3.1.1-plugins-outputs-zeromq-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v3-1-1-plugins-outputs-zeromq.md#v3.1.1-plugins-outputs-zeromq-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v3.1.1-plugins-outputs-zeromq-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v3.1.1-plugins-outputs-zeromq-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v3.1.1-plugins-outputs-zeromq-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 zeromq outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  zeromq {
    id => "my_plugin_id"
  }
}
```
