---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-outputs-xmpp.html
---

# Xmpp output plugin v3.0.5 [v3.0.5-plugins-outputs-xmpp]


* Plugin version: v3.0.5
* Released on: 2017-06-27
* [Changelog](https://github.com/logstash-plugins/logstash-output-xmpp/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-xmpp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1665]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-xmpp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1655]

This output allows you ship events over XMPP/Jabber.

This plugin can be used for posting events to humans over XMPP, or you can use it for PubSub or general message passing for logstash to logstash.


## Xmpp Output Configuration Options [v3.0.5-plugins-outputs-xmpp-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`message`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-message) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`password`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-password) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`rooms`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-rooms) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`user`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-user) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`users`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-users) | [array](logstash://reference/configuration-file-structure.md#array) | No |

Also see [Common options](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-common-options) for a list of options supported by all output plugins.

 

### `host` [v3.0.5-plugins-outputs-xmpp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The xmpp server to connect to. This is optional. If you omit this setting, the host on the user/identity is used. (foo.com for `user@foo.com`)


### `message` [v3.0.5-plugins-outputs-xmpp-message]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The message to send. This supports dynamic strings like `%{{host}}`


### `password` [v3.0.5-plugins-outputs-xmpp-password]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The xmpp password for the user/identity.


### `rooms` [v3.0.5-plugins-outputs-xmpp-rooms]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

if muc/multi-user-chat required, give the name of the room that you want to join: room@conference.domain/nick


### `user` [v3.0.5-plugins-outputs-xmpp-user]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The user or resource ID, like `foo@example.com`.


### `users` [v3.0.5-plugins-outputs-xmpp-users]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The users to send messages to



## Common options [v3.0.5-plugins-outputs-xmpp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-5-plugins-outputs-xmpp.md#v3.0.5-plugins-outputs-xmpp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.5-plugins-outputs-xmpp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.5-plugins-outputs-xmpp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.5-plugins-outputs-xmpp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 xmpp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  xmpp {
    id => "my_plugin_id"
  }
}
```



