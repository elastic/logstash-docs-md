---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-inputs-heartbeat.html
---

# Heartbeat input plugin v3.0.7 [v3.0.7-plugins-inputs-heartbeat]


* Plugin version: v3.0.7
* Released on: 2018-09-13
* [Changelog](https://github.com/logstash-plugins/logstash-input-heartbeat/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](input-heartbeat-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_456]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-heartbeat). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_450]

Generate heartbeat messages.

The general intention of this is to test the performance and availability of Logstash.


## Heartbeat Input Configuration Options [v3.0.7-plugins-inputs-heartbeat-options]

This plugin supports the following configuration options plus the [Common options](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`count`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`interval`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`message`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-message) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`threads`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-common-options) for a list of options supported by all input plugins.

 

### `count` [v3.0.7-plugins-inputs-heartbeat-count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `-1`

How many times to iterate. This is typically used only for testing purposes.


### `interval` [v3.0.7-plugins-inputs-heartbeat-interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Set how frequently messages should be sent.

The default, `60`, means send a message every 60 seconds.


### `message` [v3.0.7-plugins-inputs-heartbeat-message]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"ok"`

The message string to use in the event.

If you set this to `epoch` then this plugin will use the current timestamp in unix timestamp (which is by definition, UTC).  It will output this value into a field called `clock`

If you set this to `sequence` then this plugin will send a sequence of numbers beginning at 0 and incrementing each interval.  It will output this value into a field called `clock`

Otherwise, this value will be used verbatim as the event message. It will output this value into a field called `message`


### `threads` [v3.0.7-plugins-inputs-heartbeat-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`



## Common options [v3.0.7-plugins-inputs-heartbeat-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-7-plugins-inputs-heartbeat.md#v3.0.7-plugins-inputs-heartbeat-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.7-plugins-inputs-heartbeat-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.7-plugins-inputs-heartbeat-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.7-plugins-inputs-heartbeat-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.7-plugins-inputs-heartbeat-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 heartbeat inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  heartbeat {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.7-plugins-inputs-heartbeat-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.7-plugins-inputs-heartbeat-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



