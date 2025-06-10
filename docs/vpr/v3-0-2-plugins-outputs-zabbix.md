---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-outputs-zabbix.html
---

# Zabbix output plugin v3.0.2 [v3.0.2-plugins-outputs-zabbix]

* Plugin version: v3.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-zabbix/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](output-zabbix-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1690]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-zabbix). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1680]

The Zabbix output is used to send item data (key/value pairs) to a Zabbix server. The event `@timestamp` will automatically be associated with the Zabbix item data.

The Zabbix Sender protocol is described at <https://www.zabbix.org/wiki/Docs/protocols/zabbix_sender/2.0> Zabbix uses a kind of nested key/value store.

```
    host
      ├── item1
      │     └── value1
      ├── item2
      │     └── value2
      ├── ...
      │     └── ...
      ├── item_n
      │     └── value_n
```

Each "host" is an identifier, and each item is associated with that host. Items are typed on the Zabbix side. You can send numbers as strings and Zabbix will Do The Right Thing.

In the Zabbix UI, ensure that your hostname matches the value referenced by `zabbix_host`. Create the item with the key as it appears in the field referenced by `zabbix_key`. In the item configuration window, ensure that the type dropdown is set to Zabbix Trapper. Also be sure to set the type of information that Zabbix should expect for this item.

This plugin does not currently send in batches. While it is possible to do so, this is not supported. Be careful not to flood your Zabbix server with too many events per second.

This plugin will log a warning if a necessary field is missing. It will not attempt to resend if Zabbix is down, but will log an error message.

## Zabbix Output Configuration Options [v3.0.2-plugins-outputs-zabbix-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`multi_value`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-multi_value) | [array](/lsr/value-types.md#array) | No |
| [`timeout`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-timeout) | [number](/lsr/value-types.md#number) | No |
| [`zabbix_host`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-zabbix_host) | [string](/lsr/value-types.md#string) | Yes |
| [`zabbix_key`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-zabbix_key) | [string](/lsr/value-types.md#string) | No |
| [`zabbix_server_host`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-zabbix_server_host) | [string](/lsr/value-types.md#string) | No |
| [`zabbix_server_port`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-zabbix_server_port) | [number](/lsr/value-types.md#number) | No |
| [`zabbix_value`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-zabbix_value) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-common-options) for a list of options supported by all output plugins.

### `multi_value` [v3.0.2-plugins-outputs-zabbix-multi_value]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Use the `multi_value` directive to send multiple key/value pairs. This can be thought of as an array, like:

`[ zabbix_key1, zabbix_value1, zabbix_key2, zabbix_value2, ... zabbix_keyN, zabbix_valueN ]`

…where `zabbix_key1` is an instance of `zabbix_key`, and `zabbix_value1` is an instance of `zabbix_value`. If the field referenced by any `zabbix_key` or `zabbix_value` does not exist, that entry will be ignored.

This directive cannot be used in conjunction with the single-value directives `zabbix_key` and `zabbix_value`.

### `timeout` [v3.0.2-plugins-outputs-zabbix-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

The number of seconds to wait before giving up on a connection to the Zabbix server. This number should be very small, otherwise delays in delivery of other outputs could result.

### `zabbix_host` [v3.0.2-plugins-outputs-zabbix-zabbix_host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field name which holds the Zabbix host name. This can be a sub-field of the @metadata field.

### `zabbix_key` [v3.0.2-plugins-outputs-zabbix-zabbix_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A single field name which holds the value you intend to use as the Zabbix item key. This can be a sub-field of the @metadata field. This directive will be ignored if using `multi_value`

`zabbix_key` is required if not using `multi_value`.

### `zabbix_server_host` [v3.0.2-plugins-outputs-zabbix-zabbix_server_host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

The IP or resolvable hostname where the Zabbix server is running

### `zabbix_server_port` [v3.0.2-plugins-outputs-zabbix-zabbix_server_port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10051`

The port on which the Zabbix server is running

### `zabbix_value` [v3.0.2-plugins-outputs-zabbix-zabbix_value]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The field name which holds the value you want to send. This directive will be ignored if using `multi_value`

## Common options [v3.0.2-plugins-outputs-zabbix-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-2-plugins-outputs-zabbix.md#v3.0.2-plugins-outputs-zabbix-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.2-plugins-outputs-zabbix-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.2-plugins-outputs-zabbix-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.2-plugins-outputs-zabbix-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 zabbix outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  zabbix {
    id => "my_plugin_id"
  }
}
```
