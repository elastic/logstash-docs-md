---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-inputs-relp.html
---

# Relp input plugin v3.0.2 [v3.0.2-plugins-inputs-relp]


* Plugin version: v3.0.2
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-input-relp/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-relp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_774]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-relp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_767]

Read RELP events over a TCP socket.

For more information about RELP, see [http://www.rsyslog.com/doc/imrelp.html](http://www.rsyslog.com/doc/imrelp.md)

This protocol implements application-level acknowledgements to help protect against message loss.

Message acks only function as far as messages being put into the queue for filters; anything lost after that point will not be retransmitted


## Relp Input Configuration Options [v3.0.2-plugins-inputs-relp-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`port`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`ssl_cacert`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_cacert) | a valid filesystem path | No |
| [`ssl_cert`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_cert) | a valid filesystem path | No |
| [`ssl_enable`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_enable) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verify`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-ssl_verify) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-common-options) for a list of options supported by all input plugins.

 

### `host` [v3.0.2-plugins-inputs-relp-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

The address to listen on.


### `port` [v3.0.2-plugins-inputs-relp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The port to listen on.


### `ssl_cacert` [v3.0.2-plugins-inputs-relp-ssl_cacert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.


### `ssl_cert` [v3.0.2-plugins-inputs-relp-ssl_cert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate path


### `ssl_enable` [v3.0.2-plugins-inputs-relp-ssl_enable]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).


### `ssl_key` [v3.0.2-plugins-inputs-relp-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key path


### `ssl_key_passphrase` [v3.0.2-plugins-inputs-relp-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

SSL key passphrase


### `ssl_verify` [v3.0.2-plugins-inputs-relp-ssl_verify]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Verify the identity of the other end of the SSL connection against the CA. For input, sets the field `sslsubject` to that of the client certificate.



## Common options [v3.0.2-plugins-inputs-relp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-2-plugins-inputs-relp.md#v3.0.2-plugins-inputs-relp-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.2-plugins-inputs-relp-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.2-plugins-inputs-relp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.2-plugins-inputs-relp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-inputs-relp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 relp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  relp {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.2-plugins-inputs-relp-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.2-plugins-inputs-relp-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



