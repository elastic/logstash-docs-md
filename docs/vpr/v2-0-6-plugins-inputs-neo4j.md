---
navigation_title: "v2.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.6-plugins-inputs-neo4j.html
---

# Neo4j input plugin v2.0.6 [v2.0.6-plugins-inputs-neo4j]

* Plugin version: v2.0.6
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-neo4j/blob/v2.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-neo4j-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_751]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-neo4j). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_744]

This plugin gets data from a Neo4j database in predefined intervals. To fetch this data uses a given Cypher query.

### Usage [_usage_66]

```
input {
  neo4j {
    query => "MATCH (p:`Person`)-->(m:`Movie`) WHERE m.released = 2005 RETURN *"
    path  => "/foo/bar.db"
  }
}
```

In embedded\_db mode this plugin require a neo4j db 2.0.1 or superior. If using the remote version there is no major restriction.

## Neo4j Input Configuration Options [v2.0.6-plugins-inputs-neo4j-options]

This plugin supports the following configuration options plus the [Common options](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`path`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-path) | [string](/lsr/value-types.md#string) | Yes |
| [`query`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-query) | [string](/lsr/value-types.md#string) | Yes |
| [`schedule`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-schedule) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-common-options) for a list of options supported by all input plugins.

### `path` [v2.0.6-plugins-inputs-neo4j-path]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The path within your file system where the neo4j database is located

### `query` [v2.0.6-plugins-inputs-neo4j-query]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

If undefined, Logstash will complain, even if codec is unused. Cypher query used to retrieve data from the neo4j database, this statement should looks like something like this:

MATCH (p:`Person`)-→(m:`Movie`) WHERE m.released = 2005 RETURN \*

### `schedule` [v2.0.6-plugins-inputs-neo4j-schedule]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "\* \* \* \* \*" (execute query every minute, on the minute). If this variable is not specified then this input will run only once

## Common options [v2.0.6-plugins-inputs-neo4j-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v2-0-6-plugins-inputs-neo4j.md#v2.0.6-plugins-inputs-neo4j-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v2.0.6-plugins-inputs-neo4j-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v2.0.6-plugins-inputs-neo4j-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.0.6-plugins-inputs-neo4j-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.6-plugins-inputs-neo4j-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 neo4j inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  neo4j {
    id => "my_plugin_id"
  }
}
```

### `tags` [v2.0.6-plugins-inputs-neo4j-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v2.0.6-plugins-inputs-neo4j-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
