---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-inputs-jms.html
---

# Jms input plugin v3.0.2 [v3.0.2-plugins-inputs-jms]


* Plugin version: v3.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-jms/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-jms-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_613]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-jms). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_607]

Read events from a Jms Broker. Supports both Jms Queues and Topics.

For more information about Jms, see [http://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html](http://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html) For more information about the Ruby Gem used, see [http://github.com/reidmorrison/jruby-jms](http://github.com/reidmorrison/jruby-jms) Here is a config example to pull from a queue: jms { include_header ⇒ false include_properties ⇒ false include_body ⇒ true use_jms_timestamp ⇒ false interval ⇒ 10 destination ⇒ "myqueue" pub-sub ⇒ false yaml_file ⇒ "~/jms.yml" yaml_section ⇒ "mybroker" }


## Jms Input Configuration Options [v3.0.2-plugins-inputs-jms-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`broker_url`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-broker_url) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`destination`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-destination) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`factory`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-factory) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`include_body`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-include_body) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`include_header`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-include_header) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`include_properties`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-include_properties) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`interval`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jndi_context`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-jndi_context) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`jndi_name`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-jndi_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`pub_sub`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-pub_sub) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`require_jars`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-require_jars) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`runner`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-runner) | [string](logstash://reference/configuration-file-structure.md#string), one of `["consumer", "async", "thread"]` | No |
| [`selector`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-selector) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`threads`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`timeout`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`use_jms_timestamp`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-use_jms_timestamp) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`username`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`yaml_file`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-yaml_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`yaml_section`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-yaml_section) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-common-options) for a list of options supported by all input plugins.

 

### `broker_url` [v3.0.2-plugins-inputs-jms-broker_url]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Url to use when connecting to the JMS provider


### `destination` [v3.0.2-plugins-inputs-jms-destination]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of the destination queue or topic to use.


### `factory` [v3.0.2-plugins-inputs-jms-factory]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of JMS Provider Factory class


### `include_body` [v3.0.2-plugins-inputs-jms-include_body]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Include JMS Message Body in the event Supports TextMessage, MapMessage and ByteMessage If the JMS Message is a TextMessage or ByteMessage, then the value will be in the "message" field of the event If the JMS Message is a MapMessage, then all the key/value pairs will be added in the Hashmap of the event StreamMessage and ObjectMessage are not supported


### `include_header` [v3.0.2-plugins-inputs-jms-include_header]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

A JMS message has three parts : Message Headers (required) Message Properties (optional) Message Bodies (optional) You can tell the input plugin which parts should be included in the event produced by Logstash

Include JMS Message Header Field values in the event


### `include_properties` [v3.0.2-plugins-inputs-jms-include_properties]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Include JMS Message Properties Field values in the event


### `interval` [v3.0.2-plugins-inputs-jms-interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Polling interval in seconds. This is the time sleeping between asks to a consumed Queue. This parameter has non influence in the case of a subcribed Topic.


### `jndi_context` [v3.0.2-plugins-inputs-jms-jndi_context]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Mandatory if jndi lookup is being used, contains details on how to connect to JNDI server


### `jndi_name` [v3.0.2-plugins-inputs-jms-jndi_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Name of JNDI entry at which the Factory can be found


### `password` [v3.0.2-plugins-inputs-jms-password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password to use when connecting to the JMS provider


### `pub_sub` [v3.0.2-plugins-inputs-jms-pub_sub]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If pub-sub (topic) style should be used.


### `require_jars` [v3.0.2-plugins-inputs-jms-require_jars]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

If you do not use an yaml configuration use either the factory or jndi_name. An optional array of Jar file names to load for the specified JMS provider. By using this option it is not necessary to put all the JMS Provider specific jar files into the java CLASSPATH prior to starting Logstash.


### `runner` [v3.0.2-plugins-inputs-jms-runner]

* Value can be any of: `consumer`, `async`, `thread`
* Default value is `"consumer"`

Choose an implementation of the run block. Value can be either consumer, async or thread


### `selector` [v3.0.2-plugins-inputs-jms-selector]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Set the selector to use to get messages off the queue or topic


### `threads` [v3.0.2-plugins-inputs-jms-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`


### `timeout` [v3.0.2-plugins-inputs-jms-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Initial connection timeout in seconds.


### `use_jms_timestamp` [v3.0.2-plugins-inputs-jms-use_jms_timestamp]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Convert the JMSTimestamp header field to the @timestamp value of the event


### `username` [v3.0.2-plugins-inputs-jms-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username to connect to JMS provider with


### `yaml_file` [v3.0.2-plugins-inputs-jms-yaml_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Yaml config file


### `yaml_section` [v3.0.2-plugins-inputs-jms-yaml_section]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Yaml config file section name For some known examples, see: [Example jms.yml](https://github.com/reidmorrison/jruby-jms/blob/master/examples/jms.yml)



## Common options [v3.0.2-plugins-inputs-jms-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-2-plugins-inputs-jms.md#v3.0.2-plugins-inputs-jms-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.2-plugins-inputs-jms-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.2-plugins-inputs-jms-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.2-plugins-inputs-jms-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-inputs-jms-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jms inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  jms {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.2-plugins-inputs-jms-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.2-plugins-inputs-jms-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



