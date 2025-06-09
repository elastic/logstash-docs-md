---
navigation_title: "v2.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.2.0-plugins-inputs-kinesis.html
---

# Kinesis input plugin v2.2.0 [v2.2.0-plugins-inputs-kinesis]

* Plugin version: v2.2.0
* Released on: 2021-06-28
* [Changelog](https://github.com/logstash-plugins/logstash-input-kinesis/blob/v2.2.0/CHANGELOG.md)

For other versions, see the [overview list](input-kinesis-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_712]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-kinesis). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_706]

You can use this plugin to receive events through [AWS Kinesis](http://docs.aws.amazon.com/kinesis/latest/dev/introduction.html). This plugin uses the [Java Kinesis Client Library](http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-record-processor-implementation-app-java.html). The documentation at <https://github.com/awslabs/amazon-kinesis-client> will be useful.

AWS credentials can be specified either through environment variables, or an IAM instance role. The library uses a DynamoDB table for worker coordination, so you’ll need to grant access to that as well as to the Kinesis stream. The DynamoDB table has the same name as the `application_name` configuration option, which defaults to "logstash".

The library can optionally also send worker statistics to CloudWatch.

## Usage [v2.2.0-plugins-inputs-kinesis-usage]

```
input {
  kinesis {
    kinesis_stream_name => "my-logging-stream"
    codec => json { }
  }
}
```

## Using with CloudWatch Logs [v2.2.0-plugins-inputs-kinesis-cloudwatch]

If you want to read a CloudWatch Logs subscription stream, you’ll also need to install and configure the [CloudWatch Logs Codec](https://github.com/threadwaste/logstash-codec-cloudwatch_logs).

## Authentication [v2.2.0-plugins-inputs-kinesis-authentication]

This plugin uses the default AWS SDK auth chain, [DefaultAWSCredentialsProviderChain](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/DefaultAWSCredentialsProviderChain.html), to determine which credentials the client will use, unless `profile` is set, in which case [ProfileCredentialsProvider](http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/profile/ProfileCredentialsProvider.html) is used.

The default chain reads the credentials in this order:

* `AWS_ACCESS_KEY_ID` / `AWS_SECRET_KEY` environment variables
* `~/.aws/credentials` credentials file
* EC2 instance profile

The credentials need access to the following services:

* AWS Kinesis
* AWS DynamoDB. The client library stores information for worker coordination in DynamoDB (offsets and active worker per partition)
* AWS CloudWatch. If the metrics are enabled the credentials need CloudWatch update permissions granted.

See the [AWS documentation](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/auth/DefaultAWSCredentialsProviderChain.html) for more information on the default chain.

## Kinesis Input Configuration Options [v2.2.0-plugins-inputs-kinesis-options]

This plugin supports the following configuration options plus the [Common options](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`application_name`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-application_name) | [string](/lsr/value-types.md#string) | No |
| [`checkpoint_interval_seconds`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-checkpoint_interval_seconds) | [number](/lsr/value-types.md#number) | No |
| [`http_proxy`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-http_proxy) | [string](/lsr/value-types.md#string) | No |
| [`initial_position_in_stream`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-initial_position_in_stream) | [string](/lsr/value-types.md#string) | No |
| [`kinesis_stream_name`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-kinesis_stream_name) | [string](/lsr/value-types.md#string) | Yes |
| [`metrics`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-metrics) | [string](/lsr/value-types.md#string), one of `[nil, "cloudwatch"]` | No |
| [`non_proxy_hosts`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-non_proxy_hosts) | [string](/lsr/value-types.md#string) | No |
| [`profile`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-profile) | [string](/lsr/value-types.md#string) | No |
| [`region`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-region) | [string](/lsr/value-types.md#string) | No |
| [`role_arn`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-role_arn) | [string](/lsr/value-types.md#string) | No |
| [`role_session_name`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-role_session_name) | [string](/lsr/value-types.md#string) | No |
| [`additional_settings`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-additional_settings) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-common-options) for a list of options supported by all input plugins.

### `application_name` [v2.2.0-plugins-inputs-kinesis-application_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

The application name used for the dynamodb coordination table. Must be unique for this kinesis stream.

### `checkpoint_interval_seconds` [v2.2.0-plugins-inputs-kinesis-checkpoint_interval_seconds]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

How many seconds between worker checkpoints to dynamodb.

### `http_proxy` [v2.2.0-plugins-inputs-kinesis-http_proxy]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Proxy support for Kinesis, DynamoDB, and CloudWatch (if enabled).

### `initial_position_in_stream` [v2.2.0-plugins-inputs-kinesis-initial_position_in_stream]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"TRIM_HORIZON"`

The value for initialPositionInStream. Accepts "TRIM\_HORIZON" or "LATEST".

### `kinesis_stream_name` [v2.2.0-plugins-inputs-kinesis-kinesis_stream_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The kinesis stream name.

### `metrics` [v2.2.0-plugins-inputs-kinesis-metrics]

* Value can be any of: \`\`, `cloudwatch`
* Default value is `nil`

Worker metric tracking. By default this is disabled, set it to "cloudwatch" to enable the cloudwatch integration in the Kinesis Client Library.

### `non_proxy_hosts` [v2.2.0-plugins-inputs-kinesis-non_proxy_hosts]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Hosts that should be excluded from proxying, separated by the "|" (pipe) character.

### `profile` [v2.2.0-plugins-inputs-kinesis-profile]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS profile name for authentication. This ensures that the `~/.aws/credentials` AWS auth provider is used. By default this is empty and the default chain will be used.

### `region` [v2.2.0-plugins-inputs-kinesis-region]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"us-east-1"`

The AWS region for Kinesis, DynamoDB, and CloudWatch (if enabled)

### `role_arn` [v2.2.0-plugins-inputs-kinesis-role_arn]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS role to assume. This can be used, for example, to access a Kinesis stream in a different AWS account. This role will be assumed after the default credentials or profile credentials are created. By default this is empty and a role will not be assumed.

### `role_session_name` [v2.2.0-plugins-inputs-kinesis-role_session_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `logstash`

Session name to use when assuming an IAM role. This is recorded in CloudTrail logs for example.

### `additional_settings` [v2.2.0-plugins-inputs-kinesis-additional_settings]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting

The KCL provides several configuration options which can be set in [KinesisClientLibConfiguration](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/coordinator/KinesisClientLibConfiguration.java). These options are configured via various function calls that all begin with `with`. Some of these functions take complex types, which are not supported. However, you may invoke any one of the `withX()` functions that take a primitive by providing key-value pairs in `snake_case`.

Example:

To set the dynamodb read and write capacity values, use these functions: `withInitialLeaseTableReadCapacity` and `withInitialLeaseTableWriteCapacity`.

```
additional_settings => {"initial_lease_table_read_capacity" => 25 "initial_lease_table_write_capacity" => 100}
```

## Common options [v2.2.0-plugins-inputs-kinesis-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v2-2-0-plugins-inputs-kinesis.md#v2.2.0-plugins-inputs-kinesis-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v2.2.0-plugins-inputs-kinesis-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v2.2.0-plugins-inputs-kinesis-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.2.0-plugins-inputs-kinesis-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.2.0-plugins-inputs-kinesis-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kinesis inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  kinesis {
    id => "my_plugin_id"
  }
}
```

### `tags` [v2.2.0-plugins-inputs-kinesis-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v2.2.0-plugins-inputs-kinesis-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
