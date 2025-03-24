---
navigation_title: "v2.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.3-plugins-outputs-slack.html
---

# Slack output plugin v2.0.3 [v2.0.3-plugins-outputs-slack]


* Plugin version: v2.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-slack/blob/v2.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-slack-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1570]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-slack). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1560]

The slack output.


## Slack Output Configuration Options [v2.0.3-plugins-outputs-slack-options]

This plugin supports the following configuration options plus the [Common options](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`attachments`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-attachments) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`channel`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-channel) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`format`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`icon_emoji`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-icon_emoji) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`icon_url`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-icon_url) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`url`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-url) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`username`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-common-options) for a list of options supported by all output plugins.

 

### `attachments` [v2.0.3-plugins-outputs-slack-attachments]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Attachments array as described [https://api.slack.com/docs/attachments](https://api.slack.com/docs/attachments)


### `channel` [v2.0.3-plugins-outputs-slack-channel]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The channel to post to


### `format` [v2.0.3-plugins-outputs-slack-format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

The text to post in slack


### `icon_emoji` [v2.0.3-plugins-outputs-slack-icon_emoji]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Emoji icon to use


### `icon_url` [v2.0.3-plugins-outputs-slack-icon_url]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Icon URL to use


### `url` [v2.0.3-plugins-outputs-slack-url]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The incoming webhook URI needed to post a message


### `username` [v2.0.3-plugins-outputs-slack-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The username to use for posting



## Common options [v2.0.3-plugins-outputs-slack-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-3-plugins-outputs-slack.md#v2.0.3-plugins-outputs-slack-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v2.0.3-plugins-outputs-slack-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.3-plugins-outputs-slack-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.3-plugins-outputs-slack-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 slack outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  slack {
    id => "my_plugin_id"
  }
}
```



