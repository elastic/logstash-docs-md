---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-outputs-webhdfs.html
---

# Webhdfs output plugin v3.0.6 [v3.0.6-plugins-outputs-webhdfs]

* Plugin version: v3.0.6
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-webhdfs/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-webhdfs-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1670]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-webhdfs). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1660]

This plugin sends Logstash events into files in HDFS via the [webhdfs](https://hadoop.apache.org/docs/r1.0.4/webhdfs.html) REST API.

## Dependencies [_dependencies_2]

This plugin has no dependency on jars from hadoop, thus reducing configuration and compatibility problems. It uses the webhdfs gem from Kazuki Ohta and TAGOMORI Satoshi (@see: <https://github.com/kzk/webhdfs>). Optional dependencies are zlib and snappy gem if you use the compression functionality.

## Operational Notes [_operational_notes_4]

If you get an error like:

```
Max write retries reached. Exception: initialize: name or service not known {:level=>:error}
```

make sure that the hostname of your namenode is resolvable on the host running Logstash. When creating/appending to a file, webhdfs somtime sends a `307 TEMPORARY_REDIRECT` with the `HOSTNAME` of the machine its running on.

## Usage [_usage_130]

This is an example of Logstash config:

```
input {
  ...
}
filter {
  ...
}
output {
  webhdfs {
    host => "127.0.0.1"                 # (required)
    port => 50070                       # (optional, default: 50070)
    path => "/user/logstash/dt=%{+YYYY-MM-dd}/logstash-%{+HH}.log"  # (required)
    user => "hue"                       # (required)
  }
}
```

## Webhdfs Output Configuration Options [v3.0.6-plugins-outputs-webhdfs-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`compression`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-compression) | [string](/lsr/value-types.md#string), one of `["none", "snappy", "gzip"]` | No |
| [`flush_size`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-flush_size) | [number](/lsr/value-types.md#number) | No |
| [`host`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-host) | [string](/lsr/value-types.md#string) | Yes |
| [`idle_flush_time`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-idle_flush_time) | [number](/lsr/value-types.md#number) | No |
| [`kerberos_keytab`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-kerberos_keytab) | [string](/lsr/value-types.md#string) | No |
| [`open_timeout`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-open_timeout) | [number](/lsr/value-types.md#number) | No |
| [`path`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-path) | [string](/lsr/value-types.md#string) | Yes |
| [`port`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-port) | [number](/lsr/value-types.md#number) | No |
| [`read_timeout`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-read_timeout) | [number](/lsr/value-types.md#number) | No |
| [`retry_interval`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-retry_interval) | [number](/lsr/value-types.md#number) | No |
| [`retry_known_errors`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-retry_known_errors) | [boolean](/lsr/value-types.md#boolean) | No |
| [`retry_times`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-retry_times) | [number](/lsr/value-types.md#number) | No |
| [`single_file_per_thread`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-single_file_per_thread) | [boolean](/lsr/value-types.md#boolean) | No |
| [`snappy_bufsize`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-snappy_bufsize) | [number](/lsr/value-types.md#number) | No |
| [`snappy_format`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-snappy_format) | [string](/lsr/value-types.md#string), one of `["stream", "file"]` | No |
| [`ssl_cert`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-ssl_cert) | [string](/lsr/value-types.md#string) | No |
| [`ssl_key`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-ssl_key) | [string](/lsr/value-types.md#string) | No |
| [`standby_host`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-standby_host) | [string](/lsr/value-types.md#string) | No |
| [`standby_port`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-standby_port) | [number](/lsr/value-types.md#number) | No |
| [`use_httpfs`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-use_httpfs) | [boolean](/lsr/value-types.md#boolean) | No |
| [`use_kerberos_auth`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-use_kerberos_auth) | [boolean](/lsr/value-types.md#boolean) | No |
| [`use_ssl_auth`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-use_ssl_auth) | [boolean](/lsr/value-types.md#boolean) | No |
| [`user`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-user) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-common-options) for a list of options supported by all output plugins.

### `compression` [v3.0.6-plugins-outputs-webhdfs-compression]

* Value can be any of: `none`, `snappy`, `gzip`
* Default value is `"none"`

Compress output. One of \[*none*, *snappy*, *gzip*]

### `flush_size` [v3.0.6-plugins-outputs-webhdfs-flush_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `500`

Sending data to webhdfs if event count is above, even if `store_interval_in_secs` is not reached.

### `host` [v3.0.6-plugins-outputs-webhdfs-host]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The server name for webhdfs/httpfs connections.

### `idle_flush_time` [v3.0.6-plugins-outputs-webhdfs-idle_flush_time]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

Sending data to webhdfs in x seconds intervals.

### `kerberos_keytab` [v3.0.6-plugins-outputs-webhdfs-kerberos_keytab]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Set kerberos keytab file. Note that the gssapi library needs to be available to use this.

### `open_timeout` [v3.0.6-plugins-outputs-webhdfs-open_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `30`

WebHdfs open timeout, default 30s.

### `path` [v3.0.6-plugins-outputs-webhdfs-path]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The path to the file to write to. Event fields can be used here, as well as date fields in the joda time format, e.g.: `/user/logstash/dt=%{+YYYY-MM-dd}/%{@source_host}-%{+HH}.log`

### `port` [v3.0.6-plugins-outputs-webhdfs-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50070`

The server port for webhdfs/httpfs connections.

### `read_timeout` [v3.0.6-plugins-outputs-webhdfs-read_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `30`

The WebHdfs read timeout, default 30s.

### `retry_interval` [v3.0.6-plugins-outputs-webhdfs-retry_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0.5`

How long should we wait between retries.

### `retry_known_errors` [v3.0.6-plugins-outputs-webhdfs-retry_known_errors]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Retry some known webhdfs errors. These may be caused by race conditions when appending to same file, etc.

### `retry_times` [v3.0.6-plugins-outputs-webhdfs-retry_times]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

How many times should we retry. If retry\_times is exceeded, an error will be logged and the event will be discarded.

### `single_file_per_thread` [v3.0.6-plugins-outputs-webhdfs-single_file_per_thread]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Avoid appending to same file in multiple threads. This solves some problems with multiple logstash output threads and locked file leases in webhdfs. If this option is set to true, %{\[@metadata]\[thread\_id]} needs to be used in path config settting.

### `snappy_bufsize` [v3.0.6-plugins-outputs-webhdfs-snappy_bufsize]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `32768`

Set snappy chunksize. Only neccessary for stream format. Defaults to 32k. Max is 65536 @see <http://code.google.com/p/snappy/source/browse/trunk/framing_format.txt>

### `snappy_format` [v3.0.6-plugins-outputs-webhdfs-snappy_format]

* Value can be any of: `stream`, `file`
* Default value is `"stream"`

Set snappy format. One of "stream", "file". Set to stream to be hive compatible.

### `ssl_cert` [v3.0.6-plugins-outputs-webhdfs-ssl_cert]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Set ssl cert file.

### `ssl_key` [v3.0.6-plugins-outputs-webhdfs-ssl_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Set ssl key file.

### `standby_host` [v3.0.6-plugins-outputs-webhdfs-standby_host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `false`

Standby namenode for ha hdfs.

### `standby_port` [v3.0.6-plugins-outputs-webhdfs-standby_port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50070`

Standby namenode port for ha hdfs.

### `use_httpfs` [v3.0.6-plugins-outputs-webhdfs-use_httpfs]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Use httpfs mode if set to true, else webhdfs.

### `use_kerberos_auth` [v3.0.6-plugins-outputs-webhdfs-use_kerberos_auth]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Set kerberos authentication.

### `use_ssl_auth` [v3.0.6-plugins-outputs-webhdfs-use_ssl_auth]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Set ssl authentication. Note that the openssl library needs to be available to use this.

### `user` [v3.0.6-plugins-outputs-webhdfs-user]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The Username for webhdfs.

## Common options [v3.0.6-plugins-outputs-webhdfs-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-6-plugins-outputs-webhdfs.md#v3.0.6-plugins-outputs-webhdfs-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.6-plugins-outputs-webhdfs-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"line"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.6-plugins-outputs-webhdfs-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.6-plugins-outputs-webhdfs-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 webhdfs outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  webhdfs {
    id => "my_plugin_id"
  }
}
```
