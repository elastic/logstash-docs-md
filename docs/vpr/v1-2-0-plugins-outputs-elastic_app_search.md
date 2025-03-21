---
navigation_title: "v1.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.2.0-plugins-outputs-elastic_app_search.html
---

# App Search output plugin v1.2.0 [v1.2.0-plugins-outputs-elastic_app_search]


* Plugin version: v1.2.0
* Released on: 2021-05-04
* [Changelog](https://github.com/logstash-plugins/logstash-output-elastic_app_search/blob/v1.2.0/CHANGELOG.md)

For other versions, see the [overview list](output-elastic_app_search-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1073]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-elastic_app_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1066]

This output lets you send events to the Elastic App Search solution, both the [self-managed](https://www.elastic.co/downloads/app-search) or the [managed](https://www.elastic.co/cloud/app-search-service) service. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the App Search bulk API to index multiple events in one request.

App Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to App Search. If you want to keep the `@timestamp` field, you can use the [timestamp_destination](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-timestamp_destination) option to store the timestamp in a different field.

::::{note}
This gem does not support codec customization.
::::



## AppSearch Output Configuration Options [v1.2.0-plugins-outputs-elastic_app_search-options]

This plugin supports the following configuration options plus the [Common options](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`document_id`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-document_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`engine`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-engine) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`host`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`path`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`timestamp_destination`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-timestamp_destination) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`url`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-url) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-common-options) for a list of options supported by all output plugins.

 

### `api_key` [v1.2.0-plugins-outputs-elastic_app_search-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value

The private API Key with write permissions. Visit the [Credentials](https://app.swiftype.com/as/credentials) in the App Search dashboard to find the key associated with your account.


### `document_id` [v1.2.0-plugins-outputs-elastic_app_search-document_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The id for app search documents. This can be an interpolated value like `myapp-%{{sequence_id}}`. Reusing ids will cause documents to be rewritten.


### `engine` [v1.2.0-plugins-outputs-elastic_app_search-engine]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The name of the search engine you created in App Search, an information repository that includes the indexed document records. The `engine` field supports [sprintf format](logstash://reference/event-dependent-configuration.md#sprintf) to allow the engine name to be derived from a field value from each event, for example `engine-%{{engine_name}}`.

Invalid engine names cause ingestion to stop until the field value can be resolved into a valid engine name. This situation can happen if the interpolated field value resolves to a value without a matching engine, or, if the field is missing from the event and cannot be resolved at all.

::::{tip}
Consider adding a "default" engine type in the configuration to catch errors if the field is missing from the event.
::::


Example:

```ruby
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


### `host` [v1.2.0-plugins-outputs-elastic_app_search-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The hostname of the App Search API that is associated with your App Search account. Set this when using the [Elastic App Search managed service](https://www.elastic.co/cloud/app-search-service).


### `path` [v1.2.0-plugins-outputs-elastic_app_search-path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `/api/as/v1/`

The path that is appended to the `url` parameter when connecting to a [self-managed Elastic App Search](https://www.elastic.co/downloads/app-search).


### `timestamp_destination` [v1.2.0-plugins-outputs-elastic_app_search-timestamp_destination]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. App Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.


### `url` [v1.2.0-plugins-outputs-elastic_app_search-url]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The value of the API endpoint in the form of a URL. Note: The value of the of the `path` setting will be will be appended to this URL. Set this when using the [self-managed Elastic App Search](https://www.elastic.co/downloads/app-search).



## Common options [v1.2.0-plugins-outputs-elastic_app_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`enable_metric`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-2-0-plugins-outputs-elastic_app_search.md#v1.2.0-plugins-outputs-elastic_app_search-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `enable_metric` [v1.2.0-plugins-outputs-elastic_app_search-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.2.0-plugins-outputs-elastic_app_search-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic_app_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  elastic_app_search {
    id => "my_plugin_id"
  }
}
```



