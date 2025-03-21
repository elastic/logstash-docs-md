---
navigation_title: "v3.3.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.1-plugins-inputs-exec.html
---

# Exec input plugin v3.3.1 [v3.3.1-plugins-inputs-exec]


* Plugin version: v3.3.1
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-exec/blob/v3.3.1/CHANGELOG.md)

For other versions, see the [overview list](input-exec-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_362]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-exec). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_362]

Periodically run a shell command and capture the whole output as an event.

Notes:

* The `command` field of this event will be the command run.
* The `message` field of this event will be the entire stdout of the command.

Example:

```ruby
input {
  exec {
    command => "ls"
    interval => 30
  }
}
```

This will execute `ls` command every 30 seconds.


## Exec Input Configuration Options [v3.3.1-plugins-inputs-exec-options]

This plugin supports the following configuration options plus the [Common options](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`command`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-command) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`interval`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`schedule`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-schedule) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-common-options) for a list of options supported by all input plugins.

 

### `command` [v3.3.1-plugins-inputs-exec-command]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Command to run. For example, `uptime`


### `interval` [v3.3.1-plugins-inputs-exec-interval]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Interval to run the command. Value is in seconds.

Either `interval` or `schedule` option must be defined.


### `schedule` [v3.3.1-plugins-inputs-exec-schedule]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Schedule of when to periodically run command.

This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support).

Examples:

|     |     |
| --- | --- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).

Either `interval` or `schedule` option must be defined.



## Common options [v3.3.1-plugins-inputs-exec-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-3-1-plugins-inputs-exec.md#v3.3.1-plugins-inputs-exec-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.3.1-plugins-inputs-exec-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.3.1-plugins-inputs-exec-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.3.1-plugins-inputs-exec-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.3.1-plugins-inputs-exec-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 exec inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  exec {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.3.1-plugins-inputs-exec-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.3.1-plugins-inputs-exec-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



