---
navigation_title: "v3.1.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.7-plugins-outputs-lumberjack.html
---

# Lumberjack output plugin v3.1.7 [v3.1.7-plugins-outputs-lumberjack]


* Plugin version: v3.1.7
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-lumberjack/blob/v3.1.7/CHANGELOG.md)

For other versions, see the [overview list](output-lumberjack-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1432]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-lumberjack). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1422]

This output sends events using the lumberjack protocol.


## Lumberjack Output Configuration Options [v3.1.7-plugins-outputs-lumberjack-options]

This plugin supports the following configuration options plus the [Common options](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`flush_size`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-flush_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`hosts`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`idle_flush_time`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-idle_flush_time) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`port`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`ssl_certificate`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-ssl_certificate) | a valid filesystem path | Yes |

Also see [Common options](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-common-options) for a list of options supported by all output plugins.

 

### `flush_size` [v3.1.7-plugins-outputs-lumberjack-flush_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1024`

To make efficient calls to the lumberjack output we are buffering events locally. if the number of events exceed the number the declared `flush_size` we will send them to the logstash server.


### `hosts` [v3.1.7-plugins-outputs-lumberjack-hosts]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

list of addresses lumberjack can send to


### `idle_flush_time` [v3.1.7-plugins-outputs-lumberjack-idle_flush_time]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

The amount of time since last flush before a flush is forced.

This setting helps ensure slow event rates don’t get stuck in Logstash. For example, if your `flush_size` is 100, and you have received 10 events, and it has been more than `idle_flush_time` seconds since the last flush, Logstash will flush those 10 events automatically.

This helps keep both fast and slow log streams moving along in near-real-time.


### `port` [v3.1.7-plugins-outputs-lumberjack-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

the port to connect to


### `ssl_certificate` [v3.1.7-plugins-outputs-lumberjack-ssl_certificate]

* This is a required setting.
* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

ssl certificate to use



## Common options [v3.1.7-plugins-outputs-lumberjack-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-7-plugins-outputs-lumberjack.md#v3.1.7-plugins-outputs-lumberjack-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.7-plugins-outputs-lumberjack-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.7-plugins-outputs-lumberjack-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.7-plugins-outputs-lumberjack-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 lumberjack outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  lumberjack {
    id => "my_plugin_id"
  }
}
```



