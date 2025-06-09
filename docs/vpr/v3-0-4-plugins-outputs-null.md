---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-outputs-null.html
---

# Null output plugin v3.0.4 [v3.0.4-plugins-outputs-null]

* Plugin version: v3.0.4
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-null/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](output-null-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1472]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-null). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1462]

A null output. This is useful for testing logstash inputs and filters for performance.

## Null Output Configuration Options [v3.0.4-plugins-outputs-null-options]

There are no special configuration options for this plugin, but it does support the [Common options](v3-0-4-plugins-outputs-null.md#v3.0.4-plugins-outputs-null-common-options).

## Common options [v3.0.4-plugins-outputs-null-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-4-plugins-outputs-null.md#v3.0.4-plugins-outputs-null-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-outputs-null.md#v3.0.4-plugins-outputs-null-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-4-plugins-outputs-null.md#v3.0.4-plugins-outputs-null-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.4-plugins-outputs-null-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.4-plugins-outputs-null-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.4-plugins-outputs-null-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 null outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  null {
    id => "my_plugin_id"
  }
}
```
