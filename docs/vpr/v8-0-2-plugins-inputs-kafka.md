---
navigation_title: "v8.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v8.0.2-plugins-inputs-kafka.html
---

# Kafka input plugin v8.0.2 [v8.0.2-plugins-inputs-kafka]


* Plugin version: v8.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-input-kafka/blob/v8.0.2/CHANGELOG.md)

For other versions, see the [overview list](input-kafka-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_678]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-kafka). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_672]

This input will read events from a Kafka topic. It uses the 0.10 version of the consumer API provided by Kafka to read messages from the broker.

Here’s a compatibility matrix that shows the Kafka client versions that are compatible with each combination of Logstash and the Kafka input plugin:

| Kafka Client Version | Logstash Version | Plugin Version | Why? |
| --- | --- | --- | --- |
| 0.8 | 2.0.0 - 2.x.x | <3.0.0 | Legacy, 0.8 is still popular |
| 0.9 | 2.0.0 - 2.3.x | 3.x.x | Works with the old Ruby Event API (`event['product']['price'] = 10`) |
| 0.9 | 2.4.x - 5.x.x | 4.x.x | Works with the new getter/setter APIs (`event.set('[product][price]', 10)`) |
| 0.10.0.x | 2.4.x - 5.x.x | 5.x.x | Not compatible with the ⇐ 0.9 broker |
| 0.10.1.x | 2.4.x - 5.x.x | 6.x.x |  |
| 0.11.0.0 | 2.4.x - 5.x.x | 6.x.x | Not compatible with the ⇐ 0.9 broker |

::::{note}
We recommended that you use matching Kafka client and broker versions. During upgrades, you should upgrade brokers before clients because brokers target backwards compatibility. For example, the 0.9 broker is compatible with both the 0.8 consumer and 0.9 consumer APIs, but not the other way around.
::::


This input supports connecting to Kafka over:

* SSL (requires plugin version 3.0.0 or later)
* Kerberos SASL (requires plugin version 5.1.0 or later)

By default security is disabled but can be turned on as needed.

The Logstash Kafka consumer handles group management and uses the default offset management strategy using Kafka topics.

Logstash instances by default form a single logical group to subscribe to Kafka topics Each Logstash Kafka consumer can run multiple threads to increase read throughput. Alternatively, you could run multiple Logstash instances with the same `group_id` to spread the load across physical machines. Messages in a topic will be distributed to all Logstash instances with the same `group_id`.

Ideally you should have as many threads as the number of partitions for a perfect balance — more threads than partitions means that some threads will be idle

For more information see [http://kafka.apache.org/documentation.html#theconsumer](http://kafka.apache.org/documentation.html#theconsumer)

Kafka consumer configuration: [http://kafka.apache.org/documentation.html#consumerconfigs](http://kafka.apache.org/documentation.html#consumerconfigs)


## Metadata fields [_metadata_fields_57]

The following metadata from Kafka broker are added under the `[@metadata]` field:

* `[@metadata][kafka][topic]`: Original Kafka topic from where the message was consumed.
* `[@metadata][kafka][consumer_group]`: Consumer group
* `[@metadata][kafka][partition]`: Partition info for this message.
* `[@metadata][kafka][offset]`: Original record offset for this message.
* `[@metadata][kafka][key]`: Record key, if any.
* `[@metadata][kafka][timestamp]`: Timestamp when this message was received by the Kafka broker.

Please note that `@metadata` fields are not part of any of your events at output time. If you need these information to be inserted into your original event, you’ll have to use the `mutate` filter to manually copy the required fields into your `event`.


## Kafka Input Configuration Options [v8.0.2-plugins-inputs-kafka-options]

This plugin supports the following configuration options plus the [Common options](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`auto_commit_interval_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-auto_commit_interval_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`auto_offset_reset`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-auto_offset_reset) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`bootstrap_servers`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-bootstrap_servers) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`check_crcs`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-check_crcs) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`client_id`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-client_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`connections_max_idle_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-connections_max_idle_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`consumer_threads`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-consumer_threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`decorate_events`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-decorate_events) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`enable_auto_commit`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-enable_auto_commit) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`exclude_internal_topics`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-exclude_internal_topics) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fetch_max_bytes`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-fetch_max_bytes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fetch_max_wait_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-fetch_max_wait_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fetch_min_bytes`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-fetch_min_bytes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`group_id`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-group_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`heartbeat_interval_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-heartbeat_interval_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`jaas_path`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-jaas_path) | a valid filesystem path | No |
| [`kerberos_config`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-kerberos_config) | a valid filesystem path | No |
| [`key_deserializer_class`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-key_deserializer_class) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`max_partition_fetch_bytes`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-max_partition_fetch_bytes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`max_poll_interval_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-max_poll_interval_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`max_poll_records`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-max_poll_records) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_max_age_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-metadata_max_age_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`partition_assignment_strategy`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-partition_assignment_strategy) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`poll_timeout_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-poll_timeout_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`receive_buffer_bytes`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-receive_buffer_bytes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`reconnect_backoff_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-reconnect_backoff_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`request_timeout_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-request_timeout_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`retry_backoff_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-retry_backoff_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sasl_kerberos_service_name`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-sasl_kerberos_service_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sasl_mechanism`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-sasl_mechanism) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`security_protocol`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-security_protocol) | [string](logstash://reference/configuration-file-structure.md#string), one of `["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]` | No |
| [`send_buffer_bytes`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-send_buffer_bytes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`session_timeout_ms`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-session_timeout_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_key_password`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_key_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_location`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_keystore_location) | a valid filesystem path | No |
| [`ssl_keystore_password`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_type`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_keystore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_truststore_location`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_truststore_location) | a valid filesystem path | No |
| [`ssl_truststore_password`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_type`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-ssl_truststore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`topics`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-topics) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`topics_pattern`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-topics_pattern) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`value_deserializer_class`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-value_deserializer_class) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-common-options) for a list of options supported by all input plugins.

 

### `auto_commit_interval_ms` [v8.0.2-plugins-inputs-kafka-auto_commit_interval_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"5000"`

The frequency in milliseconds that the consumer offsets are committed to Kafka.


### `auto_offset_reset` [v8.0.2-plugins-inputs-kafka-auto_offset_reset]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

What to do when there is no initial offset in Kafka or if an offset is out of range:

* earliest: automatically reset the offset to the earliest offset
* latest: automatically reset the offset to the latest offset
* none: throw exception to the consumer if no previous offset is found for the consumer’s group
* anything else: throw exception to the consumer.


### `bootstrap_servers` [v8.0.2-plugins-inputs-kafka-bootstrap_servers]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost:9092"`

A list of URLs of Kafka instances to use for establishing the initial connection to the cluster. This list should be in the form of `host1:port1,host2:port2` These urls are just used for the initial connection to discover the full cluster membership (which may change dynamically) so this list need not contain the full set of servers (you may want more than one, though, in case a server is down).


### `check_crcs` [v8.0.2-plugins-inputs-kafka-check_crcs]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Automatically check the CRC32 of the records consumed. This ensures no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so it may be disabled in cases seeking extreme performance.


### `client_id` [v8.0.2-plugins-inputs-kafka-client_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The id string to pass to the server when making requests. The purpose of this is to be able to track the source of requests beyond just ip/port by allowing a logical application name to be included.


### `connections_max_idle_ms` [v8.0.2-plugins-inputs-kafka-connections_max_idle_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Close idle connections after the number of milliseconds specified by this config.


### `consumer_threads` [v8.0.2-plugins-inputs-kafka-consumer_threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Ideally you should have as many threads as the number of partitions for a perfect balance — more threads than partitions means that some threads will be idle


### `decorate_events` [v8.0.2-plugins-inputs-kafka-decorate_events]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Option to add Kafka metadata like topic, message size to the event. This will add a field named `kafka` to the logstash event containing the following attributes: `topic`: The topic this message is associated with `consumer_group`: The consumer group used to read in this event `partition`: The partition this message is associated with `offset`: The offset from the partition this message is associated with `key`: A ByteBuffer containing the message key


### `enable_auto_commit` [v8.0.2-plugins-inputs-kafka-enable_auto_commit]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"true"`

If true, periodically commit to Kafka the offsets of messages already returned by the consumer. This committed offset will be used when the process fails as the position from which the consumption will begin.


### `exclude_internal_topics` [v8.0.2-plugins-inputs-kafka-exclude_internal_topics]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Whether records from internal topics (such as offsets) should be exposed to the consumer. If set to true the only way to receive records from an internal topic is subscribing to it.


### `fetch_max_bytes` [v8.0.2-plugins-inputs-kafka-fetch_max_bytes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The maximum amount of data the server should return for a fetch request. This is not an absolute maximum, if the first message in the first non-empty partition of the fetch is larger than this value, the message will still be returned to ensure that the consumer can make progress.


### `fetch_max_wait_ms` [v8.0.2-plugins-inputs-kafka-fetch_max_wait_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The maximum amount of time the server will block before answering the fetch request if there isn’t sufficient data to immediately satisfy `fetch_min_bytes`. This should be less than or equal to the timeout used in `poll_timeout_ms`


### `fetch_min_bytes` [v8.0.2-plugins-inputs-kafka-fetch_min_bytes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request.


### `group_id` [v8.0.2-plugins-inputs-kafka-group_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash"`

The identifier of the group this consumer belongs to. Consumer group is a single logical subscriber that happens to be made up of multiple processors. Messages in a topic will be distributed to all Logstash instances with the same `group_id`


### `heartbeat_interval_ms` [v8.0.2-plugins-inputs-kafka-heartbeat_interval_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The expected time between heartbeats to the consumer coordinator. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than `session.timeout.ms`, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances.


### `jaas_path` [v8.0.2-plugins-inputs-kafka-jaas_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The Java Authentication and Authorization Service (JAAS) API supplies user authentication and authorization services for Kafka. This setting provides the path to the JAAS file. Sample JAAS file for Kafka client:

```java
KafkaClient {
  com.sun.security.auth.module.Krb5LoginModule required
  useTicketCache=true
  renewTicket=true
  serviceName="kafka";
  };
```

Please note that specifying `jaas_path` and `kerberos_config` in the config file will add these to the global JVM system properties. This means if you have multiple Kafka inputs, all of them would be sharing the same `jaas_path` and `kerberos_config`. If this is not desirable, you would have to run separate instances of Logstash on different JVM instances.


### `kerberos_config` [v8.0.2-plugins-inputs-kafka-kerberos_config]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Optional path to kerberos config file. This is krb5.conf style as detailed in [https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html)


### `key_deserializer_class` [v8.0.2-plugins-inputs-kafka-key_deserializer_class]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringDeserializer"`

Java Class used to deserialize the record’s key


### `max_partition_fetch_bytes` [v8.0.2-plugins-inputs-kafka-max_partition_fetch_bytes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The maximum amount of data per-partition the server will return. The maximum total memory used for a request will be <code>#partitions * max.partition.fetch.bytes</code>. This size must be at least as large as the maximum message size the server allows or else it is possible for the producer to send messages larger than the consumer can fetch. If that happens, the consumer can get stuck trying to fetch a large message on a certain partition.


### `max_poll_interval_ms` [v8.0.2-plugins-inputs-kafka-max_poll_interval_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance in order to reassign the partitions to another member. The value of the configuration `request_timeout_ms` must always be larger than max_poll_interval_ms


### `max_poll_records` [v8.0.2-plugins-inputs-kafka-max_poll_records]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The maximum number of records returned in a single call to poll().


### `metadata_max_age_ms` [v8.0.2-plugins-inputs-kafka-metadata_max_age_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The period of time in milliseconds after which we force a refresh of metadata even if we haven’t seen any partition leadership changes to proactively discover any new brokers or partitions


### `partition_assignment_strategy` [v8.0.2-plugins-inputs-kafka-partition_assignment_strategy]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The class name of the partition assignment strategy that the client will use to distribute partition ownership amongst consumer instances


### `poll_timeout_ms` [v8.0.2-plugins-inputs-kafka-poll_timeout_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100`

Time kafka consumer will wait to receive new messages from topics


### `receive_buffer_bytes` [v8.0.2-plugins-inputs-kafka-receive_buffer_bytes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The size of the TCP receive buffer (SO_RCVBUF) to use when reading data.


### `reconnect_backoff_ms` [v8.0.2-plugins-inputs-kafka-reconnect_backoff_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The amount of time to wait before attempting to reconnect to a given host. This avoids repeatedly connecting to a host in a tight loop. This backoff applies to all requests sent by the consumer to the broker.


### `request_timeout_ms` [v8.0.2-plugins-inputs-kafka-request_timeout_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted.


### `retry_backoff_ms` [v8.0.2-plugins-inputs-kafka-retry_backoff_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The amount of time to wait before attempting to retry a failed fetch request to a given topic partition. This avoids repeated fetching-and-failing in a tight loop.


### `sasl_kerberos_service_name` [v8.0.2-plugins-inputs-kafka-sasl_kerberos_service_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The Kerberos principal name that Kafka broker runs as. This can be defined either in Kafka’s JAAS config or in Kafka’s config.


### `sasl_mechanism` [v8.0.2-plugins-inputs-kafka-sasl_mechanism]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"GSSAPI"`

[SASL mechanism](http://kafka.apache.org/documentation.html#security_sasl) used for client connections. This may be any mechanism for which a security provider is available. GSSAPI is the default mechanism.


### `security_protocol` [v8.0.2-plugins-inputs-kafka-security_protocol]

* Value can be any of: `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT`, `SASL_SSL`
* Default value is `"PLAINTEXT"`

Security protocol to use, which can be either of PLAINTEXT,SSL,SASL_PLAINTEXT,SASL_SSL


### `send_buffer_bytes` [v8.0.2-plugins-inputs-kafka-send_buffer_bytes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The size of the TCP send buffer (SO_SNDBUF) to use when sending data


### `session_timeout_ms` [v8.0.2-plugins-inputs-kafka-session_timeout_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The timeout after which, if the `poll_timeout_ms` is not invoked, the consumer is marked dead and a rebalance operation is triggered for the group identified by `group_id`


### `ssl_key_password` [v8.0.2-plugins-inputs-kafka-ssl_key_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The password of the private key in the key store file.


### `ssl_keystore_location` [v8.0.2-plugins-inputs-kafka-ssl_keystore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore path.


### `ssl_keystore_password` [v8.0.2-plugins-inputs-kafka-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore password


### `ssl_keystore_type` [v8.0.2-plugins-inputs-kafka-ssl_keystore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The keystore type.


### `ssl_truststore_location` [v8.0.2-plugins-inputs-kafka-ssl_truststore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The JKS truststore path to validate the Kafka broker’s certificate.


### `ssl_truststore_password` [v8.0.2-plugins-inputs-kafka-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The truststore password


### `ssl_truststore_type` [v8.0.2-plugins-inputs-kafka-ssl_truststore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The truststore type.


### `topics` [v8.0.2-plugins-inputs-kafka-topics]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["logstash"]`

A list of topics to subscribe to, defaults to ["logstash"].


### `topics_pattern` [v8.0.2-plugins-inputs-kafka-topics_pattern]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A topic regex pattern to subscribe to. The topics configuration will be ignored when using this configuration.


### `value_deserializer_class` [v8.0.2-plugins-inputs-kafka-value_deserializer_class]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringDeserializer"`

Java Class used to deserialize the record’s value



## Common options [v8.0.2-plugins-inputs-kafka-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v8-0-2-plugins-inputs-kafka.md#v8.0.2-plugins-inputs-kafka-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v8.0.2-plugins-inputs-kafka-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v8.0.2-plugins-inputs-kafka-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v8.0.2-plugins-inputs-kafka-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v8.0.2-plugins-inputs-kafka-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kafka inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  kafka {
    id => "my_plugin_id"
  }
}
```


### `tags` [v8.0.2-plugins-inputs-kafka-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v8.0.2-plugins-inputs-kafka-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



