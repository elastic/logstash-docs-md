---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-inputs-irc.html
---

# Irc input plugin v3.0.4 [v3.0.4-plugins-inputs-irc]

* Plugin version: v3.0.4
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-irc/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](input-irc-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_560]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-irc). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_554]

Read events from an IRC Server.

## Irc Input Configuration Options [v3.0.4-plugins-inputs-irc-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`catch_all`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-catch_all) | [boolean](/lsr/value-types.md#boolean) | No |
| [`channels`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-channels) | [array](/lsr/value-types.md#array) | Yes |
| [`get_stats`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-get_stats) | [boolean](/lsr/value-types.md#boolean) | No |
| [`host`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-host) | [string](/lsr/value-types.md#string) | Yes |
| [`nick`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-nick) | [string](/lsr/value-types.md#string) | No |
| [`password`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-port) | [number](/lsr/value-types.md#number) | No |
| [`real`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-real) | [string](/lsr/value-types.md#string) | No |
| [`secure`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-secure) | [boolean](/lsr/value-types.md#boolean) | No |
| [`stats_interval`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-stats_interval) | [number](/lsr/value-types.md#number) | No |
| [`user`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-user) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-common-options) for a list of options supported by all input plugins.

### `catch_all` [v3.0.4-plugins-inputs-irc-catch_all]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Catch all IRC channel/user events not just channel messages

### `channels` [v3.0.4-plugins-inputs-irc-channels]

* This is a required setting.
* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Channels to join and read messages from.

These should be full channel names including the *#* symbol, such as "#logstash".

For passworded channels, add a space and the channel password, such as "#logstash password".

### `get_stats` [v3.0.4-plugins-inputs-irc-get_stats]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Gather and send user counts for channels - this requires catch\_all and will force it

### `host` [v3.0.4-plugins-inputs-irc-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Host of the IRC Server to connect to.

### `nick` [v3.0.4-plugins-inputs-irc-nick]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

IRC Nickname

### `password` [v3.0.4-plugins-inputs-irc-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

IRC Server password

### `port` [v3.0.4-plugins-inputs-irc-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `6667`

Port for the IRC Server

### `real` [v3.0.4-plugins-inputs-irc-real]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

IRC Real name

### `secure` [v3.0.4-plugins-inputs-irc-secure]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Set this to true to enable SSL.

### `stats_interval` [v3.0.4-plugins-inputs-irc-stats_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

How often in minutes to get the user count stats

### `user` [v3.0.4-plugins-inputs-irc-user]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

IRC Username

## Common options [v3.0.4-plugins-inputs-irc-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-4-plugins-inputs-irc.md#v3.0.4-plugins-inputs-irc-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.4-plugins-inputs-irc-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.4-plugins-inputs-irc-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.4-plugins-inputs-irc-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.4-plugins-inputs-irc-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 irc inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  irc {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.4-plugins-inputs-irc-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.4-plugins-inputs-irc-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
