---
navigation_title: "v1.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.2.1-plugins-codecs-protobuf.html
---

# Protobuf codec plugin v1.2.1 [v1.2.1-plugins-codecs-protobuf]

* Plugin version: v1.2.1
* Released on: 2019-05-28
* [Changelog](https://github.com/logstash-plugins/logstash-codec-protobuf/blob/v1.2.1/CHANGELOG.md)

For other versions, see the [overview list](codec-protobuf-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2440]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-protobuf). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2418]

This codec converts protobuf encoded messages into logstash events and vice versa. It supports the protobuf versions 2 and 3.

The plugin requires the protobuf definitions to be compiled to ruby files.\
For protobuf 2 use the [ruby-protoc compiler](https://github.com/codekitchen/ruby-protocol-buffers).\
For protobuf 3 use the [official google protobuf compiler](https://developers.google.com/protocol-buffers/docs/reference/ruby-generated).

The following shows a usage example (protobuf v2) for decoding events from a kafka stream:

```
kafka
{
 topic_id => "..."
 key_deserializer_class => "org.apache.kafka.common.serialization.ByteArrayDeserializer"
 value_deserializer_class => "org.apache.kafka.common.serialization.ByteArrayDeserializer"
 codec => protobuf
 {
   class_name => "Animals::Mammals::Unicorn"
   include_path => ['/path/to/protobuf/definitions/UnicornProtobuf.pb.rb']
 }
}
```

Usage example for protobuf v3:

```
kafka
{
  topic_id => "..."
  key_deserializer_class => "org.apache.kafka.common.serialization.ByteArrayDeserializer"
  value_deserializer_class => "org.apache.kafka.common.serialization.ByteArrayDeserializer"
  codec => protobuf
  {
    class_name => "Animals.Mammals.Unicorn"
    include_path => ['/path/to/pb_definitions/Animal_pb.rb', '/path/to/pb_definitions/Unicorn_pb.rb']
    protobuf_version => 3
  }
}
```

The codec can be used in input and output plugins.\
When using the codec in the kafka input plugin please set the deserializer classes as shown above.\
When using the codec in an output plugin:

* make sure to include all the desired fields in the protobuf definition, including timestamp. Remove fields that are not part of the protobuf definition from the event by using the mutate filter.
* the `@` symbol is currently not supported in field names when loading the protobuf definitions for encoding. Make sure to call the timestamp field `timestamp` instead of `@timestamp` in the protobuf file. Logstash event fields will be stripped of the leading `@` before conversion.

## Protobuf Codec Configuration Options [v1.2.1-plugins-codecs-protobuf-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`class_name`](v1-2-1-plugins-codecs-protobuf.md#v1.2.1-plugins-codecs-protobuf-class_name) | [string](/lsr/value-types.md#string) | Yes |
| [`include_path`](v1-2-1-plugins-codecs-protobuf.md#v1.2.1-plugins-codecs-protobuf-include_path) | [array](/lsr/value-types.md#array) | Yes |
| [`protobuf_version`](v1-2-1-plugins-codecs-protobuf.md#v1.2.1-plugins-codecs-protobuf-protobuf_version) | [number](/lsr/value-types.md#number) | Yes |

### `class_name` [v1.2.1-plugins-codecs-protobuf-class_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Fully qualified name of the class to decode. Please note that the module delimiter is different depending on the protobuf version. For protobuf v2, use double colons:

```
class_name => "Animals::Mammals::Unicorn"
```

For protobuf v3, use single dots:

```
class_name => "Animals.Mammals.Unicorn"
```

For protobuf v3, you can copy the class name from the Descriptorpool registrations at the bottom of the generated protobuf ruby file. It contains lines like this:

```
Animals.Mammals.Unicorn = Google::Protobuf::DescriptorPool.generated_pool.lookup("Animals.Mammals.Unicorn").msgclass
```

If your class references other definitions: you only have to add the name of the main class here.

### `include_path` [v1.2.1-plugins-codecs-protobuf-include_path]

* This is a required setting.
* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

List of absolute pathes to files with protobuf definitions. When using more than one file, make sure to arrange the files in reverse order of dependency so that each class is loaded before it is refered to by another.

Example: a class *Unicorn* referencing another protobuf class *Wings*

```
module Animal
  module Mammal
    class Unicorn
      set_fully_qualified_name "Animal.Mammal.Unicorn"
      optional ::Bodypart::Wings, :wings, 1
      optional :string, :name, 2
      ...
```

would be configured as

```
include_path => ['/path/to/pb_definitions/wings.pb.rb','/path/to/pb_definitions/unicorn.pb.rb']
```

Please note that protobuf v2 files have the ending `.pb.rb` whereas files compiled for protobuf v3 end in `_pb.rb`.

### `protobuf_version` [v1.2.1-plugins-codecs-protobuf-protobuf_version]

* Value type is [number](/lsr/value-types.md#number)
* Default value is 2

Protocol buffers version. Valid settings are 2, 3.
