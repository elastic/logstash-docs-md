---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-outputs-neo4j.html
---

# Neo4j output plugin v2.0.5 [v2.0.5-plugins-outputs-neo4j]


* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-neo4j/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-neo4j-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1461]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-neo4j). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1451]

The neo4j output.


## Neo4j Output Configuration Options [v2.0.5-plugins-outputs-neo4j-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`path`](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-path) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-common-options) for a list of options supported by all output plugins.

 

### `path` [v2.0.5-plugins-outputs-neo4j-path]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The path within your file system where the neo4j database is located



## Common options [v2.0.5-plugins-outputs-neo4j-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-5-plugins-outputs-neo4j.md#v2.0.5-plugins-outputs-neo4j-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v2.0.5-plugins-outputs-neo4j-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v2.0.5-plugins-outputs-neo4j-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.5-plugins-outputs-neo4j-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 neo4j outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  neo4j {
    id => "my_plugin_id"
  }
}
```



