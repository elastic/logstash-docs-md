---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-outputs-datadog.html
---

# Datadog output plugin v3.0.5 [v3.0.5-plugins-outputs-datadog]

* Plugin version: v3.0.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-datadog/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-datadog-index.md "Versioned datadog output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1091]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-datadog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1084]

This output sends events to DataDogHQ based on Logstash events.

Note that since Logstash maintains no state these will be one-shot events

### Datadog Output Configuration Options [v3.0.5-plugins-outputs-datadog-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`alert_type`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-alert_type "alert_type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["info", "error", "warning", "success"]` | No |
| [`api_key`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-api_key "api_key") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`date_happened`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-date_happened "date_happened") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`dd_tags`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-dd_tags "dd_tags") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`priority`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-priority "priority") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["normal", "low"]` | No |
| [`source_type_name`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-source_type_name "source_type_name") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string), one of `["nagios", "hudson", "jenkins", "user", "my apps", "feed", "chef", "puppet", "git", "bitbucket", "fabric", "capistrano"]` | No |
| [`text`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-text "text") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`title`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-title "title") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

Also see [Common options](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-common-options "Common options") for a list of options supported by all output plugins.

 

#### `alert_type` [v3.0.5-plugins-outputs-datadog-alert_type]

* Value can be any of: `info`, `error`, `warning`, `success`
* There is no default value for this setting.

Alert type

#### `api_key` [v3.0.5-plugins-outputs-datadog-api_key]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Your DatadogHQ API key

#### `date_happened` [v3.0.5-plugins-outputs-datadog-date_happened]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Date Happened

#### `dd_tags` [v3.0.5-plugins-outputs-datadog-dd_tags]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* There is no default value for this setting.

Tags Set any custom tags for this event Default are the Logstash tags if any

#### `priority` [v3.0.5-plugins-outputs-datadog-priority]

* Value can be any of: `normal`, `low`
* There is no default value for this setting.

Priority

#### `source_type_name` [v3.0.5-plugins-outputs-datadog-source_type_name]

* Value can be any of: `nagios`, `hudson`, `jenkins`, `user`, `my apps`, `feed`, `chef`, `puppet`, `git`, `bitbucket`, `fabric`, `capistrano`
* Default value is `"my apps"`

Source type name

#### `text` [v3.0.5-plugins-outputs-datadog-text]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"%{message}"`

Text

#### `title` [v3.0.5-plugins-outputs-datadog-title]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"Logstash event for %{host}"`

Title

### Common options [v3.0.5-plugins-outputs-datadog-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v3-0-5-plugins-outputs-datadog.md#v3.0.5-plugins-outputs-datadog-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v3.0.5-plugins-outputs-datadog-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v3.0.5-plugins-outputs-datadog-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v3.0.5-plugins-outputs-datadog-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 datadog outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  datadog {
    id => "my_plugin_id"
  }
}
```
