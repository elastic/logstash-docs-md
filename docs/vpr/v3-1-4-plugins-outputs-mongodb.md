---
navigation_title: "v3.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.4-plugins-outputs-mongodb.html
---

# Mongodb output plugin v3.1.4 [v3.1.4-plugins-outputs-mongodb]


* Plugin version: v3.1.4
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-mongodb/blob/v3.1.4/CHANGELOG.md)

For other versions, see the [overview list](output-mongodb-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1448]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-mongodb). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1438]

This output writes events to MongoDB.


## Mongodb Output Configuration Options [v3.1.4-plugins-outputs-mongodb-options]

This plugin supports the following configuration options plus the [Common options](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`bulk`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-bulk) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`bulk_interval`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-bulk_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`bulk_size`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-bulk_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`collection`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-collection) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`database`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-database) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`generateId`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-generateId) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`isodate`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-isodate) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`retry_delay`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-retry_delay) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`uri`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-uri) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-common-options) for a list of options supported by all output plugins.

 

### `bulk` [v3.1.4-plugins-outputs-mongodb-bulk]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Bulk insert flag, set to true to allow bulk insertion, else it will insert events one by one.


### `bulk_interval` [v3.1.4-plugins-outputs-mongodb-bulk_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Bulk interval, Used to insert events periodically if the "bulk" flag is activated.


### `bulk_size` [v3.1.4-plugins-outputs-mongodb-bulk_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `900`

Bulk events number, if the number of events to insert into a collection raise that limit, it will be bulk inserted whatever the bulk interval value (mongodb hard limit is 1000).


### `collection` [v3.1.4-plugins-outputs-mongodb-collection]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The collection to use. This value can use `%{{foo}}` values to dynamically select a collection based on data in the event.


### `database` [v3.1.4-plugins-outputs-mongodb-database]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The database to use.


### `generateId` [v3.1.4-plugins-outputs-mongodb-generateId]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If true, an "_id" field will be added to the document before insertion. The "_id" field will use the timestamp of the event and overwrite an existing "_id" field in the event.


### `isodate` [v3.1.4-plugins-outputs-mongodb-isodate]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If true, store the @timestamp field in MongoDB as an ISODate type instead of an ISO8601 string.  For more information about this, see [http://www.mongodb.org/display/DOCS/Dates](http://www.mongodb.org/display/DOCS/Dates).


### `retry_delay` [v3.1.4-plugins-outputs-mongodb-retry_delay]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `3`

The number of seconds to wait after failure before retrying.


### `uri` [v3.1.4-plugins-outputs-mongodb-uri]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A MongoDB URI to connect to. See [http://docs.mongodb.org/manual/reference/connection-string/](http://docs.mongodb.org/manual/reference/connection-string/).



## Common options [v3.1.4-plugins-outputs-mongodb-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-4-plugins-outputs-mongodb.md#v3.1.4-plugins-outputs-mongodb-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.4-plugins-outputs-mongodb-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.4-plugins-outputs-mongodb-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.4-plugins-outputs-mongodb-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 mongodb outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  mongodb {
    id => "my_plugin_id"
  }
}
```



