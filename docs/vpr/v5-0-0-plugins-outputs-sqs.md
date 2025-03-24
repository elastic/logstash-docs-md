---
navigation_title: "v5.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.0-plugins-outputs-sqs.html
---

# Sqs output plugin v5.0.0 [v5.0.0-plugins-outputs-sqs]


* Plugin version: v5.0.0
* Released on: 2017-08-01
* [Changelog](https://github.com/logstash-plugins/logstash-output-sqs/blob/v5.0.0/CHANGELOG.md)

For other versions, see the [overview list](output-sqs-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1608]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-sqs). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1598]

Push events to an Amazon Web Services (AWS) Simple Queue Service (SQS) queue.

SQS is a simple, scalable queue system that is part of the Amazon Web Services suite of tools. Although SQS is similar to other queuing systems such as Advanced Message Queuing Protocol (AMQP), it uses a custom API and requires that you have an AWS account. See [http://aws.amazon.com/sqs/](http://aws.amazon.com/sqs/) for more details on how SQS works, what the pricing schedule looks like and how to setup a queue.

The "consumer" identity must have the following permissions on the queue:

* `sqs:GetQueueUrl`
* `sqs:SendMessage`
* `sqs:SendMessageBatch`

Typically, you should setup an IAM policy, create a user and apply the IAM policy to the user. See [http://aws.amazon.com/iam/](http://aws.amazon.com/iam/) for more details on setting up AWS identities. A sample policy is as follows:

```json
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


## Batch Publishing [_batch_publishing_18]

This output publishes messages to SQS in batches in order to optimize event throughput and increase performance. This is done using the [`SendMessageBatch`](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) API. When publishing messages to SQS in batches, the following service limits must be respected (see [Limits in Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html)):

* The maximum allowed individual message size is 256KiB.
* The maximum total payload size (i.e. the sum of the sizes of all individual messages within a batch) is also 256KiB.

This plugin will dynamically adjust the size of the batch published to SQS in order to ensure that the total payload size does not exceed 256KiB.

::::{warning}
This output cannot currently handle messages larger than 256KiB. Any single message exceeding this size will be dropped.
::::



## Sqs Output Configuration Options [v5.0.0-plugins-outputs-sqs-options]

This plugin supports the following configuration options plus the [Common options](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_key_id`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-access_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`aws_credentials_file`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-aws_credentials_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`batch_events`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-batch_events) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`message_max_size`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-message_max_size) | [bytes](logstash://reference/configuration-file-structure.md#bytes) | No |
| [`proxy_uri`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-proxy_uri) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`queue`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-queue) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`region`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-region) | [string](logstash://reference/configuration-file-structure.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`secret_access_key`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-secret_access_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`session_token`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-session_token) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-common-options) for a list of options supported by all output plugins.

 

### `access_key_id` [v5.0.0-plugins-outputs-sqs-access_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)


### `aws_credentials_file` [v5.0.0-plugins-outputs-sqs-aws_credentials_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```ruby
    :access_key_id: "12345"
    :secret_access_key: "54321"
```


### `batch_events` [v5.0.0-plugins-outputs-sqs-batch_events]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

The number of events to be sent in each batch. Set this to `1` to disable the batch sending of messages.


### `message_max_size` [v5.0.0-plugins-outputs-sqs-message_max_size]

* Value type is [bytes](logstash://reference/configuration-file-structure.md#bytes)
* Default value is `"256KiB"`

The maximum number of bytes for any message sent to SQS. Messages exceeding this size will be dropped. See [http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html).


### `proxy_uri` [v5.0.0-plugins-outputs-sqs-proxy_uri]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URI to proxy server if required


### `queue` [v5.0.0-plugins-outputs-sqs-queue]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the target SQS queue. Note that this is just the name of the queue, not the URL or ARN.


### `region` [v5.0.0-plugins-outputs-sqs-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region


### `secret_access_key` [v5.0.0-plugins-outputs-sqs-secret_access_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Secret Access Key


### `session_token` [v5.0.0-plugins-outputs-sqs-session_token]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential



## Common options [v5.0.0-plugins-outputs-sqs-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v5-0-0-plugins-outputs-sqs.md#v5.0.0-plugins-outputs-sqs-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v5.0.0-plugins-outputs-sqs-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v5.0.0-plugins-outputs-sqs-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v5.0.0-plugins-outputs-sqs-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 sqs outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  sqs {
    id => "my_plugin_id"
  }
}
```



