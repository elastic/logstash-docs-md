---
navigation_title: "v4.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.3-plugins-outputs-sqs.html
---

# Sqs output plugin v4.0.3 [v4.0.3-plugins-outputs-sqs]

* Plugin version: v4.0.3
* Released on: 2017-08-18
* [Changelog](https://github.com/logstash-plugins/logstash-output-sqs/blob/v4.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-sqs-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1624]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-sqs). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1614]

Push events to an Amazon Web Services (AWS) Simple Queue Service (SQS) queue.

SQS is a simple, scalable queue system that is part of the Amazon Web Services suite of tools. Although SQS is similar to other queuing systems such as Advanced Message Queuing Protocol (AMQP), it uses a custom API and requires that you have an AWS account. See <http://aws.amazon.com/sqs/> for more details on how SQS works, what the pricing schedule looks like and how to setup a queue.

The "consumer" identity must have the following permissions on the queue:

* `sqs:GetQueueUrl`
* `sqs:SendMessage`
* `sqs:SendMessageBatch`

Typically, you should setup an IAM policy, create a user and apply the IAM policy to the user. See <http://aws.amazon.com/iam/> for more details on setting up AWS identities. A sample policy is as follows:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:GetQueueUrl",
        "sqs:SendMessage",
        "sqs:SendMessageBatch"
      ],
      "Resource": "arn:aws:sqs:us-east-1:123456789012:my-sqs-queue"
    }
  ]
}
```

## Batch Publishing [_batch_publishing_21]

This output publishes messages to SQS in batches in order to optimize event throughput and increase performance. This is done using the \[`SendMessageBatch`]\(<http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html>) API. When publishing messages to SQS in batches, the following service limits must be respected (see \[Limits in Amazon SQS]\(<http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html)>):

* The maximum allowed individual message size is 256KiB.
* The maximum total payload size (i.e. the sum of the sizes of all individual messages within a batch) is also 256KiB.

This plugin will dynamically adjust the size of the batch published to SQS in order to ensure that the total payload size does not exceed 256KiB.

This output cannot currently handle messages larger than 256KiB. Any single message exceeding this size will be dropped.

## Sqs Output Configuration Options [v4.0.3-plugins-outputs-sqs-options]

This plugin supports the following configuration options plus the [Common options](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`access_key_id`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-access_key_id) | [string](/lsr/value-types.md#string) | No |
| [`aws_credentials_file`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-aws_credentials_file) | [string](/lsr/value-types.md#string) | No |
| [`batch_events`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-batch_events) | [number](/lsr/value-types.md#number) | No |
| [`message_max_size`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-message_max_size) | [bytes](/lsr/value-types.md#bytes) | No |
| [`proxy_uri`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-proxy_uri) | [string](/lsr/value-types.md#string) | No |
| [`queue`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-queue) | [string](/lsr/value-types.md#string) | Yes |
| [`region`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-region) | [string](/lsr/value-types.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`secret_access_key`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-secret_access_key) | [string](/lsr/value-types.md#string) | No |
| [`session_token`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-session_token) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-common-options) for a list of options supported by all output plugins.

### `access_key_id` [v4.0.3-plugins-outputs-sqs-access_key_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)

### `aws_credentials_file` [v4.0.3-plugins-outputs-sqs-aws_credentials_file]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```
    :access_key_id: "12345"
    :secret_access_key: "54321"
```

### `batch` (DEPRECATED) [v4.0.3-plugins-outputs-sqs-batch]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Set to `true` to send messages to SQS in batches (with the `SendMessageBatch` API) or `false` to send messages to SQS individually (with the `SendMessage` API). The size of the batch is configurable via `batch_events`.

### `batch_events` [v4.0.3-plugins-outputs-sqs-batch_events]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

The number of events to be sent in each batch. Set this to `1` to disable the batch sending of messages.

### `batch_timeout` (DEPRECATED) [v4.0.3-plugins-outputs-sqs-batch_timeout]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

### `message_max_size` [v4.0.3-plugins-outputs-sqs-message_max_size]

* Value type is [bytes](/lsr/value-types.md#bytes)
* Default value is `"256KiB"`

The maximum number of bytes for any message sent to SQS. Messages exceeding this size will be dropped. See <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html>.

### `proxy_uri` [v4.0.3-plugins-outputs-sqs-proxy_uri]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

URI to proxy server if required

### `queue` [v4.0.3-plugins-outputs-sqs-queue]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the target SQS queue. Note that this is just the name of the queue, not the URL or ARN.

### `region` [v4.0.3-plugins-outputs-sqs-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region

### `secret_access_key` [v4.0.3-plugins-outputs-sqs-secret_access_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Secret Access Key

### `session_token` [v4.0.3-plugins-outputs-sqs-session_token]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential

## Common options [v4.0.3-plugins-outputs-sqs-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-3-plugins-outputs-sqs.md#v4.0.3-plugins-outputs-sqs-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v4.0.3-plugins-outputs-sqs-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.3-plugins-outputs-sqs-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.3-plugins-outputs-sqs-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 sqs outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  sqs {
    id => "my_plugin_id"
  }
}
```
