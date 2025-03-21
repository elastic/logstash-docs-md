---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-inputs-imap.html
---

# Imap input plugin v3.0.3 [v3.0.3-plugins-inputs-imap]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-imap/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](input-imap-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_535]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-imap). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_529]

Read mails from IMAP server

Periodically scan an IMAP folder (`INBOX` by default) and move any read messages to the trash.


## Imap Input Configuration Options [v3.0.3-plugins-inputs-imap-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`check_interval`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-check_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`content_type`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-content_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`delete`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-delete) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`expunge`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-expunge) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`fetch_count`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-fetch_count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`folder`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-folder) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`lowercase_headers`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-lowercase_headers) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`password`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-password) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`port`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`secure`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-secure) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`strip_attachments`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-strip_attachments) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`user`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-user) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`verify_cert`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-verify_cert) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-common-options) for a list of options supported by all input plugins.

 

### `check_interval` [v3.0.3-plugins-inputs-imap-check_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `300`


### `content_type` [v3.0.3-plugins-inputs-imap-content_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"text/plain"`

For multipart messages, use the first part that has this content-type as the event message.


### `delete` [v3.0.3-plugins-inputs-imap-delete]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`


### `expunge` [v3.0.3-plugins-inputs-imap-expunge]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`


### `fetch_count` [v3.0.3-plugins-inputs-imap-fetch_count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`


### `folder` [v3.0.3-plugins-inputs-imap-folder]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"INBOX"`


### `host` [v3.0.3-plugins-inputs-imap-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.


### `lowercase_headers` [v3.0.3-plugins-inputs-imap-lowercase_headers]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`


### `password` [v3.0.3-plugins-inputs-imap-password]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.


### `port` [v3.0.3-plugins-inputs-imap-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.


### `secure` [v3.0.3-plugins-inputs-imap-secure]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`


### `strip_attachments` [v3.0.3-plugins-inputs-imap-strip_attachments]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`


### `user` [v3.0.3-plugins-inputs-imap-user]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.


### `verify_cert` [v3.0.3-plugins-inputs-imap-verify_cert]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`



## Common options [v3.0.3-plugins-inputs-imap-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-3-plugins-inputs-imap.md#v3.0.3-plugins-inputs-imap-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.3-plugins-inputs-imap-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.3-plugins-inputs-imap-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.3-plugins-inputs-imap-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-inputs-imap-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 imap inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  imap {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.3-plugins-inputs-imap-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.3-plugins-inputs-imap-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



