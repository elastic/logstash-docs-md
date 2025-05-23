---
navigation_title: "v2.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.7-plugins-outputs-rackspace.html
---

# Rackspace output plugin v2.0.7 [v2.0.7-plugins-outputs-rackspace]


* Plugin version: v2.0.7
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-rackspace/blob/v2.0.7/CHANGELOG.md)

For other versions, see the [overview list](output-rackspace-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1502]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-rackspace). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1492]

Sends events to a Rackspace Cloud Queue service.


## Rackspace Output Configuration Options [v2.0.7-plugins-outputs-rackspace-options]

This plugin supports the following configuration options plus the [Common options](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-api_key) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`queue`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-queue) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`region`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-region) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ttl`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`username`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-username) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-common-options) for a list of options supported by all output plugins.

 

### `api_key` [v2.0.7-plugins-outputs-rackspace-api_key]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Rackspace Cloud API Key


### `queue` [v2.0.7-plugins-outputs-rackspace-queue]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

Rackspace Queue Name


### `region` [v2.0.7-plugins-outputs-rackspace-region]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"dfw"`

Rackspace region ord, dfw, lon, syd, etc


### `ttl` [v2.0.7-plugins-outputs-rackspace-ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `360`

time for item to live in queue


### `username` [v2.0.7-plugins-outputs-rackspace-username]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Rackspace Cloud Username



## Common options [v2.0.7-plugins-outputs-rackspace-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-7-plugins-outputs-rackspace.md#v2.0.7-plugins-outputs-rackspace-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v2.0.7-plugins-outputs-rackspace-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.7-plugins-outputs-rackspace-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.7-plugins-outputs-rackspace-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 rackspace outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  rackspace {
    id => "my_plugin_id"
  }
}
```



