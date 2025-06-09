---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-outputs-jms.html
---

# Jms output plugin v3.0.5 [v3.0.5-plugins-outputs-jms]

* Plugin version: v3.0.5
* Released on: 2023-05-30
* [Changelog](https://github.com/logstash-plugins/logstash-output-jms/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-jms-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1339]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-jms). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1329]

Write events to a Jms Broker. Supports both Jms Queues and Topics.

For more information about Jms, see <http://docs.oracle.com/javaee/6/tutorial/doc/bncdq.html> For more information about the Ruby Gem used, see <http://github.com/reidmorrison/jruby-jms> Here is a config example : jms { include\_header ⇒ false include\_properties ⇒ false include\_body ⇒ true use\_jms\_timestamp ⇒ false queue\_name ⇒ "myqueue" yaml\_file ⇒ "\~/jms.yml" yaml\_section ⇒ "mybroker" }

## Jms Output Configuration Options [v3.0.5-plugins-outputs-jms-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`broker_url`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-broker_url) | [string](/lsr/value-types.md#string) | No |
| [`delivery_mode`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-delivery_mode) | [string](/lsr/value-types.md#string) | No |
| [`destination`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-destination) | [string](/lsr/value-types.md#string) | No |
| [`factory`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-factory) | [string](/lsr/value-types.md#string) | No |
| [`jndi_context`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-jndi_context) | [hash](/lsr/value-types.md#hash) | No |
| [`jndi_name`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-jndi_name) | [string](/lsr/value-types.md#string) | No |
| [`password`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-password) | [password](/lsr/value-types.md#password) | No |
| [`pub_sub`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-pub_sub) | [boolean](/lsr/value-types.md#boolean) | No |
| [`require_jars`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-require_jars) | [array](/lsr/value-types.md#array) | No |
| [`username`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-username) | [string](/lsr/value-types.md#string) | No |
| [`yaml_file`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-yaml_file) | [string](/lsr/value-types.md#string) | No |
| [`yaml_section`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-yaml_section) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-common-options) for a list of options supported by all output plugins.

### `broker_url` [v3.0.5-plugins-outputs-jms-broker_url]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Url to use when connecting to the JMS provider

### `delivery_mode` [v3.0.5-plugins-outputs-jms-delivery_mode]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

Name of delivery mode to use Options are "persistent" and "non\_persistent" if not defined nothing will be passed.

### `destination` [v3.0.5-plugins-outputs-jms-destination]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Name of the destination queue or topic to use. Mandatory

### `factory` [v3.0.5-plugins-outputs-jms-factory]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Name of JMS Provider Factory class

### `jndi_context` [v3.0.5-plugins-outputs-jms-jndi_context]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Mandatory if jndi lookup is being used, contains details on how to connect to JNDI server

### `jndi_name` [v3.0.5-plugins-outputs-jms-jndi_name]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Name of JNDI entry at which the Factory can be found

### `password` [v3.0.5-plugins-outputs-jms-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to use when connecting to the JMS provider

### `pub_sub` [v3.0.5-plugins-outputs-jms-pub_sub]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If pub-sub (topic) style should be used or not. Mandatory

### `require_jars` [v3.0.5-plugins-outputs-jms-require_jars]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

If you do not use an yaml configuration use either the factory or jndi\_name. An optional array of Jar file names to load for the specified JMS provider. By using this option it is not necessary to put all the JMS Provider specific jar files into the java CLASSPATH prior to starting Logstash.

### `username` [v3.0.5-plugins-outputs-jms-username]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username to connect to JMS provider with

### `yaml_file` [v3.0.5-plugins-outputs-jms-yaml_file]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Yaml config file

### `yaml_section` [v3.0.5-plugins-outputs-jms-yaml_section]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Yaml config file section name For some known examples, see: \[Example jms.yml]\(<https://github.com/reidmorrison/jruby-jms/blob/master/examples/jms.yml>)

## Common options [v3.0.5-plugins-outputs-jms-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-5-plugins-outputs-jms.md#v3.0.5-plugins-outputs-jms-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.5-plugins-outputs-jms-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.5-plugins-outputs-jms-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.5-plugins-outputs-jms-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 jms outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  jms {
    id => "my_plugin_id"
  }
}
```
