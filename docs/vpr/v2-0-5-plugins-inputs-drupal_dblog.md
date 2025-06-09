---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-inputs-drupal_dblog.html
---

# Drupal_dblog input plugin v2.0.5 [v2.0.5-plugins-inputs-drupal_dblog]

* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-drupal_dblog/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-drupal_dblog-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_308]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-drupal_dblog). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_308]

Retrieve watchdog log events from a Drupal installation with DBLog enabled. The events are pulled out directly from the database. The original events are not deleted, and on every consecutive run only new events are pulled.

The last watchdog event id that was processed is stored in the Drupal variable table with the name "logstash\_last\_wid". Delete this variable or set it to 0 if you want to re-import all events.

More info on DBLog: <http://drupal.org/documentation/modules/dblog>

## Drupal_dblog Input Configuration Options [v2.0.5-plugins-inputs-drupal_dblog-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_usernames`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-add_usernames) | [boolean](/lsr/value-types.md#boolean) | No |
| [`bulksize`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-bulksize) | [number](/lsr/value-types.md#number) | No |
| [`databases`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-databases) | [hash](/lsr/value-types.md#hash) | No |
| [`interval`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-interval) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-common-options) for a list of options supported by all input plugins.

### `add_usernames` [v2.0.5-plugins-inputs-drupal_dblog-add_usernames]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

By default, the event only contains the current user id as a field. If you whish to add the username as an additional field, set this to true.

### `bulksize` [v2.0.5-plugins-inputs-drupal_dblog-bulksize]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5000`

The amount of log messages that should be fetched with each query. Bulk fetching is done to prevent querying huge data sets when lots of messages are in the database.

### `databases` [v2.0.5-plugins-inputs-drupal_dblog-databases]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Specify all drupal databases that you whish to import from. This can be as many as you whish. The format is a hash, with a unique site name as the key, and a databse url as the value.

Example: \[ "site1", "mysql://user1:password\@host1.com/databasename", "other\_site", "mysql://user2:password\@otherhost.com/databasename", … ]

### `interval` [v2.0.5-plugins-inputs-drupal_dblog-interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Time between checks in minutes.

## Common options [v2.0.5-plugins-inputs-drupal_dblog-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v2-0-5-plugins-inputs-drupal_dblog.md#v2.0.5-plugins-inputs-drupal_dblog-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v2.0.5-plugins-inputs-drupal_dblog-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v2.0.5-plugins-inputs-drupal_dblog-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.0.5-plugins-inputs-drupal_dblog-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.5-plugins-inputs-drupal_dblog-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 drupal\_dblog inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  drupal_dblog {
    id => "my_plugin_id"
  }
}
```

### `tags` [v2.0.5-plugins-inputs-drupal_dblog-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v2.0.5-plugins-inputs-drupal_dblog-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
