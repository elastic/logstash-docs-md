---
navigation_title: "v1.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.5-plugins-inputs-dead_letter_queue.html
---

# Dead_letter_queue input plugin v1.0.5 [v1.0.5-plugins-inputs-dead_letter_queue]


* Plugin version: v1.0.5
* Released on: 2017-07-12
* [Changelog](https://github.com/logstash-plugins/logstash-input-dead_letter_queue/blob/v1.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-dead_letter_queue-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_295]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-dead_letter_queue). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_295]

Logstash input to read events from Logstash’s dead letter queue.

```sh
input {
  dead_letter_queue {
    path => "/var/logstash/data/dead_letter_queue"
    start_timestamp => "2017-04-04T23:40:37"
  }
}
```


## Dead_letter_queue Input Configuration Options [v1.0.5-plugins-inputs-dead_letter_queue-options]

This plugin supports the following configuration options plus the [Common options](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`commit_offsets`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-commit_offsets) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`path`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-path) | a valid filesystem path | Yes |
| [`pipeline_id`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-pipeline_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sincedb_path`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-sincedb_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`start_timestamp`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-start_timestamp) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-common-options) for a list of options supported by all input plugins.

 

### `commit_offsets` [v1.0.5-plugins-inputs-dead_letter_queue-commit_offsets]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Specifies whether this input should commit offsets as it processes the events. Typically you specify `false` when you want to iterate multiple times over the events in the dead letter queue, but don’t want to save state. This is when you are exploring the events in the dead letter queue.


### `path` [v1.0.5-plugins-inputs-dead_letter_queue-path]

* This is a required setting.
* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to the dead letter queue directory that was created by a Logstash instance. This is the path from which "dead" events are read and is typically configured in the original Logstash instance with the setting `path.dead_letter_queue`.


### `pipeline_id` [v1.0.5-plugins-inputs-dead_letter_queue-pipeline_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"main"`

ID of the pipeline whose events you want to read from.


### `sincedb_path` [v1.0.5-plugins-inputs-dead_letter_queue-sincedb_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path of the sincedb database file (keeps track of the current position of dead letter queue) that will be written to disk. The default will write sincedb files to `<path.data>/plugins/inputs/dead_letter_queue`.

::::{note}
This value must be a file path and not a directory path.
::::



### `start_timestamp` [v1.0.5-plugins-inputs-dead_letter_queue-start_timestamp]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Timestamp in ISO8601 format from when you want to start processing the events from. For example, `2017-04-04T23:40:37`.



## Common options [v1.0.5-plugins-inputs-dead_letter_queue-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v1-0-5-plugins-inputs-dead_letter_queue.md#v1.0.5-plugins-inputs-dead_letter_queue-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v1.0.5-plugins-inputs-dead_letter_queue-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v1.0.5-plugins-inputs-dead_letter_queue-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v1.0.5-plugins-inputs-dead_letter_queue-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.5-plugins-inputs-dead_letter_queue-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 dead_letter_queue inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  dead_letter_queue {
    id => "my_plugin_id"
  }
}
```


### `tags` [v1.0.5-plugins-inputs-dead_letter_queue-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v1.0.5-plugins-inputs-dead_letter_queue-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



