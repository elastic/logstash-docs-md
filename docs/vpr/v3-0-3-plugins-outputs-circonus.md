---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-circonus.html
---

# Circonus output plugin v3.0.3 [v3.0.3-plugins-outputs-circonus]

* Plugin version: v3.0.3
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-circonus/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-circonus-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1061]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-circonus). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1054]

This output sends annotations to Circonus based on Logstash events.

## Circonus Output Configuration Options [v3.0.3-plugins-outputs-circonus-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`annotation`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-annotation) | [hash](/lsr/value-types.md#hash) | Yes |
| [`api_token`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-api_token) | [string](/lsr/value-types.md#string) | Yes |
| [`app_name`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-app_name) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-common-options) for a list of options supported by all output plugins.

### `annotation` [v3.0.3-plugins-outputs-circonus-annotation]

* This is a required setting.
* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Annotations Registers an annotation with Circonus The only required field is `title` and `description`. `start` and `stop` will be set to the event timestamp. You can add any other optional annotation values as well. All values will be passed through `event.sprintf`

Example:

```
  ["title":"Logstash event", "description":"Logstash event for %{host}"]
or
[source,ruby]
  ["title":"Logstash event", "description":"Logstash event for %{host}", "parent_id", "1"]
```

### `api_token` [v3.0.3-plugins-outputs-circonus-api_token]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Your Circonus API Token

### `app_name` [v3.0.3-plugins-outputs-circonus-app_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Your Circonus App name This will be passed through `event.sprintf` so variables are allowed here:

Example: `app_name => "%{myappname}"`

## Common options [v3.0.3-plugins-outputs-circonus-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-circonus.md#v3.0.3-plugins-outputs-circonus-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-circonus-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.3-plugins-outputs-circonus-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-outputs-circonus-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 circonus outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  circonus {
    id => "my_plugin_id"
  }
}
```
