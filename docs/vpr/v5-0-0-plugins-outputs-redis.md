---
navigation_title: "v5.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.0-plugins-outputs-redis.html
---

# Redis output plugin v5.0.0 [v5.0.0-plugins-outputs-redis]

* Plugin version: v5.0.0
* Released on: 2019-01-11
* [Changelog](https://github.com/logstash-plugins/logstash-output-redis/blob/v5.0.0/CHANGELOG.md)

For other versions, see the [overview list](output-redis-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1514]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-redis). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1504]

This output will send events to a Redis queue using RPUSH. The RPUSH command is supported in Redis v0.0.7+. Using PUBLISH to a channel requires at least v1.3.8+. While you may be able to make these Redis versions work, the best performance and stability will be found in more recent stable versions. Versions 2.6.0+ are recommended.

For more information, see [the Redis homepage](http://redis.io/)

## Redis Output Configuration Options [v5.0.0-plugins-outputs-redis-options]

This plugin supports the following configuration options plus the [Common options](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`batch`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-batch) | [boolean](/lsr/value-types.md#boolean) | No |
| [`batch_events`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-batch_events) | [number](/lsr/value-types.md#number) | No |
| [`batch_timeout`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-batch_timeout) | [number](/lsr/value-types.md#number) | No |
| [`congestion_interval`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-congestion_interval) | [number](/lsr/value-types.md#number) | No |
| [`congestion_threshold`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-congestion_threshold) | [number](/lsr/value-types.md#number) | No |
| [`data_type`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-data_type) | [string](/lsr/value-types.md#string), one of `["list", "channel"]` | No |
| [`db`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-db) | [number](/lsr/value-types.md#number) | No |
| [`host`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-host) | [array](/lsr/value-types.md#array) | No |
| [`key`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-key) | [string](/lsr/value-types.md#string) | No |
| [`password`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-port) | [number](/lsr/value-types.md#number) | No |
| [`reconnect_interval`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-reconnect_interval) | [number](/lsr/value-types.md#number) | No |
| [`shuffle_hosts`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-shuffle_hosts) | [boolean](/lsr/value-types.md#boolean) | No |
| [`timeout`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-timeout) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-common-options) for a list of options supported by all output plugins.

### `batch` [v5.0.0-plugins-outputs-redis-batch]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Set to true if you want Redis to batch up values and send 1 RPUSH command instead of one command per value to push on the list. Note that this only works with `data_type="list"` mode right now.

If true, we send an RPUSH every "batch\_events" events or "batch\_timeout" seconds (whichever comes first). Only supported for `data_type` is "list".

### `batch_events` [v5.0.0-plugins-outputs-redis-batch_events]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50`

If batch is set to true, the number of events we queue up for an RPUSH.

### `batch_timeout` [v5.0.0-plugins-outputs-redis-batch_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

If batch is set to true, the maximum amount of time between RPUSH commands when there are pending events to flush.

### `congestion_interval` [v5.0.0-plugins-outputs-redis-congestion_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

How often to check for congestion. Default is one second. Zero means to check on every event.

### `congestion_threshold` [v5.0.0-plugins-outputs-redis-congestion_threshold]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

In case Redis `data_type` is `list` and has more than `@congestion_threshold` items, block until someone consumes them and reduces congestion, otherwise if there are no consumers Redis will run out of memory, unless it was configured with OOM protection. But even with OOM protection, a single Redis list can block all other users of Redis, until Redis CPU consumption reaches the max allowed RAM size. A default value of 0 means that this limit is disabled. Only supported for `list` Redis `data_type`.

### `data_type` [v5.0.0-plugins-outputs-redis-data_type]

* Value can be any of: `list`, `channel`
* There is no default value for this setting.

Either list or channel. If `data_type` is list, then we will set RPUSH to key. If `data_type` is channel, then we will PUBLISH to `key`.

### `db` [v5.0.0-plugins-outputs-redis-db]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

The Redis database number.

### `host` [v5.0.0-plugins-outputs-redis-host]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["127.0.0.1"]`

The hostname(s) of your Redis server(s). Ports may be specified on any hostname, which will override the global port config. If the hosts list is an array, Logstash will pick one random host to connect to, if that host is disconnected it will then pick another.

For example:

```
    "127.0.0.1"
    ["127.0.0.1", "127.0.0.2"]
    ["127.0.0.1:6380", "127.0.0.1"]
```

### `key` [v5.0.0-plugins-outputs-redis-key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of a Redis list or channel. Dynamic names are valid here, for example `logstash-%{type}`.

### `password` [v5.0.0-plugins-outputs-redis-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to authenticate with. There is no authentication by default.

### `port` [v5.0.0-plugins-outputs-redis-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `6379`

The default port to connect on. Can be overridden on any hostname.

### `reconnect_interval` [v5.0.0-plugins-outputs-redis-reconnect_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

Interval for reconnecting to failed Redis connections

### `shuffle_hosts` [v5.0.0-plugins-outputs-redis-shuffle_hosts]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Shuffle the host list during Logstash startup.

### `timeout` [v5.0.0-plugins-outputs-redis-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

Redis initial connection timeout in seconds.

## Common options [v5.0.0-plugins-outputs-redis-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-0-0-plugins-outputs-redis.md#v5.0.0-plugins-outputs-redis-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v5.0.0-plugins-outputs-redis-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.0.0-plugins-outputs-redis-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.0.0-plugins-outputs-redis-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 redis outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  redis {
    id => "my_plugin_id"
  }
}
```
