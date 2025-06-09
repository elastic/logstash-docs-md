---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-inputs-gemfire.html
---

# Gemfire input plugin v2.0.5 [v2.0.5-plugins-inputs-gemfire]

* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-gemfire/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-gemfire-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_433]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-gemfire). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_433]

Push events to a GemFire region.

GemFire is an object database.

To use this plugin you need to add gemfire.jar to your CLASSPATH. Using format=json requires jackson.jar too; use of continuous queries requires antlr.jar.

Note: this plugin has only been tested with GemFire 7.0.

## Gemfire Input Configuration Options [v2.0.5-plugins-inputs-gemfire-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`cache_name`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-cache_name) | [string](/lsr/value-types.md#string) | No |
| [`cache_xml_file`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-cache_xml_file) | [string](/lsr/value-types.md#string) | No |
| [`interest_regexp`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-interest_regexp) | [string](/lsr/value-types.md#string) | No |
| [`query`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-query) | [string](/lsr/value-types.md#string) | No |
| [`region_name`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-region_name) | [string](/lsr/value-types.md#string) | No |
| [`serialization`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-serialization) | [string](/lsr/value-types.md#string) | No |
| [`threads`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-threads) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-common-options) for a list of options supported by all input plugins.

### `cache_name` [v2.0.5-plugins-inputs-gemfire-cache_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

Your client cache name

### `cache_xml_file` [v2.0.5-plugins-inputs-gemfire-cache_xml_file]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

The path to a GemFire client cache XML file.

Example:

```
<client-cache>
  <pool name="client-pool" subscription-enabled="true" subscription-redundancy="1">
      <locator host="localhost" port="31331"/>
  </pool>
  <region name="Logstash">
      <region-attributes refid="CACHING_PROXY" pool-name="client-pool" >
      </region-attributes>
  </region>
</client-cache>
```

### `interest_regexp` [v2.0.5-plugins-inputs-gemfire-interest_regexp]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `".*"`

A regexp to use when registering interest for cache events. Ignored if a :query is specified.

### `query` [v2.0.5-plugins-inputs-gemfire-query]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

A query to run as a GemFire "continuous query"; if specified it takes precedence over :interest\_regexp which will be ignore.

Important: use of continuous queries requires subscriptions to be enabled on the client pool.

### `region_name` [v2.0.5-plugins-inputs-gemfire-region_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"Logstash"`

The region name

### `serialization` [v2.0.5-plugins-inputs-gemfire-serialization]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `nil`

How the message is serialized in the cache. Can be one of "json" or "plain"; default is plain

### `threads` [v2.0.5-plugins-inputs-gemfire-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

## Common options [v2.0.5-plugins-inputs-gemfire-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v2-0-5-plugins-inputs-gemfire.md#v2.0.5-plugins-inputs-gemfire-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v2.0.5-plugins-inputs-gemfire-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v2.0.5-plugins-inputs-gemfire-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v2.0.5-plugins-inputs-gemfire-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.5-plugins-inputs-gemfire-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 gemfire inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  gemfire {
    id => "my_plugin_id"
  }
}
```

### `tags` [v2.0.5-plugins-inputs-gemfire-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v2.0.5-plugins-inputs-gemfire-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
