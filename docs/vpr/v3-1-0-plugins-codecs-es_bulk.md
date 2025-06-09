---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-codecs-es_bulk.html
---

# Es_bulk codec plugin v3.1.0 [v3.1.0-plugins-codecs-es_bulk]

* Plugin version: v3.1.0
* Released on: 2021-08-19
* [Changelog](https://github.com/logstash-plugins/logstash-codec-es_bulk/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](codec-es_bulk-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2331]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-es_bulk). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2309]

This codec will decode the [Elasticsearch bulk format](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) into individual events, plus metadata into the `@metadata` field.

Encoding is not supported at this time as the Elasticsearch output submits Logstash events in bulk format.

## Codec settings in the `logstash-input-http` plugin [v3.1.0-plugins-codecs-es_bulk-codec-settings]

The [input-http](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-http.html) plugin has two configuration options for codecs: `codec` and `additional_codecs`.

Values in `additional_codecs` are prioritized over those specified in the `codec` option. That is, the default `codec` is applied only if no codec for the request’s content-type is found in the `additional_codecs` setting.

## Event Metadata and the Elastic Common Schema (ECS) [v3.1.0-plugins-codecs-es_bulk-ecs_metadata]

When ECS compatibility is disabled, the metadata is stored in the `[@metadata]` field. When ECS is enabled, the metadata is stored in the `[@metadata][codec][es_bulk]` field.

## ES Bulk Codec Configuration Options [v3.1.0-plugins-codecs-es_bulk-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`ecs_compatibility`](v3-1-0-plugins-codecs-es_bulk.md#v3.1.0-plugins-codecs-es_bulk-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`target`](v3-1-0-plugins-codecs-es_bulk.md#v3.1.0-plugins-codecs-es_bulk-target) | [string](/lsr/value-types.md#string) | No |

### `ecs_compatibility` [v3.1.0-plugins-codecs-es_bulk-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: unstructured metadata added at @metadata
  * `v1`: uses `[@metadata][codec][es_bulk]` fields

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current).

### `target` [v3.1.0-plugins-codecs-es_bulk-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define the target field for placing the values. If this setting is not set, the data will be stored at the root (top level) of the event.

For example, if you want data to be put under the `document` field:

```
input {
  kafka {
    codec => es_bulk {
        target => "[document]"
    }
  }
}
```
