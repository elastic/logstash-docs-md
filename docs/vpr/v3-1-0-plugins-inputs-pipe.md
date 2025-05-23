---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-inputs-pipe.html
---

# Pipe input plugin v3.1.0 [v3.1.0-plugins-inputs-pipe]


* Plugin version: v3.1.0
* Released on: 2021-11-18
* [Changelog](https://github.com/logstash-plugins/logstash-input-pipe/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](input-pipe-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_727]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-pipe). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_720]

Stream events from a long running command pipe.

By default, each event is assumed to be one line. If you want to join lines, you’ll want to use the multiline codec.


## Compatibility with the Elastic Common Schema (ECS) [v3.1.0-plugins-inputs-pipe-ecs]

This plugin adds extra fields about the event’s source. Configure the [`ecs_compatibility`\]\(([^:]+)://reference/index.md).

These fields are added after the event has been decoded by the appropriate codec, and will not overwrite existing values.

| ECS Disabled | ECS v1 , v8 | Description |
| --- | --- | --- |
| `host` | `[host][name]` | The name of the {{ls}} host that processed the event |
| `command` | `[process][command_line]` | The command run by the plugin |


## Pipe Input Configuration Options [v3.1.0-plugins-inputs-pipe-options]

This plugin supports the following configuration options plus the [Common options](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`command`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-command) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`ecs_compatibility`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-common-options) for a list of options supported by all input plugins.

 

### `command` [v3.1.0-plugins-inputs-pipe-command]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Command to run and read events from, one line at a time.

Example:

```ruby
input {
  pipe {
    command => "echo ¡Hola!"
  }
}
```


### `ecs_compatibility` [v3.1.0-plugins-inputs-pipe-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: uses backwards compatible field names, such as `[host]`
    * `v1`, `v8`: uses fields that are compatible with ECS, such as `[host][name]`


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). See [Compatibility with the Elastic Common Schema (ECS)](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-ecs) for detailed information.

**Sample output: ECS enabled**

```ruby
{
    "@timestamp"=>2021-11-16T09:18:45.306Z,
    "message" => "¡Hola!",
    "process" => {
        "command_line" => "echo '¡Hola!'"
    },
    "host" => {
        "name" => "deus-ex-machina"
    }
}
```

**Sample output: ECS disabled**

```ruby
{
    "@timestamp"=>2021-11-16T09:18:45.306Z,
    "message" => "¡Hola!",
    "command" => "echo '¡Hola!'",
    "host" => "deus-ex-machina"
}
```



## Common options [v3.1.0-plugins-inputs-pipe-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-1-0-plugins-inputs-pipe.md#v3.1.0-plugins-inputs-pipe-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.1.0-plugins-inputs-pipe-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.1.0-plugins-inputs-pipe-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.0-plugins-inputs-pipe-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.0-plugins-inputs-pipe-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 pipe inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  pipe {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.1.0-plugins-inputs-pipe-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.1.0-plugins-inputs-pipe-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
