---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-juggernaut.html
---

# Juggernaut output plugin v3.0.3 [v3.0.3-plugins-outputs-juggernaut]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-juggernaut/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-juggernaut-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1338]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-juggernaut). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1328]

Push messages to the juggernaut websockets server:

* [https://github.com/maccman/juggernaut](https://github.com/maccman/juggernaut)

Wraps Websockets and supports other methods (including xhr longpolling) This is basically, just an extension of the redis output (Juggernaut pulls messages from redis).  But it pushes messages to a particular channel and formats the messages in the way juggernaut expects.


## Juggernaut Output Configuration Options [v3.0.3-plugins-outputs-juggernaut-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`channels`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-channels) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`db`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-db) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`message_format`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-message_format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`timeout`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-common-options) for a list of options supported by all output plugins.

 

### `channels` [v3.0.3-plugins-outputs-juggernaut-channels]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

List of channels to which to publish. Dynamic names are valid here, for example `logstash-%{{type}}`.


### `db` [v3.0.3-plugins-outputs-juggernaut-db]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The redis database number.


### `host` [v3.0.3-plugins-outputs-juggernaut-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"127.0.0.1"`

The hostname of the redis server to which juggernaut is listening.


### `message_format` [v3.0.3-plugins-outputs-juggernaut-message_format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

How should the message be formatted before pushing to the websocket.


### `password` [v3.0.3-plugins-outputs-juggernaut-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password to authenticate with.  There is no authentication by default.


### `port` [v3.0.3-plugins-outputs-juggernaut-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `6379`

The port to connect on.


### `timeout` [v3.0.3-plugins-outputs-juggernaut-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Redis initial connection timeout in seconds.



## Common options [v3.0.3-plugins-outputs-juggernaut-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-juggernaut.md#v3.0.3-plugins-outputs-juggernaut-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-juggernaut-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.3-plugins-outputs-juggernaut-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-outputs-juggernaut-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 juggernaut outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  juggernaut {
    id => "my_plugin_id"
  }
}
```



