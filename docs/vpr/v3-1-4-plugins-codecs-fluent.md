---
navigation_title: "v3.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.4-plugins-codecs-fluent.html
---

# Fluent codec plugin v3.1.4 [v3.1.4-plugins-codecs-fluent]

* Plugin version: v3.1.4
* Released on: 2017-10-12
* [Changelog](https://github.com/logstash-plugins/logstash-codec-fluent/blob/v3.1.4/CHANGELOG.md)

For other versions, see the [overview list](codec-fluent-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2344]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-fluent). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2322]

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

Notes:

* the fluent uses a second-precision time for events, so you will never see subsecond precision on events processed by this codec.
