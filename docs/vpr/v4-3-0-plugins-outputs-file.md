---
navigation_title: "v4.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.3.0-plugins-outputs-file.html
---

# File output plugin v4.3.0 [v4.3.0-plugins-outputs-file]


* Plugin version: v4.3.0
* Released on: 2020-04-27
* [Changelog](https://github.com/logstash-plugins/logstash-output-file/blob/v4.3.0/CHANGELOG.md)

For other versions, see the [overview list](output-file-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1223]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-file). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1216]

This output writes events to files on disk. You can use fields from the event as parts of the filename and/or path.

By default, this output writes one event per line in **json** format. You can customise the line format using the `line` codec like

```ruby
output {
 file {
   path => ...
   codec => line { format => "custom format: %{message}"}
 }
}
```


## File Output Configuration Options [v4.3.0-plugins-outputs-file-options]

This plugin supports the following configuration options plus the [Common options](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`create_if_deleted`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-create_if_deleted) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`dir_mode`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-dir_mode) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`file_mode`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-file_mode) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`filename_failure`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-filename_failure) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`flush_interval`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-flush_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`gzip`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-gzip) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`path`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-path) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`stale_cleanup_interval`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-stale_cleanup_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`write_behavior`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-write_behavior) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-common-options) for a list of options supported by all output plugins.

 

### `create_if_deleted` [v4.3.0-plugins-outputs-file-create_if_deleted]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

If the configured file is deleted, but an event is handled by the plugin, the plugin will recreate the file. Default ⇒ true


### `dir_mode` [v4.3.0-plugins-outputs-file-dir_mode]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `-1`

Dir access mode to use. Note that due to the bug in jruby system umask is ignored on linux: [https://github.com/jruby/jruby/issues/3426](https://github.com/jruby/jruby/issues/3426) Setting it to -1 uses default OS value. Example: `"dir_mode" => 0750`


### `file_mode` [v4.3.0-plugins-outputs-file-file_mode]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `-1`

File access mode to use. Note that due to the bug in jruby system umask is ignored on linux: [https://github.com/jruby/jruby/issues/3426](https://github.com/jruby/jruby/issues/3426) Setting it to -1 uses default OS value. Example: `"file_mode" => 0640`


### `filename_failure` [v4.3.0-plugins-outputs-file-filename_failure]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_filepath_failures"`

If the generated path is invalid, the events will be saved into this file and inside the defined path.


### `flush_interval` [v4.3.0-plugins-outputs-file-flush_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Flush interval (in seconds) for flushing writes to log files. 0 will flush on every message.


### `gzip` [v4.3.0-plugins-outputs-file-gzip]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Gzip the output stream before writing to disk.


### `path` [v4.3.0-plugins-outputs-file-path]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The path to the file to write. Event fields can be used here, like `/var/log/logstash/%{{host}}/%{{application}}` One may also utilize the path option for date-based log rotation via the joda time format. This will use the event timestamp. E.g.: `path => "./test-%{+YYYY-MM-dd}.txt"` to create `./test-2013-05-29.txt`

If you use an absolute path you cannot start with a dynamic string. E.g: `/%{{myfield}}/`, `/test-%{{myfield}}/` are not valid paths


### `stale_cleanup_interval` [v4.3.0-plugins-outputs-file-stale_cleanup_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Defines the interval, in seconds, between the stale files cleanup runs. The stale files cleanup cycle closes inactive files (i.e files not written to since the last cycle).


### `write_behavior` [v4.3.0-plugins-outputs-file-write_behavior]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `append`

If `append`, the file will be opened for appending and each new event will be written at the end of the file. If `overwrite`, the file will be truncated before writing and only the most recent event will appear in the file.



## Common options [v4.3.0-plugins-outputs-file-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-3-0-plugins-outputs-file.md#v4.3.0-plugins-outputs-file-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.3.0-plugins-outputs-file-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json_lines"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.3.0-plugins-outputs-file-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.3.0-plugins-outputs-file-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 file outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  file {
    id => "my_plugin_id"
  }
}
```
