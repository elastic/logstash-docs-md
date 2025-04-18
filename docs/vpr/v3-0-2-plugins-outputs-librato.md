---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-outputs-librato.html
---

# Librato output plugin v3.0.2 [v3.0.2-plugins-outputs-librato]


* Plugin version: v3.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-librato/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](output-librato-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1412]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-librato). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1402]

This output lets you send metrics, annotations, and alerts to Librato based on Logstash events

This is VERY experimental and inefficient right now.


## Librato Output Configuration Options [v3.0.2-plugins-outputs-librato-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`account_id`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-account_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`annotation`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-annotation) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`api_token`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-api_token) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`batch_size`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-batch_size) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`counter`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-counter) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`gauge`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-gauge) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |

Also see [Common options](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-common-options) for a list of options supported by all output plugins.

 

### `account_id` [v3.0.2-plugins-outputs-librato-account_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This output lets you send metrics, annotations and alerts to Librato based on Logstash events

This is VERY experimental and inefficient right now. Your Librato account usually an email address


### `annotation` [v3.0.2-plugins-outputs-librato-annotation]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Annotations Registers an annotation with Librato The only required field is `title` and `name`. `start_time` and `end_time` will be set to `event.get("@timestamp").to_i` You can add any other optional annotation values as well. All values will be passed through `event.sprintf`

Example:

```ruby
  {
      "title" => "Logstash event on %{host}"
      "name" => "logstash_stream"
  }
```

or

```ruby
   {
      "title" => "Logstash event"
      "description" => "%{message}"
      "name" => "logstash_stream"
   }
```


### `api_token` [v3.0.2-plugins-outputs-librato-api_token]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Your Librato API Token


### `batch_size` [v3.0.2-plugins-outputs-librato-batch_size]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"10"`

Batch size Number of events to batch up before sending to Librato.


### `counter` [v3.0.2-plugins-outputs-librato-counter]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Counters Send data to Librato as a counter

Example:

```ruby
    {
        "value" => "1"
        "source" => "%{host}"
        "name" => "messages_received"
    }
```

Additionally, you can override the `measure_time` for the event. Must be a unix timestamp:

```ruby
    {
        "value" => "1"
        "source" => "%{host}"
        "name" => "messages_received"
        "measure_time" => "%{my_unixtime_field}"
    }
Default is to use the event's timestamp
```


### `gauge` [v3.0.2-plugins-outputs-librato-gauge]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Gauges Send data to Librato as a gauge

Example:

```ruby
    {
        "value" => "%{bytes_received}"
        "source" => "%{host}"
        "name" => "apache_bytes"
    }
```

Additionally, you can override the `measure_time` for the event. Must be a unix timestamp:

```ruby
    {
        "value" => "%{bytes_received}"
        "source" => "%{host}"
        "name" => "apache_bytes"
        "measure_time" => "%{my_unixtime_field}
    }
```

Default is to use the event's timestamp

## Common options [v3.0.2-plugins-outputs-librato-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-outputs-librato.md#v3.0.2-plugins-outputs-librato-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.2-plugins-outputs-librato-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.2-plugins-outputs-librato-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-outputs-librato-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 librato outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  librato {
    id => "my_plugin_id"
  }
}
```



