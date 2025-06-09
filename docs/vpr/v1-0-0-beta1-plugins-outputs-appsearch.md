---
navigation_title: "v1.0.0.beta1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.0.beta1-plugins-outputs-appsearch.html
---

# App Search output plugin v1.0.0.beta1 [v1.0.0.beta1-plugins-outputs-appsearch]

* Plugin version: v1.0.0.beta1
* Released on: 2018-10-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-appsearch/blob/v1.0.0.beta1/CHANGELOG.md)

For other versions, see the [overview list](output-appsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1053]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-appsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1046]

This output lets you send events to Elastic’s App Search solution. On receiving a batch of events from the Logstash pipeline, the plugin will convert the events into documents and use App Search’s bulk API to index multiple events in one request.

Because App Search doesn’t allow fields to being with `@timestamp`, by default the fields `@timestamp` and `@version` will be removed from each event prior to being sent to App Search. If you want to keep the `@timestamp` field you can use the [timestamp\_destination](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-timestamp_destination) option to store this timestamp in a different field.

This gem does not support codec customization.

## AppSearch Output Configuration Options [v1.0.0.beta1-plugins-outputs-appsearch-options]

This plugin supports the following configuration options plus the [Common options](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`api_key`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-api_key) | [password](/lsr/value-types.md#password) | Yes |
| [`document_id`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-document_id) | [string](/lsr/value-types.md#string) | No |
| [`engine`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-engine) | [string](/lsr/value-types.md#string) | Yes |
| [`host`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-host) | [string](/lsr/value-types.md#string) | Yes |
| [`timestamp_destination`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-timestamp_destination) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-common-options) for a list of options supported by all output plugins.

### `api_key` [v1.0.0.beta1-plugins-outputs-appsearch-api_key]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value

The private API Key with write permissions. Visit the [Credentials](https://app.swiftype.com/as/credentials) in the App Search dashboard to find the key associated with your account.

### `document_id` [v1.0.0.beta1-plugins-outputs-appsearch-document_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

What to use as id for app search documents. This can be an interpolated value like `myapp-%{sequence_id}`. Reusing ids will cause documents to be rewritten.

### `engine` [v1.0.0.beta1-plugins-outputs-appsearch-engine]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The Engine name. Engine is your search engine created in App Search, an information repository that includes the indexed document records.

### `host` [v1.0.0.beta1-plugins-outputs-appsearch-host]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The hostname of the App Search API that is associated with your App Search account.

### `timestamp_destination` [v1.0.0.beta1-plugins-outputs-appsearch-timestamp_destination]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

Where to move the timestamp value that all Logstash events contain in the `@timestamp` field. Since App Search doesn’t support fields starting with `@timestamp`, by default this field will be deleted. If you wish to keep it, set this value to the name of the field where `@timestamp` will be copied to.

## Common options [v1.0.0.beta1-plugins-outputs-appsearch-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-0-beta1-plugins-outputs-appsearch.md#v1.0.0.beta1-plugins-outputs-appsearch-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v1.0.0.beta1-plugins-outputs-appsearch-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v1.0.0.beta1-plugins-outputs-appsearch-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.0.beta1-plugins-outputs-appsearch-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 appsearch outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  appsearch {
    id => "my_plugin_id"
  }
}
```
