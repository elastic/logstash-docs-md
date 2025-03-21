---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-outputs-gemfire.html
---

# Gemfire output plugin v2.0.5 [v2.0.5-plugins-outputs-gemfire]


* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-gemfire/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-gemfire-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1244]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-gemfire). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1237]

Push events to a GemFire region.

GemFire is an object database.

To use this plugin you need to add gemfire.jar to your CLASSPATH; using format=json requires jackson.jar too.

Note: this plugin has only been tested with GemFire 7.0.


## Gemfire Output Configuration Options [v2.0.5-plugins-outputs-gemfire-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`cache_name`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-cache_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`cache_xml_file`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-cache_xml_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key_format`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-key_format) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`region_name`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-region_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-common-options) for a list of options supported by all output plugins.

 

### `cache_name` [v2.0.5-plugins-outputs-gemfire-cache_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

Your client cache name


### `cache_xml_file` [v2.0.5-plugins-outputs-gemfire-cache_xml_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

The path to a GemFire client cache XML file.

Example:

```xml
     <client-cache>
       <pool name="client-pool">
           <locator host="localhost" port="31331"/>
       </pool>
       <region name="Logstash">
           <region-attributes refid="CACHING_PROXY" pool-name="client-pool" >
           </region-attributes>
       </region>
     </client-cache>
```


### `key_format` [v2.0.5-plugins-outputs-gemfire-key_format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{host}}-%{@timestamp}"`

A sprintf format to use when building keys


### `region_name` [v2.0.5-plugins-outputs-gemfire-region_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

The region name



## Common options [v2.0.5-plugins-outputs-gemfire-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-5-plugins-outputs-gemfire.md#v2.0.5-plugins-outputs-gemfire-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v2.0.5-plugins-outputs-gemfire-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.5-plugins-outputs-gemfire-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.5-plugins-outputs-gemfire-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 gemfire outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  gemfire {
    id => "my_plugin_id"
  }
}
```



