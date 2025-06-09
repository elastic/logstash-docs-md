---
navigation_title: "v1.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.6-plugins-inputs-google_pubsub.html
---

# Google_pubsub input plugin v1.0.6 [v1.0.6-plugins-inputs-google_pubsub]

* Plugin version: v1.0.6
* Released on: 2018-04-12
* [Changelog](https://github.com/logstash-plugins/logstash-input-google_pubsub/blob/v1.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-google_pubsub-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_459]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-google_pubsub). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_453]

Author: Eric Johnson <<erjohnso@google.com>> Date: 2016-06-01

Copyright 2016 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

```
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. Google deps This is a [Logstash](https://github.com/elastic/logstash) input plugin for [Google Pub/Sub](https://cloud.google.com/pubsub/). The plugin can subscribe to a topic and ingest messages.

The main motivation behind the development of this plugin was to ingest [Stackdriver Logging](https://cloud.google.com/logging/) messages via the [Exported Logs](https://cloud.google.com/logging/docs/export/using_exported_logs) feature of Stackdriver Logging.

## Prerequisites [_prerequisites_7]

You must first create a Google Cloud Platform project and enable the Google Pub/Sub API. If you intend to use the plugin ingest Stackdriver Logging messages, you must also enable the Stackdriver Logging API and configure log exporting to Pub/Sub. There is plentiful information on <https://cloud.google.com/> to get started:

* Google Cloud Platform Projects and [Overview](https://cloud.google.com/docs/overview/)
* Google Cloud Pub/Sub [documentation](https://cloud.google.com/pubsub/)
* Stackdriver Logging [documentation](https://cloud.google.com/logging/)

## Cloud Pub/Sub [_cloud_pubsub_7]

Currently, this module requires you to create a `topic` manually and specify it in the logstash config file. You must also specify a `subscription`, but the plugin will attempt to create the pull-based `subscription` on its own.

All messages received from Pub/Sub will be converted to a logstash `event` and added to the processing pipeline queue. All Pub/Sub messages will be `acknowledged` and removed from the Pub/Sub `topic` (please see more about [Pub/Sub concepts](https://cloud.google.com/pubsub/overview#concepts\)).

It is generally assumed that incoming messages will be in JSON and added to the logstash `event` as-is. However, if a plain text message is received, the plugin will return the raw text in as `raw_message` in the logstash `event`.

## Authentication [_authentication_7]

You have two options for authentication depending on where you run Logstash.

1. If you are running Logstash outside of Google Cloud Platform, then you will need to create a Google Cloud Platform Service Account and specify the full path to the JSON private key file in your config. You must assign sufficient roles to the Service Account to create a subscription and to pull messages from the subscription. Learn more about GCP Service Accounts and IAM roles here:

   * Google Cloud Platform IAM [overview](https://cloud.google.com/iam/)
   * Creating Service Accounts [overview](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
   * Granting Roles [overview](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts)

2. If you are running Logstash on a Google Compute Engine instance, you may opt to use Application Default Credentials. In this case, you will not need to specify a JSON private key file in your config.

## Stackdriver Logging (optional) [_stackdriver_logging_optional_7]

If you intend to use the logstash plugin for Stackdriver Logging message ingestion, you must first manually set up the Export option to Cloud Pub/Sub and the manually create the `topic`. Please see the more detailed instructions at, <https://cloud.google.com/logging/docs/export/using_exported_logs> \[Exported Logs] and ensure that the [necessary permissions](https://cloud.google.com/logging/docs/export/configure_export#manual-access-pubsub) have also been manually configured.

Logging messages from Stackdriver Logging exported to Pub/Sub are received as JSON and converted to a logstash `event` as-is in [this format](https://cloud.google.com/logging/docs/export/using_exported_logs#log_entries_in_google_pubsub_topics).

## Sample Configuration [_sample_configuration_7]

Below is a copy of the included `example.conf-tmpl` file that shows a basic configuration for this plugin.

```
input {
    google_pubsub {
        # Your GCP project id (name)
        project_id => "my-project-1234"

        # The topic name below is currently hard-coded in the plugin. You
        # must first create this topic by hand and ensure you are exporting
        # logging to this pubsub topic.
        topic => "logstash-input-dev"

        # The subscription name is customizeable. The plugin will attempt to
        # create the subscription (but use the hard-coded topic name above).
        subscription => "logstash-sub"

        # If you are running logstash within GCE, it will use
        # Application Default Credentials and use GCE's metadata
        # service to fetch tokens.  However, if you are running logstash
        # outside of GCE, you will need to specify the service account's
        # JSON key file below.
        #json_key_file => "/home/erjohnso/pkey.json"
    }
}
output { stdout { codec => rubydebug } }
```

## Google_pubsub Input Configuration Options [v1.0.6-plugins-inputs-google_pubsub-options]

This plugin supports the following configuration options plus the [Common options](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`json_key_file`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-json_key_file) | a valid filesystem path | No |
| [`max_messages`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-max_messages) | [number](/lsr/value-types.md#number) | Yes |
| [`project_id`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-project_id) | [string](/lsr/value-types.md#string) | Yes |
| [`subscription`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-subscription) | [string](/lsr/value-types.md#string) | Yes |
| [`topic`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-topic) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-common-options) for a list of options supported by all input plugins.

### `json_key_file` [v1.0.6-plugins-inputs-google_pubsub-json_key_file]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If logstash is running within Google Compute Engine, the plugin will use GCE’s Application Default Credentials. Outside of GCE, you will need to specify a Service Account JSON key file.

### `max_messages` [v1.0.6-plugins-inputs-google_pubsub-max_messages]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

The maximum number of messages returned per request. The Pub/Sub system may return fewer than the number specified.

### `project_id` [v1.0.6-plugins-inputs-google_pubsub-project_id]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Google Cloud Project ID (name, not number).

### `subscription` [v1.0.6-plugins-inputs-google_pubsub-subscription]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `topic` [v1.0.6-plugins-inputs-google_pubsub-topic]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Google Cloud Pub/Sub Topic and Subscription. Note that the topic must be created manually with Cloud Logging pre-configured export to PubSub configured to use the defined topic. The subscription will be created automatically by the plugin.

## Common options [v1.0.6-plugins-inputs-google_pubsub-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v1-0-6-plugins-inputs-google_pubsub.md#v1.0.6-plugins-inputs-google_pubsub-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v1.0.6-plugins-inputs-google_pubsub-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v1.0.6-plugins-inputs-google_pubsub-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v1.0.6-plugins-inputs-google_pubsub-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.6-plugins-inputs-google_pubsub-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 google\_pubsub inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  google_pubsub {
    id => "my_plugin_id"
  }
}
```

### `tags` [v1.0.6-plugins-inputs-google_pubsub-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v1.0.6-plugins-inputs-google_pubsub-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
