---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-inputs-rackspace.html
---

# Rackspace input plugin v3.0.5 [v3.0.5-plugins-inputs-rackspace]


* Plugin version: v3.0.5
* Released on: 2023-05-30
* [Changelog](https://github.com/logstash-plugins/logstash-input-rackspace/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-rackspace-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_755]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-rackspace). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_748]

Receives events from a Rackspace Cloud Queue service.


## Rackspace Input Configuration Options [v3.0.5-plugins-inputs-rackspace-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`claim`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-claim) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`queue`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-queue) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`region`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-region) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ttl`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`username`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-username) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-common-options) for a list of options supported by all input plugins.

 

### `api_key` [v3.0.5-plugins-inputs-rackspace-api_key]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Rackspace Cloud API Key


### `claim` [v3.0.5-plugins-inputs-rackspace-claim]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

number of messages to claim Min: 1, Max: 10


### `queue` [v3.0.5-plugins-inputs-rackspace-queue]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

Rackspace Queue Name


### `region` [v3.0.5-plugins-inputs-rackspace-region]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"dfw"`

Rackspace region `ord, dfw, lon, syd,` etc


### `ttl` [v3.0.5-plugins-inputs-rackspace-ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

length of time to hold claim Min: 60


### `username` [v3.0.5-plugins-inputs-rackspace-username]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Rackspace Cloud Username



## Common options [v3.0.5-plugins-inputs-rackspace-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-5-plugins-inputs-rackspace.md#v3.0.5-plugins-inputs-rackspace-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.5-plugins-inputs-rackspace-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.5-plugins-inputs-rackspace-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.5-plugins-inputs-rackspace-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.5-plugins-inputs-rackspace-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 rackspace inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  rackspace {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.5-plugins-inputs-rackspace-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.5-plugins-inputs-rackspace-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



