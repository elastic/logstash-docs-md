---
navigation_title: "v1.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.3-plugins-outputs-monasca_log_api.html
---

# Monasca_log_api output plugin v1.0.3 [v1.0.3-plugins-outputs-monasca_log_api]

* Plugin version: v1.0.3
* Released on: 2018-11-20
* [Changelog](https://github.com/logstash-plugins/logstash-output-monasca_log_api/blob/v1.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-monasca_log_api-index.md "Versioned monasca_log_api output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1451]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-monasca_log_api). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1441]

relative requirements This Logstash Output plugin, sends events to monasca-api. It authenticates against keystone and gets a token. The token is used to authenticate against the monasca-api and send log events.

### Monasca_log_api Output Configuration Options [v1.0.3-plugins-outputs-monasca_log_api-options]

This plugin supports the following configuration options plus the [Common options](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`delay`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-delay "delay") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`dimensions`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-dimensions "dimensions") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`elapsed_time_sec`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-elapsed_time_sec "elapsed_time_sec") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`keystone_api_insecure`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-keystone_api_insecure "keystone_api_insecure") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`keystone_api_url`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-keystone_api_url "keystone_api_url") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`max_data_size_kb`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-max_data_size_kb "max_data_size_kb") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`monasca_log_api_insecure`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-monasca_log_api_insecure "monasca_log_api_insecure") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`monasca_log_api_url`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-monasca_log_api_url "monasca_log_api_url") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`num_of_logs`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-num_of_logs "num_of_logs") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`password`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-password "password") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`project_domain_name`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-project_domain_name "project_domain_name") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`project_name`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-project_name "project_name") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`user_domain_name`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-user_domain_name "user_domain_name") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`username`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-username "username") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |

Also see [Common options](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-common-options "Common options") for a list of options supported by all output plugins.

 

#### `delay` [v1.0.3-plugins-outputs-monasca_log_api-delay]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `10`

#### `dimensions` [v1.0.3-plugins-outputs-monasca_log_api-dimensions]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* There is no default value for this setting.

global dimensions

#### `elapsed_time_sec` [v1.0.3-plugins-outputs-monasca_log_api-elapsed_time_sec]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `30`

#### `keystone_api_insecure` [v1.0.3-plugins-outputs-monasca_log_api-keystone_api_insecure]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

#### `keystone_api_url` [v1.0.3-plugins-outputs-monasca_log_api-keystone_api_url]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

keystone configuration

#### `max_data_size_kb` [v1.0.3-plugins-outputs-monasca_log_api-max_data_size_kb]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `5120`

#### `monasca_log_api_insecure` [v1.0.3-plugins-outputs-monasca_log_api-monasca_log_api_insecure]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

#### `monasca_log_api_url` [v1.0.3-plugins-outputs-monasca_log_api-monasca_log_api_url]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

monasca-log-api configuration

#### `num_of_logs` [v1.0.3-plugins-outputs-monasca_log_api-num_of_logs]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `125`

#### `password` [v1.0.3-plugins-outputs-monasca_log_api-password]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

#### `project_domain_name` [v1.0.3-plugins-outputs-monasca_log_api-project_domain_name]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

#### `project_name` [v1.0.3-plugins-outputs-monasca_log_api-project_name]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

#### `user_domain_name` [v1.0.3-plugins-outputs-monasca_log_api-user_domain_name]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

#### `username` [v1.0.3-plugins-outputs-monasca_log_api-username]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

### Common options [v1.0.3-plugins-outputs-monasca_log_api-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v1-0-3-plugins-outputs-monasca_log_api.md#v1.0.3-plugins-outputs-monasca_log_api-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v1.0.3-plugins-outputs-monasca_log_api-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v1.0.3-plugins-outputs-monasca_log_api-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v1.0.3-plugins-outputs-monasca_log_api-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 monasca\_log\_api outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  monasca_log_api {
    id => "my_plugin_id"
  }
}
```
