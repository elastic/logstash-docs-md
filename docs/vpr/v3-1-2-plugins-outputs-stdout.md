---
navigation_title: "v3.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.2-plugins-outputs-stdout.html
---

# Stdout output plugin v3.1.2 [v3.1.2-plugins-outputs-stdout]


* Plugin version: v3.1.2
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-stdout/blob/v3.1.2/CHANGELOG.md)

For other versions, see the [overview list](output-stdout-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1618]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-stdout). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1608]

A simple output which prints to the STDOUT of the shell running Logstash. This output can be quite convenient when debugging plugin configurations, by allowing instant access to the event data after it has passed through the inputs and filters.

For example, the following output configuration, in conjunction with the Logstash `-e` command-line flag, will allow you to see the results of your event pipeline for quick iteration.

```ruby
    output {
      stdout {}
    }
```

Useful codecs include:

`rubydebug`: outputs event data using the ruby "awesome_print" [library](http://rubygems.org/gems/awesome_print)

```ruby
    output {
      stdout { codec => rubydebug }
    }
```

`json`: outputs event data in structured JSON format

```ruby
    output {
      stdout { codec => json }
    }
```


## Stdout Output Configuration Options [v3.1.2-plugins-outputs-stdout-options]

There are no special configuration options for this plugin, but it does support the [Common options](v3-1-2-plugins-outputs-stdout.md#v3.1.2-plugins-outputs-stdout-common-options).


## Common options [v3.1.2-plugins-outputs-stdout-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-1-2-plugins-outputs-stdout.md#v3.1.2-plugins-outputs-stdout-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-2-plugins-outputs-stdout.md#v3.1.2-plugins-outputs-stdout-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-2-plugins-outputs-stdout.md#v3.1.2-plugins-outputs-stdout-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.1.2-plugins-outputs-stdout-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.2-plugins-outputs-stdout-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.2-plugins-outputs-stdout-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 stdout outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  stdout {
    id => "my_plugin_id"
  }
}
```



