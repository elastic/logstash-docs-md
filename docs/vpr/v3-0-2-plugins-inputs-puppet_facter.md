---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-inputs-puppet_facter.html
---

# Puppet_facter input plugin v3.0.2 [v3.0.2-plugins-inputs-puppet_facter]


* Plugin version: v3.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-puppet_facter/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-puppet_facter-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_734]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-puppet_facter). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_727]

Connects to a puppet server and requests facts


## Puppet_facter Input Configuration Options [v3.0.2-plugins-inputs-puppet_facter-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`environment`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-environment) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`interval`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`port`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`private_key`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-private_key) | a valid filesystem path | No |
| [`public_key`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-public_key) | a valid filesystem path | No |
| [`ssl`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-common-options) for a list of options supported by all input plugins.

 

### `environment` [v3.0.2-plugins-inputs-puppet_facter-environment]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"production"`


### `host` [v3.0.2-plugins-inputs-puppet_facter-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`


### `interval` [v3.0.2-plugins-inputs-puppet_facter-interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `600`


### `port` [v3.0.2-plugins-inputs-puppet_facter-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `8140`


### `private_key` [v3.0.2-plugins-inputs-puppet_facter-private_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.


### `public_key` [v3.0.2-plugins-inputs-puppet_facter-public_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.


### `ssl` [v3.0.2-plugins-inputs-puppet_facter-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`



## Common options [v3.0.2-plugins-inputs-puppet_facter-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-2-plugins-inputs-puppet_facter.md#v3.0.2-plugins-inputs-puppet_facter-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.2-plugins-inputs-puppet_facter-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.2-plugins-inputs-puppet_facter-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.2-plugins-inputs-puppet_facter-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-inputs-puppet_facter-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 puppet_facter inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  puppet_facter {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.2-plugins-inputs-puppet_facter-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.2-plugins-inputs-puppet_facter-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



