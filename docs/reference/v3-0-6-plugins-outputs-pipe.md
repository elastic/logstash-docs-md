---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-pipe.html
---

# Pipe output plugin v3.0.6 [v3.0.6-plugins-outputs-pipe]


* Plugin version: v3.0.6
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-pipe/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-pipe-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1475]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-pipe). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1465]

Pipe output.

Pipe events to stdin of another program. You can use fields from the event as parts of the command. WARNING: This feature can cause logstash to fork off multiple children if you are not carefull with per-event commandline.


## Pipe Output Configuration Options [v3.0.6-plugins-outputs-pipe-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`command`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-command) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`message_format`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-message_format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ttl`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-common-options) for a list of options supported by all output plugins.

 

### `command` [v3.0.6-plugins-outputs-pipe-command]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Command line to launch and pipe to


### `message_format` [v3.0.6-plugins-outputs-pipe-message_format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The format to use when writing events to the pipe. This value supports any string and can include `%{{name}}` and other dynamic strings.

If this setting is omitted, the full json representation of the event will be written as a single line.


### `ttl` [v3.0.6-plugins-outputs-pipe-ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Close pipe that hasn’t been used for TTL seconds. -1 or 0 means never close.



## Common options [v3.0.6-plugins-outputs-pipe-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-pipe.md#v3.0.6-plugins-outputs-pipe-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-pipe-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-outputs-pipe-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-outputs-pipe-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 pipe outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  pipe {
    id => "my_plugin_id"
  }
}
```



