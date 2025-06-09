---
navigation_title: "v3.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.0-plugins-inputs-snmptrap.html
---

# Snmptrap input plugin v3.1.0 [v3.1.0-plugins-inputs-snmptrap]

* Plugin version: v3.1.0
* Released on: 2021-11-19
* [Changelog](https://github.com/logstash-plugins/logstash-input-snmptrap/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [overview list](input-snmptrap-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_881]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-snmptrap). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_874]

Read snmp trap messages as events

Resulting `message` field resembles:

```
  #<SNMP::SNMPv1_Trap:0x6f1a7a4 @varbind_list=[#<SNMP::VarBind:0x2d7bcd8f @value="teststring",
  @name=[1.11.12.13.14.15]>], @timestamp=#<SNMP::TimeTicks:0x1af47e9d @value=55>, @generic_trap=6,
  @enterprise=[1.2.3.4.5.6], @source_ip="127.0.0.1", @agent_addr=#<SNMP::IpAddress:0x29a4833e @value="\xC0\xC1\xC2\xC3">,
  @specific_trap=99>
```

## Compatibility with the Elastic Common Schema (ECS) [v3.1.0-plugins-inputs-snmptrap-ecs]

Because SNMP data has specific field names based on OIDs, we recommend setting a [`target`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-target). The source host field changes based on [`ecs_compatibility`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-ecs_compatibility).

| | | | |
| :- | :- | :- | :- |
| ECS disabled | ECS v1, v8 | *Description* | *\[host]* |

## Snmptrap Input Configuration Options [v3.1.0-plugins-inputs-snmptrap-options]

This plugin supports the following configuration options plus the [Common options](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`community`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-community) | [array](/lsr/value-types.md#array) | No |
| [`ecs_compatibility`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`host`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-host) | [string](/lsr/value-types.md#string) | No |
| [`port`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-port) | [number](/lsr/value-types.md#number) | No |
| [`target`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-target) | [string](/lsr/value-types.md#string) | No |
| [`yamlmibdir`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-yamlmibdir) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-common-options) for a list of options supported by all input plugins.

### `community` [v3.1.0-plugins-inputs-snmptrap-community]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `"public"`

SNMP Community String to listen for.

### `ecs_compatibility` [v3.1.0-plugins-inputs-snmptrap-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: does not use ECS-compatible field names (fields might be set at the root of the event)
  * `v1`, `v8`: avoids field names that might conflict with Elastic Common Schema (for example, the `host` field)

* Default value depends on which version of Logstash is running:

  * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
  * Otherwise, the default value is `disabled`.

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current).

### `host` [v3.1.0-plugins-inputs-snmptrap-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The address to listen on

### `port` [v3.1.0-plugins-inputs-snmptrap-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1062`

The port to listen on. Remember that ports less than 1024 (privileged ports) may require root to use. hence the default of 1062.

### `target` [v3.1.0-plugins-inputs-snmptrap-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting

The name of the field under which SNMP payloads are assigned. If not specified data will be stored in the root of the event.

Setting a target is recommended when [`ecs_compatibility`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-ecs_compatibility) is enabled.

### `yamlmibdir` [v3.1.0-plugins-inputs-snmptrap-yamlmibdir]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

directory of YAML MIB maps (same format ruby-snmp uses)

## Common options [v3.1.0-plugins-inputs-snmptrap-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-1-0-plugins-inputs-snmptrap.md#v3.1.0-plugins-inputs-snmptrap-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.1.0-plugins-inputs-snmptrap-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.1.0-plugins-inputs-snmptrap-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.0-plugins-inputs-snmptrap-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.0-plugins-inputs-snmptrap-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 snmptrap inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  snmptrap {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.1.0-plugins-inputs-snmptrap-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.1.0-plugins-inputs-snmptrap-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
