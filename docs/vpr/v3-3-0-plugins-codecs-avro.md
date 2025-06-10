---
navigation_title: "v3.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.0-plugins-codecs-avro.html
---

# Avro codec plugin v3.3.0 [v3.3.0-plugins-codecs-avro]

* Plugin version: v3.3.0
* Released on: 2021-08-19
* [Changelog](https://github.com/logstash-plugins/logstash-codec-avro/blob/v3.3.0/CHANGELOG.md)

For other versions, see the [overview list](codec-avro-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2248]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-avro). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2226]

Read serialized Avro records as Logstash events

This plugin is used to serialize Logstash events as Avro datums, as well as deserializing Avro datums into Logstash events.

## Event Metadata and the Elastic Common Schema (ECS) [v3.3.0-plugins-codecs-avro-ecs_metadata]

The plugin behaves the same regardless of ECS compatibility, except adding the original message to `[event][original]`.

## Encoding [_encoding_4]

This codec is for serializing individual Logstash events as Avro datums that are Avro binary blobs. It does not encode Logstash events into an Avro file.

## Decoding [_decoding_4]

This codec is for deserializing individual Avro records. It is not for reading Avro files. Avro files have a unique format that must be handled upon input.

Partial deserialization

Avro format is known to support partial deserialization of arbitrary fields, providing a schema containing a subset of the schema which was used to serialize the data. This codec **doesn’t support partial deserialization of arbitrary fields**. Partial deserialization *might* work only when providing a schema which contains the first `N` fields of the schema used to serialize the data (and in the same order).

## Usage [_usage_137]

Example usage with Kafka input.

```
input {
  kafka {
    codec => avro {
        schema_uri => "/tmp/schema.avsc"
    }
  }
}
filter {
  ...
}
output {
  ...
}
```

## Avro Codec Configuration Options [v3.3.0-plugins-codecs-avro-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`ecs_compatibility`](v3-3-0-plugins-codecs-avro.md#v3.3.0-plugins-codecs-avro-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`schema_uri`](v3-3-0-plugins-codecs-avro.md#v3.3.0-plugins-codecs-avro-schema_uri) | [string](/lsr/value-types.md#string) | Yes |
| [`tag_on_failure`](v3-3-0-plugins-codecs-avro.md#v3.3.0-plugins-codecs-avro-tag_on_failure) | [boolean](/lsr/value-types.md#boolean) | No |
| [`target`](v3-3-0-plugins-codecs-avro.md#v3.3.0-plugins-codecs-avro-target) | [string](/lsr/value-types.md#string) | No |

### `ecs_compatibility` [v3.3.0-plugins-codecs-avro-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: Avro data added at root level
  * `v1`,`v8`: Elastic Common Schema compliant behavior (`[event][original]` is also added)

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current).

### `schema_uri` [v3.3.0-plugins-codecs-avro-schema_uri]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

schema path to fetch the schema from. This can be a *http* or *file* scheme URI example:

* http - `http://example.com/schema.avsc`
* file - `/path/to/schema.avsc`

### `tag_on_failure` [v3.3.0-plugins-codecs-avro-tag_on_failure]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

tag events with `_avroparsefailure` when decode fails

### `target` [v3.3.0-plugins-codecs-avro-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* This is only relevant when decode data into an event

Define the target field for placing the values. If this setting is not set, the Avro data will be stored at the root (top level) of the event.

**Example**

```
input {
  kafka {
    codec => avro {
        schema_uri => "/tmp/schema.avsc"
        target => "[document]"
    }
  }
}
```
