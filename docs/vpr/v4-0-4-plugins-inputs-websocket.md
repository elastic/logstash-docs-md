---
navigation_title: "v4.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.4-plugins-inputs-websocket.html
---

# Websocket input plugin v4.0.4 [v4.0.4-plugins-inputs-websocket]

* Plugin version: v4.0.4
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-websocket/blob/v4.0.4/CHANGELOG.md)

For other versions, see the [overview list](input-websocket-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1035]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-websocket). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1028]

Read events over the websocket protocol.

## Websocket Input Configuration Options [v4.0.4-plugins-inputs-websocket-options]

This plugin supports the following configuration options plus the [Common options](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`mode`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-mode) | [string](/lsr/value-types.md#string), one of `["client"]` | No |
| [`url`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-url) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-common-options) for a list of options supported by all input plugins.

### `mode` [v4.0.4-plugins-inputs-websocket-mode]

* Value can be any of: `client`
* Default value is `"client"`

Select the plugin’s mode of operation. Right now only client mode is supported, i.e. this plugin connects to a websocket server and receives events from the server as websocket messages.

### `url` [v4.0.4-plugins-inputs-websocket-url]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The URL to connect to.

## Common options [v4.0.4-plugins-inputs-websocket-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v4-0-4-plugins-inputs-websocket.md#v4.0.4-plugins-inputs-websocket-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v4.0.4-plugins-inputs-websocket-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v4.0.4-plugins-inputs-websocket-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.4-plugins-inputs-websocket-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.4-plugins-inputs-websocket-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 websocket inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  websocket {
    id => "my_plugin_id"
  }
}
```

### `tags` [v4.0.4-plugins-inputs-websocket-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v4.0.4-plugins-inputs-websocket-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
