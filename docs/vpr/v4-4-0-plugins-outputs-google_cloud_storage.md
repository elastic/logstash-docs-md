---
navigation_title: "v4.4.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.4.0-plugins-outputs-google_cloud_storage.html
---

# Google Cloud Storage output plugin v4.4.0 [v4.4.0-plugins-outputs-google_cloud_storage]


* Plugin version: v4.4.0
* Released on: 2023-08-22
* [Changelog](https://github.com/logstash-plugins/logstash-output-google_cloud_storage/blob/v4.4.0/CHANGELOG.md)

For other versions, see the [overview list](output-google_cloud_storage-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1263]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-google_cloud_storage). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1256]

A plugin to upload log events to Google Cloud Storage (GCS), rolling files based on the date pattern provided as a configuration setting. Events are written to files locally and, once file is closed, this plugin uploads it to the configured bucket.

For more info on Google Cloud Storage, please go to: [https://cloud.google.com/products/cloud-storage](https://cloud.google.com/products/cloud-storage)

In order to use this plugin, a Google service account must be used. For more information, please refer to: [https://developers.google.com/storage/docs/authentication#service_accounts](https://developers.google.com/storage/docs/authentication#service_accounts)

Recommendation: experiment with the settings depending on how much log data you generate, so the uploader can keep up with the generated logs. Using gzip output can be a good option to reduce network traffic when uploading the log files and in terms of storage costs as well.


## Usage [_usage_80]

This is an example of logstash config:

```json
output {
   google_cloud_storage {
     bucket => "my_bucket"                                     (required)
     json_key_file => "/path/to/privatekey.json"               (optional)
     temp_directory => "/tmp/logstash-gcs"                     (optional)
     log_file_prefix => "logstash_gcs"                         (optional)
     max_file_size_kbytes => 1024                              (optional)
     output_format => "plain"                                  (optional)
     date_pattern => "%Y-%m-%dT%H:00"                          (optional)
     flush_interval_secs => 2                                  (optional)
     gzip => false                                             (optional)
     gzip_content_encoding => false                            (optional)
     uploader_interval_secs => 60                              (optional)
     include_uuid => true                                      (optional)
     include_hostname => true                                  (optional)
   }
}
```

### Additional Resources [_additional_resources_15]

* [Application Default Credentials (ADC) Overview](https://cloud.google.com/docs/authentication/production)
* [Cloud Storage Introduction](https://cloud.google.com/storage/)
* [Pricing Information](https://cloud.google.com/storage/pricing)



## Improvements TODO List [_improvements_todo_list_2]

* Support logstash event variables to determine filename.
* Turn Google API code into a Plugin Mixin (like AwsConfig).
* There’s no recover method, so if logstash/plugin crashes, files may not be uploaded to GCS.
* Allow user to configure file name.
* Allow parallel uploads for heavier loads (+ connection configuration if exposed by Ruby API client)


## Google_cloud_storage Output Configuration Options [v4.4.0-plugins-outputs-google_cloud_storage-options]

This plugin supports the following configuration options plus the [Common options](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`bucket`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-bucket) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`date_pattern`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-date_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`flush_interval_secs`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-flush_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`gzip`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-gzip) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`gzip_content_encoding`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-gzip_content_encoding) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`include_hostname`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-include_hostname) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`include_uuid`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-include_uuid) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`json_key_file`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-json_key_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key_password`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-key_password) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`key_path`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-key_path) | [string](logstash://reference/configuration-file-structure.md#string) | **Obsolete** |
| [`log_file_prefix`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-log_file_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`max_concurrent_uploads`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-max_concurrent_uploads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_file_size_kbytes`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-max_file_size_kbytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`output_format`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-output_format) | [string](logstash://reference/configuration-file-structure.md#string), one of `["json", "plain", nil]` | *Deprecated* |
| [`service_account`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-service_account) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`temp_directory`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-temp_directory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`uploader_interval_secs`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-uploader_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-common-options) for a list of options supported by all output plugins.

 

### `bucket` [v4.4.0-plugins-outputs-google_cloud_storage-bucket]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

GCS bucket name, without "gs://" or any other prefix.


### `date_pattern` [v4.4.0-plugins-outputs-google_cloud_storage-date_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%Y-%m-%dT%H:00"`

Time pattern for log file, defaults to hourly files. Must Time.strftime patterns: www.ruby-doc.org/core-2.0/Time.html#method-i-strftime


### `flush_interval_secs` [v4.4.0-plugins-outputs-google_cloud_storage-flush_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Flush interval in seconds for flushing writes to log files. 0 will flush on every message.


### `gzip` [v4.4.0-plugins-outputs-google_cloud_storage-gzip]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Gzip output stream when writing events to log files, set `Content-Type` to `application/gzip` instead of `text/plain`, and use file suffix `.log.gz` instead of `.log`.


### `gzip_content_encoding` [v4.4.0-plugins-outputs-google_cloud_storage-gzip_content_encoding]

::::{note}
Added in 3.3.0.
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Gzip output stream when writing events to log files and set `Content-Encoding` to `gzip`. This will upload your files as `gzip` saving network and storage costs, but they will be transparently decompressed when you read them from the storage bucket.

See the Cloud Storage documentation on [metadata](https://cloud.google.com/storage/docs/metadata#content-encoding) and [transcoding](https://cloud.google.com/storage/docs/transcoding#content-type_vs_content-encoding) for more information.

**Note**: It is not recommended to use both `gzip_content_encoding` and `gzip`. This compresses your file *twice*, will increase the work your machine does and makes the files larger than just compressing once.


### `include_hostname` [v4.4.0-plugins-outputs-google_cloud_storage-include_hostname]

::::{note}
Added in 3.1.0.
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Should the hostname be included in the file name? You may want to turn this off for privacy reasons or if you are running multiple instances of Logstash and need to match the files you create with a simple glob such as if you wanted to import files to BigQuery.


### `include_uuid` [v4.4.0-plugins-outputs-google_cloud_storage-include_uuid]

::::{note}
Added in 3.1.0.
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Adds a UUID to the end of a file name. You may want to enable this feature so files don’t clobber one another if you’re running multiple instances of Logstash or if you expect frequent node restarts.


### `json_key_file` [v4.4.0-plugins-outputs-google_cloud_storage-json_key_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

The plugin can use [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/production), if it’s running on Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions.

Outside of Google Cloud, you will need create a Service Account JSON key file through the web interface or with the following command: `gcloud iam service-accounts keys create key.json --iam-account my-sa-123@my-project-123.iam.gserviceaccount.com`


### `key_password` [v4.4.0-plugins-outputs-google_cloud_storage-key_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"notasecret"`

**Deprecated** this feature is no longer used, the setting is now a part of [`json_key_file`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-json_key_file).


### `key_path` [v4.4.0-plugins-outputs-google_cloud_storage-key_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)

**Obsolete:** The PKCS12 key file format is no longer supported. Please use one of the following mechanisms:

* [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/production), configured via environment variables on Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions.
* A JSON authentication key file. You can generate them in the console for the service account like you did with the `.P12` file or with the following command: `gcloud iam service-accounts keys create key.json --iam-account my-sa-123@my-project-123.iam.gserviceaccount.com`


### `log_file_prefix` [v4.4.0-plugins-outputs-google_cloud_storage-log_file_prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash_gcs"`

Log file prefix. Log file will follow the format: <prefix>_hostname_date<.part?>.log


### `max_concurrent_uploads` [v4.4.0-plugins-outputs-google_cloud_storage-max_concurrent_uploads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Sets the maximum number of concurrent uploads to Cloud Storage at a time. Uploads are I/O bound so it makes sense to tune this paramater with regards to the network bandwidth available and the latency between your server and Cloud Storage.


### `max_file_size_kbytes` [v4.4.0-plugins-outputs-google_cloud_storage-max_file_size_kbytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

Sets max file size in kbytes. 0 disable max file check.


### `output_format` [v4.4.0-plugins-outputs-google_cloud_storage-output_format]

* Value can be any of: `json`, `plain`, or no value
* Default value is no value

**Deprecated**, this feature will be removed in the next major release. Use codecs instead.

* If you are using the `json` value today, switch to the `json_lines` codec.
* If you are using the `plain` value today, switch to the `line` codec.

The event format you want to store in files. Defaults to plain text.

Note: if you want to use a codec you MUST not set this value.


### `service_account` [v4.4.0-plugins-outputs-google_cloud_storage-service_account]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

**Deprecated** this feature is no longer used, the setting is now a part of [`json_key_file`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-json_key_file).


### `temp_directory` [v4.4.0-plugins-outputs-google_cloud_storage-temp_directory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Directory where temporary files are stored. Defaults to /tmp/logstash-gcs-<random-suffix>


### `uploader_interval_secs` [v4.4.0-plugins-outputs-google_cloud_storage-uploader_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Uploader interval when uploading new files to GCS. Adjust time based on your time pattern (for example, for hourly files, this interval can be around one hour).



## Common options [v4.4.0-plugins-outputs-google_cloud_storage-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-4-0-plugins-outputs-google_cloud_storage.md#v4.4.0-plugins-outputs-google_cloud_storage-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.4.0-plugins-outputs-google_cloud_storage-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"line"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.4.0-plugins-outputs-google_cloud_storage-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.4.0-plugins-outputs-google_cloud_storage-id]

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
