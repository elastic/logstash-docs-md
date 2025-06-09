---
navigation_title: "v3.0.8"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.8-plugins-outputs-pagerduty.html
---

# Pagerduty output plugin v3.0.8 [v3.0.8-plugins-outputs-pagerduty]

* Plugin version: v3.0.8
* Released on: 2019-01-05
* [Changelog](https://github.com/logstash-plugins/logstash-output-pagerduty/blob/v3.0.8/CHANGELOG.md)

For other versions, see the [overview list](output-pagerduty-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1479]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-pagerduty). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1469]

The PagerDuty output will send notifications based on pre-configured services and escalation policies. Logstash can send "trigger", "acknowledge" and "resolve" event types. In addition, you may configure custom descriptions and event details. The only required field is the PagerDuty "Service API Key", which can be found on the service’s web page on pagerduty.com. In the default case, the description and event details will be populated by Logstash, using `message`, `timestamp` and `host` data.

## Pagerduty Output Configuration Options [v3.0.8-plugins-outputs-pagerduty-options]

This plugin supports the following configuration options plus the [Common options](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`description`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-description) | [string](/lsr/value-types.md#string) | No |
| [`details`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-details) | [hash](/lsr/value-types.md#hash) | No |
| [`event_type`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-event_type) | [string](/lsr/value-types.md#string), one of `["trigger", "acknowledge", "resolve"]` | No |
| [`incident_key`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-incident_key) | [string](/lsr/value-types.md#string) | No |
| [`pdurl`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-pdurl) | [string](/lsr/value-types.md#string) | No |
| [`service_key`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-service_key) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-common-options) for a list of options supported by all output plugins.

### `description` [v3.0.8-plugins-outputs-pagerduty-description]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Logstash event for %{host}"`

Custom description

### `details` [v3.0.8-plugins-outputs-pagerduty-details]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"timestamp"=>"%{@timestamp}", "message"=>"%{message}"}`

The event details. These might be data from the Logstash event fields you wish to include. Tags are automatically included if detected so there is no need to explicitly add them here.

### `event_type` [v3.0.8-plugins-outputs-pagerduty-event_type]

* Value can be any of: `trigger`, `acknowledge`, `resolve`
* Default value is `"trigger"`

Event type

### `incident_key` [v3.0.8-plugins-outputs-pagerduty-incident_key]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash/%{host}/%{type}"`

The service key to use. You’ll need to set this up in PagerDuty beforehand.

### `pdurl` [v3.0.8-plugins-outputs-pagerduty-pdurl]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"https://events.pagerduty.com/generic/2010-04-15/create_event.json"`

PagerDuty API URL. You shouldn’t need to change this, but is included to allow for flexibility should PagerDuty iterate the API and Logstash hasn’t been updated yet.

### `service_key` [v3.0.8-plugins-outputs-pagerduty-service_key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The PagerDuty Service API Key

## Common options [v3.0.8-plugins-outputs-pagerduty-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-8-plugins-outputs-pagerduty.md#v3.0.8-plugins-outputs-pagerduty-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.8-plugins-outputs-pagerduty-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.8-plugins-outputs-pagerduty-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.8-plugins-outputs-pagerduty-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 pagerduty outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  pagerduty {
    id => "my_plugin_id"
  }
}
```
