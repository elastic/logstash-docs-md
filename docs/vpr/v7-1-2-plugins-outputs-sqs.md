---
navigation_title: "v7.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v7.1.2-plugins-outputs-sqs.html
---

# Sqs output plugin v7.1.2 [v7.1.2-plugins-outputs-sqs]


* A component of the [aws integration plugin](integration-aws-index.md)
* Integration version: v7.1.2
* Released on: 2023-06-08
* [Changelog](https://github.com/logstash-plugins/logstash-integration-aws/blob/v7.1.2/CHANGELOG.md)

For other versions, see the [overview list](output-sqs-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1597]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-aws). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1587]

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


## Batch Publishing [_batch_publishing_7]

This output publishes messages to SQS in batches in order to optimize event throughput and increase performance. This is done using the [`SendMessageBatch`](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) API. When publishing messages to SQS in batches, the following service limits must be respected (see [Limits in Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html)):

* The maximum allowed individual message size is 256KiB.
* The maximum total payload size (i.e. the sum of the sizes of all individual messages within a batch) is also 256KiB.

This plugin will dynamically adjust the size of the batch published to SQS in order to ensure that the total payload size does not exceed 256KiB.

::::{warning}
This output cannot currently handle messages larger than 256KiB. Any single message exceeding this size will be dropped.
::::



## Sqs Output Configuration Options [v7.1.2-plugins-outputs-sqs-options]

This plugin supports the following configuration options plus the [Common options](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_key_id`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-access_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`aws_credentials_file`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-aws_credentials_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`batch_events`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-batch_events) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`endpoint`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-endpoint) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`message_max_size`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-message_max_size) | [bytes](logstash://reference/configuration-file-structure.md#bytes) | No |
| [`proxy_uri`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-proxy_uri) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`queue`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-queue) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`queue_owner_aws_account_id`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-queue_owner_aws_account_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`region`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-region) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`role_arn`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-role_arn) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`role_session_name`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-role_session_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`secret_access_key`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-secret_access_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`session_token`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-session_token) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-common-options) for a list of options supported by all output plugins.

 

### `access_key_id` [v7.1.2-plugins-outputs-sqs-access_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)


### `aws_credentials_file` [v7.1.2-plugins-outputs-sqs-aws_credentials_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```ruby
    :access_key_id: "12345"
    :secret_access_key: "54321"
```


### `batch_events` [v7.1.2-plugins-outputs-sqs-batch_events]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

The number of events to be sent in each batch. Set this to `1` to disable the batch sending of messages.


### `endpoint` [v7.1.2-plugins-outputs-sqs-endpoint]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The endpoint to connect to. By default it is constructed using the value of `region`. This is useful when connecting to S3 compatible services, but beware that these aren’t guaranteed to work correctly with the AWS SDK.


### `message_max_size` [v7.1.2-plugins-outputs-sqs-message_max_size]

* Value type is [bytes](logstash://reference/configuration-file-structure.md#bytes)
* Default value is `"256KiB"`

The maximum number of bytes for any message sent to SQS. Messages exceeding this size will be dropped. See [http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html).


### `proxy_uri` [v7.1.2-plugins-outputs-sqs-proxy_uri]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URI to proxy server if required


### `queue` [v7.1.2-plugins-outputs-sqs-queue]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the target SQS queue. Note that this is just the name of the queue, not the URL or ARN.


### `queue_owner_aws_account_id` [v7.1.2-plugins-outputs-sqs-queue_owner_aws_account_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The owning account id of the target SQS queue. IAM permissions need to be configured on both accounts to function.


### `region` [v7.1.2-plugins-outputs-sqs-region]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"us-east-1"`

The AWS Region


### `role_arn` [v7.1.2-plugins-outputs-sqs-role_arn]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS IAM Role to assume, if any. This is used to generate temporary credentials, typically for cross-account access. See the [AssumeRole API documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) for more information.


### `role_session_name` [v7.1.2-plugins-outputs-sqs-role_session_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

Session name to use when assuming an IAM role.


### `secret_access_key` [v7.1.2-plugins-outputs-sqs-secret_access_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Secret Access Key


### `session_token` [v7.1.2-plugins-outputs-sqs-session_token]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential



## Common options [v7.1.2-plugins-outputs-sqs-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v7-1-2-plugins-outputs-sqs.md#v7.1.2-plugins-outputs-sqs-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v7.1.2-plugins-outputs-sqs-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v7.1.2-plugins-outputs-sqs-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v7.1.2-plugins-outputs-sqs-id]

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



