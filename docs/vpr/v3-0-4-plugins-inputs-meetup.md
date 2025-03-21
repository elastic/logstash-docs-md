---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-inputs-meetup.html
---

# Meetup input plugin v3.0.4 [v3.0.4-plugins-inputs-meetup]


* Plugin version: v3.0.4
* Released on: 2018-01-30
* [Changelog](https://github.com/logstash-plugins/logstash-input-meetup/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](input-meetup-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_720]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-meetup). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_713]

Periodically query meetup.com regarding updates on events for the given meetupkey


## Meetup Input Configuration Options [v3.0.4-plugins-inputs-meetup-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`eventstatus`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-eventstatus) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`groupid`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-groupid) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`interval`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-interval) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`meetupkey`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-meetupkey) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`urlname`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-urlname) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`venueid`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-venueid) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-common-options) for a list of options supported by all input plugins.

 

### `eventstatus` [v3.0.4-plugins-inputs-meetup-eventstatus]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"upcoming,past"`

Event Status'


### `groupid` [v3.0.4-plugins-inputs-meetup-groupid]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The Group ID, multiple may be specified seperated by commas Must have one of `urlname`, `venueid`, `groupid`


### `interval` [v3.0.4-plugins-inputs-meetup-interval]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Interval to run the command. Value is in minutes.


### `meetupkey` [v3.0.4-plugins-inputs-meetup-meetupkey]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Meetup Key


### `urlname` [v3.0.4-plugins-inputs-meetup-urlname]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URLName - the URL name ie `ElasticSearch-Oklahoma-City` Must have one of urlname, venue_id, group_id


### `venueid` [v3.0.4-plugins-inputs-meetup-venueid]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The venue ID Must have one of `urlname`, `venue_id`, `group_id`



## Common options [v3.0.4-plugins-inputs-meetup-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-4-plugins-inputs-meetup.md#v3.0.4-plugins-inputs-meetup-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.4-plugins-inputs-meetup-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.4-plugins-inputs-meetup-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.4-plugins-inputs-meetup-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.4-plugins-inputs-meetup-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 meetup inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  meetup {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.4-plugins-inputs-meetup-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.4-plugins-inputs-meetup-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



