---
navigation_title: "v3.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.2-plugins-inputs-couchdb_changes.html
---

# Couchdb_changes input plugin v3.1.2 [v3.1.2-plugins-inputs-couchdb_changes]


* Plugin version: v3.1.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-couchdb_changes/blob/v3.1.2/CHANGELOG.md)

For other versions, see the [overview list](input-couchdb_changes-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_280]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-couchdb_changes). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_280]

This CouchDB input allows you to automatically stream events from the CouchDB [_changes](http://guide.couchdb.org/draft/notifications.html) URI. Moreover, any "future" changes will automatically be streamed as well making it easy to synchronize your CouchDB data with any target destination

### Upsert and delete [_upsert_and_delete_5]

You can use event metadata to allow for document deletion. All non-delete operations are treated as upserts


### Starting at a Specific Sequence [_starting_at_a_specific_sequence_5]

The CouchDB input stores the last sequence number value in location defined by `sequence_path`. You can use this fact to start or resume the stream at a particular sequence.



## Couchdb_changes Input Configuration Options [v3.1.2-plugins-inputs-couchdb_changes-options]

This plugin supports the following configuration options plus the [Common options](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`always_reconnect`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-always_reconnect) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ca_file`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-ca_file) | a valid filesystem path | No |
| [`db`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-db) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`heartbeat`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-heartbeat) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ignore_attachments`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-ignore_attachments) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`initial_sequence`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-initial_sequence) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`keep_id`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-keep_id) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`keep_revision`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-keep_revision) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`password`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`reconnect_delay`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-reconnect_delay) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`secure`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-secure) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`sequence_path`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-sequence_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`timeout`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`username`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-common-options) for a list of options supported by all input plugins.

 

### `always_reconnect` [v3.1.2-plugins-inputs-couchdb_changes-always_reconnect]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Reconnect flag.  When true, always try to reconnect after a failure


### `ca_file` [v3.1.2-plugins-inputs-couchdb_changes-ca_file]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to a CA certificate file, used to validate certificates


### `db` [v3.1.2-plugins-inputs-couchdb_changes-db]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The CouchDB db to connect to. Required parameter.


### `heartbeat` [v3.1.2-plugins-inputs-couchdb_changes-heartbeat]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

Logstash connects to CouchDB’s _changes with feed=continuous The heartbeat is how often (in milliseconds) Logstash will ping CouchDB to ensure the connection is maintained.  Changing this setting is not recommended unless you know what you are doing.


### `host` [v3.1.2-plugins-inputs-couchdb_changes-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

IP or hostname of your CouchDB instance


### `ignore_attachments` [v3.1.2-plugins-inputs-couchdb_changes-ignore_attachments]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Future feature! Until implemented, changing this from the default will not do anything.

Ignore attachments associated with CouchDB documents.


### `initial_sequence` [v3.1.2-plugins-inputs-couchdb_changes-initial_sequence]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

If unspecified, Logstash will attempt to read the last sequence number from the `sequence_path` file.  If that is empty or non-existent, it will begin with 0 (the beginning).

If you specify this value, it is anticipated that you will only be doing so for an initial read under special circumstances and that you will unset this value afterwards.


### `keep_id` [v3.1.2-plugins-inputs-couchdb_changes-keep_id]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Preserve the CouchDB document id "_id" value in the output.


### `keep_revision` [v3.1.2-plugins-inputs-couchdb_changes-keep_revision]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Preserve the CouchDB document revision "_rev" value in the output.


### `password` [v3.1.2-plugins-inputs-couchdb_changes-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

Password, if authentication is needed to connect to CouchDB


### `port` [v3.1.2-plugins-inputs-couchdb_changes-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5984`

Port of your CouchDB instance.


### `reconnect_delay` [v3.1.2-plugins-inputs-couchdb_changes-reconnect_delay]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Reconnect delay: time between reconnect attempts, in seconds.


### `secure` [v3.1.2-plugins-inputs-couchdb_changes-secure]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Connect to CouchDB’s _changes feed securely (via https) Default: false (via http)


### `sequence_path` [v3.1.2-plugins-inputs-couchdb_changes-sequence_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

File path where the last sequence number in the _changes stream is stored. If unset it will write to `$HOME/.couchdb_seq`


### `timeout` [v3.1.2-plugins-inputs-couchdb_changes-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Timeout: Number of milliseconds to wait for new data before terminating the connection.  If a timeout is set it will disable the heartbeat configuration option.


### `username` [v3.1.2-plugins-inputs-couchdb_changes-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Username, if authentication is needed to connect to CouchDB



## Common options [v3.1.2-plugins-inputs-couchdb_changes-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-1-2-plugins-inputs-couchdb_changes.md#v3.1.2-plugins-inputs-couchdb_changes-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.1.2-plugins-inputs-couchdb_changes-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.1.2-plugins-inputs-couchdb_changes-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.2-plugins-inputs-couchdb_changes-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.2-plugins-inputs-couchdb_changes-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 couchdb_changes inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  couchdb_changes {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.1.2-plugins-inputs-couchdb_changes-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.1.2-plugins-inputs-couchdb_changes-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



