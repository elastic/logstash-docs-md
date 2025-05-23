---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-inputs-log4j.html
---

# Log4j input plugin v3.1.0 [v3.1.0-plugins-inputs-log4j]


* Plugin version: v3.1.0
* Released on: 2017-08-01
* [Changelog](https://github.com/logstash-plugins/logstash-input-log4j/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](input-log4j-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_702]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-log4j). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Deprecation Notice [_deprecation_notice_4]

::::{note}
This plugin is deprecated. It is recommended that you use filebeat to collect logs from log4j.
::::


The following section is a guide for how to migrate from SocketAppender to use filebeat.

To migrate away from log4j SocketAppender to using filebeat, you will need to make 3 changes:

1) Configure your log4j.properties (in your app) to write to a local file. 2) Install and configure filebeat to collect those logs and ship them to Logstash 3) Configure Logstash to use the beats input.

In your log4j.properties file, remove SocketAppender and replace it with RollingFileAppender.

For example, you can use the following log4j.properties configuration to write daily log files.

```
# Your app's log4j.properties (log4j 1.2 only)
log4j.rootLogger=daily
log4j.appender.daily=org.apache.log4j.rolling.RollingFileAppender
log4j.appender.daily.RollingPolicy=org.apache.log4j.rolling.TimeBasedRollingPolicy
log4j.appender.daily.RollingPolicy.FileNamePattern=/var/log/your-app/app.%d.log
log4j.appender.daily.layout = org.apache.log4j.PatternLayout
log4j.appender.daily.layout.ConversionPattern=%d{YYYY-MM-dd HH:mm:ss,SSSZ} %p %c{{1}}:%L - %m%n
```
Configuring log4j.properties in more detail is outside the scope of this migration guide.

Next, [install filebeat](https://www.elastic.co/guide/en/beats/filebeat/6.0/filebeat-installation.html). Based on the above log4j.properties, we can use this filebeat configuration:

```
# filebeat.yml
filebeat:
  prospectors:
    -
      paths:
        - /var/log/your-app/app.*.log
      input_type: log
output:
  logstash:
    hosts: ["your-logstash-host:5000"]
```
For more details on configuring filebeat, see [Configure filebeat](https://www.elastic.co/guide/en/beats/filebeat/6.0/filebeat-configuration.html).

Finally, configure Logstash with a beats input:

```
# logstash configuration
input {
  beats {
    port => 5000
  }
}
```
It is strongly recommended that you also enable TLS in filebeat and logstash beats input for protection and safety of your log data..

For more details on configuring the beats input, see [the logstash beats input documentation](https://www.elastic.co/guide/en/logstash/6.0/plugins-inputs-beats.html).


## Description [_description_696]

Read events over a TCP socket from a Log4j SocketAppender. This plugin works only with log4j version 1.x.

Can either accept connections from clients or connect to a server, depending on `mode`. Depending on which `mode` is configured, you need a matching SocketAppender or a SocketHubAppender on the remote side.

One event is created per received log4j LoggingEvent with the following schema:

* `timestamp` ⇒ the number of milliseconds elapsed from 1/1/1970 until logging event was created.
* `path` ⇒ the name of the logger
* `priority` ⇒ the level of this event
* `logger_name` ⇒ the name of the logger
* `thread` ⇒ the thread name making the logging request
* `class` ⇒ the fully qualified class name of the caller making the logging request.
* `file` ⇒ the source file name and line number of the caller making the logging request in a colon-separated format "fileName:lineNumber".
* `method` ⇒ the method name of the caller making the logging request.
* `NDC` ⇒ the NDC string
* `stack_trace` ⇒ the multi-line stack-trace

Also if the original log4j LoggingEvent contains MDC hash entries, they will be merged in the event as fields.


## Log4j Input Configuration Options [v3.1.0-plugins-inputs-log4j-options]

This plugin supports the following configuration options plus the [Common options](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`mode`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["server", "client"]` | No |
| [`port`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`proxy_protocol`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-proxy_protocol) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-common-options) for a list of options supported by all input plugins.

 

### `host` [v3.1.0-plugins-inputs-log4j-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

When mode is `server`, the address to listen on. When mode is `client`, the address to connect to.


### `mode` [v3.1.0-plugins-inputs-log4j-mode]

* Value can be any of: `server`, `client`
* Default value is `"server"`

Mode to operate in. `server` listens for client connections, `client` connects to a server.


### `port` [v3.1.0-plugins-inputs-log4j-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `4560`

When mode is `server`, the port to listen on. When mode is `client`, the port to connect to.


### `proxy_protocol` [v3.1.0-plugins-inputs-log4j-proxy_protocol]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Proxy protocol support, only v1 is supported at this time [http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt)



## Common options [v3.1.0-plugins-inputs-log4j-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-1-0-plugins-inputs-log4j.md#v3.1.0-plugins-inputs-log4j-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.1.0-plugins-inputs-log4j-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.1.0-plugins-inputs-log4j-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.1.0-plugins-inputs-log4j-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.0-plugins-inputs-log4j-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 log4j inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  log4j {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.1.0-plugins-inputs-log4j-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.1.0-plugins-inputs-log4j-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



