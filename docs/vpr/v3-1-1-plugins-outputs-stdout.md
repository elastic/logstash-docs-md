---
navigation_title: "v3.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.1-plugins-outputs-stdout.html
---

# Stdout output plugin v3.1.1 [v3.1.1-plugins-outputs-stdout]

* Plugin version: v3.1.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-stdout/blob/v3.1.1/CHANGELOG.md)

For other versions, see the [overview list](output-stdout-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1636]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-stdout). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1626]

A simple output which prints to the STDOUT of the shell running Logstash. This output can be quite convenient when debugging plugin configurations, by allowing instant access to the event data after it has passed through the inputs and filters.

For example, the following output configuration, in conjunction with the Logstash `-e` command-line flag, will allow you to see the results of your event pipeline for quick iteration.

```
    output {
      stdout {}
    }
```

Useful codecs include:

`rubydebug`: outputs event data using the ruby "awesome\_print" [library](http://rubygems.org/gems/awesome_print)

```
    output {
      stdout { codec => rubydebug }
    }
```

`json`: outputs event data in structured JSON format

```
    output {
      stdout { codec => json }
    }
```

## Stdout Output Configuration Options [v3.1.1-plugins-outputs-stdout-options]

There are no special configuration options for this plugin, but it does support the [Common options](v3-1-1-plugins-outputs-stdout.md#v3.1.1-plugins-outputs-stdout-common-options).

## Common options [v3.1.1-plugins-outputs-stdout-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-1-1-plugins-outputs-stdout.md#v3.1.1-plugins-outputs-stdout-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-1-plugins-outputs-stdout.md#v3.1.1-plugins-outputs-stdout-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-1-plugins-outputs-stdout.md#v3.1.1-plugins-outputs-stdout-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.1.1-plugins-outputs-stdout-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.1-plugins-outputs-stdout-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.1-plugins-outputs-stdout-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 stdout outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  stdout {
    id => "my_plugin_id"
  }
}
```
