---
navigation_title: "v2.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.6-plugins-inputs-kinesis.html
---

# Kinesis input plugin v2.0.6 [v2.0.6-plugins-inputs-kinesis]


* Plugin version: v2.0.6
* Released on: 2017-08-22
* [Changelog](https://github.com/logstash-plugins/logstash-input-kinesis/blob/v2.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-kinesis-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_696]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-kinesis). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_690]

Receive events through an AWS Kinesis stream.

This input plugin uses the Java Kinesis Client Library underneath, so the documentation at [https://github.com/awslabs/amazon-kinesis-client](https://github.com/awslabs/amazon-kinesis-client) will be useful.

AWS credentials can be specified either through environment variables, or an IAM instance role. The library uses a DynamoDB table for worker coordination, so you’ll need to grant access to that as well as to the Kinesis stream. The DynamoDB table has the same name as the `application_name` configuration option, which defaults to "logstash".

The library can optionally also send worker statistics to CloudWatch.


## Kinesis Input Configuration Options [v2.0.6-plugins-inputs-kinesis-options]

This plugin supports the following configuration options plus the [Common options](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`application_name`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-application_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`checkpoint_interval_seconds`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-checkpoint_interval_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`kinesis_stream_name`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-kinesis_stream_name) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`metrics`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-metrics) | [string](logstash://reference/configuration-file-structure.md#string), one of `[nil, "cloudwatch"]` | No |
| [`region`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-region) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`profile`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-profile) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-common-options) for a list of options supported by all input plugins.

 

### `application_name` [v2.0.6-plugins-inputs-kinesis-application_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The application name used for the dynamodb coordination table. Must be unique for this kinesis stream.


### `checkpoint_interval_seconds` [v2.0.6-plugins-inputs-kinesis-checkpoint_interval_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

How many seconds between worker checkpoints to dynamodb.


### `kinesis_stream_name` [v2.0.6-plugins-inputs-kinesis-kinesis_stream_name]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The kinesis stream name.


### `metrics` [v2.0.6-plugins-inputs-kinesis-metrics]

* Value can be any of: ``, `cloudwatch`
* Default value is `nil`

Worker metric tracking. By default this is disabled, set it to "cloudwatch" to enable the cloudwatch integration in the Kinesis Client Library.


### `region` [v2.0.6-plugins-inputs-kinesis-region]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"us-east-1"`

The AWS region for Kinesis, DynamoDB, and CloudWatch (if enabled)


### `profile` [v2.0.6-plugins-inputs-kinesis-profile]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

The AWS profile name for authentication. This ensures that the `~/.aws/credentials` AWS auth provider is used. By default this is empty and the default chain will be used.



## Common options [v2.0.6-plugins-inputs-kinesis-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v2-0-6-plugins-inputs-kinesis.md#v2.0.6-plugins-inputs-kinesis-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v2.0.6-plugins-inputs-kinesis-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v2.0.6-plugins-inputs-kinesis-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.6-plugins-inputs-kinesis-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.6-plugins-inputs-kinesis-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kinesis inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  kinesis {
    id => "my_plugin_id"
  }
}
```


### `tags` [v2.0.6-plugins-inputs-kinesis-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v2.0.6-plugins-inputs-kinesis-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



