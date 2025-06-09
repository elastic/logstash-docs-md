---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-inputs-stomp.html
---

# Stomp input plugin v3.0.7 [v3.0.7-plugins-inputs-stomp]

* Plugin version: v3.0.7
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-input-stomp/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](input-stomp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_920]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-stomp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_913]

Creates events received with the STOMP protocol.

## Stomp Input Configuration Options [v3.0.7-plugins-inputs-stomp-options]

This plugin supports the following configuration options plus the [Common options](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`destination`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-destination) | [string](/lsr/value-types.md#string) | Yes |
| [`host`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-host) | [string](/lsr/value-types.md#string) | Yes |
| [`password`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-port) | [number](/lsr/value-types.md#number) | No |
| [`reconnect`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-reconnect) | [boolean](/lsr/value-types.md#boolean) | No |
| [`reconnect_interval`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-reconnect_interval) | [number](/lsr/value-types.md#number) | No |
| [`user`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-user) | [string](/lsr/value-types.md#string) | No |
| [`vhost`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-vhost) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-common-options) for a list of options supported by all input plugins.

### `destination` [v3.0.7-plugins-inputs-stomp-destination]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The destination to read events from.

Example: `/topic/logstash`

### `host` [v3.0.7-plugins-inputs-stomp-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

The address of the STOMP server.

### `password` [v3.0.7-plugins-inputs-stomp-password]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `""`

The password to authenticate with.

### `port` [v3.0.7-plugins-inputs-stomp-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `61613`

The port to connet to on your STOMP server.

### `reconnect` [v3.0.7-plugins-inputs-stomp-reconnect]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Auto reconnect

### `reconnect_interval` [v3.0.7-plugins-inputs-stomp-reconnect_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `30`

### `user` [v3.0.7-plugins-inputs-stomp-user]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

The username to authenticate with.

### `vhost` [v3.0.7-plugins-inputs-stomp-vhost]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

The vhost to use

## Common options [v3.0.7-plugins-inputs-stomp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-7-plugins-inputs-stomp.md#v3.0.7-plugins-inputs-stomp-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.7-plugins-inputs-stomp-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.7-plugins-inputs-stomp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.7-plugins-inputs-stomp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.7-plugins-inputs-stomp-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 stomp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  stomp {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.7-plugins-inputs-stomp-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.7-plugins-inputs-stomp-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
