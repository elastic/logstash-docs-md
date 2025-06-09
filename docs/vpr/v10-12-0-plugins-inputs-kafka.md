---
navigation_title: "v10.12.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v10.12.0-plugins-inputs-kafka.html
---

# Kafka input plugin v10.12.0 [v10.12.0-plugins-inputs-kafka]

* A component of the [kafka integration plugin](integration-kafka-index.md)
* Integration version: v10.12.0
* Released on: 2022-05-09
* [Changelog](https://github.com/logstash-plugins/logstash-integration-kafka/blob/v10.12.0/CHANGELOG.md)

For other versions, see the [overview list](input-kafka-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_665]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-kafka). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_659]

This input will read events from a Kafka topic.

This plugin uses Kafka Client 2.8. For broker compatibility, see the official [Kafka compatibility reference](https://cwiki.apache.org/confluence/display/KAFKA/Compatibility+Matrix). If the linked compatibility wiki is not up-to-date, please contact Kafka support/community to confirm compatibility.

If you require features not yet available in this plugin (including client version upgrades), please file an issue with details about what you need.

This input supports connecting to Kafka over:

* SSL (requires plugin version 3.0.0 or later)
* Kerberos SASL (requires plugin version 5.1.0 or later)

By default security is disabled but can be turned on as needed.

This plugin does not support using a proxy when communicating to the Kafka broker.

This plugin does support using a proxy when communicating to the Schema Registry using the [`schema_registry_proxy`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_proxy) option.

The Logstash Kafka consumer handles group management and uses the default offset management strategy using Kafka topics.

Logstash instances by default form a single logical group to subscribe to Kafka topics Each Logstash Kafka consumer can run multiple threads to increase read throughput. Alternatively, you could run multiple Logstash instances with the same `group_id` to spread the load across physical machines. Messages in a topic will be distributed to all Logstash instances with the same `group_id`.

Ideally you should have as many threads as the number of partitions for a perfect balance—more threads than partitions means that some threads will be idle

For more information see <https://kafka.apache.org/25/documentation.html#theconsumer>

Kafka consumer configuration: <https://kafka.apache.org/25/documentation.html#consumerconfigs>

## Metadata fields [_metadata_fields_22]

The following metadata from Kafka broker are added under the `[@metadata]` field:

* `[@metadata][kafka][topic]`: Original Kafka topic from where the message was consumed.
* `[@metadata][kafka][consumer_group]`: Consumer group
* `[@metadata][kafka][partition]`: Partition info for this message.
* `[@metadata][kafka][offset]`: Original record offset for this message.
* `[@metadata][kafka][key]`: Record key, if any.
* `[@metadata][kafka][timestamp]`: Timestamp in the Record. Depending on your broker configuration, this can be either when the record was created (default) or when it was received by the broker. See more about property log.message.timestamp.type at <https://kafka.apache.org/25/documentation.html#brokerconfigs>

Metadata is only added to the event if the `decorate_events` option is set to `basic` or `extended` (it defaults to `none`).

Please note that `@metadata` fields are not part of any of your events at output time. If you need these information to be inserted into your original event, you’ll have to use the `mutate` filter to manually copy the required fields into your `event`.

## Kafka Input Configuration Options [v10.12.0-plugins-inputs-kafka-options]

This plugin supports these configuration options plus the [Common options](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-common-options) described later.

Some of these options map to a Kafka option. Defaults usually reflect the Kafka default setting, and might change if Kafka’s consumer defaults change. See the <https://kafka.apache.org/25/documentation> for more details.

| Setting | Input type | Required |
| :- | :- | :- |
| [`auto_commit_interval_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-auto_commit_interval_ms) | [number](/lsr/value-types.md#number) | No |
| [`auto_offset_reset`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-auto_offset_reset) | [string](/lsr/value-types.md#string) | No |
| [`bootstrap_servers`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-bootstrap_servers) | [string](/lsr/value-types.md#string) | No |
| [`check_crcs`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-check_crcs) | [boolean](/lsr/value-types.md#boolean) | No |
| [`client_dns_lookup`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-client_dns_lookup) | [string](/lsr/value-types.md#string) | No |
| [`client_id`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-client_id) | [string](/lsr/value-types.md#string) | No |
| [`client_rack`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-client_rack) | [string](/lsr/value-types.md#string) | No |
| [`connections_max_idle_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-connections_max_idle_ms) | [number](/lsr/value-types.md#number) | No |
| [`consumer_threads`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-consumer_threads) | [number](/lsr/value-types.md#number) | No |
| [`decorate_events`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-decorate_events) | [string](/lsr/value-types.md#string) | No |
| [`enable_auto_commit`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-enable_auto_commit) | [boolean](/lsr/value-types.md#boolean) | No |
| [`exclude_internal_topics`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-exclude_internal_topics) | [string](/lsr/value-types.md#string) | No |
| [`fetch_max_bytes`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-fetch_max_bytes) | [number](/lsr/value-types.md#number) | No |
| [`fetch_max_wait_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-fetch_max_wait_ms) | [number](/lsr/value-types.md#number) | No |
| [`fetch_min_bytes`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-fetch_min_bytes) | [number](/lsr/value-types.md#number) | No |
| [`group_id`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-group_id) | [string](/lsr/value-types.md#string) | No |
| [`heartbeat_interval_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-heartbeat_interval_ms) | [number](/lsr/value-types.md#number) | No |
| [`isolation_level`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-isolation_level) | [string](/lsr/value-types.md#string) | No |
| [`jaas_path`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-jaas_path) | a valid filesystem path | No |
| [`kerberos_config`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-kerberos_config) | a valid filesystem path | No |
| [`key_deserializer_class`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-key_deserializer_class) | [string](/lsr/value-types.md#string) | No |
| [`max_partition_fetch_bytes`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-max_partition_fetch_bytes) | [number](/lsr/value-types.md#number) | No |
| [`max_poll_interval_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-max_poll_interval_ms) | [number](/lsr/value-types.md#number) | No |
| [`max_poll_records`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-max_poll_records) | [number](/lsr/value-types.md#number) | No |
| [`metadata_max_age_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-metadata_max_age_ms) | [number](/lsr/value-types.md#number) | No |
| [`partition_assignment_strategy`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-partition_assignment_strategy) | [string](/lsr/value-types.md#string) | No |
| [`poll_timeout_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-poll_timeout_ms) | [number](/lsr/value-types.md#number) | No |
| [`receive_buffer_bytes`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-receive_buffer_bytes) | [number](/lsr/value-types.md#number) | No |
| [`reconnect_backoff_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-reconnect_backoff_ms) | [number](/lsr/value-types.md#number) | No |
| [`request_timeout_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-request_timeout_ms) | [number](/lsr/value-types.md#number) | No |
| [`retry_backoff_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-retry_backoff_ms) | [number](/lsr/value-types.md#number) | No |
| [`sasl_jaas_config`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-sasl_jaas_config) | [string](/lsr/value-types.md#string) | No |
| [`sasl_kerberos_service_name`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-sasl_kerberos_service_name) | [string](/lsr/value-types.md#string) | No |
| [`sasl_mechanism`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-sasl_mechanism) | [string](/lsr/value-types.md#string) | No |
| [`schema_registry_key`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_key) | [string](/lsr/value-types.md#string) | No |
| [`schema_registry_proxy`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_proxy) | [uri](/lsr/value-types.md#uri) | No |
| [`schema_registry_secret`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_secret) | [string](/lsr/value-types.md#string) | No |
| [`schema_registry_url`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_url) | [uri](/lsr/value-types.md#uri) | No |
| [`schema_registry_validation`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_validation) | [string](/lsr/value-types.md#string) | No |
| [`security_protocol`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-security_protocol) | [string](/lsr/value-types.md#string), one of `["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]` | No |
| [`send_buffer_bytes`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-send_buffer_bytes) | [number](/lsr/value-types.md#number) | No |
| [`session_timeout_ms`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-session_timeout_ms) | [number](/lsr/value-types.md#number) | No |
| [`ssl_endpoint_identification_algorithm`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_endpoint_identification_algorithm) | [string](/lsr/value-types.md#string) | No |
| [`ssl_key_password`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_key_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_keystore_location`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_keystore_location) | a valid filesystem path | No |
| [`ssl_keystore_password`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_keystore_type`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_keystore_type) | [string](/lsr/value-types.md#string) | No |
| [`ssl_truststore_location`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_truststore_location) | a valid filesystem path | No |
| [`ssl_truststore_password`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_truststore_type`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-ssl_truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`topics`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-topics) | [array](/lsr/value-types.md#array) | No |
| [`topics_pattern`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-topics_pattern) | [string](/lsr/value-types.md#string) | No |
| [`value_deserializer_class`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-value_deserializer_class) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-common-options) for a list of options supported by all input plugins.

### `auto_commit_interval_ms` [v10.12.0-plugins-inputs-kafka-auto_commit_interval_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5000`.

The frequency in milliseconds that the consumer offsets are committed to Kafka.

### `auto_offset_reset` [v10.12.0-plugins-inputs-kafka-auto_offset_reset]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

What to do when there is no initial offset in Kafka or if an offset is out of range:

* earliest: automatically reset the offset to the earliest offset
* latest: automatically reset the offset to the latest offset
* none: throw exception to the consumer if no previous offset is found for the consumer’s group
* anything else: throw exception to the consumer.

### `bootstrap_servers` [v10.12.0-plugins-inputs-kafka-bootstrap_servers]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"localhost:9092"`

A list of URLs of Kafka instances to use for establishing the initial connection to the cluster. This list should be in the form of `host1:port1,host2:port2` These urls are just used for the initial connection to discover the full cluster membership (which may change dynamically) so this list need not contain the full set of servers (you may want more than one, though, in case a server is down).

### `check_crcs` [v10.12.0-plugins-inputs-kafka-check_crcs]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Automatically check the CRC32 of the records consumed. This ensures no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so it may be disabled in cases seeking extreme performance.

### `client_dns_lookup` [v10.12.0-plugins-inputs-kafka-client_dns_lookup]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"default"`

How DNS lookups should be done. If set to `use_all_dns_ips`, when the lookup returns multiple IP addresses for a hostname, they will all be attempted to connect to before failing the connection. If the value is `resolve_canonical_bootstrap_servers_only` each entry will be resolved and expanded into a list of canonical names.

### `client_id` [v10.12.0-plugins-inputs-kafka-client_id]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

The id string to pass to the server when making requests. The purpose of this is to be able to track the source of requests beyond just ip/port by allowing a logical application name to be included.

### `client_rack` [v10.12.0-plugins-inputs-kafka-client_rack]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A rack identifier for the Kafka consumer. Used to select the physically closest rack for the consumer to read from. The setting corresponds with Kafka’s `broker.rack` configuration.

Available only for Kafka 2.4.0 and higher. See [KIP-392](https://cwiki.apache.org/confluence/display/KAFKA/KIP-392%3A+Allow+consumers+to+fetch+from+closest+replica).

### `connections_max_idle_ms` [v10.12.0-plugins-inputs-kafka-connections_max_idle_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `540000` milliseconds (9 minutes).

Close idle connections after the number of milliseconds specified by this config.

### `consumer_threads` [v10.12.0-plugins-inputs-kafka-consumer_threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

Ideally you should have as many threads as the number of partitions for a perfect balance—more threads than partitions means that some threads will be idle

### `decorate_events` [v10.12.0-plugins-inputs-kafka-decorate_events]

* Value type is [string](/lsr/value-types.md#string)

* Accepted values are:

  * `none`: no metadata is added
  * `basic`: record’s attributes are added
  * `extended`: record’s attributes, headers are added
  * `false`: deprecated alias for `none`
  * `true`: deprecated alias for `basic`

* Default value is `none`

Option to add Kafka metadata like topic, message size and header key values to the event. This will add a field named `kafka` to the logstash event containing the following attributes:

* `topic`: The topic this message is associated with
* `consumer_group`: The consumer group used to read in this event
* `partition`: The partition this message is associated with
* `offset`: The offset from the partition this message is associated with
* `key`: A ByteBuffer containing the message key

### `enable_auto_commit` [v10.12.0-plugins-inputs-kafka-enable_auto_commit]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

This committed offset will be used when the process fails as the position from which the consumption will begin.

If true, periodically commit to Kafka the offsets of messages already returned by the consumer. If value is `false` however, the offset is committed every time the consumer writes data fetched from the topic to the in-memory or persistent queue.

### `exclude_internal_topics` [v10.12.0-plugins-inputs-kafka-exclude_internal_topics]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Whether records from internal topics (such as offsets) should be exposed to the consumer. If set to true the only way to receive records from an internal topic is subscribing to it.

### `fetch_max_bytes` [v10.12.0-plugins-inputs-kafka-fetch_max_bytes]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `52428800` (50MB)

The maximum amount of data the server should return for a fetch request. This is not an absolute maximum, if the first message in the first non-empty partition of the fetch is larger than this value, the message will still be returned to ensure that the consumer can make progress.

### `fetch_max_wait_ms` [v10.12.0-plugins-inputs-kafka-fetch_max_wait_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `500` milliseconds.

The maximum amount of time the server will block before answering the fetch request if there isn’t sufficient data to immediately satisfy `fetch_min_bytes`. This should be less than or equal to the timeout used in `poll_timeout_ms`

### `fetch_min_bytes` [v10.12.0-plugins-inputs-kafka-fetch_min_bytes]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request.

### `group_id` [v10.12.0-plugins-inputs-kafka-group_id]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash"`

The identifier of the group this consumer belongs to. Consumer group is a single logical subscriber that happens to be made up of multiple processors. Messages in a topic will be distributed to all Logstash instances with the same `group_id`.

In cases when multiple inputs are being used in a single pipeline, reading from different topics, it’s essential to set a different `group_id => ...` for each input. Setting a unique `client_id => ...` is also recommended.

### `heartbeat_interval_ms` [v10.12.0-plugins-inputs-kafka-heartbeat_interval_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3000` milliseconds (3 seconds).

The expected time between heartbeats to the consumer coordinator. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than `session.timeout.ms`, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances.

### `isolation_level` [v10.12.0-plugins-inputs-kafka-isolation_level]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"read_uncommitted"`

Controls how to read messages written transactionally. If set to `read_committed`, polling messages will only return transactional messages which have been committed. If set to `read_uncommitted` (the default), polling messages will return all messages, even transactional messages which have been aborted. Non-transactional messages will be returned unconditionally in either mode.

### `jaas_path` [v10.12.0-plugins-inputs-kafka-jaas_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The Java Authentication and Authorization Service (JAAS) API supplies user authentication and authorization services for Kafka. This setting provides the path to the JAAS file. Sample JAAS file for Kafka client:

```
KafkaClient {
  com.sun.security.auth.module.Krb5LoginModule required
  useTicketCache=true
  renewTicket=true
  serviceName="kafka";
  };
```

Please note that specifying `jaas_path` and `kerberos_config` in the config file will add these to the global JVM system properties. This means if you have multiple Kafka inputs, all of them would be sharing the same `jaas_path` and `kerberos_config`. If this is not desirable, you would have to run separate instances of Logstash on different JVM instances.

### `kerberos_config` [v10.12.0-plugins-inputs-kafka-kerberos_config]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Optional path to kerberos config file. This is krb5.conf style as detailed in <https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html>

### `key_deserializer_class` [v10.12.0-plugins-inputs-kafka-key_deserializer_class]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringDeserializer"`

Java Class used to deserialize the record’s key

### `max_partition_fetch_bytes` [v10.12.0-plugins-inputs-kafka-max_partition_fetch_bytes]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1048576` (1MB).

The maximum amount of data per-partition the server will return. The maximum total memory used for a request will be `#partitions * max.partition.fetch.bytes`. This size must be at least as large as the maximum message size the server allows or else it is possible for the producer to send messages larger than the consumer can fetch. If that happens, the consumer can get stuck trying to fetch a large message on a certain partition.

### `max_poll_interval_ms` [v10.12.0-plugins-inputs-kafka-max_poll_interval_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `300000` milliseconds (5 minutes).

The maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance in order to reassign the partitions to another member.

### `max_poll_records` [v10.12.0-plugins-inputs-kafka-max_poll_records]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `500`.

The maximum number of records returned in a single call to poll().

### `metadata_max_age_ms` [v10.12.0-plugins-inputs-kafka-metadata_max_age_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `300000` milliseconds (5 minutes).

The period of time in milliseconds after which we force a refresh of metadata even if we haven’t seen any partition leadership changes to proactively discover any new brokers or partitions

### `partition_assignment_strategy` [v10.12.0-plugins-inputs-kafka-partition_assignment_strategy]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the partition assignment strategy that the client uses to distribute partition ownership amongst consumer instances, supported options are:

* `range`
* `round_robin`
* `sticky`
* `cooperative_sticky`

These map to Kafka’s corresponding [`ConsumerPartitionAssignor`](https://kafka.apache.org/25/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html) implementations.

### `poll_timeout_ms` [v10.12.0-plugins-inputs-kafka-poll_timeout_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `100` milliseconds.

Time Kafka consumer will wait to receive new messages from topics.

After subscribing to a set of topics, the Kafka consumer automatically joins the group when polling. The plugin poll-ing in a loop ensures consumer liveness. Underneath the covers, Kafka client sends periodic heartbeats to the server. The timeout specified the time to block waiting for input on each poll.

### `receive_buffer_bytes` [v10.12.0-plugins-inputs-kafka-receive_buffer_bytes]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `32768` (32KB).

The size of the TCP receive buffer (SO\_RCVBUF) to use when reading data.

### `reconnect_backoff_ms` [v10.12.0-plugins-inputs-kafka-reconnect_backoff_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50` milliseconds.

The amount of time to wait before attempting to reconnect to a given host. This avoids repeatedly connecting to a host in a tight loop. This backoff applies to all requests sent by the consumer to the broker.

### `request_timeout_ms` [v10.12.0-plugins-inputs-kafka-request_timeout_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `40000` milliseconds (40 seconds).

The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted.

### `retry_backoff_ms` [v10.12.0-plugins-inputs-kafka-retry_backoff_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `100` milliseconds.

The amount of time to wait before attempting to retry a failed fetch request to a given topic partition. This avoids repeated fetching-and-failing in a tight loop.

### `sasl_jaas_config` [v10.12.0-plugins-inputs-kafka-sasl_jaas_config]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JAAS configuration setting local to this plugin instance, as opposed to settings using config file configured using `jaas_path`, which are shared across the JVM. This allows each plugin instance to have its own configuration.

If both `sasl_jaas_config` and `jaas_path` configurations are set, the setting here takes precedence.

Example (setting for Azure Event Hub):

```
    input {
      kafka {
        sasl_jaas_config => "org.apache.kafka.common.security.plain.PlainLoginModule required username='auser'  password='apassword';"
      }
    }
```

### `sasl_kerberos_service_name` [v10.12.0-plugins-inputs-kafka-sasl_kerberos_service_name]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The Kerberos principal name that Kafka broker runs as. This can be defined either in Kafka’s JAAS config or in Kafka’s config.

### `sasl_mechanism` [v10.12.0-plugins-inputs-kafka-sasl_mechanism]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"GSSAPI"`

[SASL mechanism](http://kafka.apache.org/documentation.html#security_sasl) used for client connections. This may be any mechanism for which a security provider is available. GSSAPI is the default mechanism.

### `schema_registry_key` [v10.12.0-plugins-inputs-kafka-schema_registry_key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Set the username for basic authorization to access remote Schema Registry.

### `schema_registry_proxy` [v10.12.0-plugins-inputs-kafka-schema_registry_proxy]

* Value type is [uri](/lsr/value-types.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. An empty string is treated as if proxy was not set.

### `schema_registry_secret` [v10.12.0-plugins-inputs-kafka-schema_registry_secret]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Set the password for basic authorization to access remote Schema Registry.

### `schema_registry_url` [v10.12.0-plugins-inputs-kafka-schema_registry_url]

* Value type is [uri](/lsr/value-types.md#uri)

The URI that points to an instance of the [Schema Registry](https://docs.confluent.io/current/schema-registry/index.html) service, used to manage Avro schemas. Be sure that the Avro schemas for deserializing the data from the specified topics have been uploaded to the Schema Registry service. The schemas must follow a naming convention with the pattern \<topic name>-value.

Use either the Schema Registry config option or the [`value_deserializer_class`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-value_deserializer_class) config option, but not both.

### `schema_registry_validation` [v10.12.0-plugins-inputs-kafka-schema_registry_validation]

* Value can be either of: `auto`, `skip`
* Default value is `"auto"`

Under most circumstances, the default setting of `auto` should not need to be changed.

When using the schema registry, by default the plugin checks connectivity and validates the schema registry, during plugin registration, before events are processed. In some circumstances, this process may fail when it tries to validate an authenticated schema registry, causing the plugin to crash. This setting allows the plugin to skip validation during registration, which allows the plugin to continue and events to be processed. Note that an incorrectly configured schema registry will still stop the plugin from processing events.

### `security_protocol` [v10.12.0-plugins-inputs-kafka-security_protocol]

* Value can be any of: `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT`, `SASL_SSL`
* Default value is `"PLAINTEXT"`

Security protocol to use, which can be either of PLAINTEXT,SSL,SASL\_PLAINTEXT,SASL\_SSL

### `send_buffer_bytes` [v10.12.0-plugins-inputs-kafka-send_buffer_bytes]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `131072` (128KB).

The size of the TCP send buffer (SO\_SNDBUF) to use when sending data

### `session_timeout_ms` [v10.12.0-plugins-inputs-kafka-session_timeout_ms]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000` milliseconds (10 seconds).

The timeout after which, if the `poll_timeout_ms` is not invoked, the consumer is marked dead and a rebalance operation is triggered for the group identified by `group_id`

### `ssl_endpoint_identification_algorithm` [v10.12.0-plugins-inputs-kafka-ssl_endpoint_identification_algorithm]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"https"`

The endpoint identification algorithm, defaults to `"https"`. Set to empty string `""` to disable endpoint verification

### `ssl_key_password` [v10.12.0-plugins-inputs-kafka-ssl_key_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

The password of the private key in the key store file.

### `ssl_keystore_location` [v10.12.0-plugins-inputs-kafka-ssl_keystore_location]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore path.

### `ssl_keystore_password` [v10.12.0-plugins-inputs-kafka-ssl_keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore password

### `ssl_keystore_type` [v10.12.0-plugins-inputs-kafka-ssl_keystore_type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The keystore type.

### `ssl_truststore_location` [v10.12.0-plugins-inputs-kafka-ssl_truststore_location]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The JKS truststore path to validate the Kafka broker’s certificate.

### `ssl_truststore_password` [v10.12.0-plugins-inputs-kafka-ssl_truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

The truststore password.

### `ssl_truststore_type` [v10.12.0-plugins-inputs-kafka-ssl_truststore_type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The truststore type.

### `topics` [v10.12.0-plugins-inputs-kafka-topics]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["logstash"]`

A list of topics to subscribe to, defaults to \["logstash"].

### `topics_pattern` [v10.12.0-plugins-inputs-kafka-topics_pattern]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A topic regex pattern to subscribe to. The topics configuration will be ignored when using this configuration.

### `value_deserializer_class` [v10.12.0-plugins-inputs-kafka-value_deserializer_class]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringDeserializer"`

Java Class used to deserialize the record’s value. A custom value deserializer can be used only if you are not using a Schema Registry. Use either the value\_deserializer\_class config option or the [`schema_registry_url`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-schema_registry_url) config option, but not both.

## Common options [v10.12.0-plugins-inputs-kafka-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v10-12-0-plugins-inputs-kafka.md#v10.12.0-plugins-inputs-kafka-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v10.12.0-plugins-inputs-kafka-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v10.12.0-plugins-inputs-kafka-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v10.12.0-plugins-inputs-kafka-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v10.12.0-plugins-inputs-kafka-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 kafka inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  kafka {
    id => "my_plugin_id"
  }
}
```

### `tags` [v10.12.0-plugins-inputs-kafka-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v10.12.0-plugins-inputs-kafka-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
