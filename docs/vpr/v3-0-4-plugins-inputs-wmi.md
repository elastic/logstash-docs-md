---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-inputs-wmi.html
---

# Wmi input plugin v3.0.4 [v3.0.4-plugins-inputs-wmi]

* Plugin version: v3.0.4
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-wmi/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](input-wmi-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1039]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-wmi). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1032]

Collect data from WMI query

This is useful for collecting performance metrics and other data which is accessible via WMI on a Windows host

Example:

```
    input {
      wmi {
        query => "select * from Win32_Process"
        interval => 10
      }
      wmi {
        query => "select PercentProcessorTime from Win32_PerfFormattedData_PerfOS_Processor where name = '_Total'"
      }
      wmi { # Connect to a remote host
        query => "select * from Win32_Process"
        host => "MyRemoteHost"
        user => "mydomain\myuser"
        password => "Password"
      }
    }
```

## Wmi Input Configuration Options [v3.0.4-plugins-inputs-wmi-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`host`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-host) | [string](/lsr/value-types.md#string) | No |
| [`interval`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-interval) | [number](/lsr/value-types.md#number) | No |
| [`namespace`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-namespace) | [string](/lsr/value-types.md#string) | No |
| [`password`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-password) | [password](/lsr/value-types.md#password) | No |
| [`query`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-query) | [string](/lsr/value-types.md#string) | Yes |
| [`user`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-user) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-common-options) for a list of options supported by all input plugins.

### `host` [v3.0.4-plugins-inputs-wmi-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost"`

Host to connect to ( Defaults to localhost )

### `interval` [v3.0.4-plugins-inputs-wmi-interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Polling interval

### `namespace` [v3.0.4-plugins-inputs-wmi-namespace]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"root\cimv2"`

Namespace when doing remote connections

### `password` [v3.0.4-plugins-inputs-wmi-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password when doing remote connections

### `query` [v3.0.4-plugins-inputs-wmi-query]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

WMI query

### `user` [v3.0.4-plugins-inputs-wmi-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username when doing remote connections

## Common options [v3.0.4-plugins-inputs-wmi-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-4-plugins-inputs-wmi.md#v3.0.4-plugins-inputs-wmi-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.4-plugins-inputs-wmi-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.4-plugins-inputs-wmi-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.4-plugins-inputs-wmi-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.4-plugins-inputs-wmi-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 wmi inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  wmi {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.4-plugins-inputs-wmi-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.4-plugins-inputs-wmi-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
