---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-inputs-heroku.html
---

# Heroku input plugin v3.0.1 [v3.0.1-plugins-inputs-heroku]

* Plugin version: v3.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-heroku/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](input-heroku-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_478]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-heroku). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_472]

Stream events from a heroku app’s logs.

This will read events in a manner similar to how the `heroku logs -t` command fetches logs.

Recommended filters:

```
    filter {
      grok {
        pattern => "^%{TIMESTAMP_ISO8601:timestamp} %{WORD:component}\[%{WORD:process}(?:\.%{INT:instance:int})?\]: %{DATA:message}$"
      }
      date { timestamp => ISO8601 }
    }
```

## Heroku Input Configuration Options [v3.0.1-plugins-inputs-heroku-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`app`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-app) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-common-options) for a list of options supported by all input plugins.

### `app` [v3.0.1-plugins-inputs-heroku-app]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of your heroku application. This is usually the first part of the the domain name `my-app-name.herokuapp.com`

## Common options [v3.0.1-plugins-inputs-heroku-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-1-plugins-inputs-heroku.md#v3.0.1-plugins-inputs-heroku-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.1-plugins-inputs-heroku-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.1-plugins-inputs-heroku-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.1-plugins-inputs-heroku-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.1-plugins-inputs-heroku-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 heroku inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  heroku {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.1-plugins-inputs-heroku-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.1-plugins-inputs-heroku-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
