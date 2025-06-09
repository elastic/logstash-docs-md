---
navigation_title: "v3.0.8"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.8-plugins-outputs-stomp.html
---

# Stomp output plugin v3.0.8 [v3.0.8-plugins-outputs-stomp]

* Plugin version: v3.0.8
* Released on: 2017-11-13
* [Changelog](https://github.com/logstash-plugins/logstash-output-stomp/blob/v3.0.8/CHANGELOG.md)

For other versions, see the [overview list](output-stomp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1636]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-stomp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1626]

This output writes events using the STOMP protocol.

## Stomp Output Configuration Options [v3.0.8-plugins-outputs-stomp-options]

This plugin supports the following configuration options plus the [Common options](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`debug`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-debug) | [boolean](/lsr/value-types.md#boolean) | No |
| [`destination`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-destination) | [string](/lsr/value-types.md#string) | Yes |
| [`headers`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-headers) | [hash](/lsr/value-types.md#hash) | No |
| [`host`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-host) | [string](/lsr/value-types.md#string) | Yes |
| [`password`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-port) | [number](/lsr/value-types.md#number) | No |
| [`user`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-user) | [string](/lsr/value-types.md#string) | No |
| [`vhost`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-vhost) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-common-options) for a list of options supported by all output plugins.

### `debug` [v3.0.8-plugins-outputs-stomp-debug]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable debugging output?

### `destination` [v3.0.8-plugins-outputs-stomp-destination]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The destination to read events from. Supports string expansion, meaning `%{foo}` values will expand to the field value.

Example: "/topic/logstash"

### `headers` [v3.0.8-plugins-outputs-stomp-headers]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Custom headers to send with each message. Supports string expansion, meaning %{foo} values will expand to the field value.

Example: headers ⇒ \["amq-msg-type", "text", "host", "%{host}"]

### `host` [v3.0.8-plugins-outputs-stomp-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The address of the STOMP server.

### `password` [v3.0.8-plugins-outputs-stomp-password]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `""`

The password to authenticate with.

### `port` [v3.0.8-plugins-outputs-stomp-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `61613`

The port to connect to on your STOMP server.

### `user` [v3.0.8-plugins-outputs-stomp-user]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

The username to authenticate with.

### `vhost` [v3.0.8-plugins-outputs-stomp-vhost]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

The vhost to use

## Common options [v3.0.8-plugins-outputs-stomp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-8-plugins-outputs-stomp.md#v3.0.8-plugins-outputs-stomp-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.8-plugins-outputs-stomp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.8-plugins-outputs-stomp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.8-plugins-outputs-stomp-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 stomp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  stomp {
    id => "my_plugin_id"
  }
}
```
