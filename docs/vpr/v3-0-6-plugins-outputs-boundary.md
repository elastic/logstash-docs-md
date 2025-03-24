---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-boundary.html
---

# Boundary output plugin v3.0.6 [v3.0.6-plugins-outputs-boundary]


* Plugin version: v3.0.6
* Released on: 2023-05-30
* [Changelog](https://github.com/logstash-plugins/logstash-output-boundary/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-boundary-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1019]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-boundary). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1012]

This output lets you send annotations to Boundary based on Logstash events

Note that since Logstash maintains no state these will be one-shot events

By default the start and stop time will be the event timestamp


## Boundary Output Configuration Options [v3.0.6-plugins-outputs-boundary-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`auto`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-auto) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`bsubtype`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-bsubtype) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`btags`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-btags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`btype`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-btype) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`end_time`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-end_time) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`org_id`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-org_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`start_time`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-start_time) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-common-options) for a list of options supported by all output plugins.

 

### `api_key` [v3.0.6-plugins-outputs-boundary-api_key]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Your Boundary API key


### `auto` [v3.0.6-plugins-outputs-boundary-auto]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Auto If set to true, logstash will try to pull boundary fields out of the event. Any field explicitly set by config options will override these. `['type', 'subtype', 'creation_time', 'end_time', 'links', 'tags', 'loc']`


### `bsubtype` [v3.0.6-plugins-outputs-boundary-bsubtype]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Sub-Type


### `btags` [v3.0.6-plugins-outputs-boundary-btags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Tags Set any custom tags for this event Default are the Logstash tags if any


### `btype` [v3.0.6-plugins-outputs-boundary-btype]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Type


### `end_time` [v3.0.6-plugins-outputs-boundary-end_time]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

End time Override the stop time Note that Boundary requires this to be seconds since epoch If overriding, it is your responsibility to type this correctly By default this is set to `event.get("@timestamp").to_i`


### `org_id` [v3.0.6-plugins-outputs-boundary-org_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Your Boundary Org ID


### `start_time` [v3.0.6-plugins-outputs-boundary-start_time]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Start time Override the start time Note that Boundary requires this to be seconds since epoch If overriding, it is your responsibility to type this correctly By default this is set to `event.get("@timestamp").to_i`



## Common options [v3.0.6-plugins-outputs-boundary-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-boundary.md#v3.0.6-plugins-outputs-boundary-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-boundary-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-outputs-boundary-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-outputs-boundary-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 boundary outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  boundary {
    id => "my_plugin_id"
  }
}
```



