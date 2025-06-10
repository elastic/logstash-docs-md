---
navigation_title: "v2.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.1.2-plugins-outputs-elastic_workplace_search.html
---

# Elastic Workplace Search output plugin v2.1.2 [v2.1.2-plugins-outputs-elastic_workplace_search]

* A component of the [elastic\_enterprise\_search integration plugin](integration-elastic_enterprise_search-index.md)
* Integration version: v2.1.2
* Released on: 2021-06-07
* [Changelog](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search/blob/v2.1.2/CHANGELOG.md)

For other versions, see the [overview list](output-elastic_workplace_search-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1118]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1111]

This output lets you send events to the [Elastic Workplace Search](https://www.elastic.co/workplace-search) solution. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the Workplace Search bulk API to index multiple events in one request.

Workplace Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to Workplace Search. If you want to keep the `@timestamp` field, you can use the [timestamp\_destination](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-timestamp_destination) option to store the timestamp in a different field.

This gem does not support codec customization.

## Workplace Search Output Configuration Options [v2.1.2-plugins-outputs-elastic_workplace_search-options]

This plugin supports the following configuration options plus the [Common options](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`access_token`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-access_token) | [password](/lsr/value-types.md#password) | Yes |
| [`document_id`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-document_id) | [string](/lsr/value-types.md#string) | No |
| [`source`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-source) | [string](/lsr/value-types.md#string) | Yes |
| [`timestamp_destination`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-timestamp_destination) | [string](/lsr/value-types.md#string) | No |
| [`url`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-url) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-common-options) for a list of options supported by all output plugins.

### `access_token` [v2.1.2-plugins-outputs-elastic_workplace_search-access_token]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value

The source access token. Visit the source overview page in the Workplace Search dashboard to find the token associated with your source.

### `document_id` [v2.1.2-plugins-outputs-elastic_workplace_search-document_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The id for workplace search documents. This can be an interpolated value like `myapp-%{sequence_id}`. Reusing ids will cause documents to be rewritten.

### `source` [v2.1.2-plugins-outputs-elastic_workplace_search-source]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The ID of the source you created in Workplace Search. The `source` field supports [sprintf format](https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html#sprintf) to allow the source ID to be derived from a field value from each event, for example `%{source_id}`.

Invalid source IDs cause ingestion to stop until the field value can be resolved into a valid source ID. This situation can happen if the interpolated field value resolves to a value without a matching source, or, if the field is missing from the event and cannot be resolved at all.

Consider adding a "default" source type in the configuration to catch errors if the field is missing from the event.

Example:

```
input {
  stdin {
    codec => json
  }
}

filter {
  if ![source_id] {
    mutate {
      add_field => {"source_id" => "default"}
    }
  }
}

output {
  elastic_workplace_search {
    source => "%{[source_id]}"
  }
}
```

### `timestamp_destination` [v2.1.2-plugins-outputs-elastic_workplace_search-timestamp_destination]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. Workplace Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.

### `url` [v2.1.2-plugins-outputs-elastic_workplace_search-url]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The value of the API endpoint in the form of a URL.

## Common options [v2.1.2-plugins-outputs-elastic_workplace_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`enable_metric`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-1-2-plugins-outputs-elastic_workplace_search.md#v2.1.2-plugins-outputs-elastic_workplace_search-id) | [string](/lsr/value-types.md#string) | No |

### `enable_metric` [v2.1.2-plugins-outputs-elastic_workplace_search-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.1.2-plugins-outputs-elastic_workplace_search-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic\_workplace\_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  elastic_workplace_search {
    id => "my_plugin_id"
  }
}
```
