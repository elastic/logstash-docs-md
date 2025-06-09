---
navigation_title: "v3.6.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.6.0-plugins-inputs-redis.html
---

# Redis input plugin v3.6.0 [v3.6.0-plugins-inputs-redis]

* Plugin version: v3.6.0
* Released on: 2020-12-22
* [Changelog](https://github.com/logstash-plugins/logstash-input-redis/blob/v3.6.0/CHANGELOG.md)

For other versions, see the [overview list](input-redis-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_787]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-redis). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_780]

This input will read events from a Redis instance; it supports both Redis channels and lists. The list command (BLPOP) used by Logstash is supported in Redis v1.3.1+, and the channel commands used by Logstash are found in Redis v1.3.8+. While you may be able to make these Redis versions work, the best performance and stability will be found in more recent stable versions. Versions 2.6.0+ are recommended.

For more information about Redis, see <http://redis.io/>

`batch_count` note: If you use the `batch_count` setting, you **must** use a Redis version 2.6.0 or newer. Anything older does not support the operations used by batching.

## Redis Input Configuration Options [v3.6.0-plugins-inputs-redis-options]

This plugin supports the following configuration options plus the [Common options](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`batch_count`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-batch_count) | [number](/lsr/value-types.md#number) | No |
| [`command_map`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-command_map) | [hash](/lsr/value-types.md#hash) | No |
| [`data_type`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-data_type) | [string](/lsr/value-types.md#string), one of `["list", "channel", "pattern_channel"]` | Yes |
| [`db`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-db) | [number](/lsr/value-types.md#number) | No |
| [`host`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-host) | [string](/lsr/value-types.md#string) | No |
| [`path`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-path) | [string](/lsr/value-types.md#string) | No |
| [`key`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-key) | [string](/lsr/value-types.md#string) | Yes |
| [`password`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-port) | [number](/lsr/value-types.md#number) | No |
| [`ssl`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`threads`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-threads) | [number](/lsr/value-types.md#number) | No |
| [`timeout`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-timeout) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-common-options) for a list of options supported by all input plugins.

### `batch_count` [v3.6.0-plugins-inputs-redis-batch_count]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `125`

The number of events to return from Redis using EVAL.

### `command_map` [v3.6.0-plugins-inputs-redis-command_map]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.
* key is the default command name, value is the renamed command.

Configure renamed redis commands in the form of "oldname" ⇒ "newname". Redis allows for the renaming or disabling of commands in its protocol, see: <https://redis.io/topics/security>

### `data_type` [v3.6.0-plugins-inputs-redis-data_type]

* This is a required setting.
* Value can be any of: `list`, `channel`, `pattern_channel`
* There is no default value for this setting.

Specify either list or channel. If `data_type` is `list`, then we will BLPOP the key. If `data_type` is `channel`, then we will SUBSCRIBE to the key. If `data_type` is `pattern_channel`, then we will PSUBSCRIBE to the key.

### `db` [v3.6.0-plugins-inputs-redis-db]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

The Redis database number.

### `host` [v3.6.0-plugins-inputs-redis-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"127.0.0.1"`

The hostname of your Redis server.

### `path` [v3.6.0-plugins-inputs-redis-path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* Path will override Host configuration if both specified.

The unix socket path of your Redis server.

### `key` [v3.6.0-plugins-inputs-redis-key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of a Redis list or channel.

### `password` [v3.6.0-plugins-inputs-redis-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to authenticate with. There is no authentication by default.

### `port` [v3.6.0-plugins-inputs-redis-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `6379`

The port to connect on.

### `ssl` [v3.6.0-plugins-inputs-redis-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable SSL support.

### `threads` [v3.6.0-plugins-inputs-redis-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

### `timeout` [v3.6.0-plugins-inputs-redis-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

Initial connection timeout in seconds.

## Common options [v3.6.0-plugins-inputs-redis-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-6-0-plugins-inputs-redis.md#v3.6.0-plugins-inputs-redis-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.6.0-plugins-inputs-redis-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.6.0-plugins-inputs-redis-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.6.0-plugins-inputs-redis-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.6.0-plugins-inputs-redis-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 redis inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  redis {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.6.0-plugins-inputs-redis-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.6.0-plugins-inputs-redis-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
