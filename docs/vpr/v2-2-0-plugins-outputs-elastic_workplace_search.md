---
navigation_title: "v2.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.2.0-plugins-outputs-elastic_workplace_search.html
---

# Elastic Workplace Search output plugin v2.2.0 [v2.2.0-plugins-outputs-elastic_workplace_search]


* A component of the [elastic_enterprise_search integration plugin](integration-elastic_enterprise_search-index.md)
* Integration version: v2.2.0
* Released on: 2022-01-24
* [Changelog](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search/blob/v2.2.0/CHANGELOG.md)

For other versions, see the [overview list](output-elastic_workplace_search-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1080]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1073]

This output lets you send events to the [Elastic Workplace Search](https://www.elastic.co/workplace-search) solution. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the Workplace Search bulk API to index multiple events in one request.

Workplace Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to Workplace Search. If you want to keep the `@timestamp` field, you can use the [timestamp_destination](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-timestamp_destination) option to store the timestamp in a different field.

::::{note}
This gem does not support codec customization.
::::



## Workplace Search Output Configuration Options [v2.2.0-plugins-outputs-elastic_workplace_search-options]

This plugin supports the following configuration options plus the [Common options](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_token`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-access_token) | [password](logstash://reference/configuration-file-structure.md#password) | Yes |
| [`document_id`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-document_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`source`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-source) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`timestamp_destination`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-timestamp_destination) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`url`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-url) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-common-options) for a list of options supported by all output plugins.

 

### `access_token` [v2.2.0-plugins-outputs-elastic_workplace_search-access_token]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value

The source access token. Visit the source overview page in the Workplace Search dashboard to find the token associated with your source.


### `document_id` [v2.2.0-plugins-outputs-elastic_workplace_search-document_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The id for workplace search documents. This can be an interpolated value like `myapp-%{{sequence_id}}`. Reusing ids will cause documents to be rewritten.


### `source` [v2.2.0-plugins-outputs-elastic_workplace_search-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The ID of the source you created in Workplace Search. The `source` field supports [sprintf format](logstash://reference/event-dependent-configuration.md#sprintf) to allow the source ID to be derived from a field value from each event, for example `%{{source_id}}`.

Invalid source IDs cause ingestion to stop until the field value can be resolved into a valid source ID. This situation can happen if the interpolated field value resolves to a value without a matching source, or, if the field is missing from the event and cannot be resolved at all.

::::{tip}
Consider adding a "default" source type in the configuration to catch errors if the field is missing from the event.
::::


Example:

```ruby
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
    access_token => "abracadabra"
    url => "http://workplace.search.com:3002"
  }
}
```


### `timestamp_destination` [v2.2.0-plugins-outputs-elastic_workplace_search-timestamp_destination]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. Workplace Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.


### `url` [v2.2.0-plugins-outputs-elastic_workplace_search-url]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value

The value of the API endpoint in the form of a URL.

**Examples**

On premise instance:

`http://workplace.company.com:3002`

Elastic Cloud instance:

`https://7c455f508468426cb53912be65548117.ent-search.eu-west-1.aws.cloud.es.io`



## Common options [v2.2.0-plugins-outputs-elastic_workplace_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`enable_metric`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-2-0-plugins-outputs-elastic_workplace_search.md#v2.2.0-plugins-outputs-elastic_workplace_search-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `enable_metric` [v2.2.0-plugins-outputs-elastic_workplace_search-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.2.0-plugins-outputs-elastic_workplace_search-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic_workplace_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  elastic_workplace_search {
    id => "my_plugin_id"
  }
}
```
