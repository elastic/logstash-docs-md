---
navigation_title: "solr_http"
---

# Solr_http output plugin [plugins-outputs-solr_http]


* Plugin version: v3.0.5
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-solr_http/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/output-solr_http-index.md).

## Installation [_installation_46]

For plugins not bundled by default, it is easy to install by running `bin/logstash-plugin install logstash-output-solr_http`. See [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html) for more details.


## Getting help [_getting_help_110]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-solr_http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_109]

This output lets you index&store your logs in Solr. If you want to get started quickly you should use version 4.4 or above in schemaless mode, which will try and guess your fields automatically. To turn that on, you can use the example included in the Solr archive:

```shell
    tar zxf solr-4.4.0.tgz
    cd example
    mv solr solr_ #back up the existing sample conf
    cp -r example-schemaless/solr/ .  #put the schemaless conf in place
    java -jar start.jar   #start Solr
```

You can learn more at [the Solr home page](https://lucene.apache.org/solr/)


## Solr_http Output Configuration Options [plugins-outputs-solr_http-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-solr_http.md#plugins-outputs-solr_http-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`document_id`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-document_id) | [string](introduction.md#string) | No |
| [`flush_size`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-flush_size) | [number](introduction.md#number) | No |
| [`idle_flush_time`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-idle_flush_time) | [number](introduction.md#number) | No |
| [`solr_url`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-solr_url) | [string](introduction.md#string) | No |

Also see [Common options](plugins-outputs-solr_http.md#plugins-outputs-solr_http-common-options) for a list of options supported by all output plugins.

 

### `document_id` [plugins-outputs-solr_http-document_id]

* Value type is [string](introduction.md#string)
* Default value is `nil`

Solr document ID for events. You’d typically have a variable here, like *%{{foo}}* so you can assign your own IDs


### `flush_size` [plugins-outputs-solr_http-flush_size]

* Value type is [number](introduction.md#number)
* Default value is `100`

Number of events to queue up before writing to Solr


### `idle_flush_time` [plugins-outputs-solr_http-idle_flush_time]

* Value type is [number](introduction.md#number)
* Default value is `1`

Amount of time since the last flush before a flush is done even if the number of buffered events is smaller than flush_size


### `solr_url` [plugins-outputs-solr_http-solr_url]

* Value type is [string](introduction.md#string)
* Default value is `"http://localhost:8983/solr"`

URL used to connect to Solr



## Common options [plugins-outputs-solr_http-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-codec) | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-outputs-solr_http.md#plugins-outputs-solr_http-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

### `codec` [plugins-outputs-solr_http-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [plugins-outputs-solr_http-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-solr_http-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 solr_http outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  solr_http {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




