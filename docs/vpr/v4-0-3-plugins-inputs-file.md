---
navigation_title: "v4.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.3-plugins-inputs-file.html
---

# File input plugin v4.0.3 [v4.0.3-plugins-inputs-file]


* Plugin version: v4.0.3
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-file/blob/v4.0.3/CHANGELOG.md)

For other versions, see the [overview list](input-file-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_402]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-file). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_402]

Stream events from files, normally by tailing them in a manner similar to `tail -0F` but optionally reading them from the beginning.

By default, each event is assumed to be one line and a line is taken to be the text before a newline character. Normally, logging will add a newline to the end of each line written. If you would like to join multiple log lines into one event, you’ll want to use the multiline codec or filter.

The plugin aims to track changing files and emit new content as it’s appended to each file. It’s not well-suited for reading a file from beginning to end and storing all of it in a single event (not even with the multiline codec or filter).


## Reading from remote network volumes [_reading_from_remote_network_volumes_35]

The file input is not tested on remote filesystems such as NFS, Samba, s3fs-fuse, etc. These remote filesystems typically have behaviors that are very different from local filesystems and are therefore unlikely to work correctly when used with the file input.


## Tracking of current position in watched files [_tracking_of_current_position_in_watched_files_35]

The plugin keeps track of the current position in each file by recording it in a separate file named sincedb. This makes it possible to stop and restart Logstash and have it pick up where it left off without missing the lines that were added to the file while Logstash was stopped.

By default, the sincedb file is placed in the home directory of the user running Logstash with a filename based on the filename patterns being watched (i.e. the `path` option). Thus, changing the filename patterns will result in a new sincedb file being used and any existing current position state will be lost. If you change your patterns with any frequency it might make sense to explicitly choose a sincedb path with the `sincedb_path` option.

A different `sincedb_path` must be used for each input. Using the same path will cause issues. The read checkpoints for each input must be stored in a different path so the information does not override.

Sincedb files are text files with four columns:

1. The inode number (or equivalent).
2. The major device number of the file system (or equivalent).
3. The minor device number of the file system (or equivalent).
4. The current byte offset within the file.

On non-Windows systems you can obtain the inode number of a file with e.g. `ls -li`.


## File rotation [_file_rotation_2]

File rotation is detected and handled by this input, regardless of whether the file is rotated via a rename or a copy operation. To support programs that write to the rotated file for some time after the rotation has taken place, include both the original filename and the rotated filename (e.g. /var/log/syslog and /var/log/syslog.1) in the filename patterns to watch (the `path` option). Note that the rotated filename will be treated as a new file so if `start_position` is set to *beginning* the rotated file will be reprocessed.

With the default value of `start_position` (*end*) any messages written to the end of the file between the last read operation prior to the rotation and its reopening under the new name (an interval determined by the `stat_interval` and `discover_interval` options) will not get picked up.


## File Input Configuration Options [v4.0.3-plugins-inputs-file-options]

This plugin supports the following configuration options plus the [Common options](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`close_older`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-close_older) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`delimiter`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-delimiter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`discover_interval`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-discover_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`exclude`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-exclude) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ignore_older`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-ignore_older) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_open_files`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-max_open_files) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`path`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-path) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`sincedb_path`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-sincedb_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sincedb_write_interval`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-sincedb_write_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`start_position`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-start_position) | [string](logstash://reference/configuration-file-structure.md#string), one of `["beginning", "end"]` | No |
| [`stat_interval`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-stat_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-common-options) for a list of options supported by all input plugins.

 

### `close_older` [v4.0.3-plugins-inputs-file-close_older]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `3600`

The file input closes any files that were last read the specified timespan in seconds ago. This has different implications depending on if a file is being tailed or read. If tailing, and there is a large time gap in incoming data the file can be closed (allowing other files to be opened) but will be queued for reopening when new data is detected. If reading, the file will be closed after closed_older seconds from when the last bytes were read. The default is 1 hour


### `delimiter` [v4.0.3-plugins-inputs-file-delimiter]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"\n"`

set the new line delimiter, defaults to "\n"


### `discover_interval` [v4.0.3-plugins-inputs-file-discover_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `15`

How often (in seconds) we expand the filename patterns in the `path` option to discover new files to watch.


### `exclude` [v4.0.3-plugins-inputs-file-exclude]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Exclusions (matched against the filename, not full path). Filename patterns are valid here, too. For example, if you have

```ruby
    path => "/var/log/*"
```

You might want to exclude gzipped files:

```ruby
    exclude => "*.gz"
```


### `ignore_older` [v4.0.3-plugins-inputs-file-ignore_older]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

When the file input discovers a file that was last modified before the specified timespan in seconds, the file is ignored. After it’s discovery, if an ignored file is modified it is no longer ignored and any new data is read. By default, this option is disabled. Note this unit is in seconds.


### `max_open_files` [v4.0.3-plugins-inputs-file-max_open_files]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

What is the maximum number of file_handles that this input consumes at any one time. Use close_older to close some files if you need to process more files than this number. This should not be set to the maximum the OS can do because file handles are needed for other LS plugins and OS processes. The default of 4095 is set in filewatch.


### `path` [v4.0.3-plugins-inputs-file-path]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The path(s) to the file(s) to use as an input. You can use filename patterns here, such as `/var/log/*.log`. If you use a pattern like `/var/log/**/*.log`, a recursive search of `/var/log` will be done for all `*.log` files. Paths must be absolute and cannot be relative.

You may also configure multiple paths. See an example on the [Logstash configuration page](logstash://reference/configuration-file-structure.md#array).


### `sincedb_path` [v4.0.3-plugins-inputs-file-sincedb_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path of the sincedb database file (keeps track of the current position of monitored log files) that will be written to disk. The default will write sincedb files to `<path.data>/plugins/inputs/file` NOTE: it must be a file path and not a directory path


### `sincedb_write_interval` [v4.0.3-plugins-inputs-file-sincedb_write_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `15`

How often (in seconds) to write a since database with the current position of monitored log files.


### `start_position` [v4.0.3-plugins-inputs-file-start_position]

* Value can be any of: `beginning`, `end`
* Default value is `"end"`

Choose where Logstash starts initially reading files: at the beginning or at the end. The default behavior treats files like live streams and thus starts at the end. If you have old data you want to import, set this to *beginning*.

This option only modifies "first contact" situations where a file is new and not seen before, i.e. files that don’t have a current position recorded in a sincedb file read by Logstash. If a file has already been seen before, this option has no effect and the position recorded in the sincedb file will be used.


### `stat_interval` [v4.0.3-plugins-inputs-file-stat_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

How often (in seconds) we stat files to see if they have been modified. Increasing this interval will decrease the number of system calls we make, but increase the time to detect new log lines.



## Common options [v4.0.3-plugins-inputs-file-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v4-0-3-plugins-inputs-file.md#v4.0.3-plugins-inputs-file-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v4.0.3-plugins-inputs-file-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v4.0.3-plugins-inputs-file-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.0.3-plugins-inputs-file-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.0.3-plugins-inputs-file-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 file inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  file {
    id => "my_plugin_id"
  }
}
```


### `tags` [v4.0.3-plugins-inputs-file-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v4.0.3-plugins-inputs-file-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



