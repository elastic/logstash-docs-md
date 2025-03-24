---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-irc.html
---

# Irc output plugin v3.0.6 [v3.0.6-plugins-outputs-irc]


* Plugin version: v3.0.6
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-irc/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-irc-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1324]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-irc). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1314]

Write events to IRC


## Irc Output Configuration Options [v3.0.6-plugins-outputs-irc-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`channels`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-channels) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`format`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`messages_per_second`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-messages_per_second) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`nick`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-nick) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`post_string`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-post_string) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pre_string`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-pre_string) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`real`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-real) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`secure`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-secure) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`user`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-common-options) for a list of options supported by all output plugins.

 

### `channels` [v3.0.6-plugins-outputs-irc-channels]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Channels to broadcast to.

These should be full channel names including the *#* symbol, such as "#logstash".


### `format` [v3.0.6-plugins-outputs-irc-format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

Message format to send, event tokens are usable here


### `host` [v3.0.6-plugins-outputs-irc-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Address of the host to connect to


### `messages_per_second` [v3.0.6-plugins-outputs-irc-messages_per_second]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0.5`

Limit the rate of messages sent to IRC in messages per second.


### `nick` [v3.0.6-plugins-outputs-irc-nick]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

IRC Nickname


### `password` [v3.0.6-plugins-outputs-irc-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

IRC server password


### `port` [v3.0.6-plugins-outputs-irc-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `6667`

Port on host to connect to.


### `post_string` [v3.0.6-plugins-outputs-irc-post_string]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Static string after event


### `pre_string` [v3.0.6-plugins-outputs-irc-pre_string]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Static string before event


### `real` [v3.0.6-plugins-outputs-irc-real]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

IRC Real name


### `secure` [v3.0.6-plugins-outputs-irc-secure]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Set this to true to enable SSL.


### `user` [v3.0.6-plugins-outputs-irc-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

IRC Username



## Common options [v3.0.6-plugins-outputs-irc-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-irc.md#v3.0.6-plugins-outputs-irc-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-irc-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-outputs-irc-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-outputs-irc-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 irc outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  irc {
    id => "my_plugin_id"
  }
}
```



