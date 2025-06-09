---
navigation_title: "v1.1.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.1.2-plugins-inputs-azure_event_hubs.html
---

# Azure Event Hubs plugin [v1.1.2-plugins-inputs-azure_event_hubs]

* Plugin version: v1.1.2
* Released on: 2019-05-28
* [Changelog](https://github.com/logstash-plugins/logstash-input-azure_event_hubs/blob/v1.1.2/CHANGELOG.md)

For other versions, see the [overview list](input-azure_event_hubs-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_158]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-azure_event_hubs). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_158]

This plugin consumes events from [Azure Event Hubs](https://azure.microsoft.com/en-us/services/event-hubs), a highly scalable data streaming platform and event ingestion service. Event producers send events to the Azure Event Hub, and this plugin consumes those events for use with Logstash.

Many Azure services integrate with the Azure Event Hubs. [Azure Monitor](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-azure-monitor), for example, integrates with Azure Event Hubs to provide infrastructure metrics.

### Event Hub connection string [_event_hub_connection_string_20]

The plugin uses the connection string to access Azure Events Hubs. Find the connection string here: [Azure Portal](https://portal.azure.com)`-> Event Hub -> Shared access polices`. The event\_hub\_connections option passes the Event Hub connection strings for the basic configuration.

Sample connection string:

```
Endpoint=sb://logstash.servicebus.windows.net/;SharedAccessKeyName=activity-log-read-only;SharedAccessKey=mm6AbDcEfj8lk7sjsbzoTJ10qAkiSaG663YykEAG2eg=;EntityPath=insights-operational-logs
```

### Blob Storage and connection string [_blob_storage_and_connection_string_20]

[Azure Blob Storage account](https://azure.microsoft.com/en-us/services/storage/blobs) is an essential part of Azure-to-Logstash configuration. A Blob Storage account is a central location that enables multiple instances of Logstash to work together to process events. It records the offset (location) of processed events. On restart, Logstash resumes processing exactly where it left off.

Configuration notes:

* A Blob Storage account is highly recommended for use with this plugin, and is likely required for production servers.
* The `storage_connection` option passes the blob storage connection string.
* Configure all Logstash instances to use the same `storage_connection` to get the benefits of shared processing.

Sample Blob Storage connection string:

```
DefaultEndpointsProtocol=https;AccountName=logstash;AccountKey=ETOPnkd/hDAWidkEpPZDiXffQPku/SZdXhPSLnfqdRTalssdEuPkZwIcouzXjCLb/xPZjzhmHfwRCGo0SBSw==;EndpointSuffix=core.windows.net
```

Find the connection string to Blob Storage here: [Azure Portal](https://portal.azure.com)`-> Blob Storage account -> Access keys`.

### Best practices [v1.1.2-plugins-inputs-azure_event_hubs-best-practices]

Here are some guidelines to help you avoid data conflicts that can cause lost events.

* **Create a Logstash consumer group.** Create a new consumer group specifically for Logstash. Do not use the $default or any other consumer group that might already be in use. Reusing consumer groups among non-related consumers can cause unexpected behavior and possibly lost events. All Logstash instances should use the same consumer group so that they can work together for processing events.

* **Avoid overwriting offset with multiple Event Hubs.** The offsets (position) of the Event Hubs are stored in the configured Azure Blob store. The Azure Blob store uses paths like a file system to store the offsets. If the paths between multiple Event Hubs overlap, then the offsets may be stored incorrectly. To avoid duplicate file paths, use the advanced configuration model and make sure that at least one of these options is different per Event Hub:

  * storage\_connection
  * storage\_container (defaults to Event Hub name if not defined)
  * consumer\_group

* **Set number of threads correctly.** The number of threads should equal the number of Event Hubs plus one (or more). Each Event Hub needs at least one thread. An additional thread is needed to help coordinate the other threads. The number of threads should not exceed the number of Event Hubs multiplied by the number of partitions per Event Hub plus one. Threads are currently available only as a global setting.

  * Sample scenario: Event Hubs = 4. Partitions on each Event Hub = 3. Minimum threads is 5 (4 Event Hubs plus one). Maximum threads is 13 (4 Event Hubs times 3 partitions plus one).
  * If you’re collecting activity logs from one event hub instance, then only 2 threads (1 Event Hub plus one) are required.

## Configuration models [v1.1.2-plugins-inputs-azure_event_hubs-eh_config_models]

This plugin supports two configuration models: basic and advanced. Basic configuration is recommended for most use cases, and is illustrated in the examples throughout this topic.

### Basic configuration (default) [v1.1.2-plugins-inputs-azure_event_hubs-eh_basic_config]

Basic configuration is the default and supports consuming from multiple Event Hubs. All Events Hubs, except for the connection string, share the same configuration.

You supply a list of Event Hub connection strings, complete with the Event Hub EntityPath that defines the Event Hub name. All other configuration settings are shared.

```
input {
   azure_event_hubs {
      event_hub_connections => ["Endpoint=sb://example1...EntityPath=insights-logs-errors", "Endpoint=sb://example2...EntityPath=insights-metrics-pt1m"]
      threads => 8
      decorate_events => true
      consumer_group => "logstash"
      storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
   }
}
```

### Advanced configuration [v1.1.2-plugins-inputs-azure_event_hubs-eh_advanced_config]

The advanced configuration model accommodates deployments where different Event Hubs require different configurations. Options can be configured per Event Hub. You provide a list of Event Hub names through the `event_hubs` option. Under each name, specify the configuration for that Event Hub. Options can be defined globally or expressed per Event Hub.

If the same configuration option appears in both the global and `event_hub` sections, the more specific (event\_hub) setting takes precedence.

Advanced configuration is not necessary or recommended for most use cases.

```
input {
   azure_event_hubs {
     config_mode => "advanced"
     threads => 8
     decorate_events => true
     storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
     event_hubs => [
        {"insights-operational-logs" => {
         event_hub_connection => "Endpoint=sb://example1..."
         initial_position => "beginning"
         consumer_group => "iam_team"
        }},
      {"insights-metrics-pt1m" => {
         event_hub_connection => "Endpoint=sb://example2..."
         initial_position => "end"
         consumer_group => "db_team"
       }}
     ]
   }
}
```

In this example, `storage_connection` and `decorate_events` are applied globally. The two Event Hubs each have their own settings for `consumer_groups` and `initial_position`.

## Azure Event Hubs Configuration Options [v1.1.2-plugins-inputs-azure_event_hubs-options]

This plugin supports the following configuration options plus the [Common options](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`config_mode`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-config_mode) | [string](/lsr/value-types.md#string), (`basic` or `advanced`) | No |
| [`event_hubs`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-event_hubs) | [array](/lsr/value-types.md#array) | Yes, when `config_mode => advanced` |
| [`event_hub_connections`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-event_hub_connections) | [array](/lsr/value-types.md#array) | Yes, when `config_mode => basic` |
| [`event_hub_connection`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-event_hub_connection) | [string](/lsr/value-types.md#string) | Yes, when `config_mode => advanced` |
| [`checkpoint_interval`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-checkpoint_interval) | [number](/lsr/value-types.md#number) | No |
| [`consumer_group`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-consumer_group) | [string](/lsr/value-types.md#string) | No |
| [`decorate_events`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-decorate_events) | [boolean](/lsr/value-types.md#boolean) | No |
| [`initial_position`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-initial_position) | [string](/lsr/value-types.md#string), (`beginning`, `end`, or `look_back`) | No |
| [`initial_position_look_back`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-initial_position_look_back) | [number](/lsr/value-types.md#number) | No, unless `initial_position => look_back` |
| [`max_batch_size`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-max_batch_size) | [number](/lsr/value-types.md#number) | No |
| [`storage_connection`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-storage_connection) | [string](/lsr/value-types.md#string) | No |
| [`storage_container`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-storage_container) | [string](/lsr/value-types.md#string) | No |
| [`threads`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-threads) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-common-options) for a list of options supported by all input plugins.

All Event Hubs options are common to both basic and advanced configurations, with the following exceptions. The basic configuration uses `event_hub_connections` to support multiple connections. The advanced configuration uses `event_hubs` and `event_hub_connection` (singular).

### `config_mode` [v1.1.2-plugins-inputs-azure_event_hubs-config_mode]

* Value type is [string](/lsr/value-types.md#string)
* Valid entries are `basic` or `advanced`
* Default value is `basic`

Sets configuration to either [Basic configuration (default)](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-eh_basic_config) or [Advanced configuration](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-eh_advanced_config).

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"  , "Endpoint=sb://example2...;EntityPath=event_hub_name2"  ]
}
```

### `event_hubs` [v1.1.2-plugins-inputs-azure_event_hubs-event_hubs]

* Value type is [array](/lsr/value-types.md#array)
* No default value
* Ignored for basic configuration
* Required for advanced configuration

Defines the Event Hubs to be read. An array of hashes where each entry is a hash of the Event Hub name and its configuration options.

```
azure_event_hubs {
  config_mode => "advanced"
  event_hubs => [
      { "event_hub_name1" => {
          event_hub_connection => "Endpoint=sb://example1..."
      }},
      { "event_hub_name2" => {
          event_hub_connection => "Endpoint=sb://example2..."
          storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
          storage_container => "my_container"
     }}
   ]
   consumer_group => "logstash" # shared across all Event Hubs
}
```

### `event_hub_connections` [v1.1.2-plugins-inputs-azure_event_hubs-event_hub_connections]

* Value type is [array](/lsr/value-types.md#array)
* No default value
* Required for basic configuration

List of connection strings that identifies the Event Hubs to be read. Connection strings include the EntityPath for the Event Hub.

The `event_hub_connections` option is defined per Event Hub. All other configuration options are shared among Event Hubs.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"  , "Endpoint=sb://example2...;EntityPath=event_hub_name2"  ]
}
```

### `event_hub_connection` [v1.1.2-plugins-inputs-azure_event_hubs-event_hub_connection]

* Value type is [string](/lsr/value-types.md#string)
* No default value
* Valid only for advanced configuration

Connection string that identifies the Event Hub to be read. Advanced configuration options can be set per Event Hub. This option modifies `event_hub_name`, and should be nested under it. (See sample.) This option accepts only one connection string.

```
azure_event_hubs {
   config_mode => "advanced"
   event_hubs => [
     { "event_hub_name1" => {
        event_hub_connection => "Endpoint=sb://example1...;EntityPath=event_hub_name1"
     }}
   ]
}
```

### `checkpoint_interval` [v1.1.2-plugins-inputs-azure_event_hubs-checkpoint_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5` seconds
* Set to `0` to disable.

Interval in seconds to write checkpoints during batch processing. Checkpoints tell Logstash where to resume processing after a restart. Checkpoints are automatically written at the end of each batch, regardless of this setting.

Writing checkpoints too frequently can slow down processing unnecessarily.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   checkpoint_interval => 5
}
```

### `consumer_group` [v1.1.2-plugins-inputs-azure_event_hubs-consumer_group]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `$Default`

Consumer group used to read the Event Hub(s). Create a consumer group specifically for Logstash. Then ensure that all instances of Logstash use that consumer group so that they can work together properly.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   consumer_group => "logstash"
}
```

### `decorate_events` [v1.1.2-plugins-inputs-azure_event_hubs-decorate_events]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Adds metadata about the Event Hub, including Event Hub name, consumer\_group, processor\_host, partition, offset, sequence, timestamp, and event\_size.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   decorate_events => true
}
```

### `initial_position` [v1.1.2-plugins-inputs-azure_event_hubs-initial_position]

* Value type is [string](/lsr/value-types.md#string)
* Valid arguments are `beginning`, `end`, `look_back`
* Default value is `beginning`

When first reading from an Event Hub, start from this position:

* `beginning` reads all pre-existing events in the Event Hub
* `end` does not read any pre-existing events in the Event Hub
* `look_back` reads `end` minus a number of seconds worth of pre-existing events. You control the number of seconds using the `initial_position_look_back` option.

Note: If `storage_connection` is set, the `initial_position` value is used only the first time Logstash reads from the Event Hub.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   initial_position => "beginning"
}
```

### `initial_position_look_back` [v1.1.2-plugins-inputs-azure_event_hubs-initial_position_look_back]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `86400`
* Used only if `initial_position` is set to `look-back`

Number of seconds to look back to find the initial position for pre-existing events. This option is used only if `initial_position` is set to `look_back`. If `storage_connection` is set, this configuration applies only the first time Logstash reads from the Event Hub.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   initial_position => "look_back"
   initial_position_look_back => 86400
}
```

### `max_batch_size` [v1.1.2-plugins-inputs-azure_event_hubs-max_batch_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `125`

Maximum number of events retrieved and processed together. A checkpoint is created after each batch. Increasing this value may help with performance, but requires more memory.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   max_batch_size => 125
}
```

### `storage_connection` [v1.1.2-plugins-inputs-azure_event_hubs-storage_connection]

* Value type is [string](/lsr/value-types.md#string)
* No default value

Connection string for blob account storage. Blob account storage persists the offsets between restarts, and ensures that multiple instances of Logstash process different partitions. When this value is set, restarts resume where processing left off. When this value is not set, the `initial_position` value is used on every restart.

We strongly recommend that you define this value for production environments.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
}
```

### `storage_container` [v1.1.2-plugins-inputs-azure_event_hubs-storage_container]

* Value type is [string](/lsr/value-types.md#string)
* Defaults to the Event Hub name if not defined

Name of the storage container used to persist offsets and allow multiple instances of Logstash to work together.

```
azure_event_hubs {
   event_hub_connections => ["Endpoint=sb://example1...;EntityPath=event_hub_name1"]
   storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
   storage_container => "my_container"
}
```

To avoid overwriting offsets, you can use different storage containers. This is particularly important if you are monitoring two Event Hubs with the same name. You can use the advanced configuration model to configure different storage containers.

```
azure_event_hubs {
     config_mode => "advanced"
     consumer_group => "logstash"
     storage_connection => "DefaultEndpointsProtocol=https;AccountName=example...."
     event_hubs => [
        {"insights-operational-logs" => {
         event_hub_connection => "Endpoint=sb://example1..."
         storage_container => "insights-operational-logs-1"
        }},
        {"insights-operational-logs" => {
         event_hub_connection => "Endpoint=sb://example2..."
         storage_container => "insights-operational-logs-2"
        }}
     ]
   }
```

### `threads` [v1.1.2-plugins-inputs-azure_event_hubs-threads]

* Value type is [number](/lsr/value-types.md#number)
* Minimum value is `2`
* Default value is `4`

Total number of threads used to process events. The value you set here applies to all Event Hubs. Even with advanced configuration, this value is a global setting, and can’t be set per event hub.

```
azure_event_hubs {
   threads => 4
}
```

The number of threads should be the number of Event Hubs plus one or more. See [Best practices](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-best-practices) for more information.

## Common options [v1.1.2-plugins-inputs-azure_event_hubs-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v1-1-2-plugins-inputs-azure_event_hubs.md#v1.1.2-plugins-inputs-azure_event_hubs-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v1.1.2-plugins-inputs-azure_event_hubs-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v1.1.2-plugins-inputs-azure_event_hubs-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v1.1.2-plugins-inputs-azure_event_hubs-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.1.2-plugins-inputs-azure_event_hubs-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 azure\_event\_hubs inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  azure_event_hubs {
    id => "my_plugin_id"
  }
}
```

### `tags` [v1.1.2-plugins-inputs-azure_event_hubs-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v1.1.2-plugins-inputs-azure_event_hubs-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
