---
navigation_title: "v3.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.4-plugins-inputs-lumberjack.html
---

# Lumberjack input plugin v3.1.4 [v3.1.4-plugins-inputs-lumberjack]

* Plugin version: v3.1.4
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-input-lumberjack/blob/v3.1.4/CHANGELOG.md)

For other versions, see the [overview list](input-lumberjack-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_741]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-lumberjack). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_734]

Receive events using the Lumberjack protocol.

This input can be used to reliably and securely transport events between Logstash instances. To do so, use the [lumberjack output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-lumberjack.html) in the sending Logstash instance(s).

It can also be used to receive events from the deprecated [logstash-forwarder](https://github.com/elastic/logstash-forwarder) tool that has been replaced by [Filebeat](https://github.com/elastic/beats/tree/master/filebeat).

## Lumberjack Input Configuration Options [v3.1.4-plugins-inputs-lumberjack-options]

This plugin supports the following configuration options plus the [Common options](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`congestion_threshold`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-congestion_threshold) | [number](/lsr/value-types.md#number) | No |
| [`host`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-host) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-port) | [number](/lsr/value-types.md#number) | Yes |
| [`ssl_certificate`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-ssl_certificate) | a valid filesystem path | Yes |
| [`ssl_key`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-ssl_key) | a valid filesystem path | Yes |
| [`ssl_key_passphrase`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |

Also see [Common options](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-common-options) for a list of options supported by all input plugins.

### `congestion_threshold` [v3.1.4-plugins-inputs-lumberjack-congestion_threshold]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

The number of seconds before we raise a timeout, this option is useful to control how much time to wait if something is blocking the pipeline.

### `host` [v3.1.4-plugins-inputs-lumberjack-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The IP address to listen on.

### `port` [v3.1.4-plugins-inputs-lumberjack-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

The port to listen on.

### `ssl_certificate` [v3.1.4-plugins-inputs-lumberjack-ssl_certificate]

* This is a required setting.
* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use.

### `ssl_key` [v3.1.4-plugins-inputs-lumberjack-ssl_key]

* This is a required setting.
* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key to use.

### `ssl_key_passphrase` [v3.1.4-plugins-inputs-lumberjack-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

SSL key passphrase to use.

## Common options [v3.1.4-plugins-inputs-lumberjack-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-1-4-plugins-inputs-lumberjack.md#v3.1.4-plugins-inputs-lumberjack-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.1.4-plugins-inputs-lumberjack-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.1.4-plugins-inputs-lumberjack-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.4-plugins-inputs-lumberjack-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.4-plugins-inputs-lumberjack-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 lumberjack inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  lumberjack {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.1.4-plugins-inputs-lumberjack-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.1.4-plugins-inputs-lumberjack-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
