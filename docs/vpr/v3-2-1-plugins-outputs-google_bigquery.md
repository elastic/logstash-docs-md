---
navigation_title: "v3.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.1-plugins-outputs-google_bigquery.html
---

# Google_bigquery output plugin v3.2.1 [v3.2.1-plugins-outputs-google_bigquery]


* Plugin version: v3.2.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-google_bigquery/blob/v3.2.1/CHANGELOG.md)

For other versions, see the [overview list](output-google_bigquery-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1261]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-google_bigquery). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1254]

```txt
Author: Rodrigo De Castro <rdc@google.com>
Date: 2013-09-20

Copyright 2013 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

Summary: plugin to upload log events to Google BigQuery (BQ), rolling files based on the date pattern provided as a configuration setting. Events are written to files locally and, once file is closed, this plugin uploads it to the configured BigQuery dataset.

VERY IMPORTANT: . To make good use of BigQuery, your log events should be parsed and structured. Consider using grok to parse your events into fields that can be uploaded to BQ. . You must configure your plugin so it gets events with the same structure, so the BigQuery schema suits them. In case you want to upload log events with different structures, you can utilize multiple configuration blocks, separating different log events with Logstash conditionals. More details on Logstash conditionals can be found here: [http://logstash.net/docs/1.2.1/configuration#conditionals](http://logstash.net/docs/1.2.1/configuration#conditionals)

For more info on Google BigQuery, please go to: [https://developers.google.com/bigquery/](https://developers.google.com/bigquery/)

In order to use this plugin, a Google service account must be used. For more information, please refer to: [https://developers.google.com/storage/docs/authentication#service_accounts](https://developers.google.com/storage/docs/authentication#service_accounts)

Recommendations:

1. Experiment with the settings depending on how much log data you generate, your needs to see "fresh" data, and how much data you could lose in the event of crash. For instance, if you want to see recent data in BQ quickly, you could configure the plugin to upload data every minute or so (provided you have enough log events to justify that). Note also, that if uploads are too frequent, there is no guarantee that they will be imported in the same order, so later data may be available before earlier data.
2. BigQuery charges for storage and for queries, depending on how much data it reads to perform a query. These are other aspects to consider when considering the date pattern which will be used to create new tables and also how to compose the queries when using BQ. For more info on BigQuery Pricing, please access: [https://developers.google.com/bigquery/pricing](https://developers.google.com/bigquery/pricing)

USAGE: This is an example of logstash config:

```json
output {
   google_bigquery {
     project_id => "folkloric-guru-278"                        (required)
     dataset => "logs"                                         (required)
     csv_schema => "path:STRING,status:INTEGER,score:FLOAT"    (required) <1>
     key_path => "/path/to/privatekey.p12"                     (required)
     key_password => "notasecret"                              (optional)
     service_account => "1234@developer.gserviceaccount.com"   (required)
     temp_directory => "/tmp/logstash-bq"                      (optional)
     temp_file_prefix => "logstash_bq"                         (optional)
     date_pattern => "%Y-%m-%dT%H:00"                          (optional)
     flush_interval_secs => 2                                  (optional)
     uploader_interval_secs => 60                              (optional)
     deleter_interval_secs => 60                               (optional)
   }
}
```

1. Specify either a csv_schema or a json_schema.* Refactor common code between Google BQ and GCS plugins.
* Turn Google API code into a Plugin Mixin (like AwsConfig).
* There’s no recover method, so if logstash/plugin crashes, files may not be uploaded to BQ.




## Google_bigquery Output Configuration Options [v3.2.1-plugins-outputs-google_bigquery-options]

This plugin supports the following configuration options plus the [Common options](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`csv_schema`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-csv_schema) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`dataset`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-dataset) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`date_pattern`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-date_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`deleter_interval_secs`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-deleter_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`flush_interval_secs`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-flush_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ignore_unknown_values`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-ignore_unknown_values) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`json_schema`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-json_schema) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`key_password`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-key_password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key_path`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-key_path) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`project_id`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-project_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`service_account`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-service_account) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`table_prefix`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-table_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`table_separator`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-table_separator) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`temp_directory`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-temp_directory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`temp_file_prefix`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-temp_file_prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`uploader_interval_secs`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-uploader_interval_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-common-options) for a list of options supported by all output plugins.

 

### `csv_schema` [v3.2.1-plugins-outputs-google_bigquery-csv_schema]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Schema for log data. It must follow this format: <field1-name>:<field1-type>,<field2-name>:<field2-type>,…​ Example: path:STRING,status:INTEGER,score:FLOAT


### `dataset` [v3.2.1-plugins-outputs-google_bigquery-dataset]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

BigQuery dataset to which these events will be added to.


### `date_pattern` [v3.2.1-plugins-outputs-google_bigquery-date_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%Y-%m-%dT%H:00"`

Time pattern for BigQuery table, defaults to hourly tables. Must Time.strftime patterns: www.ruby-doc.org/core-2.0/Time.html#method-i-strftime


### `deleter_interval_secs` [v3.2.1-plugins-outputs-google_bigquery-deleter_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Deleter interval when checking if upload jobs are done for file deletion. This only affects how long files are on the hard disk after the job is done.


### `flush_interval_secs` [v3.2.1-plugins-outputs-google_bigquery-flush_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

Flush interval in seconds for flushing writes to log files. 0 will flush on every message.


### `ignore_unknown_values` [v3.2.1-plugins-outputs-google_bigquery-ignore_unknown_values]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false.


### `json_schema` [v3.2.1-plugins-outputs-google_bigquery-json_schema]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `nil`

Schema for log data, as a hash. Example: json_schema ⇒ { fields ⇒ [{ name ⇒ "timestamp" type ⇒ "TIMESTAMP" }, { name ⇒ "host" type ⇒ "STRING" }, { name ⇒ "message" type ⇒ "STRING" }] }


### `key_password` [v3.2.1-plugins-outputs-google_bigquery-key_password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"notasecret"`

Private key password for service account private key.


### `key_path` [v3.2.1-plugins-outputs-google_bigquery-key_path]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to private key file for Google Service Account.


### `project_id` [v3.2.1-plugins-outputs-google_bigquery-project_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Google Cloud Project ID (number, not Project Name!).


### `service_account` [v3.2.1-plugins-outputs-google_bigquery-service_account]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Service account to access Google APIs.


### `table_prefix` [v3.2.1-plugins-outputs-google_bigquery-table_prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

BigQuery table ID prefix to be used when creating new tables for log data. Table name will be <table_prefix><table_separator><date>


### `table_separator` [v3.2.1-plugins-outputs-google_bigquery-table_separator]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_"`

BigQuery table separator to be added between the table_prefix and the date suffix.


### `temp_directory` [v3.2.1-plugins-outputs-google_bigquery-temp_directory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Directory where temporary files are stored. Defaults to /tmp/logstash-bq-<random-suffix>


### `temp_file_prefix` [v3.2.1-plugins-outputs-google_bigquery-temp_file_prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash_bq"`

Temporary local file prefix. Log file will follow the format: <prefix>_hostname_date.part?.log


### `uploader_interval_secs` [v3.2.1-plugins-outputs-google_bigquery-uploader_interval_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Uploader interval when uploading new files to BigQuery. Adjust time based on your time pattern (for example, for hourly files, this interval can be around one hour).



## Common options [v3.2.1-plugins-outputs-google_bigquery-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-2-1-plugins-outputs-google_bigquery.md#v3.2.1-plugins-outputs-google_bigquery-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.2.1-plugins-outputs-google_bigquery-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.2.1-plugins-outputs-google_bigquery-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.2.1-plugins-outputs-google_bigquery-id]

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



