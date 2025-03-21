---
navigation_title: "v4.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.3.0-plugins-outputs-s3.html
---

# S3 output plugin v4.3.0 [v4.3.0-plugins-outputs-s3]


* Plugin version: v4.3.0
* Released on: 2020-02-11
* [Changelog](https://github.com/logstash-plugins/logstash-output-s3/blob/v4.3.0/CHANGELOG.md)

For other versions, see the [overview list](output-s3-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1548]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-s3). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1538]

This plugin batches and uploads logstash events into Amazon Simple Storage Service (Amazon S3).

S3 outputs create temporary files into the OS' temporary directory. You can specify where to save them using the `temporary_directory` option.

::::{important}
For configurations containing multiple s3 outputs with the restore option enabled, each output should define its own *temporary_directory*.
::::


### Requirements [_requirements_21]

* Amazon S3 Bucket and S3 Access Permissions (Typically access_key_id and secret_access_key)
* S3 PutObject permission


### S3 output file [_s3_output_file_21]

```txt
`ls.s3.312bc026-2f5d-49bc-ae9f-5940cf4ad9a6.2013-04-18T10.00.tag_hello.part0.txt`
```

|     |     |     |
| --- | --- | --- |
| ls.s3 | indicates logstash plugin s3 |  |
| 312bc026-2f5d-49bc-ae9f-5940cf4ad9a6 | a new, random uuid per file. |  |
| 2013-04-18T10.00 | represents the time whenever you specify time_file. |  |
| tag_hello | indicates the event’s tag. |  |
| part0 | If you indicate size_file, it will generate more parts if your file.size > size_file.When a file is full, it gets pushed to the bucket and then deleted from the temporary directory.If a file is empty, it is simply deleted.  Empty files will not be pushed. |  |


### Crash Recovery [_crash_recovery_21]

This plugin will recover and upload temporary log files after crash/abnormal termination when using `restore` set to true


### Usage [_usage_106]

This is an example of logstash config:

```ruby
output {
   s3{
     access_key_id => "crazy_key"             (optional)
     secret_access_key => "monkey_access_key" (optional)
     region => "eu-west-1"                    (optional, default = "us-east-1")
     bucket => "your_bucket"                  (required)
     size_file => 2048                        (optional) - Bytes
     time_file => 5                           (optional) - Minutes
     codec => "plain"                         (optional)
     canned_acl => "private"                  (optional. Options are "private", "public-read", "public-read-write", "authenticated-read", "aws-exec-read", "bucket-owner-read", "bucket-owner-full-control", "log-delivery-write". Defaults to "private" )
   }
```



## S3 Output Configuration Options [v4.3.0-plugins-outputs-s3-options]

This plugin supports the following configuration options plus the [Common options](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_key_id`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-access_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`additional_settings`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-additional_settings) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`aws_credentials_file`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-aws_credentials_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`bucket`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-bucket) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`canned_acl`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-canned_acl) | [string](logstash://reference/configuration-file-structure.md#string), one of `["private", "public-read", "public-read-write", "authenticated-read", "aws-exec-read", "bucket-owner-read", "bucket-owner-full-control", "log-delivery-write"]` | No |
| [`encoding`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-encoding) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "gzip"]` | No |
| [`endpoint`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-endpoint) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`prefix`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`proxy_uri`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-proxy_uri) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`region`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-region) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`restore`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-restore) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`retry_count`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-retry_count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_delay`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-retry_delay) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`role_arn`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-role_arn) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`role_session_name`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-role_session_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`rotation_strategy`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-rotation_strategy) | [string](logstash://reference/configuration-file-structure.md#string), one of `["size_and_time", "size", "time"]` | No |
| [`secret_access_key`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-secret_access_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`server_side_encryption`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-server_side_encryption) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`server_side_encryption_algorithm`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-server_side_encryption_algorithm) | [string](logstash://reference/configuration-file-structure.md#string), one of `["AES256", "aws:kms"]` | No |
| [`session_token`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-session_token) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`signature_version`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-signature_version) | [string](logstash://reference/configuration-file-structure.md#string), one of `["v2", "v4"]` | No |
| [`size_file`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-size_file) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssekms_key_id`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-ssekms_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`storage_class`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-storage_class) | [string](logstash://reference/configuration-file-structure.md#string), one of `["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA", "ONEZONE_IA"]` | No |
| [`temporary_directory`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-temporary_directory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`time_file`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-time_file) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`upload_multipart_threshold`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-upload_multipart_threshold) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`upload_queue_size`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-upload_queue_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`upload_workers_count`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-upload_workers_count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`validate_credentials_on_root_bucket`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-validate_credentials_on_root_bucket) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-common-options) for a list of options supported by all output plugins.

 

### `access_key_id` [v4.3.0-plugins-outputs-s3-access_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)


### `additional_settings` [v4.3.0-plugins-outputs-s3-additional_settings]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Key-value pairs of settings and corresponding values used to parametrize the connection to S3. See full list in [the AWS SDK documentation](https://docs.aws.amazon.com/sdkforruby/api/Aws/S3/Client.html). Example:

```ruby
    output {
      s3 {
        access_key_id => "1234",
        secret_access_key => "secret",
        region => "eu-west-1",
        bucket => "logstash-test",
        additional_settings => {
          "force_path_style" => true,
          "follow_redirects" => false
        }
      }
    }
```


### `aws_credentials_file` [v4.3.0-plugins-outputs-s3-aws_credentials_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```ruby
    :access_key_id: "12345"
    :secret_access_key: "54321"
```


### `bucket` [v4.3.0-plugins-outputs-s3-bucket]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

S3 bucket


### `canned_acl` [v4.3.0-plugins-outputs-s3-canned_acl]

* Value can be any of: `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, `bucket-owner-full-control`, `log-delivery-write`
* Default value is `"private"`

The S3 canned ACL to use when putting the file. Defaults to "private".


### `encoding` [v4.3.0-plugins-outputs-s3-encoding]

* Value can be any of: `none`, `gzip`
* Default value is `"none"`

Specify the content encoding. Supports ("gzip"). Defaults to "none"


### `endpoint` [v4.3.0-plugins-outputs-s3-endpoint]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The endpoint to connect to. By default it is constructed using the value of `region`. This is useful when connecting to S3 compatible services, but beware that these aren’t guaranteed to work correctly with the AWS SDK. The endpoint should be an HTTP or HTTPS URL, e.g. [https://example.com](https://example.com)


### `prefix` [v4.3.0-plugins-outputs-s3-prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Specify a prefix to the uploaded filename, this can simulate directories on S3.  Prefix does not require leading slash. This option supports logstash interpolation: [/logstash/docs/reference/ingestion-tools/logstash/event-dependent-configuration.md#sprintf](logstash://reference/event-dependent-configuration.md#sprintf); for example, files can be prefixed with the event date using `prefix = "%{+YYYY}/%{+MM}/%{+dd}"`. Be warned this can create a lot of temporary local files.


### `proxy_uri` [v4.3.0-plugins-outputs-s3-proxy_uri]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URI to proxy server if required


### `region` [v4.3.0-plugins-outputs-s3-region]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"us-east-1"`

The AWS Region


### `restore` [v4.3.0-plugins-outputs-s3-restore]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Used to enable recovery after crash/abnormal termination. Temporary log files will be recovered and uploaded.


### `retry_count` [v4.3.0-plugins-outputs-s3-retry_count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `Infinity`

Allows to limit number of retries when S3 uploading fails.


### `retry_delay` [v4.3.0-plugins-outputs-s3-retry_delay]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Delay (in seconds) to wait between consecutive retries on upload failures.


### `role_arn` [v4.3.0-plugins-outputs-s3-role_arn]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS IAM Role to assume, if any. This is used to generate temporary credentials, typically for cross-account access. See the [AssumeRole API documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) for more information.


### `role_session_name` [v4.3.0-plugins-outputs-s3-role_session_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

Session name to use when assuming an IAM role.


### `rotation_strategy` [v4.3.0-plugins-outputs-s3-rotation_strategy]

* Value can be any of: `size_and_time`, `size`, `time`
* Default value is `"size_and_time"`

Define the strategy to use to decide when we need to rotate the file and push it to S3, The default strategy is to check for both size and time, the first one to match will rotate the file.


### `secret_access_key` [v4.3.0-plugins-outputs-s3-secret_access_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Secret Access Key


### `server_side_encryption` [v4.3.0-plugins-outputs-s3-server_side_encryption]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Specifies whether or not to use S3’s server side encryption. Defaults to no encryption.


### `server_side_encryption_algorithm` [v4.3.0-plugins-outputs-s3-server_side_encryption_algorithm]

* Value can be any of: `AES256`, `aws:kms`
* Default value is `"AES256"`

Specifies what type of encryption to use when SSE is enabled.


### `session_token` [v4.3.0-plugins-outputs-s3-session_token]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential


### `signature_version` [v4.3.0-plugins-outputs-s3-signature_version]

* Value can be any of: `v2`, `v4`
* There is no default value for this setting.

The version of the S3 signature hash to use. Normally uses the internal client default, can be explicitly specified here


### `size_file` [v4.3.0-plugins-outputs-s3-size_file]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5242880`

Set the size of file in bytes, this means that files on bucket when dimension > file_size, are stored in two or more files. If you have tags then it will generate a specific size file for every tags


### `ssekms_key_id` [v4.3.0-plugins-outputs-s3-ssekms_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The key to use when specified along with server_side_encryption ⇒ aws:kms. If server_side_encryption ⇒ aws:kms is set but this is not default KMS key is used. [http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html)


### `storage_class` [v4.3.0-plugins-outputs-s3-storage_class]

* Value can be any of: `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`
* Default value is `"STANDARD"`

Specifies what S3 storage class to use when uploading the file. More information about the different storage classes can be found: [http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) Defaults to STANDARD.


### `temporary_directory` [v4.3.0-plugins-outputs-s3-temporary_directory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/tmp/logstash"`

Set the directory where logstash will store the tmp files before sending it to S3 default to the current OS temporary directory in linux /tmp/logstash


### `time_file` [v4.3.0-plugins-outputs-s3-time_file]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `15`

Set the time, in MINUTES, to close the current sub_time_section of bucket. If you define file_size you have a number of files in consideration of the section and the current tag. 0 stay all time on listener, beware if you specific 0 and size_file 0, because you will not put the file on bucket, for now the only thing this plugin can do is to put the file when logstash restart.


### `upload_multipart_threshold` [v4.3.0-plugins-outputs-s3-upload_multipart_threshold]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `15728640`

Files larger than this number are uploaded using the S3 multipart APIs


### `upload_queue_size` [v4.3.0-plugins-outputs-s3-upload_queue_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `4`

Number of items we can keep in the local queue before uploading them


### `upload_workers_count` [v4.3.0-plugins-outputs-s3-upload_workers_count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `4`

Specify how many workers to use to upload the files to S3


### `validate_credentials_on_root_bucket` [v4.3.0-plugins-outputs-s3-validate_credentials_on_root_bucket]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

The common use case is to define permission on the root bucket and give Logstash full access to write its logs. In some circumstances you need finer grained permission on subfolder, this allows you to disable the check at startup.



## Common options [v4.3.0-plugins-outputs-s3-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-3-0-plugins-outputs-s3.md#v4.3.0-plugins-outputs-s3-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.3.0-plugins-outputs-s3-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"line"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.3.0-plugins-outputs-s3-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.3.0-plugins-outputs-s3-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 s3 outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  s3 {
    id => "my_plugin_id"
  }
}
```



