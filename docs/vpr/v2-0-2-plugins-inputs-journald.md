---
navigation_title: "v2.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.2-plugins-inputs-journald.html
---

# Journald input plugin v2.0.2 [v2.0.2-plugins-inputs-journald]

* Plugin version: v2.0.2
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-input-journald/blob/v2.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-journald-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_644]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-journald). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_638]

Pull events from a local systemd journal.

See requirements <https://github.com/ledbettj/systemd-journal>

## Journald Input Configuration Options [v2.0.2-plugins-inputs-journald-options]

This plugin supports the following configuration options plus the [Common options](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`filter`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-filter) | [hash](/lsr/value-types.md#hash) | No |
| [`flags`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-flags) | [string](/lsr/value-types.md#string), one of `[0, 1, 2, 4]` | No |
| [`lowercase`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-lowercase) | [boolean](/lsr/value-types.md#boolean) | No |
| [`path`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-path) | [string](/lsr/value-types.md#string) | No |
| [`seekto`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-seekto) | [string](/lsr/value-types.md#string), one of `["head", "tail"]` | No |
| [`sincedb_path`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-sincedb_path) | [string](/lsr/value-types.md#string) | No |
| [`sincedb_write_interval`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-sincedb_write_interval) | [number](/lsr/value-types.md#number) | No |
| [`thisboot`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-thisboot) | [boolean](/lsr/value-types.md#boolean) | No |
| [`threads`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-threads) | [number](/lsr/value-types.md#number) | No |
| [`wait_timeout`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-wait_timeout) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-common-options) for a list of options supported by all input plugins.

### `filter` [v2.0.2-plugins-inputs-journald-filter]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Filter on events. Not heavily tested.

### `flags` [v2.0.2-plugins-inputs-journald-flags]

* Value can be any of: `0`, `1`, `2`, `4`
* Default value is `0`

System journal flags 0 = all avalable 1 = local only 2 = runtime only 4 = system only

### `lowercase` [v2.0.2-plugins-inputs-journald-lowercase]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Lowercase annoying UPPERCASE fieldnames. (May clobber existing fields)

### `path` [v2.0.2-plugins-inputs-journald-path]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"/var/log/journal"`

Path to read journal files from

### `seekto` [v2.0.2-plugins-inputs-journald-seekto]

* Value can be any of: `head`, `tail`
* Default value is `"tail"`

Where in the journal to start capturing logs Options: head, tail

### `sincedb_path` [v2.0.2-plugins-inputs-journald-sincedb_path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Where to write the sincedb database (keeps track of the current position of the journal). The default will write the sincedb file to matching `$HOME/.sincedb_journal`

### `sincedb_write_interval` [v2.0.2-plugins-inputs-journald-sincedb_write_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `15`

How often (in seconds) to write a since database with the current position of the journal.

### `thisboot` [v2.0.2-plugins-inputs-journald-thisboot]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Filter logs since the system booted (only relevant with seekto ⇒ "head")

### `threads` [v2.0.2-plugins-inputs-journald-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

### `wait_timeout` [v2.0.2-plugins-inputs-journald-wait_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3000000`

The max timeout in microsends to wait for new events from the journal. Set to -1 to wait indefinitely. Setting this to a large value will result in delayed shutdown of the plugin.

## Common options [v2.0.2-plugins-inputs-journald-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v2-0-2-plugins-inputs-journald.md#v2.0.2-plugins-inputs-journald-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v2.0.2-plugins-inputs-journald-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v2.0.2-plugins-inputs-journald-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.0.2-plugins-inputs-journald-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.2-plugins-inputs-journald-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 journald inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  journald {
    id => "my_plugin_id"
  }
}
```

### `tags` [v2.0.2-plugins-inputs-journald-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v2.0.2-plugins-inputs-journald-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
