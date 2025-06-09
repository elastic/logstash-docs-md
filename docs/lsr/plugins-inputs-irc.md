---
navigation_title: "irc"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash/current/plugins-inputs-irc.html
---

# Irc input plugin [plugins-inputs-irc]

* Plugin version: v3.0.7
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-irc/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/input-irc-index.html).

## Installation [_installation_4]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-input-irc`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/8.18/working-with-plugins.html) for more details.

## Getting help [_getting_help_29]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-irc). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).

## Description [_description_29]

Read events from an IRC Server.

## Irc Input Configuration Options [plugins-inputs-irc-options]

This plugin supports the following configuration options plus the [Common options](plugins-inputs-irc.md#plugins-inputs-irc-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`catch_all`](plugins-inputs-irc.md#plugins-inputs-irc-catch_all) | [boolean](value-types.md#boolean) | No |
| [`channels`](plugins-inputs-irc.md#plugins-inputs-irc-channels) | [array](value-types.md#array) | Yes |
| [`get_stats`](plugins-inputs-irc.md#plugins-inputs-irc-get_stats) | [boolean](value-types.md#boolean) | No |
| [`host`](plugins-inputs-irc.md#plugins-inputs-irc-host) | [string](value-types.md#string) | Yes |
| [`nick`](plugins-inputs-irc.md#plugins-inputs-irc-nick) | [string](value-types.md#string) | No |
| [`password`](plugins-inputs-irc.md#plugins-inputs-irc-password) | [password](value-types.md#password) | No |
| [`port`](plugins-inputs-irc.md#plugins-inputs-irc-port) | [number](value-types.md#number) | No |
| [`real`](plugins-inputs-irc.md#plugins-inputs-irc-real) | [string](value-types.md#string) | No |
| [`secure`](plugins-inputs-irc.md#plugins-inputs-irc-secure) | [boolean](value-types.md#boolean) | No |
| [`stats_interval`](plugins-inputs-irc.md#plugins-inputs-irc-stats_interval) | [number](value-types.md#number) | No |
| [`user`](plugins-inputs-irc.md#plugins-inputs-irc-user) | [string](value-types.md#string) | No |

Also see [Common options](plugins-inputs-irc.md#plugins-inputs-irc-common-options) for a list of options supported by all input plugins.

### `catch_all` [plugins-inputs-irc-catch_all]

* Value type is [boolean](value-types.md#boolean)
* Default value is `false`

Catch all IRC channel/user events not just channel messages

### `channels` [plugins-inputs-irc-channels]

* This is a required setting.
* Value type is [array](value-types.md#array)
* There is no default value for this setting.

Channels to join and read messages from.

These should be full channel names including the *#* symbol, such as "#logstash".

For passworded channels, add a space and the channel password, such as "#logstash password".

### `get_stats` [plugins-inputs-irc-get_stats]

* Value type is [boolean](value-types.md#boolean)
* Default value is `false`

Gather and send user counts for channels - this requires catch\_all and will force it

### `host` [plugins-inputs-irc-host]

* This is a required setting.
* Value type is [string](value-types.md#string)
* There is no default value for this setting.

Host of the IRC Server to connect to.

### `nick` [plugins-inputs-irc-nick]

* Value type is [string](value-types.md#string)
* Default value is `"logstash"`

IRC Nickname

### `password` [plugins-inputs-irc-password]

* Value type is [password](value-types.md#password)
* There is no default value for this setting.

IRC Server password

### `port` [plugins-inputs-irc-port]

* Value type is [number](value-types.md#number)
* Default value is `6667`

Port for the IRC Server

### `real` [plugins-inputs-irc-real]

* Value type is [string](value-types.md#string)
* Default value is `"logstash"`

IRC Real name

### `secure` [plugins-inputs-irc-secure]

* Value type is [boolean](value-types.md#boolean)
* Default value is `false`

Set this to true to enable SSL.

### `stats_interval` [plugins-inputs-irc-stats_interval]

* Value type is [number](value-types.md#number)
* Default value is `5`

How often in minutes to get the user count stats

### `user` [plugins-inputs-irc-user]

* Value type is [string](value-types.md#string)
* Default value is `"logstash"`

IRC Username

## Common options [plugins-inputs-irc-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](plugins-inputs-irc.md#plugins-inputs-irc-add_field) | [hash](value-types.md#hash) | No |
| [`codec`](plugins-inputs-irc.md#plugins-inputs-irc-codec) | [codec](value-types.md#codec) | No |
| [`enable_metric`](plugins-inputs-irc.md#plugins-inputs-irc-enable_metric) | [boolean](value-types.md#boolean) | No |
| [`id`](plugins-inputs-irc.md#plugins-inputs-irc-id) | [string](value-types.md#string) | No |
| [`tags`](plugins-inputs-irc.md#plugins-inputs-irc-tags) | [array](value-types.md#array) | No |
| [`type`](plugins-inputs-irc.md#plugins-inputs-irc-type) | [string](value-types.md#string) | No |

### `add_field` [plugins-inputs-irc-add_field]

* Value type is [hash](value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [plugins-inputs-irc-codec]

* Value type is [codec](value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [plugins-inputs-irc-enable_metric]

* Value type is [boolean](value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [plugins-inputs-irc-id]

* Value type is [string](value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 irc inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  irc {
    id => "my_plugin_id"
  }
}
```

Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.

### `tags` [plugins-inputs-irc-tags]

* Value type is [array](value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [plugins-inputs-irc-type]

* Value type is [string](value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
