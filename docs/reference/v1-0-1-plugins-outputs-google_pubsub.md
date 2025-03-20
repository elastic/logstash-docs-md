---
navigation_title: "v1.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.1-plugins-outputs-google_pubsub.html
---

# Google Cloud Pub/Sub Output Plugin [v1.0.1-plugins-outputs-google_pubsub]


* Plugin version: v1.0.1
* Released on: 2018-09-25
* [Changelog](https://github.com/logstash-plugins/logstash-output-google_pubsub/blob/v1.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-google_pubsub-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1279]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-google_pubsub). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1272]

A Logstash plugin to upload log events to [Google Cloud Pubsub](https://cloud.google.com/pubsub/). Events are batched and uploaded in the background for the sake of efficiency. Message payloads are serialized JSON representations of the events.

Example use-cases:

* Stream events to Dataproc via Pub/Sub for real-time analysis.
* Forward events from an on-prem datacenter to the Logstash in the cloud.
* Use Pub/Sub as an scalable buffer to even out event flow between processing steps.

Note: While this project is partially maintained by Google, this is not an official Google product.


## Environment Configuration [_environment_configuration_17]

To use this plugin, you must create a [service account](https://developers.google.com/storage/docs/authentication#service_accounts) and grant it the publish permission on a topic. You MAY also use the [Application Default Credentials](https://cloud.google.com/docs/authentication/production) assigned to a compute instance.

The Pub/Sub topic *must* exist before you run the plugin.


## Example Configurations [_example_configurations_4]

### Basic [_basic_10]

A basic configuration which only includes a project, topic, and JSON key file:

```ruby
output {
  google_pubsub {
    # Required attributes
    project_id => "my_project"
    topic => "my_topic"

    # Optional if you're using app default credentials
    json_key_file => "service_account_key.json"
  }
}
```


### High Volume [_high_volume_4]

If you find that uploads are going too slowly, you can increase the message batching:

```ruby
output {
  google_pubsub {
    project_id => "my_project"
    topic => "my_topic"
    json_key_file => "service_account_key.json"

    # Options for configuring the upload
    message_count_threshold => 10000
    delay_threshold_secs => 10
    request_byte_threshold => 5MB
  }
}
```


### Attributes [_attributes_4]

You can attach additional attributes to each request. For example, you could attach a datacenter label to a log message to help with debugging:

```ruby
output {
  google_pubsub {
    project_id => "my_project"
    topic => "my_topic"
    json_key_file => "service_account_key.json"


    attributes => {"origin" => "pacific-datacenter"}
  }
}
```


### Different Codecs [_different_codecs_4]

You can use codecs with this plugin to change the body of the events:

```ruby
output {
  google_pubsub {
    project_id => "my_project"
    topic => "my_topic"
    json_key_file => "service_account_key.json"


    codec => plain {format => "%{[time]}: %{[message]}"}
  }
}
```



## Additional Resources [_additional_resources_24]

* [Cloud Pub/Sub Homepage](https://cloud.google.com/pubsub/)
* [Cloud Pub/Sub Pricing](https://cloud.google.com/pubsub/pricing/)
* [IAM Service Accounts](https://cloud.google.com/iam/docs/service-accounts)
* [Application Default Credentials](https://cloud.google.com/docs/authentication/production)


## Google Cloud Pub/Sub Output Configuration Options [v1.0.1-plugins-outputs-google_pubsub-options]

This plugin supports the following configuration options plus the [Common options](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`project_id`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-project_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`topic`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-topic) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`json_key_file`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-json_key_file) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`delay_threshold_secs`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-delay_threshold_secs) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`message_count_threshold`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-message_count_threshold) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`request_byte_threshold`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-request_byte_threshold) | [bytes](logstash://reference/configuration-file-structure.md#bytes) | No |
| [`attributes`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-attributes) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |

Also see [Common options](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-common-options) for a list of options supported by all input plugins.

### `project_id` [v1.0.1-plugins-outputs-google_pubsub-project_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Google Cloud Project ID (name, not number).


### `topic` [v1.0.1-plugins-outputs-google_pubsub-topic]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Google Cloud Pub/Sub Topic. You must create the topic manually before running this plugin.


### `json_key_file` [v1.0.1-plugins-outputs-google_pubsub-json_key_file]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The path to the key to authenticate your user to the bucket. This service user *must* have the `pubsub.topics.publish` permission so it can publish to the topic.

If Logstash is running within Google Compute Engine and no `json_key_file` is defined, the plugin will use GCE’s Application Default Credentials. Outside of GCE, you must to specify a Service Account JSON key file.


### `delay_threshold_secs` [v1.0.1-plugins-outputs-google_pubsub-delay_threshold_secs]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default is: `5`

Send the batch once this delay has passed, from the time the first message is queued. Must be greater than 0.


### `message_count_threshold` [v1.0.1-plugins-outputs-google_pubsub-message_count_threshold]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default is: `100`

Once this many messages are queued, send all the messages in a single call, even if the delay threshold hasn’t elapsed yet. Must be < 1000. A value of 0 will cause messages to instantly be sent but will reduce total throughput due to overhead.


### `request_byte_threshold` [v1.0.1-plugins-outputs-google_pubsub-request_byte_threshold]

* Value type is [bytes](logstash://reference/configuration-file-structure.md#bytes)
* Default is: `1_000_000`

Once the number of bytes in the batched request reaches this threshold, send all of the messages in a single call, even if neither the delay or message count thresholds have been exceeded yet. This includes full message payload size, including any attributes set.


### `attributes` [v1.0.1-plugins-outputs-google_pubsub-attributes]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default is: `{}`

Attributes to add to the message in key: value formats. Keys and values MUST be strings.



## Common options [v1.0.1-plugins-outputs-google_pubsub-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-1-plugins-outputs-google_pubsub.md#v1.0.1-plugins-outputs-google_pubsub-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v1.0.1-plugins-outputs-google_pubsub-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v1.0.1-plugins-outputs-google_pubsub-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.1-plugins-outputs-google_pubsub-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 google_pubsub outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  google_pubsub {
    id => "my_plugin_id"
  }
}
```



