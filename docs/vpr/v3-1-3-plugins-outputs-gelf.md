---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-outputs-gelf.html
---

# Gelf output plugin v3.1.3 [v3.1.3-plugins-outputs-gelf]


* Plugin version: v3.1.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-gelf/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](output-gelf-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1241]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-gelf). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1234]

This output generates messages in GELF format. This is most useful if you want to use Logstash to output events to Graylog2.

More information at [The Graylog2 GELF specs page](http://graylog2.org/gelf#specs)


## Gelf Output Configuration Options [v3.1.3-plugins-outputs-gelf-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`chunksize`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-chunksize) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`custom_fields`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-custom_fields) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`full_message`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-full_message) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`ignore_metadata`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-ignore_metadata) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`level`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-level) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`port`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`sender`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-sender) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ship_metadata`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-ship_metadata) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ship_tags`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-ship_tags) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`short_message`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-short_message) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-common-options) for a list of options supported by all output plugins.

 

### `chunksize` [v3.1.3-plugins-outputs-gelf-chunksize]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1420`

The GELF chunksize. You usually don’t need to change this.


### `custom_fields` [v3.1.3-plugins-outputs-gelf-custom_fields]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

The GELF custom field mappings. GELF supports arbitrary attributes as custom fields. This exposes that. Exclude the `_` portion of the field name e.g. `custom_fields => ['foo_field', 'some_value']` sets `_foo_field` = `some_value`.


### `full_message` [v3.1.3-plugins-outputs-gelf-full_message]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

The GELF full message. Dynamic values like `%{{foo}}` are permitted here.


### `host` [v3.1.3-plugins-outputs-gelf-host]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Graylog2 server IP address or hostname.


### `ignore_metadata` [v3.1.3-plugins-outputs-gelf-ignore_metadata]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["@timestamp", "@version", "severity", "host", "source_host", "source_path", "short_message"]`

Ignore these fields when `ship_metadata` is set. Typically this lists the fields used in dynamic values for GELF fields.


### `level` [v3.1.3-plugins-outputs-gelf-level]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["%{{severity}}", "INFO"]`

The GELF message level. Dynamic values like `%{{level}}` are permitted here; useful if you want to parse the *log level* from an event and use that as the GELF level/severity.

Values here can be integers [0..7] inclusive or any of "debug", "info", "warn", "error", "fatal" (case insensitive). Single-character versions of these are also valid, "d", "i", "w", "e", "f", "u" The following additional severity\_labels from Logstash’s  syslog\_pri filter are accepted: "emergency", "alert", "critical",  "warning", "notice", and "informational".


### `port` [v3.1.3-plugins-outputs-gelf-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `12201`

Graylog2 server port number.


### `sender` [v3.1.3-plugins-outputs-gelf-sender]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `%{{host}}`

Allow overriding of the GELF `sender` field. This is useful if you want to use something other than the event’s source host as the "sender" of an event. A common case for this is using the application name instead of the hostname.


### `ship_metadata` [v3.1.3-plugins-outputs-gelf-ship_metadata]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Should Logstash ship metadata within event object? This will cause Logstash to ship any fields in the event (such as those created by grok) in the GELF messages. These will be sent as underscored "additional fields".


### `ship_tags` [v3.1.3-plugins-outputs-gelf-ship_tags]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Ship tags within events. This will cause Logstash to ship the tags of an event as the field `\_tags`.


### `short_message` [v3.1.3-plugins-outputs-gelf-short_message]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"short_message"`

The GELF short message field name. If the field does not exist or is empty, the event message is taken instead.



## Common options [v3.1.3-plugins-outputs-gelf-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-3-plugins-outputs-gelf.md#v3.1.3-plugins-outputs-gelf-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.3-plugins-outputs-gelf-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.3-plugins-outputs-gelf-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.3-plugins-outputs-gelf-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 gelf outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  gelf {
    id => "my_plugin_id"
  }
}
```



