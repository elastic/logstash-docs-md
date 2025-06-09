---
navigation_title: "v4.0.12"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.12-plugins-outputs-s3.html
---

# S3 output plugin v4.0.12 [v4.0.12-plugins-outputs-s3]

* Plugin version: v4.0.12
* Released on: 2017-10-14
* [Changelog](https://github.com/logstash-plugins/logstash-output-s3/blob/v4.0.12/CHANGELOG.md)

For other versions, see the [overview list](output-s3-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1573]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-s3). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1563]

This plugin batches and uploads logstash events into Amazon Simple Storage Service (Amazon S3).

Requirements:

* Amazon S3 Bucket and S3 Access Permissions (Typically access\_key\_id and secret\_access\_key)
* S3 PutObject permission

S3 outputs create temporary files into the OS' temporary directory, you can specify where to save them using the `temporary_directory` option.

S3 output files have the following format

ls.s3.312bc026-2f5d-49bc-ae9f-5940cf4ad9a6.2013-04-18T10.00.tag\_hello.part0.txt

| | | |
| :- | :- | :- |
| ls.s3 | indicate logstash plugin s3 | |
| 312bc026-2f5d-49bc-ae9f-5940cf4ad9a6 | a new, random uuid per file. | |
| 2013-04-18T10.00 | represents the time whenever you specify time\_file. | |
| tag\_hello | this indicates the event’s tag. | |
| part0 | this means if you indicate size\_file then it will generate more parts if you file.size > size\_file. When a file is full it will be pushed to the bucket and then deleted from the temporary directory. If a file is empty, it is simply deleted. Empty files will not be pushed | |

### Crash Recovery [_crash_recovery_37]

This plugin will recover and upload temporary log files after crash/abnormal termination when using `restore` set to true

### Usage [_usage_124]

This is an example of logstash config:

```
output {
   s3{
     access_key_id => "crazy_key"             (required)
     secret_access_key => "monkey_access_key" (required)
     region => "eu-west-1"                    (optional, default = "us-east-1")
     bucket => "your_bucket"                  (required)
     size_file => 2048                        (optional) - Bytes
     time_file => 5                           (optional) - Minutes
     codec => "plain"                         (optional)
     canned_acl => "private"                  (optional. Options are "private", "public-read", "public-read-write", "authenticated-read". Defaults to "private" )
   }
```

## S3 Output Configuration Options [v4.0.12-plugins-outputs-s3-options]

This plugin supports the following configuration options plus the [Common options](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`access_key_id`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-access_key_id) | [string](/lsr/value-types.md#string) | No |
| [`aws_credentials_file`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-aws_credentials_file) | [string](/lsr/value-types.md#string) | No |
| [`bucket`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-bucket) | [string](/lsr/value-types.md#string) | Yes |
| [`canned_acl`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-canned_acl) | [string](/lsr/value-types.md#string), one of `["private", "public-read", "public-read-write", "authenticated-read"]` | No |
| [`encoding`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-encoding) | [string](/lsr/value-types.md#string), one of `["none", "gzip"]` | No |
| [`prefix`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-prefix) | [string](/lsr/value-types.md#string) | No |
| [`proxy_uri`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-proxy_uri) | [string](/lsr/value-types.md#string) | No |
| [`region`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-region) | [string](/lsr/value-types.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`restore`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-restore) | [boolean](/lsr/value-types.md#boolean) | No |
| [`rotation_strategy`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-rotation_strategy) | [string](/lsr/value-types.md#string), one of `["size_and_time", "size", "time"]` | No |
| [`secret_access_key`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-secret_access_key) | [string](/lsr/value-types.md#string) | No |
| [`server_side_encryption`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-server_side_encryption) | [boolean](/lsr/value-types.md#boolean) | No |
| [`server_side_encryption_algorithm`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-server_side_encryption_algorithm) | [string](/lsr/value-types.md#string), one of `["AES256", "aws:kms"]` | No |
| [`session_token`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-session_token) | [string](/lsr/value-types.md#string) | No |
| [`signature_version`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-signature_version) | [string](/lsr/value-types.md#string), one of `["v2", "v4"]` | No |
| [`size_file`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-size_file) | [number](/lsr/value-types.md#number) | No |
| [`ssekms_key_id`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-ssekms_key_id) | [string](/lsr/value-types.md#string) | No |
| [`storage_class`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-storage_class) | [string](/lsr/value-types.md#string), one of `["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"]` | No |
| [`temporary_directory`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-temporary_directory) | [string](/lsr/value-types.md#string) | No |
| [`time_file`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-time_file) | [number](/lsr/value-types.md#number) | No |
| [`upload_queue_size`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-upload_queue_size) | [number](/lsr/value-types.md#number) | No |
| [`upload_workers_count`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-upload_workers_count) | [number](/lsr/value-types.md#number) | No |
| [`validate_credentials_on_root_bucket`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-validate_credentials_on_root_bucket) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-common-options) for a list of options supported by all output plugins.

### `access_key_id` [v4.0.12-plugins-outputs-s3-access_key_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)

### `aws_credentials_file` [v4.0.12-plugins-outputs-s3-aws_credentials_file]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```
    :access_key_id: "12345"
    :secret_access_key: "54321"
```

### `bucket` [v4.0.12-plugins-outputs-s3-bucket]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

S3 bucket

### `canned_acl` [v4.0.12-plugins-outputs-s3-canned_acl]

* Value can be any of: `private`, `public-read`, `public-read-write`, `authenticated-read`
* Default value is `"private"`

The S3 canned ACL to use when putting the file. Defaults to "private".

### `encoding` [v4.0.12-plugins-outputs-s3-encoding]

* Value can be any of: `none`, `gzip`
* Default value is `"none"`

Specify the content encoding. Supports ("gzip"). Defaults to "none"

### `prefix` [v4.0.12-plugins-outputs-s3-prefix]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Specify a prefix to the uploaded filename, this can simulate directories on S3. Prefix does not require leading slash. This option support string interpolation, be warned this can created a lot of temporary local files.

### `proxy_uri` [v4.0.12-plugins-outputs-s3-proxy_uri]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

URI to proxy server if required

### `region` [v4.0.12-plugins-outputs-s3-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region

### `restore` [v4.0.12-plugins-outputs-s3-restore]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

### `rotation_strategy` [v4.0.12-plugins-outputs-s3-rotation_strategy]

* Value can be any of: `size_and_time`, `size`, `time`
* Default value is `"size_and_time"`

Define the strategy to use to decide when we need to rotate the file and push it to S3, The default strategy is to check for both size and time, the first one to match will rotate the file.

### `secret_access_key` [v4.0.12-plugins-outputs-s3-secret_access_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Secret Access Key

### `server_side_encryption` [v4.0.12-plugins-outputs-s3-server_side_encryption]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Specifies wether or not to use S3’s server side encryption. Defaults to no encryption.

### `server_side_encryption_algorithm` [v4.0.12-plugins-outputs-s3-server_side_encryption_algorithm]

* Value can be any of: `AES256`, `aws:kms`
* Default value is `"AES256"`

Specifies what type of encryption to use when SSE is enabled.

### `session_token` [v4.0.12-plugins-outputs-s3-session_token]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential

### `signature_version` [v4.0.12-plugins-outputs-s3-signature_version]

* Value can be any of: `v2`, `v4`
* There is no default value for this setting.

The version of the S3 signature hash to use. Normally uses the internal client default, can be explicitly specified here

### `size_file` [v4.0.12-plugins-outputs-s3-size_file]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5242880`

Set the size of file in bytes, this means that files on bucket when have dimension > file\_size, they are stored in two or more file. If you have tags then it will generate a specific size file for every tags

### `ssekms_key_id` [v4.0.12-plugins-outputs-s3-ssekms_key_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The key to use when specified along with server\_side\_encryption ⇒ aws:kms. If server\_side\_encryption ⇒ aws:kms is set but this is not default KMS key is used. <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>

### `storage_class` [v4.0.12-plugins-outputs-s3-storage_class]

* Value can be any of: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`
* Default value is `"STANDARD"`

Specifies what S3 storage class to use when uploading the file. More information about the different storage classes can be found: <http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html> Defaults to STANDARD.

### `temporary_directory` [v4.0.12-plugins-outputs-s3-temporary_directory]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"/tmp/logstash"`

Set the directory where logstash will store the tmp files before sending it to S3 default to the current OS temporary directory in linux /tmp/logstash

### `time_file` [v4.0.12-plugins-outputs-s3-time_file]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `15`

Set the time, in MINUTES, to close the current sub\_time\_section of bucket. If you define file\_size you have a number of files in consideration of the section and the current tag. 0 stay all time on listerner, beware if you specific 0 and size\_file 0, because you will not put the file on bucket, for now the only thing this plugin can do is to put the file when logstash restart.

### `upload_queue_size` [v4.0.12-plugins-outputs-s3-upload_queue_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `4`

Number of items we can keep in the local queue before uploading them

### `upload_workers_count` [v4.0.12-plugins-outputs-s3-upload_workers_count]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `4`

Specify how many workers to use to upload the files to S3

### `validate_credentials_on_root_bucket` [v4.0.12-plugins-outputs-s3-validate_credentials_on_root_bucket]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

The common use case is to define permission on the root bucket and give Logstash full access to write its logs. In some circonstances you need finer grained permission on subfolder, this allow you to disable the check at startup.

## Common options [v4.0.12-plugins-outputs-s3-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-12-plugins-outputs-s3.md#v4.0.12-plugins-outputs-s3-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v4.0.12-plugins-outputs-s3-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.12-plugins-outputs-s3-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.12-plugins-outputs-s3-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 s3 outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  s3 {
    id => "my_plugin_id"
  }
}
```
