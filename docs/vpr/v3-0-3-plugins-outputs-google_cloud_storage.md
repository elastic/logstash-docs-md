---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-google_cloud_storage.html
---

# Google_cloud_storage output plugin v3.0.3 [v3.0.3-plugins-outputs-google_cloud_storage]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-google_cloud_storage/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-google_cloud_storage-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1275]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-google_cloud_storage). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1268]

Summary: plugin to upload log events to Google Cloud Storage (GCS), rolling files based on the date pattern provided as a configuration setting. Events are written to files locally and, once file is closed, this plugin uploads it to the configured bucket.

For more info on Google Cloud Storage, please go to: [https://cloud.google.com/products/cloud-storage](https://cloud.google.com/products/cloud-storage)

In order to use this plugin, a Google service account must be used. For more information, please refer to: [https://developers.google.com/storage/docs/authentication#service_accounts](https://developers.google.com/storage/docs/authentication#service_accounts)

Recommendation: experiment with the settings depending on how much log data you generate, so the uploader can keep up with the generated logs. Using gzip output can be a good option to reduce network traffic when uploading the log files and in terms of storage costs as well.

USAGE: This is an example of logstash config:

```json
output {
   google_cloud_storage {
     bucket => "my_bucket"                                     (required)
     key_path => "/path/to/privatekey.p12"                     (required)
     key_password => "notasecret"                              (optional)
     service_account => "1234@developer.gserviceaccount.com"   (required)
     temp_directory => "/tmp/logstash-gcs"                     (optional)
     log_file_prefix => "logstash_gcs"                         (optional)
     max_file_size_kbytes => 1024                              (optional)
     output_format => "plain"                                  (optional)
     date_pattern => "%Y-%m-%dT%H:00"                          (optional)
     flush_interval_secs => 2                                  (optional)
     gzip => false                                             (optional)
     uploader_interval_secs => 60                              (optional)
   }
}
```

* Support logstash event variables to determine filename.
* Turn Google API code into a Plugin Mixin (like AwsConfig).
* There’s no recover method, so if logstash/plugin crashes, files may not be uploaded to GCS.
* Allow user to configure file name.
* Allow parallel uploads for heavier loads (+ connection configuration if exposed by Ruby API client)


## Google_cloud_storage Output Configuration Options [v3.0.3-plugins-outputs-google_cloud_storage-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`bucket`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-bucket) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`date_pattern`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-date_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`flush_interval_secs`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-flush_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`gzip`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-gzip) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`key_password`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-key_password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key_path`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-key_path) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`log_file_prefix`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-log_file_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`max_file_size_kbytes`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-max_file_size_kbytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`output_format`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-output_format) | [string](logstash://reference/configuration-file-structure.md#string), one of `["json", "plain"]` | No |
| [`service_account`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-service_account) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`temp_directory`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-temp_directory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`uploader_interval_secs`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-uploader_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-common-options) for a list of options supported by all output plugins.

 

### `bucket` [v3.0.3-plugins-outputs-google_cloud_storage-bucket]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

GCS bucket name, without "gs://" or any other prefix.


### `date_pattern` [v3.0.3-plugins-outputs-google_cloud_storage-date_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%Y-%m-%dT%H:00"`

Time pattern for log file, defaults to hourly files. Must Time.strftime patterns: www.ruby-doc.org/core-2.0/Time.html#method-i-strftime


### `flush_interval_secs` [v3.0.3-plugins-outputs-google_cloud_storage-flush_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Flush interval in seconds for flushing writes to log files. 0 will flush on every message.


### `gzip` [v3.0.3-plugins-outputs-google_cloud_storage-gzip]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Gzip output stream when writing events to log files.


### `key_password` [v3.0.3-plugins-outputs-google_cloud_storage-key_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"notasecret"`

GCS private key password.


### `key_path` [v3.0.3-plugins-outputs-google_cloud_storage-key_path]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

GCS path to private key file.


### `log_file_prefix` [v3.0.3-plugins-outputs-google_cloud_storage-log_file_prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash_gcs"`

Log file prefix. Log file will follow the format: <prefix>_hostname_date<.part?>.log


### `max_file_size_kbytes` [v3.0.3-plugins-outputs-google_cloud_storage-max_file_size_kbytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

Sets max file size in kbytes. 0 disable max file check.


### `output_format` [v3.0.3-plugins-outputs-google_cloud_storage-output_format]

* Value can be any of: `json`, `plain`
* Default value is `"plain"`

The event format you want to store in files. Defaults to plain text.


### `service_account` [v3.0.3-plugins-outputs-google_cloud_storage-service_account]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

GCS service account.


### `temp_directory` [v3.0.3-plugins-outputs-google_cloud_storage-temp_directory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Directory where temporary files are stored. Defaults to /tmp/logstash-gcs-<random-suffix>


### `uploader_interval_secs` [v3.0.3-plugins-outputs-google_cloud_storage-uploader_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Uploader interval when uploading new files to GCS. Adjust time based on your time pattern (for example, for hourly files, this interval can be around one hour).



## Common options [v3.0.3-plugins-outputs-google_cloud_storage-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-google_cloud_storage.md#v3.0.3-plugins-outputs-google_cloud_storage-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-google_cloud_storage-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.3-plugins-outputs-google_cloud_storage-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-outputs-google_cloud_storage-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 google_cloud_storage outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  google_cloud_storage {
    id => "my_plugin_id"
  }
}
```



