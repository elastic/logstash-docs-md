---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-outputs-jms.html
---

# Jms output plugin v3.0.1 [v3.0.1-plugins-outputs-jms]


* Plugin version: v3.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-jms/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-jms-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1334]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-jms). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1324]

Write events to a Jms Broker. Supports both Jms Queues and Topics.

For more information about Jms, see [http://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html](http://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html) For more information about the Ruby Gem used, see [http://github.com/reidmorrison/jruby-jms](http://github.com/reidmorrison/jruby-jms) Here is a config example : jms { include_header ⇒ false include_properties ⇒ false include_body ⇒ true use_jms_timestamp ⇒ false queue_name ⇒ "myqueue" yaml_file ⇒ "~/jms.yml" yaml_section ⇒ "mybroker" }


## Jms Output Configuration Options [v3.0.1-plugins-outputs-jms-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`broker_url`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-broker_url) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`delivery_mode`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-delivery_mode) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`destination`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-destination) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`factory`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-factory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`jndi_context`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-jndi_context) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`jndi_name`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-jndi_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pub_sub`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-pub_sub) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`require_jars`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-require_jars) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`username`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`yaml_file`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-yaml_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`yaml_section`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-yaml_section) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-common-options) for a list of options supported by all output plugins.

 

### `broker_url` [v3.0.1-plugins-outputs-jms-broker_url]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Url to use when connecting to the JMS provider


### `delivery_mode` [v3.0.1-plugins-outputs-jms-delivery_mode]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `nil`

Name of delivery mode to use Options are "persistent" and "non_persistent" if not defined nothing will be passed.


### `destination` [v3.0.1-plugins-outputs-jms-destination]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the destination queue or topic to use. Mandatory


### `factory` [v3.0.1-plugins-outputs-jms-factory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of JMS Provider Factory class


### `jndi_context` [v3.0.1-plugins-outputs-jms-jndi_context]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Mandatory if jndi lookup is being used, contains details on how to connect to JNDI server


### `jndi_name` [v3.0.1-plugins-outputs-jms-jndi_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of JNDI entry at which the Factory can be found


### `password` [v3.0.1-plugins-outputs-jms-password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password to use when connecting to the JMS provider


### `pub_sub` [v3.0.1-plugins-outputs-jms-pub_sub]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If pub-sub (topic) style should be used or not. Mandatory


### `require_jars` [v3.0.1-plugins-outputs-jms-require_jars]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

If you do not use an yaml configuration use either the factory or jndi_name. An optional array of Jar file names to load for the specified JMS provider. By using this option it is not necessary to put all the JMS Provider specific jar files into the java CLASSPATH prior to starting Logstash.


### `username` [v3.0.1-plugins-outputs-jms-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username to connect to JMS provider with


### `yaml_file` [v3.0.1-plugins-outputs-jms-yaml_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Yaml config file


### `yaml_section` [v3.0.1-plugins-outputs-jms-yaml_section]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Yaml config file section name For some known examples, see: [Example jms.yml](https://github.com/reidmorrison/jruby-jms/blob/master/examples/jms.yml)



## Common options [v3.0.1-plugins-outputs-jms-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-1-plugins-outputs-jms.md#v3.0.1-plugins-outputs-jms-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.1-plugins-outputs-jms-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.1-plugins-outputs-jms-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.1-plugins-outputs-jms-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 jms outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  jms {
    id => "my_plugin_id"
  }
}
```



