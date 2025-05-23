---
navigation_title: "v11.3.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v11.3.4-plugins-outputs-kafka.html
---

# Kafka output plugin v11.3.4 [v11.3.4-plugins-outputs-kafka]


* A component of the [kafka integration plugin](integration-kafka-index.md)
* Integration version: v11.3.4
* Released on: 2024-02-06
* [Changelog](https://github.com/logstash-plugins/logstash-integration-kafka/blob/v11.3.4/CHANGELOG.md)

For other versions, see the [overview list](output-kafka-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1348]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-kafka). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1338]

Write events to a Kafka topic.

This plugin uses Kafka Client 3.4. For broker compatibility, see the official [Kafka compatibility reference](https://cwiki.apache.org/confluence/display/KAFKA/Compatibility+Matrix). If the linked compatibility wiki is not up-to-date, please contact Kafka support/community to confirm compatibility.

If you require features not yet available in this plugin (including client version upgrades), please file an issue with details about what you need.

This output supports connecting to Kafka over:

* SSL (requires plugin version 3.0.0 or later)
* Kerberos SASL (requires plugin version 5.1.0 or later)

By default security is disabled but can be turned on as needed.

The only required configuration is the topic_id.

The default codec is plain. Logstash will encode your events with not only the message field but also with a timestamp and hostname.

If you want the full content of your events to be sent as json, you should set the codec in the output configuration like this:

```ruby
    output {
      kafka {
        codec => json
        topic_id => "mytopic"
      }
    }
```

For more information see [https://kafka.apache.org/34/documentation.html#theproducer](https://kafka.apache.org/34/documentation.html#theproducer)

Kafka producer configuration: [https://kafka.apache.org/34/documentation.html#producerconfigs](https://kafka.apache.org/34/documentation.html#producerconfigs)

::::{note}
This plugin does not support using a proxy when communicating to the Kafka broker.
::::



## Kafka Output Configuration Options [v11.3.4-plugins-outputs-kafka-options]

This plugin supports the following configuration options plus the [Common options](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-common-options) described later.

::::{note}
Some of these options map to a Kafka option. Defaults usually reflect the Kafka default setting, and might change if Kafka’s producer defaults change. See the [https://kafka.apache.org/34/documentation](https://kafka.apache.org/34/documentation) for more details.
::::


| Setting | Input type | Required |
| --- | --- | --- |
| [`acks`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-acks) | [string](logstash://reference/configuration-file-structure.md#string), one of `["0", "1", "all"]` | No |
| [`batch_size`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-batch_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`bootstrap_servers`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-bootstrap_servers) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`buffer_memory`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-buffer_memory) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`client_dns_lookup`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-client_dns_lookup) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`client_id`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-client_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`compression_type`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-compression_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "gzip", "snappy", "lz4", "zstd"]` | No |
| [`connections_max_idle_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-connections_max_idle_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jaas_path`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-jaas_path) | a valid filesystem path | No |
| [`kerberos_config`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-kerberos_config) | a valid filesystem path | No |
| [`key_serializer`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-key_serializer) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`linger_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-linger_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_request_size`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-max_request_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`message_key`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-message_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_fetch_timeout_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-metadata_fetch_timeout_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`metadata_max_age_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-metadata_max_age_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`partitioner`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-partitioner) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`receive_buffer_bytes`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-receive_buffer_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`reconnect_backoff_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-reconnect_backoff_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`request_timeout_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-request_timeout_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retries`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-retries) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_backoff_ms`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-retry_backoff_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`sasl_jaas_config`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-sasl_jaas_config) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sasl_kerberos_service_name`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-sasl_kerberos_service_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sasl_mechanism`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-sasl_mechanism) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`security_protocol`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-security_protocol) | [string](logstash://reference/configuration-file-structure.md#string), one of `["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]` | No |
| [`send_buffer_bytes`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-send_buffer_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_endpoint_identification_algorithm`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_endpoint_identification_algorithm) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_key_password`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_key_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_location`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_keystore_location) | a valid filesystem path | No |
| [`ssl_keystore_password`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_type`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_keystore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_truststore_location`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_truststore_location) | a valid filesystem path | No |
| [`ssl_truststore_password`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_type`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-ssl_truststore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`topic_id`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-topic_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`value_serializer`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-value_serializer) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-common-options) for a list of options supported by all output plugins.

 

### `acks` [v11.3.4-plugins-outputs-kafka-acks]

* Value can be any of: `0`, `1`, `all`
* Default value is `"1"`

The number of acknowledgments the producer requires the leader to have received before considering a request complete.

`acks=0`. The producer will not wait for any acknowledgment from the server.

`acks=1`. The leader will write the record to its local log, but will respond without waiting for full acknowledgement from all followers.

`acks=all`. The leader will wait for the full set of in-sync replicas before acknowledging the record.


### `batch_size` [v11.3.4-plugins-outputs-kafka-batch_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `16384`.

The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes.


### `bootstrap_servers` [v11.3.4-plugins-outputs-kafka-bootstrap_servers]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost:9092"`

This is for bootstrapping and the producer will only use it for getting metadata (topics, partitions and replicas). The socket connections for sending the actual data will be established based on the broker information returned in the metadata. The format is `host1:port1,host2:port2`, and the list can be a subset of brokers or a VIP pointing to a subset of brokers.


### `buffer_memory` [v11.3.4-plugins-outputs-kafka-buffer_memory]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `33554432` (32MB).

The total bytes of memory the producer can use to buffer records waiting to be sent to the server.


### `client_dns_lookup` [v11.3.4-plugins-outputs-kafka-client_dns_lookup]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Valid options are `use_all_dns_ips`, `resolve_canonical_bootstrap_servers_only`, `default`
* Default value is `"default"`

Controls how DNS lookups are done. If set to `use_all_dns_ips`, Logstash tries all IP addresses returned for a hostname before failing the connection. If set to `resolve_canonical_bootstrap_servers_only`, each entry will be resolved and expanded into a list of canonical names.

::::{note}
Starting from Kafka 3 `default` value for `client.dns.lookup` value has been removed. If not explicitly configured it defaults to `use_all_dns_ips`.

::::



### `client_id` [v11.3.4-plugins-outputs-kafka-client_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The id string to pass to the server when making requests. The purpose of this is to be able to track the source of requests beyond just ip/port by allowing a logical application name to be included with the request


### `compression_type` [v11.3.4-plugins-outputs-kafka-compression_type]

* Value can be any of: `none`, `gzip`, `snappy`, `lz4`, `zstd`
* Default value is `"none"`

The compression type for all data generated by the producer. The default is none (meaning no compression). Valid values are none, gzip, snappy, lz4, or zstd.


### `connections_max_idle_ms` [v11.3.4-plugins-outputs-kafka-connections_max_idle_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `540000` milliseconds (9 minutes).

Close idle connections after the number of milliseconds specified by this config.


### `jaas_path` [v11.3.4-plugins-outputs-kafka-jaas_path]

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


### `kerberos_config` [v11.3.4-plugins-outputs-kafka-kerberos_config]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Optional path to kerberos config file. This is krb5.conf style as detailed in [https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html)


### `key_serializer` [v11.3.4-plugins-outputs-kafka-key_serializer]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringSerializer"`

Serializer class for the key of the message


### `linger_ms` [v11.3.4-plugins-outputs-kafka-linger_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they can be sent out. However in some circumstances the client may want to reduce the number of requests even under moderate load. This setting accomplishes this by adding a small amount of artificial delay—that is, rather than immediately sending out a record the producer will wait for up to the given delay to allow other records to be sent so that the sends can be batched together.


### `max_request_size` [v11.3.4-plugins-outputs-kafka-max_request_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1048576` (1MB).

The maximum size of a request


### `message_key` [v11.3.4-plugins-outputs-kafka-message_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The key for the message.


### `metadata_fetch_timeout_ms` [v11.3.4-plugins-outputs-kafka-metadata_fetch_timeout_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60000` milliseconds (60 seconds).

The timeout setting for initial metadata request to fetch topic metadata.


### `metadata_max_age_ms` [v11.3.4-plugins-outputs-kafka-metadata_max_age_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `300000` milliseconds (5 minutes).

The max time in milliseconds before a metadata refresh is forced.


### `partitioner` [v11.3.4-plugins-outputs-kafka-partitioner]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The default behavior is to hash the `message_key` of an event to get the partition. When no message key is present, the plugin picks a partition in a round-robin fashion.

Available options for choosing a partitioning strategy are as follows:

* `default` use the default partitioner as described above
* `round_robin` distributes writes to all partitions equally, regardless of `message_key`
* `uniform_sticky` sticks to a partition for the duration of a batch than randomly picks a new one


### `receive_buffer_bytes` [v11.3.4-plugins-outputs-kafka-receive_buffer_bytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `32768` (32KB).

The size of the TCP receive buffer to use when reading data


### `reconnect_backoff_ms` [v11.3.4-plugins-outputs-kafka-reconnect_backoff_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`.

The amount of time to wait before attempting to reconnect to a given host when a connection fails.


### `request_timeout_ms` [v11.3.4-plugins-outputs-kafka-request_timeout_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `40000` milliseconds (40 seconds).

The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted.


### `retries` [v11.3.4-plugins-outputs-kafka-retries]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The default retry behavior is to retry until successful. To prevent data loss, changing this setting is discouraged.

If you choose to set `retries`, a value greater than zero will cause the client to only retry a fixed number of times. This will result in data loss if a transport fault exists for longer than your retry count (network outage, Kafka down, etc).

A value less than zero is a configuration error.

Starting with version 10.5.0, this plugin will only retry exceptions that are a subclass of [RetriableException](https://kafka.apache.org/34/javadoc/org/apache/kafka/common/errors/RetriableException.html) and [InterruptException](https://kafka.apache.org/34/javadoc/org/apache/kafka/common/errors/InterruptException.html). If producing a message throws any other exception, an error is logged and the message is dropped without retrying. This prevents the Logstash pipeline from hanging indefinitely.

In versions prior to 10.5.0, any exception is retried indefinitely unless the `retries` option is configured.


### `retry_backoff_ms` [v11.3.4-plugins-outputs-kafka-retry_backoff_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100` milliseconds.

The amount of time to wait before attempting to retry a failed produce request to a given topic partition.


### `sasl_jaas_config` [v11.3.4-plugins-outputs-kafka-sasl_jaas_config]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JAAS configuration setting local to this plugin instance, as opposed to settings using config file configured using `jaas_path`, which are shared across the JVM. This allows each plugin instance to have its own configuration.

If both `sasl_jaas_config` and `jaas_path` configurations are set, the setting here takes precedence.

Example (setting for Azure Event Hub):

```ruby
    output {
      kafka {
        sasl_jaas_config => "org.apache.kafka.common.security.plain.PlainLoginModule required username='auser'  password='apassword';"
      }
    }
```


### `sasl_kerberos_service_name` [v11.3.4-plugins-outputs-kafka-sasl_kerberos_service_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The Kerberos principal name that Kafka broker runs as. This can be defined either in Kafka’s JAAS config or in Kafka’s config.


### `sasl_mechanism` [v11.3.4-plugins-outputs-kafka-sasl_mechanism]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"GSSAPI"`

[SASL mechanism](http://kafka.apache.org/documentation.html#security_sasl) used for client connections. This may be any mechanism for which a security provider is available. GSSAPI is the default mechanism.


### `security_protocol` [v11.3.4-plugins-outputs-kafka-security_protocol]

* Value can be any of: `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT`, `SASL_SSL`
* Default value is `"PLAINTEXT"`

Security protocol to use, which can be either of PLAINTEXT,SSL,SASL_PLAINTEXT,SASL_SSL


### `send_buffer_bytes` [v11.3.4-plugins-outputs-kafka-send_buffer_bytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `131072` (128KB).

The size of the TCP send buffer to use when sending data.


### `ssl_endpoint_identification_algorithm` [v11.3.4-plugins-outputs-kafka-ssl_endpoint_identification_algorithm]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"https"`

The endpoint identification algorithm, defaults to `"https"`. Set to empty string `""` to disable


### `ssl_key_password` [v11.3.4-plugins-outputs-kafka-ssl_key_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The password of the private key in the key store file.


### `ssl_keystore_location` [v11.3.4-plugins-outputs-kafka-ssl_keystore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore path.


### `ssl_keystore_password` [v11.3.4-plugins-outputs-kafka-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore password


### `ssl_keystore_type` [v11.3.4-plugins-outputs-kafka-ssl_keystore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The keystore type.


### `ssl_truststore_location` [v11.3.4-plugins-outputs-kafka-ssl_truststore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The JKS truststore path to validate the Kafka broker’s certificate.


### `ssl_truststore_password` [v11.3.4-plugins-outputs-kafka-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The truststore password


### `ssl_truststore_type` [v11.3.4-plugins-outputs-kafka-ssl_truststore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The truststore type.


### `topic_id` [v11.3.4-plugins-outputs-kafka-topic_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The topic to produce messages to


### `value_serializer` [v11.3.4-plugins-outputs-kafka-value_serializer]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringSerializer"`

Serializer class for the value of the message



## Common options [v11.3.4-plugins-outputs-kafka-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v11-3-4-plugins-outputs-kafka.md#v11.3.4-plugins-outputs-kafka-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v11.3.4-plugins-outputs-kafka-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v11.3.4-plugins-outputs-kafka-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v11.3.4-plugins-outputs-kafka-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 kafka outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  kafka {
    id => "my_plugin_id"
  }
}
```



