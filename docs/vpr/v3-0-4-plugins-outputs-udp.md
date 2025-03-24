---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-outputs-udp.html
---

# Udp output plugin v3.0.4 [v3.0.4-plugins-outputs-udp]


* Plugin version: v3.0.4
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-udp/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](output-udp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1650]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-udp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1640]

Send events over UDP

Keep in mind that UDP will lose messages.


## Udp Output Configuration Options [v3.0.4-plugins-outputs-udp-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`port`](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |

Also see [Common options](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-common-options) for a list of options supported by all output plugins.

 

### `host` [v3.0.4-plugins-outputs-udp-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The address to send messages to


### `port` [v3.0.4-plugins-outputs-udp-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The port to send messages on



## Common options [v3.0.4-plugins-outputs-udp-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-4-plugins-outputs-udp.md#v3.0.4-plugins-outputs-udp-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.4-plugins-outputs-udp-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.4-plugins-outputs-udp-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.4-plugins-outputs-udp-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 udp outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  udp {
    id => "my_plugin_id"
  }
}
```



