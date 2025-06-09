---
navigation_title: "v3.1.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.7-plugins-inputs-s3.html
---

# S3 input plugin v3.1.7 [v3.1.7-plugins-inputs-s3]

* Plugin version: v3.1.7
* Released on: 2017-10-03
* [Changelog](https://github.com/logstash-plugins/logstash-input-s3/blob/v3.1.7/CHANGELOG.md)

For other versions, see the [overview list](input-s3-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_838]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-s3). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_831]

Stream events from files from a S3 bucket.

Each line from each file generates an event. Files ending in `.gz` are handled as gzip’ed files.

## S3 Input Configuration Options [v3.1.7-plugins-inputs-s3-options]

This plugin supports the following configuration options plus the [Common options](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`access_key_id`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-access_key_id) | [string](/lsr/value-types.md#string) | No |
| [`aws_credentials_file`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-aws_credentials_file) | [string](/lsr/value-types.md#string) | No |
| [`backup_add_prefix`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-backup_add_prefix) | [string](/lsr/value-types.md#string) | No |
| [`backup_to_bucket`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-backup_to_bucket) | [string](/lsr/value-types.md#string) | No |
| [`backup_to_dir`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-backup_to_dir) | [string](/lsr/value-types.md#string) | No |
| [`bucket`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-bucket) | [string](/lsr/value-types.md#string) | Yes |
| [`delete`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-delete) | [boolean](/lsr/value-types.md#boolean) | No |
| [`exclude_pattern`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-exclude_pattern) | [string](/lsr/value-types.md#string) | No |
| [`interval`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-interval) | [number](/lsr/value-types.md#number) | No |
| [`prefix`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-prefix) | [string](/lsr/value-types.md#string) | No |
| [`proxy_uri`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-proxy_uri) | [string](/lsr/value-types.md#string) | No |
| [`region`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-region) | [string](/lsr/value-types.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`secret_access_key`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-secret_access_key) | [string](/lsr/value-types.md#string) | No |
| [`session_token`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-session_token) | [string](/lsr/value-types.md#string) | No |
| [`sincedb_path`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-sincedb_path) | [string](/lsr/value-types.md#string) | No |
| [`temporary_directory`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-temporary_directory) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-common-options) for a list of options supported by all input plugins.

### `access_key_id` [v3.1.7-plugins-inputs-s3-access_key_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)

### `aws_credentials_file` [v3.1.7-plugins-inputs-s3-aws_credentials_file]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```
    :access_key_id: "12345"
    :secret_access_key: "54321"
```

### `backup_add_prefix` [v3.1.7-plugins-inputs-s3-backup_add_prefix]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Append a prefix to the key (full path including file name in s3) after processing. If backing up to another (or the same) bucket, this effectively lets you choose a new *folder* to place the files in

### `backup_to_bucket` [v3.1.7-plugins-inputs-s3-backup_to_bucket]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Name of a S3 bucket to backup processed files to.

### `backup_to_dir` [v3.1.7-plugins-inputs-s3-backup_to_dir]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Path of a local directory to backup processed files to.

### `bucket` [v3.1.7-plugins-inputs-s3-bucket]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the S3 bucket.

### `delete` [v3.1.7-plugins-inputs-s3-delete]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Whether to delete processed files from the original bucket.

### `exclude_pattern` [v3.1.7-plugins-inputs-s3-exclude_pattern]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Ruby style regexp of keys to exclude from the bucket

### `interval` [v3.1.7-plugins-inputs-s3-interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Interval to wait between to check the file list again after a run is finished. Value is in seconds.

### `prefix` [v3.1.7-plugins-inputs-s3-prefix]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

If specified, the prefix of filenames in the bucket must match (not a regexp)

### `proxy_uri` [v3.1.7-plugins-inputs-s3-proxy_uri]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

URI to proxy server if required

### `region` [v3.1.7-plugins-inputs-s3-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region

### `secret_access_key` [v3.1.7-plugins-inputs-s3-secret_access_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Secret Access Key

### `session_token` [v3.1.7-plugins-inputs-s3-session_token]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential

### `sincedb_path` [v3.1.7-plugins-inputs-s3-sincedb_path]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Where to write the since database (keeps track of the date the last handled file was added to S3). The default will write sincedb files to some path matching "$HOME/.sincedb\*" Should be a path with filename not just a directory.

### `temporary_directory` [v3.1.7-plugins-inputs-s3-temporary_directory]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"/tmp/logstash"`

Set the directory where logstash will store the tmp files before processing them. default to the current OS temporary directory in linux /tmp/logstash

## Common options [v3.1.7-plugins-inputs-s3-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-1-7-plugins-inputs-s3.md#v3.1.7-plugins-inputs-s3-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.1.7-plugins-inputs-s3-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.1.7-plugins-inputs-s3-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.7-plugins-inputs-s3-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.7-plugins-inputs-s3-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 s3 inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  s3 {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.1.7-plugins-inputs-s3-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.1.7-plugins-inputs-s3-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
