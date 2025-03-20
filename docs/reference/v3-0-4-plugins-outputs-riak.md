---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-outputs-riak.html
---

# Riak output plugin v3.0.4 [v3.0.4-plugins-outputs-riak]


* Plugin version: v3.0.4
* Released on: 2018-04-06
* [Changelog](https://github.com/logstash-plugins/logstash-output-riak/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](output-riak-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1517]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-riak). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1507]

Riak is a distributed k/v store from Basho. It’s based on the Dynamo model.


## Riak Output Configuration Options [v3.0.4-plugins-outputs-riak-options]

This plugin supports the following configuration options plus the [Common options](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`bucket`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-bucket) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`bucket_props`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-bucket_props) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`enable_search`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-enable_search) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`enable_ssl`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-enable_ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`indices`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-indices) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`key_name`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-key_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`nodes`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-nodes) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`proto`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-proto) | [string](logstash://reference/configuration-file-structure.md#string), one of `["http", "pb"]` | No |
| [`ssl_opts`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-ssl_opts) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |

Also see [Common options](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-common-options) for a list of options supported by all output plugins.

 

### `bucket` [v3.0.4-plugins-outputs-riak-bucket]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["logstash-%{+YYYY.MM.dd}"]`

The bucket name to write events to Expansion is supported here as values are passed through event.sprintf Multiple buckets can be specified here but any bucket-specific settings defined apply to ALL the buckets.


### `bucket_props` [v3.0.4-plugins-outputs-riak-bucket_props]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Bucket properties (NYI) Logstash hash of properties for the bucket i.e.

```ruby
    bucket_props => {
        "r" => "one"
        "w" => "one"
        "dw", "one
     }
or
[source,ruby]
    bucket_props => { "n_val" => "3" }
Properties will be passed as-is
```


### `enable_search` [v3.0.4-plugins-outputs-riak-enable_search]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Search Enable search on the bucket defined above


### `enable_ssl` [v3.0.4-plugins-outputs-riak-enable_ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

SSL Enable SSL


### `indices` [v3.0.4-plugins-outputs-riak-indices]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Indices Array of fields to add 2i on e.g.

```ruby
    `indices => ["source_host", "type"]
Off by default as not everyone runs eleveldb
```


### `key_name` [v3.0.4-plugins-outputs-riak-key_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The event key name variables are valid here.

Choose this carefully. Best to let riak decide.


### `nodes` [v3.0.4-plugins-outputs-riak-nodes]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{"localhost"=>"8098"}`

The nodes of your Riak cluster This can be a single host or a Logstash hash of node/port pairs e.g

```ruby
    {
        "node1" => "8098"
        "node2" => "8098"
    }
```


### `proto` [v3.0.4-plugins-outputs-riak-proto]

* Value can be any of: `http`, `pb`
* Default value is `"http"`

The protocol to use HTTP or ProtoBuf Applies to ALL backends listed above No mix and match


### `ssl_opts` [v3.0.4-plugins-outputs-riak-ssl_opts]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

SSL Options Options for SSL connections Only applied if SSL is enabled Logstash hash that maps to the riak-client options here: [https://github.com/basho/riak-ruby-client/wiki/Connecting-to-Riak](https://github.com/basho/riak-ruby-client/wiki/Connecting-to-Riak) You’ll likely want something like this:

```ruby
    ssl_opts => {
       "pem" => "/etc/riak.pem"
       "ca_path" => "/usr/share/certificates"
    }
```

Per the riak client docs, the above sample options will turn on SSL `VERIFY_PEER`



## Common options [v3.0.4-plugins-outputs-riak-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-4-plugins-outputs-riak.md#v3.0.4-plugins-outputs-riak-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.4-plugins-outputs-riak-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.4-plugins-outputs-riak-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.4-plugins-outputs-riak-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 riak outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  riak {
    id => "my_plugin_id"
  }
}
```



