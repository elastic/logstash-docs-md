---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-outputs-graphtastic.html
---

# Graphtastic output plugin v3.0.4 [v3.0.4-plugins-outputs-graphtastic]

* Plugin version: v3.0.4
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-graphtastic/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](output-graphtastic-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1293]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-graphtastic). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1286]

A plugin for a newly developed Java/Spring Metrics application I didn’t really want to code this project but I couldn’t find a respectable alternative that would also run on any Windows machine - which is the problem and why I am not going with Graphite and statsd. This application provides multiple integration options so as to make its use under your network requirements possible. This includes a REST option that is always enabled for your use in case you want to write a small script to send the occasional metric data.

Find GraphTastic here : <https://github.com/NickPadilla/GraphTastic>

## Graphtastic Output Configuration Options [v3.0.4-plugins-outputs-graphtastic-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`batch_number`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-batch_number) | [number](/lsr/value-types.md#number) | No |
| [`context`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-context) | [string](/lsr/value-types.md#string) | No |
| [`error_file`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-error_file) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-host) | [string](/lsr/value-types.md#string) | No |
| [`integration`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-integration) | [string](/lsr/value-types.md#string), one of `["udp", "tcp", "rmi", "rest"]` | No |
| [`metrics`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-metrics) | [hash](/lsr/value-types.md#hash) | No |
| [`port`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-port) | [number](/lsr/value-types.md#number) | No |
| [`retries`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-retries) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-common-options) for a list of options supported by all output plugins.

### `batch_number` [v3.0.4-plugins-outputs-graphtastic-batch_number]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

the number of metrics to send to GraphTastic at one time. 60 seems to be the perfect amount for UDP, with default packet size.

### `context` [v3.0.4-plugins-outputs-graphtastic-context]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"graphtastic"`

if using rest as your end point you need to also provide the application url it defaults to localhost/graphtastic. You can customize the application url by changing the name of the .war file. There are other ways to change the application context, but they vary depending on the Application Server in use. Please consult your application server documentation for more on application contexts.

### `error_file` [v3.0.4-plugins-outputs-graphtastic-error_file]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

setting allows you to specify where we save errored transactions this makes the most sense at this point - will need to decide on how we reintegrate these error metrics NOT IMPLEMENTED!

### `host` [v3.0.4-plugins-outputs-graphtastic-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"127.0.0.1"`

host for the graphtastic server - defaults to 127.0.0.1

### `integration` [v3.0.4-plugins-outputs-graphtastic-integration]

* Value can be any of: `udp`, `tcp`, `rmi`, `rest`
* Default value is `"udp"`

options are udp(fastest - default) - rmi(faster) - rest(fast) - tcp(don’t use TCP yet - some problems - errors out on linux)

### `metrics` [v3.0.4-plugins-outputs-graphtastic-metrics]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

metrics hash - you will provide a name for your metric and the metric data as key value pairs. so for example:

```
metrics => { "Response" => "%{response}" }
```

example for the logstash config

```
metrics => [ "Response", "%{response}" ]
```

you can also use the dynamic fields for the key value as well as the actual value

### `port` [v3.0.4-plugins-outputs-graphtastic-port]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

port for the graphtastic instance - defaults to 1199 for RMI, 1299 for TCP, 1399 for UDP, and 8080 for REST

### `retries` [v3.0.4-plugins-outputs-graphtastic-retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

number of attempted retry after send error - currently only way to integrate errored transactions - should try and save to a file or later consumption either by graphtastic utility or by this program after connectivity is ensured to be established.

## Common options [v3.0.4-plugins-outputs-graphtastic-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-4-plugins-outputs-graphtastic.md#v3.0.4-plugins-outputs-graphtastic-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.4-plugins-outputs-graphtastic-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.4-plugins-outputs-graphtastic-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.4-plugins-outputs-graphtastic-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 graphtastic outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  graphtastic {
    id => "my_plugin_id"
  }
}
```
