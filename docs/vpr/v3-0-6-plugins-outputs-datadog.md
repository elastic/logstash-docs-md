---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-datadog.html
---

# Datadog output plugin v3.0.6 [v3.0.6-plugins-outputs-datadog]


* Plugin version: v3.0.6
* Released on: 2023-05-31
* [Changelog](https://github.com/logstash-plugins/logstash-output-datadog/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-datadog-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1055]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-datadog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1048]

This output sends events to DataDogHQ based on Logstash events.

Note that since Logstash maintains no state these will be one-shot events


## Datadog Output Configuration Options [v3.0.6-plugins-outputs-datadog-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`alert_type`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-alert_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["info", "error", "warning", "success"]` | No |
| [`api_key`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`date_happened`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-date_happened) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`dd_tags`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-dd_tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`priority`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-priority) | [string](logstash://reference/configuration-file-structure.md#string), one of `["normal", "low"]` | No |
| [`source_type_name`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-source_type_name) | [string](logstash://reference/configuration-file-structure.md#string), one of `["nagios", "hudson", "jenkins", "user", "my apps", "feed", "chef", "puppet", "git", "bitbucket", "fabric", "capistrano"]` | No |
| [`text`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-text) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`title`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-title) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-common-options) for a list of options supported by all output plugins.

 

### `alert_type` [v3.0.6-plugins-outputs-datadog-alert_type]

* Value can be any of: `info`, `error`, `warning`, `success`
* There is no default value for this setting.

Alert type


### `api_key` [v3.0.6-plugins-outputs-datadog-api_key]

* This is a required setting.
* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Your DatadogHQ API key


### `date_happened` [v3.0.6-plugins-outputs-datadog-date_happened]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Date Happened


### `dd_tags` [v3.0.6-plugins-outputs-datadog-dd_tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Tags Set any custom tags for this event Default are the Logstash tags if any


### `priority` [v3.0.6-plugins-outputs-datadog-priority]

* Value can be any of: `normal`, `low`
* There is no default value for this setting.

Priority


### `source_type_name` [v3.0.6-plugins-outputs-datadog-source_type_name]

* Value can be any of: `nagios`, `hudson`, `jenkins`, `user`, `my apps`, `feed`, `chef`, `puppet`, `git`, `bitbucket`, `fabric`, `capistrano`
* Default value is `"my apps"`

Source type name


### `text` [v3.0.6-plugins-outputs-datadog-text]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

Text


### `title` [v3.0.6-plugins-outputs-datadog-title]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash event for %{{host}}"`

Title



## Common options [v3.0.6-plugins-outputs-datadog-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-datadog.md#v3.0.6-plugins-outputs-datadog-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-datadog-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-outputs-datadog-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-outputs-datadog-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 datadog outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  datadog {
    id => "my_plugin_id"
  }
}
```



