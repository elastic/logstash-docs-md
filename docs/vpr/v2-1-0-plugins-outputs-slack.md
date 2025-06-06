---
navigation_title: "v2.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.1.0-plugins-outputs-slack.html
---

# Slack output plugin v2.1.0 [v2.1.0-plugins-outputs-slack]

* Plugin version: v2.1.0
* Released on: 2017-12-22
* [Changelog](https://github.com/logstash-plugins/logstash-output-slack/blob/v2.1.0/CHANGELOG.md)

For other versions, see the [overview list](output-slack-index.md "Versioned slack output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1580]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-slack). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1570]

The slack output.

### Slack Output Configuration Options [v2.1.0-plugins-outputs-slack-options]

This plugin supports the following configuration options plus the [Common options](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`attachments`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-attachments "attachments") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`channel`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-channel "channel") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`format`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-format "format") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`icon_emoji`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-icon_emoji "icon_emoji") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`icon_url`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-icon_url "icon_url") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`url`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-url "url") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`username`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-username "username") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

Also see [Common options](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-common-options "Common options") for a list of options supported by all output plugins.

 

#### `attachments` [v2.1.0-plugins-outputs-slack-attachments]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* There is no default value for this setting.

Attachments array as described <https://api.slack.com/docs/attachments>

#### `channel` [v2.1.0-plugins-outputs-slack-channel]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

The channel to post to

#### `format` [v2.1.0-plugins-outputs-slack-format]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"%{message}"`

The text to post in slack

#### `icon_emoji` [v2.1.0-plugins-outputs-slack-icon_emoji]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Emoji icon to use

#### `icon_url` [v2.1.0-plugins-outputs-slack-icon_url]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Icon URL to use

#### `url` [v2.1.0-plugins-outputs-slack-url]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

The incoming webhook URI needed to post a message

#### `username` [v2.1.0-plugins-outputs-slack-username]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

The username to use for posting

### Common options [v2.1.0-plugins-outputs-slack-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v2-1-0-plugins-outputs-slack.md#v2.1.0-plugins-outputs-slack-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v2.1.0-plugins-outputs-slack-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v2.1.0-plugins-outputs-slack-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v2.1.0-plugins-outputs-slack-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 slack outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  slack {
    id => "my_plugin_id"
  }
}
```
