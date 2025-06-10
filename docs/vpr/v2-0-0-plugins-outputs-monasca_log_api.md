---
navigation_title: "v2.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.0-plugins-outputs-monasca_log_api.html
---

# Monasca_log_api output plugin v2.0.0 [v2.0.0-plugins-outputs-monasca_log_api]

* Plugin version: v2.0.0
* Released on: 2019-08-28
* [Changelog](https://github.com/logstash-plugins/logstash-output-monasca_log_api/blob/v2.0.0/CHANGELOG.md)

For other versions, see the [overview list](output-monasca_log_api-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1451]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-monasca_log_api). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1441]

relative requirements This Logstash Output plugin, sends events to monasca-api. It authenticates against keystone and gets a token. The token is used to authenticate against the monasca-api and send log events.

## Monasca_log_api Output Configuration Options [v2.0.0-plugins-outputs-monasca_log_api-options]

This plugin supports the following configuration options plus the [Common options](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`delay`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-delay) | [number](/lsr/value-types.md#number) | No |
| [`dimensions`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-dimensions) | [array](/lsr/value-types.md#array) | No |
| [`elapsed_time_sec`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-elapsed_time_sec) | [number](/lsr/value-types.md#number) | No |
| [`keystone_api_insecure`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-keystone_api_insecure) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keystone_api_url`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-keystone_api_url) | [string](/lsr/value-types.md#string) | Yes |
| [`max_data_size_kb`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-max_data_size_kb) | [number](/lsr/value-types.md#number) | No |
| [`monasca_log_api_insecure`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-monasca_log_api_insecure) | [boolean](/lsr/value-types.md#boolean) | No |
| [`monasca_log_api_url`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-monasca_log_api_url) | [string](/lsr/value-types.md#string) | Yes |
| [`num_of_logs`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-num_of_logs) | [number](/lsr/value-types.md#number) | No |
| [`password`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-password) | [string](/lsr/value-types.md#string) | Yes |
| [`project_domain_name`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-project_domain_name) | [string](/lsr/value-types.md#string) | Yes |
| [`project_name`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-project_name) | [string](/lsr/value-types.md#string) | Yes |
| [`user_domain_name`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-user_domain_name) | [string](/lsr/value-types.md#string) | Yes |
| [`username`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-username) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-common-options) for a list of options supported by all output plugins.

### `delay` [v2.0.0-plugins-outputs-monasca_log_api-delay]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

### `dimensions` [v2.0.0-plugins-outputs-monasca_log_api-dimensions]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

global dimensions

### `elapsed_time_sec` [v2.0.0-plugins-outputs-monasca_log_api-elapsed_time_sec]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `30`

### `keystone_api_insecure` [v2.0.0-plugins-outputs-monasca_log_api-keystone_api_insecure]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

### `keystone_api_url` [v2.0.0-plugins-outputs-monasca_log_api-keystone_api_url]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

keystone configuration

### `max_data_size_kb` [v2.0.0-plugins-outputs-monasca_log_api-max_data_size_kb]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5120`

### `monasca_log_api_insecure` [v2.0.0-plugins-outputs-monasca_log_api-monasca_log_api_insecure]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

### `monasca_log_api_url` [v2.0.0-plugins-outputs-monasca_log_api-monasca_log_api_url]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

monasca-log-api configuration

### `num_of_logs` [v2.0.0-plugins-outputs-monasca_log_api-num_of_logs]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `125`

### `password` [v2.0.0-plugins-outputs-monasca_log_api-password]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `project_domain_name` [v2.0.0-plugins-outputs-monasca_log_api-project_domain_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `project_name` [v2.0.0-plugins-outputs-monasca_log_api-project_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `user_domain_name` [v2.0.0-plugins-outputs-monasca_log_api-user_domain_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `username` [v2.0.0-plugins-outputs-monasca_log_api-username]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

## Common options [v2.0.0-plugins-outputs-monasca_log_api-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-0-plugins-outputs-monasca_log_api.md#v2.0.0-plugins-outputs-monasca_log_api-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v2.0.0-plugins-outputs-monasca_log_api-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.0.0-plugins-outputs-monasca_log_api-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.0-plugins-outputs-monasca_log_api-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 monasca\_log\_api outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  monasca_log_api {
    id => "my_plugin_id"
  }
}
```
