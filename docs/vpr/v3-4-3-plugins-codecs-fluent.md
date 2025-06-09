---
navigation_title: "v3.4.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.4.3-plugins-codecs-fluent.html
---

# Fluent codec plugin v3.4.3 [v3.4.3-plugins-codecs-fluent]

* Plugin version: v3.4.3
* Released on: 2024-06-25
* [Changelog](https://github.com/logstash-plugins/logstash-codec-fluent/blob/v3.4.3/CHANGELOG.md)

For other versions, see the [overview list](codec-fluent-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2339]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-fluent). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2317]

This codec handles fluentd’s msgpack schema.

For example, you can receive logs from `fluent-logger-ruby` with:

```
    input {
      tcp {
        codec => fluent
        port => 4000
      }
    }
```

And from your ruby code in your own application:

```
    logger = Fluent::Logger::FluentLogger.new(nil, :host => "example.log", :port => 4000)
    logger.post("some_tag", { "your" => "data", "here" => "yay!" })
```

Fluent uses second-precision for events, so you will not see sub-second precision on events processed by this codec.

## Fluent Codec configuration options [v3.4.3-plugins-codecs-fluent-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`nanosecond_precision`](v3-4-3-plugins-codecs-fluent.md#v3.4.3-plugins-codecs-fluent-nanosecond_precision) | [boolean](/lsr/value-types.md#boolean) | No |
| [`target`](v3-4-3-plugins-codecs-fluent.md#v3.4.3-plugins-codecs-fluent-target) | [string](/lsr/value-types.md#string) | No |

### `nanosecond_precision` [v3.4.3-plugins-codecs-fluent-nanosecond_precision]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enables sub-second level precision while encoding events.

### `target` [v3.4.3-plugins-codecs-fluent-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define the target field for placing the decoded values. If this setting is not set, data will be stored at the root (top level) of the event.

For example, if you want data to be put under the `logs` field:

```
    input {
      tcp {
        codec => fluent {
          target => "[logs]"
        }
        port => 4000
      }
    }
```
