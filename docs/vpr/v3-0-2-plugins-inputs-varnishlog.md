---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-inputs-varnishlog.html
---

# Varnishlog input plugin v3.0.2 [v3.0.2-plugins-inputs-varnishlog]

* Plugin version: v3.0.2
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-input-varnishlog/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-varnishlog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1033]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-varnishlog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1026]

Read from varnish cache’s shared memory log

## Varnishlog Input Configuration Options [v3.0.2-plugins-inputs-varnishlog-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`threads`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-threads) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-common-options) for a list of options supported by all input plugins.

### `threads` [v3.0.2-plugins-inputs-varnishlog-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

## Common options [v3.0.2-plugins-inputs-varnishlog-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-2-plugins-inputs-varnishlog.md#v3.0.2-plugins-inputs-varnishlog-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.2-plugins-inputs-varnishlog-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.2-plugins-inputs-varnishlog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.2-plugins-inputs-varnishlog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.2-plugins-inputs-varnishlog-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 varnishlog inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  varnishlog {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.2-plugins-inputs-varnishlog-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.2-plugins-inputs-varnishlog-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
