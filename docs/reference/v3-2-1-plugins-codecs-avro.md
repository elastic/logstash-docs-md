---
navigation_title: "v3.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.1-plugins-codecs-avro.html
---

# Avro codec plugin v3.2.1 [v3.2.1-plugins-codecs-avro]


* Plugin version: v3.2.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-avro/blob/v3.2.1/CHANGELOG.md)

For other versions, see the [overview list](codec-avro-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2220]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-avro). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2198]

Read serialized Avro records as Logstash events

This plugin is used to serialize Logstash events as Avro datums, as well as deserializing Avro datums into Logstash events.


## Encoding [_encoding_8]

This codec is for serializing individual Logstash events as Avro datums that are Avro binary blobs. It does not encode Logstash events into an Avro file.


## Decoding [_decoding_8]

This codec is for deserializing individual Avro records. It is not for reading Avro files. Avro files have a unique format that must be handled upon input.


## Usage [_usage_137]

Example usage with Kafka input.

```ruby
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


## Avro Codec Configuration Options [v3.2.1-plugins-codecs-avro-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`schema_uri`](v3-2-1-plugins-codecs-avro.md#v3.2.1-plugins-codecs-avro-schema_uri) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`tag_on_failure`](v3-2-1-plugins-codecs-avro.md#v3.2.1-plugins-codecs-avro-tag_on_failure) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

 

### `schema_uri` [v3.2.1-plugins-codecs-avro-schema_uri]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

schema path to fetch the schema from. This can be a *http* or *file* scheme URI example:

* http - `http://example.com/schema.avsc`
* file - `/path/to/schema.avsc`


### `tag_on_failure` [v3.2.1-plugins-codecs-avro-tag_on_failure]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

tag events with `_avroparsefailure` when decode fails



