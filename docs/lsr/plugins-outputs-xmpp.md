---
navigation_title: "xmpp"
---

# Xmpp output plugin [plugins-outputs-xmpp]


* Plugin version: v3.0.8
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-xmpp/blob/v3.0.8/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/output-xmpp-index.md).

## Installation [_installation_52]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-output-xmpp`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html) for more details.


## Getting help [_getting_help_121]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-xmpp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_120]

This output allows you ship events over XMPP/Jabber.

This plugin can be used for posting events to humans over XMPP, or you can use it for PubSub or general message passing for logstash to logstash.


## Xmpp Output Configuration Options [plugins-outputs-xmpp-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-xmpp.md#plugins-outputs-xmpp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-host) | [string](introduction.md#string) | No |
| [`message`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-message) | [string](introduction.md#string) | Yes |
| [`password`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-password) | [password](introduction.md#password) | Yes |
| [`rooms`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-rooms) | [array](introduction.md#array) | No |
| [`user`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-user) | [string](introduction.md#string) | Yes |
| [`users`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-users) | [array](introduction.md#array) | No |

Also see [Common options](plugins-outputs-xmpp.md#plugins-outputs-xmpp-common-options) for a list of options supported by all output plugins.

 

### `host` [plugins-outputs-xmpp-host]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The xmpp server to connect to. This is optional. If you omit this setting, the host on the user/identity is used. (foo.com for [user@foo.com](mailto:user@foo.com))


### `message` [plugins-outputs-xmpp-message]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The message to send. This supports dynamic strings like `%{{host}}`


### `password` [plugins-outputs-xmpp-password]

* This is a required setting.
* Value type is [password](introduction.md#password)
* There is no default value for this setting.

The xmpp password for the user/identity.


### `rooms` [plugins-outputs-xmpp-rooms]

* Value type is [array](introduction.md#array)
* There is no default value for this setting.

if muc/multi-user-chat required, give the name of the room that you want to join: room@conference.domain/nick


### `user` [plugins-outputs-xmpp-user]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The user or resource ID, like `foo@example.com`.


### `users` [plugins-outputs-xmpp-users]

* Value type is [array](introduction.md#array)
* There is no default value for this setting.

The users to send messages to



## Common options [plugins-outputs-xmpp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-codec) | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-outputs-xmpp.md#plugins-outputs-xmpp-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

### `codec` [plugins-outputs-xmpp-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [plugins-outputs-xmpp-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-xmpp-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 xmpp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  xmpp {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




