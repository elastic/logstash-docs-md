---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-csv.html
---

# Csv output plugin v3.0.6 [v3.0.6-plugins-outputs-csv]


* Plugin version: v3.0.6
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-output-csv/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-csv-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1052]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-csv). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1045]

CSV output.

Write events to disk in CSV or other delimited format Based on the file output, many config values are shared Uses the Ruby csv library internally


## Csv Output Configuration Options [v3.0.6-plugins-outputs-csv-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`create_if_deleted`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-create_if_deleted) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`csv_options`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-csv_options) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`dir_mode`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-dir_mode) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`fields`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-fields) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`file_mode`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-file_mode) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`filename_failure`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-filename_failure) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`flush_interval`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-flush_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`gzip`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-gzip) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`path`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-path) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`spreadsheet_safe`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-spreadsheet_safe) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-common-options) for a list of options supported by all output plugins.

 

### `create_if_deleted` [v3.0.6-plugins-outputs-csv-create_if_deleted]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

If the configured file is deleted, but an event is handled by the plugin, the plugin will recreate the file. Default ⇒ true


### `csv_options` [v3.0.6-plugins-outputs-csv-csv_options]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Options for CSV output. This is passed directly to the Ruby stdlib to_csv function. Full documentation is available on the [Ruby CSV documentation page](http://ruby-doc.org/stdlib-2.0.0/libdoc/csv/rdoc/index.md). A typical use case would be to use alternative column or row seperators eg: `csv_options => {"col_sep" => "\t" "row_sep" => "\r\n"}` gives tab seperated data with windows line endings


### `dir_mode` [v3.0.6-plugins-outputs-csv-dir_mode]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `-1`

Dir access mode to use. Note that due to the bug in jruby system umask is ignored on linux: [https://github.com/jruby/jruby/issues/3426](https://github.com/jruby/jruby/issues/3426) Setting it to -1 uses default OS value. Example: `"dir_mode" => 0750`


### `fields` [v3.0.6-plugins-outputs-csv-fields]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The field names from the event that should be written to the CSV file. Fields are written to the CSV in the same order as the array. If a field does not exist on the event, an empty string will be written. Supports field reference syntax eg: `fields => ["field1", "[nested][field]"]`.


### `file_mode` [v3.0.6-plugins-outputs-csv-file_mode]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `-1`

File access mode to use. Note that due to the bug in jruby system umask is ignored on linux: [https://github.com/jruby/jruby/issues/3426](https://github.com/jruby/jruby/issues/3426) Setting it to -1 uses default OS value. Example: `"file_mode" => 0640`


### `filename_failure` [v3.0.6-plugins-outputs-csv-filename_failure]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_filepath_failures"`

If the generated path is invalid, the events will be saved into this file and inside the defined path.


### `flush_interval` [v3.0.6-plugins-outputs-csv-flush_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Flush interval (in seconds) for flushing writes to log files. 0 will flush on every message.


### `gzip` [v3.0.6-plugins-outputs-csv-gzip]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Gzip the output stream before writing to disk.


### `path` [v3.0.6-plugins-outputs-csv-path]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This output writes events to files on disk. You can use fields from the event as parts of the filename and/or path.

By default, this output writes one event per line in **json** format. You can customise the line format using the `line` codec like

```ruby
output {
 file {
   path => ...
   codec => line { format => "custom format: %{message}"}
 }
}
The path to the file to write. Event fields can be used here,
like `/var/log/logstash/%{host}/%{application}`
One may also utilize the path option for date-based log
rotation via the joda time format. This will use the event
timestamp.
E.g.: `path => "./test-%{+YYYY-MM-dd}.txt"` to create
`./test-2013-05-29.txt`
```

If you use an absolute path you cannot start with a dynamic string. E.g: `/%{{myfield}}/`, `/test-%{{myfield}}/` are not valid paths


### `spreadsheet_safe` [v3.0.6-plugins-outputs-csv-spreadsheet_safe]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Option to not escape/munge string values. Please note turning off this option may not make the values safe in your spreadsheet application



## Common options [v3.0.6-plugins-outputs-csv-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-csv.md#v3.0.6-plugins-outputs-csv-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-csv-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-outputs-csv-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-outputs-csv-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 csv outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  csv {
    id => "my_plugin_id"
  }
}
```
