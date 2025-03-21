---
navigation_title: "v4.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.3-plugins-outputs-hipchat.html
---

# Hipchat output plugin v4.0.3 [v4.0.3-plugins-outputs-hipchat]


* Plugin version: v4.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-hipchat/blob/v4.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-hipchat-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1292]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-hipchat). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1285]

This output allows you to write events to [HipChat](https://www.hipchat.com/).

Make sure your API token have the appropriate permissions and support sending  messages.


## Hipchat Output Configuration Options [v4.0.3-plugins-outputs-hipchat-options]

This plugin supports the following configuration options plus the [Common options](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`color`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-color) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`format`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`from`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-from) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`message_format`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-message_format) | [string](logstash://reference/configuration-file-structure.md#string), one of `["html", "text"]` | No |
| [`room_id`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-room_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`token`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-token) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`trigger_notify`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-trigger_notify) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-common-options) for a list of options supported by all output plugins.

 

### `color` [v4.0.3-plugins-outputs-hipchat-color]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"yellow"`

Background color for message. HipChat currently supports one of "yellow", "red", "green", "purple", "gray", or "random". (default: yellow), support fieldref


### `format` [v4.0.3-plugins-outputs-hipchat-format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

Message format to send, event tokens are usable here.


### `from` [v4.0.3-plugins-outputs-hipchat-from]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The name the message will appear be sent from, you can use fieldref


### `host` [v4.0.3-plugins-outputs-hipchat-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

HipChat host to use


### `message_format` [v4.0.3-plugins-outputs-hipchat-message_format]

* Value can be any of: `html`, `text`
* Default value is `"html"`

Specify `Message Format`


### `room_id` [v4.0.3-plugins-outputs-hipchat-room_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The ID or name of the room, support fieldref


### `token` [v4.0.3-plugins-outputs-hipchat-token]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The HipChat authentication token.


### `trigger_notify` [v4.0.3-plugins-outputs-hipchat-trigger_notify]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Whether or not this message should trigger a notification for people in the room.



## Common options [v4.0.3-plugins-outputs-hipchat-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-0-3-plugins-outputs-hipchat.md#v4.0.3-plugins-outputs-hipchat-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.0.3-plugins-outputs-hipchat-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.0.3-plugins-outputs-hipchat-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.0.3-plugins-outputs-hipchat-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 hipchat outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  hipchat {
    id => "my_plugin_id"
  }
}
```



