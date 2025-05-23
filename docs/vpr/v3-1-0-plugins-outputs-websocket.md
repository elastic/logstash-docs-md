---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-outputs-websocket.html
---

# Websocket output plugin v3.1.0 [v3.1.0-plugins-outputs-websocket]


* Plugin version: v3.1.0
* Released on: 2024-01-11
* [Changelog](https://github.com/logstash-plugins/logstash-output-websocket/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](output-websocket-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1657]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-websocket). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1647]

This output runs a websocket server and publishes any messages to all connected websocket clients.

You can connect to it with ws://<host\>:<port\>/

If no clients are connected, any messages received are ignored.


## Websocket Output Configuration Options [v3.1.0-plugins-outputs-websocket-options]

This plugin supports the following configuration options plus the [Common options](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`port`](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-common-options) for a list of options supported by all output plugins.

 

### `host` [v3.1.0-plugins-outputs-websocket-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

The address to serve websocket data from


### `port` [v3.1.0-plugins-outputs-websocket-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `3232`

The port to serve websocket data from



## Common options [v3.1.0-plugins-outputs-websocket-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-0-plugins-outputs-websocket.md#v3.1.0-plugins-outputs-websocket-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.0-plugins-outputs-websocket-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.0-plugins-outputs-websocket-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.0-plugins-outputs-websocket-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 websocket outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  websocket {
    id => "my_plugin_id"
  }
}
```



