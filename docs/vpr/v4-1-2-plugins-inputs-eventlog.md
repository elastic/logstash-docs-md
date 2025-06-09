---
navigation_title: "v4.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.1.2-plugins-inputs-eventlog.html
---

# Eventlog [v4.1.2-plugins-inputs-eventlog]

* Plugin version: v4.1.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-eventlog/blob/v4.1.2/CHANGELOG.md)

For other versions, see the [overview list](input-eventlog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_371]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-eventlog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_371]

This input will pull events from a [Windows Event Log](http://msdn.microsoft.com/en-us/library/windows/desktop/bb309026%28v=vs.85%29.aspx). Note that Windows Event Logs are stored on disk in a binary format and are only accessible from the Win32 API. This means Losgtash needs to be running as an agent on Windows servers where you wish to collect logs from, and will not be accesible across the network.

To collect Events from the System Event Log, use a config like:

```
    input {
      eventlog {
        type  => 'Win32-EventLog'
        logfile  => 'System'
      }
    }
```

## Eventlog Input Configuration Options [v4.1.2-plugins-inputs-eventlog-options]

This plugin supports the following configuration options plus the [Common options](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`interval`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-interval) | [number](/lsr/value-types.md#number) | No |
| [`logfile`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-logfile) | [string](/lsr/value-types.md#string), one of `["Application", "Security", "System"]` | No |

Also see [Common options](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-common-options) for a list of options supported by all input plugins.

### `interval` [v4.1.2-plugins-inputs-eventlog-interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1000`

How frequently should tail check for new event logs in ms (default: 1 second)

### `logfile` [v4.1.2-plugins-inputs-eventlog-logfile]

* Value can be any of: `Application`, `Security`, `System`
* Default value is `"Application"`

Event Log Name System and Security may require that privileges are given to the user running logstash. see more at: <https://social.technet.microsoft.com/forums/windowsserver/en-US/d2f813db-6142-4b5b-8d86-253ebb740473/easy-way-to-read-security-log>

## Common options [v4.1.2-plugins-inputs-eventlog-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v4-1-2-plugins-inputs-eventlog.md#v4.1.2-plugins-inputs-eventlog-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v4.1.2-plugins-inputs-eventlog-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v4.1.2-plugins-inputs-eventlog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.1.2-plugins-inputs-eventlog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.1.2-plugins-inputs-eventlog-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 eventlog inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  eventlog {
    id => "my_plugin_id"
  }
}
```

### `tags` [v4.1.2-plugins-inputs-eventlog-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v4.1.2-plugins-inputs-eventlog-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
