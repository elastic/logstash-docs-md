---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-inputs-sqs.html
---

# Sqs input plugin v3.0.6 [v3.0.6-plugins-inputs-sqs]


* Plugin version: v3.0.6
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-input-sqs/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-sqs-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_881]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-sqs). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_874]

Pull events from an Amazon Web Services Simple Queue Service (SQS) queue.

SQS is a simple, scalable queue system that is part of the Amazon Web Services suite of tools.

Although SQS is similar to other queuing systems like AMQP, it uses a custom API and requires that you have an AWS account. See [http://aws.amazon.com/sqs/](http://aws.amazon.com/sqs/) for more details on how SQS works, what the pricing schedule looks like and how to setup a queue.

To use this plugin, you **must**:

* Have an AWS account
* Setup an SQS queue
* Create an identify that has access to consume messages from the queue.

The "consumer" identity must have the following permissions on the queue:

* `sqs:ChangeMessageVisibility`
* `sqs:ChangeMessageVisibilityBatch`
* `sqs:DeleteMessage`
* `sqs:DeleteMessageBatch`
* `sqs:GetQueueAttributes`
* `sqs:GetQueueUrl`
* `sqs:ListQueues`
* `sqs:ReceiveMessage`

Typically, you should setup an IAM policy, create a user and apply the IAM policy to the user. A sample policy is as follows:

```json
    {
      "Statement": [
        {
          "Action": [
            "sqs:ChangeMessageVisibility",
            "sqs:ChangeMessageVisibilityBatch",
            "sqs:GetQueueAttributes",
            "sqs:GetQueueUrl",
            "sqs:ListQueues",
            "sqs:SendMessage",
            "sqs:SendMessageBatch"
          ],
          "Effect": "Allow",
          "Resource": [
            "arn:aws:sqs:us-east-1:123456789012:Logstash"
          ]
        }
      ]
    }
```

See [http://aws.amazon.com/iam/](http://aws.amazon.com/iam/) for more details on setting up AWS identities.


## Sqs Input Configuration Options [v3.0.6-plugins-inputs-sqs-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_key_id`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-access_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`aws_credentials_file`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-aws_credentials_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`id_field`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-id_field) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`md5_field`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-md5_field) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`polling_frequency`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-polling_frequency) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`proxy_uri`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-proxy_uri) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`queue`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-queue) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`region`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-region) | [string](logstash://reference/configuration-file-structure.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`secret_access_key`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-secret_access_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sent_timestamp_field`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-sent_timestamp_field) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`session_token`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-session_token) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`threads`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-common-options) for a list of options supported by all input plugins.

 

### `access_key_id` [v3.0.6-plugins-inputs-sqs-access_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)


### `aws_credentials_file` [v3.0.6-plugins-inputs-sqs-aws_credentials_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```ruby
    :access_key_id: "12345"
    :secret_access_key: "54321"
```


### `id_field` [v3.0.6-plugins-inputs-sqs-id_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the event field in which to store the SQS message ID


### `md5_field` [v3.0.6-plugins-inputs-sqs-md5_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the event field in which to store the SQS message MD5 checksum


### `polling_frequency` [v3.0.6-plugins-inputs-sqs-polling_frequency]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `20`

Polling frequency, default is 20 seconds


### `proxy_uri` [v3.0.6-plugins-inputs-sqs-proxy_uri]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URI to proxy server if required


### `queue` [v3.0.6-plugins-inputs-sqs-queue]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the SQS Queue name to pull messages from. Note that this is just the name of the queue, not the URL or ARN.


### `region` [v3.0.6-plugins-inputs-sqs-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region


### `secret_access_key` [v3.0.6-plugins-inputs-sqs-secret_access_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Secret Access Key


### `sent_timestamp_field` [v3.0.6-plugins-inputs-sqs-sent_timestamp_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the event field in which to store the SQS message Sent Timestamp


### `session_token` [v3.0.6-plugins-inputs-sqs-session_token]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential


### `threads` [v3.0.6-plugins-inputs-sqs-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`



## Common options [v3.0.6-plugins-inputs-sqs-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-6-plugins-inputs-sqs.md#v3.0.6-plugins-inputs-sqs-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.6-plugins-inputs-sqs-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.6-plugins-inputs-sqs-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-inputs-sqs-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-inputs-sqs-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 sqs inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  sqs {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.6-plugins-inputs-sqs-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.6-plugins-inputs-sqs-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



