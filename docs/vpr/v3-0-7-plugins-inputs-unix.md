---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-inputs-unix.html
---

# Unix input plugin v3.0.7 [v3.0.7-plugins-inputs-unix]

* Plugin version: v3.0.7
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-unix/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](input-unix-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1027]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-unix). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1020]

Read events over a UNIX socket.

Like `stdin` and `file` inputs, each event is assumed to be one line of text.

Can either accept connections from clients or connect to a server, depending on `mode`.

## Unix Input Configuration Options [v3.0.7-plugins-inputs-unix-options]

This plugin supports the following configuration options plus the [Common options](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`data_timeout`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-data_timeout) | [number](/lsr/value-types.md#number) | No |
| [`force_unlink`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-force_unlink) | [boolean](/lsr/value-types.md#boolean) | No |
| [`mode`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`path`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-path) | [string](/lsr/value-types.md#string) | Yes |
| [`socket_not_present_retry_interval_seconds`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-socket_not_present_retry_interval_seconds) | [number](/lsr/value-types.md#number) | Yes |

Also see [Common options](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-common-options) for a list of options supported by all input plugins.

### `data_timeout` [v3.0.7-plugins-inputs-unix-data_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `-1`

The *read* timeout in seconds. If a particular connection is idle for more than this timeout period, we will assume it is dead and close it.

If you never want to timeout, use -1.

### `force_unlink` [v3.0.7-plugins-inputs-unix-force_unlink]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Remove socket file in case of EADDRINUSE failure

### `mode` [v3.0.7-plugins-inputs-unix-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.

### `path` [v3.0.7-plugins-inputs-unix-path]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

When mode is `server`, the path to listen on. When mode is `client`, the path to connect to.

### `socket_not_present_retry_interval_seconds` [v3.0.7-plugins-inputs-unix-socket_not_present_retry_interval_seconds]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

Amount of time in seconds to wait if the socket file is not present, before retrying. Only positive values are allowed.

This setting is only used if `mode` is `client`.

## Common options [v3.0.7-plugins-inputs-unix-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-7-plugins-inputs-unix.md#v3.0.7-plugins-inputs-unix-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.7-plugins-inputs-unix-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.7-plugins-inputs-unix-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"line"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.7-plugins-inputs-unix-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.7-plugins-inputs-unix-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 unix inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  unix {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.7-plugins-inputs-unix-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.7-plugins-inputs-unix-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
