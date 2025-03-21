---
navigation_title: "v3.4.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.4.0-plugins-codecs-fluent.html
---

# Fluent codec plugin v3.4.0 [v3.4.0-plugins-codecs-fluent]


* Plugin version: v3.4.0
* Released on: 2021-08-09
* [Changelog](https://github.com/logstash-plugins/logstash-codec-fluent/blob/v3.4.0/CHANGELOG.md)

For other versions, see the [overview list](codec-fluent-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2306]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-fluent). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2284]

This codec handles fluentd’s msgpack schema.

For example, you can receive logs from `fluent-logger-ruby` with:

```ruby
    input {
      tcp {
        codec => fluent
        port => 4000
      }
    }
```

And from your ruby code in your own application:

```ruby
    logger = Fluent::Logger::FluentLogger.new(nil, :host => "example.log", :port => 4000)
    logger.post("some_tag", { "your" => "data", "here" => "yay!" })
```

::::{note}
Fluent uses second-precision for events, so you will not see sub-second precision on events processed by this codec.
::::



## Fluent Codec configuration options [v3.4.0-plugins-codecs-fluent-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`nanosecond_precision`](v3-4-0-plugins-codecs-fluent.md#v3.4.0-plugins-codecs-fluent-nanosecond_precision) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`target`](v3-4-0-plugins-codecs-fluent.md#v3.4.0-plugins-codecs-fluent-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

 

### `nanosecond_precision` [v3.4.0-plugins-codecs-fluent-nanosecond_precision]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enables sub-second level precision while encoding events.


### `target` [v3.4.0-plugins-codecs-fluent-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Define the target field for placing the decoded values. If this setting is not set, data will be stored at the root (top level) of the event.

For example, if you want data to be put under the `logs` field:

```ruby
    input {
      tcp {
        codec => fluent {
          target => "[logs]"
        }
        port => 4000
      }
    }
```



