---
navigation_title: "v1.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.2-plugins-codecs-protobuf.html
---

# Protobuf codec plugin v1.0.2 [v1.0.2-plugins-codecs-protobuf]

* Plugin version: v1.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-protobuf/blob/v1.0.2/CHANGELOG.md)

For other versions, see the [overview list](codec-protobuf-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2446]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-protobuf). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2424]

This codec converts protobuf encoded messages into logstash events and vice versa.

Requires the protobuf definitions as ruby files. You can create those using the \[ruby-protoc compiler]\(<https://github.com/codekitchen/ruby-protocol-buffers>).

The following shows a usage example for decoding events from a kafka stream:

```
kafka
{
 zk_connect => "127.0.0.1"
 topic_id => "your_topic_goes_here"
 codec => protobuf
 {
   class_name => "Animal::Unicorn"
   include_path => ['/path/to/protobuf/definitions/UnicornProtobuf.pb.rb']
 }
}
```

## Protobuf Codec Configuration Options [v1.0.2-plugins-codecs-protobuf-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`class_name`](v1-0-2-plugins-codecs-protobuf.md#v1.0.2-plugins-codecs-protobuf-class_name) | [string](/lsr/value-types.md#string) | Yes |
| [`include_path`](v1-0-2-plugins-codecs-protobuf.md#v1.0.2-plugins-codecs-protobuf-include_path) | [array](/lsr/value-types.md#array) | Yes |

### `class_name` [v1.0.2-plugins-codecs-protobuf-class_name]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Name of the class to decode. If your protobuf definition contains modules, prepend them to the class name with double colons like so:

```
class_name => "Foods::Dairy::Cheese"
```

This corresponds to a protobuf definition starting as follows:

```
module Foods
   module Dairy
       class Cheese
           # here are your field definitions.
```

If your class references other definitions: you only have to add the main class here.

### `include_path` [v1.0.2-plugins-codecs-protobuf-include_path]

* This is a required setting.
* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

List of absolute pathes to files with protobuf definitions. When using more than one file, make sure to arrange the files in reverse order of dependency so that each class is loaded before it is refered to by another.

Example: a class *Cheese* referencing another protobuf class *Milk*

```
module Foods
  module Dairy
        class Cheese
           set_fully_qualified_name "Foods.Dairy.Cheese"
           optional ::Foods::Cheese::Milk, :milk, 1
           optional :int64, :unique_id, 2
           # here be more field definitions
```

would be configured as

```
include_path => ['/path/to/protobuf/definitions/Milk.pb.rb','/path/to/protobuf/definitions/Cheese.pb.rb']
```

When using the codec in an output plugin: \* make sure to include all the desired fields in the protobuf definition, including timestamp. Remove fields that are not part of the protobuf definition from the event by using the mutate filter. \* the @ symbol is currently not supported in field names when loading the protobuf definitions for encoding. Make sure to call the timestamp field "timestamp" instead of "@timestamp" in the protobuf file. Logstash event fields will be stripped of the leading @ before conversion.
