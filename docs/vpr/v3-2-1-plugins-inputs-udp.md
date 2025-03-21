---
navigation_title: "v3.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.1-plugins-inputs-udp.html
---

# Udp input plugin v3.2.1 [v3.2.1-plugins-inputs-udp]


* Plugin version: v3.2.1
* Released on: 2017-12-19
* [Changelog](https://github.com/logstash-plugins/logstash-input-udp/blob/v3.2.1/CHANGELOG.md)

For other versions, see the [overview list](input-udp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_984]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-udp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_977]

Read messages as events over the network via udp. The only required configuration item is `port`, which specifies the udp port logstash will listen on for event streams.


## Udp Input Configuration Options [v3.2.1-plugins-inputs-udp-options]

This plugin supports the following configuration options plus the [Common options](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`buffer_size`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-buffer_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`port`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`queue_size`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-queue_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`receive_buffer_bytes`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-receive_buffer_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`workers`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-workers) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-common-options) for a list of options supported by all input plugins.

 

### `buffer_size` [v3.2.1-plugins-inputs-udp-buffer_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `65536`

The maximum packet size to read from the network


### `host` [v3.2.1-plugins-inputs-udp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

The address which logstash will listen on.


### `port` [v3.2.1-plugins-inputs-udp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The port which logstash will listen on. Remember that ports less than 1024 (privileged ports) may require root or elevated privileges to use.


### `queue_size` [v3.2.1-plugins-inputs-udp-queue_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2000`

This is the number of unprocessed UDP packets you can hold in memory before packets will start dropping.


### `receive_buffer_bytes` [v3.2.1-plugins-inputs-udp-receive_buffer_bytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The socket receive buffer size in bytes. If option is not set, the operating system default is used. The operating system will use the max allowed value if receive_buffer_bytes is larger than allowed. Consult your operating system documentation if you need to increase this max allowed value.


### `workers` [v3.2.1-plugins-inputs-udp-workers]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Number of threads processing packets



## Common options [v3.2.1-plugins-inputs-udp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-2-1-plugins-inputs-udp.md#v3.2.1-plugins-inputs-udp-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.2.1-plugins-inputs-udp-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.2.1-plugins-inputs-udp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.2.1-plugins-inputs-udp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.2.1-plugins-inputs-udp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 udp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  udp {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.2.1-plugins-inputs-udp-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.2.1-plugins-inputs-udp-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



