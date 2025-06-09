---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-inputs-sqlite.html
---

# Sqlite input plugin v3.0.3 [v3.0.3-plugins-inputs-sqlite]

* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-input-sqlite/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](input-sqlite-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_885]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-sqlite). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_878]

Read rows from an sqlite database.

This is most useful in cases where you are logging directly to a table. Any tables being watched must have an `id` column that is monotonically increasing.

All tables are read by default except:

* ones matching `sqlite_%` - these are internal/adminstrative tables for sqlite
* `since_table` - this is used by this plugin to track state.

Example

```
    % sqlite /tmp/example.db
    sqlite> CREATE TABLE weblogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip STRING,
        request STRING,
        response INTEGER);
    sqlite> INSERT INTO weblogs (ip, request, response)
        VALUES ("1.2.3.4", "/index.html", 200);
```

Then with this logstash config:

```
    input {
      sqlite {
        path => "/tmp/example.db"
        type => weblogs
      }
    }
    output {
      stdout {
        debug => true
      }
    }
```

Sample output:

```
    {
      "@source"      => "sqlite://sadness/tmp/x.db",
      "@tags"        => [],
      "@fields"      => {
        "ip"       => "1.2.3.4",
        "request"  => "/index.html",
        "response" => 200
      },
      "@timestamp"   => "2013-05-29T06:16:30.850Z",
      "@source_host" => "sadness",
      "@source_path" => "/tmp/x.db",
      "@message"     => "",
      "@type"        => "foo"
    }
```

## Sqlite Input Configuration Options [v3.0.3-plugins-inputs-sqlite-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`batch`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-batch) | [number](/lsr/value-types.md#number) | No |
| [`exclude_tables`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-exclude_tables) | [array](/lsr/value-types.md#array) | No |
| [`path`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-path) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-common-options) for a list of options supported by all input plugins.

### `batch` [v3.0.3-plugins-inputs-sqlite-batch]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

How many rows to fetch at a time from each `SELECT` call.

### `exclude_tables` [v3.0.3-plugins-inputs-sqlite-exclude_tables]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Any tables to exclude by name. By default all tables are followed.

### `path` [v3.0.3-plugins-inputs-sqlite-path]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The path to the sqlite database file.

## Common options [v3.0.3-plugins-inputs-sqlite-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-3-plugins-inputs-sqlite.md#v3.0.3-plugins-inputs-sqlite-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.3-plugins-inputs-sqlite-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.3-plugins-inputs-sqlite-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.3-plugins-inputs-sqlite-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.3-plugins-inputs-sqlite-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 sqlite inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  sqlite {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.3-plugins-inputs-sqlite-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.3-plugins-inputs-sqlite-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
