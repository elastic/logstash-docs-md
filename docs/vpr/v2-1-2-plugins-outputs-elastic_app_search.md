---
navigation_title: "v2.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.1.2-plugins-outputs-elastic_app_search.html
---

# Elastic App Search output plugin v2.1.2 [v2.1.2-plugins-outputs-elastic_app_search]

* A component of the [elastic\_enterprise\_search integration plugin](integration-elastic_enterprise_search-index.md)
* Integration version: v2.1.2
* Released on: 2021-06-07
* [Changelog](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search/blob/v2.1.2/CHANGELOG.md)

For other versions, see the [overview list](output-elastic_app_search-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1104]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1097]

This output lets you send events to the [Elastic App Search](https://www.elastic.co/app-search) solution, both the [self-managed](https://www.elastic.co/downloads/app-search) or the [managed](https://www.elastic.co/cloud/app-search-service) service. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the App Search bulk API to index multiple events in one request.

App Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to App Search. If you want to keep the `@timestamp` field, you can use the [timestamp\_destination](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-timestamp_destination) option to store the timestamp in a different field.

This gem does not support codec customization.

## AppSearch Output configuration options [v2.1.2-plugins-outputs-elastic_app_search-options]

This plugin supports the following configuration options plus the [Common options](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`api_key`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-api_key) | [password](/lsr/value-types.md#password) | Yes |
| [`document_id`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-document_id) | [string](/lsr/value-types.md#string) | No |
| [`engine`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-engine) | [string](/lsr/value-types.md#string) | Yes |
| [`host`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-host) | [string](/lsr/value-types.md#string) | No |
| [`path`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-path) | [string](/lsr/value-types.md#string) | No |
| [`timestamp_destination`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-timestamp_destination) | [string](/lsr/value-types.md#string) | No |
| [`url`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-url) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-common-options) for a list of options supported by all output plugins.

### `api_key` [v2.1.2-plugins-outputs-elastic_app_search-api_key]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value

The private API Key with write permissions. Visit the [Credentials](https://app.swiftype.com/as/credentials) in the App Search dashboard to find the key associated with your account.

### `document_id` [v2.1.2-plugins-outputs-elastic_app_search-document_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The id for app search documents. This can be an interpolated value like `myapp-%{sequence_id}`. Reusing ids will cause documents to be rewritten.

### `engine` [v2.1.2-plugins-outputs-elastic_app_search-engine]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The name of the search engine you created in App Search, an information repository that includes the indexed document records. The `engine` field supports [sprintf format](https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html#sprintf) to allow the engine name to be derived from a field value from each event, for example `engine-%{engine_name}`.

Invalid engine names cause ingestion to stop until the field value can be resolved into a valid engine name. This situation can happen if the interpolated field value resolves to a value without a matching engine, or, if the field is missing from the event and cannot be resolved at all.

Consider adding a "default" engine type in the configuration to catch errors if the field is missing from the event.

Example:

```
input {
  stdin {
    codec => json
  }
}

filter {
  if ![engine_name] {
    mutate {
      add_field => {"engine_name" => "default"}
    }
  }
}

output {
  appsearch {
    engine => "engine_%{[engine_name]}"
  }
}
```

### `host` [v2.1.2-plugins-outputs-elastic_app_search-host]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The hostname of the App Search API that is associated with your App Search account. Set this when using the [Elastic App Search managed service](https://www.elastic.co/cloud/app-search-service).

### `path` [v2.1.2-plugins-outputs-elastic_app_search-path]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `/api/as/v1/`

The path that is appended to the `url` parameter when connecting to a [self-managed Elastic App Search](https://www.elastic.co/downloads/app-search).

### `timestamp_destination` [v2.1.2-plugins-outputs-elastic_app_search-timestamp_destination]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. App Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.

### `url` [v2.1.2-plugins-outputs-elastic_app_search-url]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The value of the API endpoint in the form of a URL. Note: The value of the of the `path` setting will be will be appended to this URL. Set this when using the [self-managed Elastic App Search](https://www.elastic.co/downloads/app-search).

## Common options [v2.1.2-plugins-outputs-elastic_app_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`enable_metric`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-1-2-plugins-outputs-elastic_app_search.md#v2.1.2-plugins-outputs-elastic_app_search-id) | [string](/lsr/value-types.md#string) | No |

### `enable_metric` [v2.1.2-plugins-outputs-elastic_app_search-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.1.2-plugins-outputs-elastic_app_search-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic\_app\_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  elastic_app_search {
    id => "my_plugin_id"
  }
}
```
