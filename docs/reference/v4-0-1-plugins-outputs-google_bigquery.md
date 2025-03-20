---
navigation_title: "v4.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.1-plugins-outputs-google_bigquery.html
---

# Google BigQuery output plugin v4.0.1 [v4.0.1-plugins-outputs-google_bigquery]


* Plugin version: v4.0.1
* Released on: 2018-05-03
* [Changelog](https://github.com/logstash-plugins/logstash-output-google_bigquery/blob/v4.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-google_bigquery-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1256]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-google_bigquery). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1249]

### Summary [_summary_30]

This plugin uploads events to Google BigQuery using the streaming API so data can become available nearly immediately.

You can configure it to flush periodically, after N events or after a certain amount of data is ingested.


### Environment Configuration [_environment_configuration_12]

You must enable BigQuery on your Google Cloud Storage (GCS) account and create a dataset to hold the tables this plugin generates.

You must also grant the service account this plugin uses access to the dataset.

You can use [Logstash conditionals](logstash://reference/event-dependent-configuration.md) and multiple configuration blocks to upload events with different structures.


### Usage [_usage_77]

This is an example of logstash config:

```ruby
output {
   google_bigquery {
     project_id => "folkloric-guru-278"                        (required)
     dataset => "logs"                                         (required)
     csv_schema => "path:STRING,status:INTEGER,score:FLOAT"    (required) <1>
     json_key_file => "/path/to/key.json"                      (optional) <2>
     error_directory => "/tmp/bigquery-errors"                 (required)
     date_pattern => "%Y-%m-%dT%H:00"                          (optional)
     flush_interval_secs => 30                                 (optional)
   }
}
```

1. Specify either a csv_schema or a json_schema.
2. If the key is not used, then the plugin tries to find [Application Default Credentials](https://cloud.google.com/docs/authentication/production)



### Considerations [_considerations_12]

* There is a small fee to insert data into BigQuery using the streaming API
* This plugin buffers events in-memory, so make sure the flush configurations are appropriate for your use-case and consider using [Logstash Persistent Queues](logstash://reference/persistent-queues.md)


### Additional Resources [_additional_resources_12]

* [Application Default Credentials (ADC) Overview](https://cloud.google.com/docs/authentication/production)
* [BigQuery Introduction](https://cloud.google.com/bigquery/)
* [BigQuery Schema Formats and Types](https://cloud.google.com/bigquery/docs/schemas)



## Google BigQuery Output Configuration Options [v4.0.1-plugins-outputs-google_bigquery-options]

This plugin supports the following configuration options plus the [Common options](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`batch_size`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-batch_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`batch_size_bytes`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-batch_size_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`csv_schema`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-csv_schema) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`dataset`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-dataset) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`date_pattern`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-date_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`deleter_interval_secs`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-deleter_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | *Deprecated* |
| [`error_directory`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-error_directory) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`flush_interval_secs`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-flush_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ignore_unknown_values`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-ignore_unknown_values) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`json_key_file`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-json_key_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`json_schema`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-json_schema) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`key_password`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-key_password) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`key_path`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-key_path) | [string](logstash://reference/configuration-file-structure.md#string) | **Obsolete** |
| [`project_id`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-project_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`service_account`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-service_account) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`table_prefix`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-table_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`table_separator`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-table_separator) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`temp_directory`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-temp_directory) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`temp_file_prefix`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-temp_file_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | *Deprecated* |
| [`uploader_interval_secs`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-uploader_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | *Deprecated* |

Also see [Common options](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-common-options) for a list of options supported by all output plugins.

 

### `batch_size` [v4.0.1-plugins-outputs-google_bigquery-batch_size]

::::{note}
Added in 4.0.0.
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `128`

The number of messages to upload at a single time. (< 1000, default: 128)


### `batch_size_bytes` [v4.0.1-plugins-outputs-google_bigquery-batch_size_bytes]

::::{note}
Added in 4.0.0.
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1_000_000`

An approximate number of bytes to upload as part of a batch. Default: 1MB


### `csv_schema` [v4.0.1-plugins-outputs-google_bigquery-csv_schema]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Schema for log data. It must follow the format `name1:type1(,name2:type2)*`. For example, `path:STRING,status:INTEGER,score:FLOAT`.


### `dataset` [v4.0.1-plugins-outputs-google_bigquery-dataset]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The BigQuery dataset the tables for the events will be added to.


### `date_pattern` [v4.0.1-plugins-outputs-google_bigquery-date_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%Y-%m-%dT%H:00"`

Time pattern for BigQuery table, defaults to hourly tables. Must Time.strftime patterns: www.ruby-doc.org/core-2.0/Time.html#method-i-strftime


### `deleter_interval_secs` [v4.0.1-plugins-outputs-google_bigquery-deleter_interval_secs]

::::{admonition} Deprecated in 4.0.0.
:class: warning

Events are uploaded in real-time without being stored to disk.
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)


### `error_directory` [v4.0.1-plugins-outputs-google_bigquery-error_directory]

::::{note}
Added in 4.0.0.
::::


* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/tmp/bigquery"`.

The location to store events that could not be uploaded due to errors. Consider using an additional Logstash input to pipe the contents of these to an alert platform so you can manually fix the events.

Or use [GCS FUSE](https://cloud.google.com/storage/docs/gcs-fuse) to transparently upload to a GCS bucket.

Files names follow the pattern `[table name]-[UNIX timestamp].log`


### `flush_interval_secs` [v4.0.1-plugins-outputs-google_bigquery-flush_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Uploads all data this often even if other upload criteria aren’t met. Default: 5s


### `ignore_unknown_values` [v4.0.1-plugins-outputs-google_bigquery-ignore_unknown_values]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Indicates if BigQuery should ignore values that are not represented in the table schema. If true, the extra values are discarded. If false, BigQuery will reject the records with extra fields and the job will fail. The default value is false.

::::{note}
You may want to add a Logstash filter like the following to remove common fields it adds:
::::


```ruby
mutate {
    remove_field => ["@version","@timestamp","path","host","type", "message"]
}
```


### `json_key_file` [v4.0.1-plugins-outputs-google_bigquery-json_key_file]

::::{admonition} Added in 4.0.0.
:class: note

Replaces [`key_password`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-key_password)
::::


* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

If logstash is running within Google Compute Engine, the plugin can use GCE’s Application Default Credentials. Outside of GCE, you will need to specify a Service Account JSON key file.


### `json_schema` [v4.0.1-plugins-outputs-google_bigquery-json_schema]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `nil`

Schema for log data as a hash. These can include nested records, descriptions, and modes.

Example:

```ruby
json_schema => {
  fields => [{
    name => "endpoint"
    type => "STRING"
    description => "Request route"
  }, {
    name => "status"
    type => "INTEGER"
    mode => "NULLABLE"
  }, {
    name => "params"
    type => "RECORD"
    mode => "REPEATED"
    fields => [{
      name => "key"
      type => "STRING"
     }, {
      name => "value"
      type => "STRING"
    }]
  }]
}
```


### `key_password` [v4.0.1-plugins-outputs-google_bigquery-key_password]

::::{admonition} Deprecated in 4.0.0.
:class: warning

Replaced by `json_key_file` or by using ADC. See [`json_key_file`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-json_key_file)
::::


* Value type is [string](logstash://reference/configuration-file-structure.md#string)


### `key_path` [v4.0.1-plugins-outputs-google_bigquery-key_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)

**Obsolete:** The PKCS12 key file format is no longer supported.

Please use one of the following mechanisms:

* [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/production), configured via environment variables on Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions.
* A JSON authentication key file. You can generate them in the console for the service account like you did with the `.P12` file or with the following command: `gcloud iam service-accounts keys create key.json --iam-account my-sa-123@my-project-123.iam.gserviceaccount.com`


### `project_id` [v4.0.1-plugins-outputs-google_bigquery-project_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Google Cloud Project ID (number, not Project Name!).


### `service_account` [v4.0.1-plugins-outputs-google_bigquery-service_account]

::::{admonition} Deprecated in 4.0.0.
:class: warning

Replaced by `json_key_file` or by using ADC. See [`json_key_file`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-json_key_file)
::::


* Value type is [string](logstash://reference/configuration-file-structure.md#string)


### `table_prefix` [v4.0.1-plugins-outputs-google_bigquery-table_prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

BigQuery table ID prefix to be used when creating new tables for log data. Table name will be `<table_prefix><table_separator><date>`


### `table_separator` [v4.0.1-plugins-outputs-google_bigquery-table_separator]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_"`

BigQuery table separator to be added between the table_prefix and the date suffix.


### `temp_directory` [v4.0.1-plugins-outputs-google_bigquery-temp_directory]

::::{admonition} Deprecated in 4.0.0.
:class: warning

Events are uploaded in real-time without being stored to disk.
::::


* Value type is [string](logstash://reference/configuration-file-structure.md#string)


### `temp_file_prefix` [v4.0.1-plugins-outputs-google_bigquery-temp_file_prefix]

::::{admonition} Deprecated in 4.0.0.
:class: warning

Events are uploaded in real-time without being stored to disk
::::


* Value type is [string](logstash://reference/configuration-file-structure.md#string)


### `uploader_interval_secs` [v4.0.1-plugins-outputs-google_bigquery-uploader_interval_secs]

::::{admonition} Deprecated in 4.0.0.
:class: warning

This field is no longer used
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Uploader interval when uploading new files to BigQuery. Adjust time based on your time pattern (for example, for hourly files, this interval can be around one hour).



## Common options [v4.0.1-plugins-outputs-google_bigquery-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-0-1-plugins-outputs-google_bigquery.md#v4.0.1-plugins-outputs-google_bigquery-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.0.1-plugins-outputs-google_bigquery-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.0.1-plugins-outputs-google_bigquery-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.0.1-plugins-outputs-google_bigquery-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 google_bigquery outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  google_bigquery {
    id => "my_plugin_id"
  }
}
```
