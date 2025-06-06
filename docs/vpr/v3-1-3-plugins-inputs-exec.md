---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-inputs-exec.html
---

# Exec input plugin v3.1.3 [v3.1.3-plugins-inputs-exec]

* Plugin version: v3.1.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-exec/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](input-exec-index.md "Versioned exec input plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_380]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-exec). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_380]

Periodically run a shell command and capture the whole output as an event.

Notes:

* The `command` field of this event will be the command run.
* The `message` field of this event will be the entire stdout of the command.

### Exec Input Configuration Options [v3.1.3-plugins-inputs-exec-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`command`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-command "command") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`interval`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-interval "interval") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | Yes |

Also see [Common options](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-common-options "Common options") for a list of options supported by all input plugins.

 

#### `command` [v3.1.3-plugins-inputs-exec-command]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Command to run. For example, `uptime`

#### `interval` [v3.1.3-plugins-inputs-exec-interval]

* This is a required setting.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

Interval to run the command. Value is in seconds.

### Common options [v3.1.3-plugins-inputs-exec-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-add_field "add_field") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`codec`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`tags`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-tags "tags") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`type`](v3-1-3-plugins-inputs-exec.md#v3.1.3-plugins-inputs-exec-type "type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `add_field` [v3.1.3-plugins-inputs-exec-add_field]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* Default value is `{}`

Add a field to an event

#### `codec` [v3.1.3-plugins-inputs-exec-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v3.1.3-plugins-inputs-exec-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v3.1.3-plugins-inputs-exec-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 exec inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  exec {
    id => "my_plugin_id"
  }
}
```

#### `tags` [v3.1.3-plugins-inputs-exec-tags]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

#### `type` [v3.1.3-plugins-inputs-exec-type]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
