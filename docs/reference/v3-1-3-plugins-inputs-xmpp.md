---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-inputs-xmpp.html
---

# Xmpp input plugin v3.1.3 [v3.1.3-plugins-inputs-xmpp]


* Plugin version: v3.1.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-xmpp/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](input-xmpp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1012]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-xmpp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1005]

This input allows you to receive events over XMPP/Jabber.

This plugin can be used for accepting events from humans or applications XMPP, or you can use it for PubSub or general message passing for logstash to logstash.


## Xmpp Input Configuration Options [v3.1.3-plugins-inputs-xmpp-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-password) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`rooms`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-rooms) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`user`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-user) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-common-options) for a list of options supported by all input plugins.

 

### `host` [v3.1.3-plugins-inputs-xmpp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The xmpp server to connect to. This is optional. If you omit this setting, the host on the user/identity is used. (`foo.com` for `user@foo.com`)


### `password` [v3.1.3-plugins-inputs-xmpp-password]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The xmpp password for the user/identity.


### `rooms` [v3.1.3-plugins-inputs-xmpp-rooms]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

if muc/multi-user-chat required, give the name of the room that you want to join: `room@conference.domain/nick`


### `user` [v3.1.3-plugins-inputs-xmpp-user]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The user or resource ID, like `foo@example.com`.



## Common options [v3.1.3-plugins-inputs-xmpp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-1-3-plugins-inputs-xmpp.md#v3.1.3-plugins-inputs-xmpp-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.1.3-plugins-inputs-xmpp-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.1.3-plugins-inputs-xmpp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.3-plugins-inputs-xmpp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.3-plugins-inputs-xmpp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 xmpp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  xmpp {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.1.3-plugins-inputs-xmpp-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.1.3-plugins-inputs-xmpp-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



