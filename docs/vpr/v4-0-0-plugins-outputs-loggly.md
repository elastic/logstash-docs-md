---
navigation_title: "v4.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.0-plugins-outputs-loggly.html
---

# Loggly output plugin v4.0.0 [v4.0.0-plugins-outputs-loggly]

* Plugin version: v4.0.0
* Released on: 2018-05-15
* [Changelog](https://github.com/logstash-plugins/logstash-output-loggly/blob/v4.0.0/CHANGELOG.md)

For other versions, see the [overview list](output-loggly-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1424]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-loggly). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1414]

Got a loggly account? Use logstash to ship logs to Loggly!

This is most useful so you can use logstash to parse and structure your logs and ship structured, json events to your account at Loggly.

To use this, you’ll need to use a Loggly input with type *http* and *json logging* enabled.

## Loggly Output Configuration Options [v4.0.0-plugins-outputs-loggly-options]

This plugin supports the following configuration options plus the [Common options](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`can_retry`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-can_retry) | [boolean](/lsr/value-types.md#boolean) | No |
| [`host`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-host) | [string](/lsr/value-types.md#string) | No |
| [`key`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-key) | [string](/lsr/value-types.md#string) | Yes |
| [`max_event_size`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-max_event_size) | [bytes](/lsr/value-types.md#bytes) | Yes |
| [`max_payload_size`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-max_payload_size) | [bytes](/lsr/value-types.md#bytes) | Yes |
| [`proto`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-proto) | [string](/lsr/value-types.md#string) | No |
| [`proxy_host`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-proxy_host) | [string](/lsr/value-types.md#string) | No |
| [`proxy_password`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-proxy_password) | [password](/lsr/value-types.md#password) | No |
| [`proxy_port`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-proxy_port) | [number](/lsr/value-types.md#number) | No |
| [`proxy_user`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-proxy_user) | [string](/lsr/value-types.md#string) | No |
| [`retry_count`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-retry_count) | [number](/lsr/value-types.md#number) | No |
| [`tag`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-tag) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-common-options) for a list of options supported by all output plugins.

### `can_retry` [v4.0.0-plugins-outputs-loggly-can_retry]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Can Retry. Setting this value true helps user to send multiple retry attempts if the first request fails

### `host` [v4.0.0-plugins-outputs-loggly-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logs-01.loggly.com"`

The hostname to send logs to. This should target the loggly http input server which is usually "logs-01.loggly.com" (Gen2 account). See the [Loggly HTTP endpoint documentation](https://www.loggly.com/docs/http-endpoint/).

### `key` [v4.0.0-plugins-outputs-loggly-key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The loggly http customer token to use for sending. You can find yours in "Source Setup", under "Customer Tokens".

You can use `%{foo}` field lookups here if you need to pull the api key from the event. This is mainly aimed at multitenant hosting providers who want to offer shipping a customer’s logs to that customer’s loggly account.

### `max_event_size` [v4.0.0-plugins-outputs-loggly-max_event_size]

* This is a required setting.
* Value type is [bytes](/lsr/value-types.md#bytes)
* Default value is 1 Mib

The Loggly API supports event size up to 1 Mib.

You should only need to change this setting if the API limits have changed and you need to override the plugin’s behaviour.

See the [Loggly bulk API documentation](https://www.loggly.com/docs/http-bulk-endpoint/)

### `max_payload_size` [v4.0.0-plugins-outputs-loggly-max_payload_size]

* This is a required setting.
* Value type is [bytes](/lsr/value-types.md#bytes)
* Default value is 5 Mib

The Loggly API supports API call payloads up to 5 Mib.

You should only need to change this setting if the API limits have changed and you need to override the plugin’s behaviour.

See the [Loggly bulk API documentation](https://www.loggly.com/docs/http-bulk-endpoint/)

### `proto` [v4.0.0-plugins-outputs-loggly-proto]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"http"`

Should the log action be sent over https instead of plain http

### `proxy_host` [v4.0.0-plugins-outputs-loggly-proxy_host]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Proxy Host

### `proxy_password` [v4.0.0-plugins-outputs-loggly-proxy_password]

* Value type is [password](/lsr/value-types.md#password)
* Default value is `""`

Proxy Password

### `proxy_port` [v4.0.0-plugins-outputs-loggly-proxy_port]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

Proxy Port

### `proxy_user` [v4.0.0-plugins-outputs-loggly-proxy_user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Proxy Username

### `retry_count` [v4.0.0-plugins-outputs-loggly-retry_count]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

Retry count. It may be possible that the request may timeout due to slow Internet connection if such condition appears, retry\_count helps in retrying request for multiple times It will try to submit request until retry\_count and then halt

### `tag` [v4.0.0-plugins-outputs-loggly-tag]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

Loggly Tags help you to find your logs in the Loggly dashboard easily. You can search for a tag in Loggly using `"tag:logstash"`.

If you need to specify multiple tags here on your events, specify them as outlined in [the tag documentation](https://www.loggly.com/docs/tags/). E.g. `"tag" => "foo,bar,myApp"`.

You can also use `"tag" => "%{somefield}"` to take your tag value from `somefield` on your event. Helpful for leveraging [Loggly source groups](https://www.loggly.com/docs/source-groups/).

## Common options [v4.0.0-plugins-outputs-loggly-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-0-plugins-outputs-loggly.md#v4.0.0-plugins-outputs-loggly-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v4.0.0-plugins-outputs-loggly-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.0-plugins-outputs-loggly-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.0-plugins-outputs-loggly-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 loggly outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  loggly {
    id => "my_plugin_id"
  }
}
```
