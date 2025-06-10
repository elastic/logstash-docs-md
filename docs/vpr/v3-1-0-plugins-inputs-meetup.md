---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-inputs-meetup.html
---

# Meetup input plugin v3.1.0 [v3.1.0-plugins-inputs-meetup]

* Plugin version: v3.1.0
* Released on: 2018-02-14
* [Changelog](https://github.com/logstash-plugins/logstash-input-meetup/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](input-meetup-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_745]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-meetup). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_738]

Periodically query meetup.com regarding updates on events for the given Meetup key.

## Meetup Input Configuration Options [v3.1.0-plugins-inputs-meetup-options]

This plugin supports the following configuration options plus the [Common options](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`eventstatus`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-eventstatus) | [string](/lsr/value-types.md#string) | No |
| [`groupid`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-groupid) | [string](/lsr/value-types.md#string) | No |
| [`interval`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-interval) | [number](/lsr/value-types.md#number) | Yes |
| [`meetupkey`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-meetupkey) | [string](/lsr/value-types.md#string) | Yes |
| [`urlname`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-urlname) | [string](/lsr/value-types.md#string) | No |
| [`venueid`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-venueid) | [string](/lsr/value-types.md#string) | No |
| [`text`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-text) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-common-options) for a list of options supported by all input plugins.

### `eventstatus` [v3.1.0-plugins-inputs-meetup-eventstatus]

* Value type is [string](/lsr/value-types.md#string).
* Default value is `"upcoming,past"`.

Event Status can be one of `"upcoming"`, `"past"`, or `"upcoming,past"`. Default is `"upcoming,past"`.

### `groupid` [v3.1.0-plugins-inputs-meetup-groupid]

* Value type is [string](/lsr/value-types.md#string).
* There is no default value for this setting.

The Group ID, multiple may be specified seperated by commas. Must have one of `urlname`, `venueid`, `groupid`, `text`.

### `interval` [v3.1.0-plugins-inputs-meetup-interval]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number).
* There is no default value for this setting.

Interval to run the command. Value is in minutes.

### `meetupkey` [v3.1.0-plugins-inputs-meetup-meetupkey]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string).
* There is no default value for this setting.

Meetup Key, aka personal token.

### `urlname` [v3.1.0-plugins-inputs-meetup-urlname]

* Value type is [string](/lsr/value-types.md#string).
* There is no default value for this setting.

URLName - the URL name ie `ElasticSearch-Oklahoma-City`. Must have one of urlname, venue\_id, group\_id, `text`.

### `venueid` [v3.1.0-plugins-inputs-meetup-venueid]

* Value type is [string](/lsr/value-types.md#string).
* There is no default value for this setting.

The venue ID Must have one of `urlname`, `venue_id`, `group_id`, `text`.

### `text` [v3.1.0-plugins-inputs-meetup-text]

* Value type is [string](/lsr/value-types.md#string).
* There is no default value for this setting.

A text string to search meetup events by. Must have one of `urlname`, `venue_id`, `group_id`, `text`.

## Common options [v3.1.0-plugins-inputs-meetup-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-1-0-plugins-inputs-meetup.md#v3.1.0-plugins-inputs-meetup-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.1.0-plugins-inputs-meetup-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.1.0-plugins-inputs-meetup-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.0-plugins-inputs-meetup-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.0-plugins-inputs-meetup-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 meetup inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  meetup {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.1.0-plugins-inputs-meetup-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.1.0-plugins-inputs-meetup-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
