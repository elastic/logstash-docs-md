---
navigation_title: "v7.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v7.0.0-plugins-outputs-kafka.html
---

# Kafka output plugin v7.0.0 [v7.0.0-plugins-outputs-kafka]


* Plugin version: v7.0.0
* Released on: 2017-08-01
* [Changelog](https://github.com/logstash-plugins/logstash-output-kafka/blob/v7.0.0/CHANGELOG.md)

For other versions, see the [overview list](output-kafka-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1404]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-kafka). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1394]

Write events to a Kafka topic. This uses the Kafka Producer API to write messages to a topic on the broker.

Here’s a compatibility matrix that shows the Kafka client versions that are compatible with each combination of Logstash and the Kafka output plugin:

| Kafka Client Version | Logstash Version | Plugin Version | Why? |
| --- | --- | --- | --- |
| 0.8 | 2.0.0 - 2.x.x | <3.0.0 | Legacy, 0.8 is still popular |
| 0.9 | 2.0.0 - 2.3.x | 3.x.x | Works with the old Ruby Event API (`event['product']['price'] = 10`) |
| 0.9 | 2.4.x - 5.x.x | 4.x.x | Works with the new getter/setter APIs (`event.set('[product][price]', 10)`) |
| 0.10.0.x | 2.4.x - 5.x.x | 5.x.x | Not compatible with the ⇐ 0.9 broker |
| 0.10.1.x | 2.4.x - 5.x.x | 6.x.x |  |
| 0.11.0.0 | 2.4.x - 5.x.x | 6.2.2 | Not compatible with the ⇐ 0.9 broker |

::::{note}
We recommended that you use matching Kafka client and broker versions. During upgrades, you should upgrade brokers before clients because brokers target backwards compatibility. For example, the 0.9 broker is compatible with both the 0.8 consumer and 0.9 consumer APIs, but not the other way around.
::::


This output supports connecting to Kafka over:

* SSL (requires plugin version 3.0.0 or later)
* Kerberos SASL (requires plugin version 5.1.0 or later)

By default security is disabled but can be turned on as needed.

The only required configuration is the topic_id. The default codec is plain, so events will be persisted on the broker in plain format. Logstash will encode your messages with not only the message but also with a timestamp and hostname. If you do not want anything but your message passing through, you should make the output configuration something like:

```ruby
    output {
      kafka {
        codec => plain {
           format => "%{message}"
        }
        topic_id => "mytopic"
      }
    }
For more information see http://kafka.apache.org/documentation.html#theproducer
```

Kafka producer configuration: [http://kafka.apache.org/documentation.html#newproducerconfigs](http://kafka.apache.org/documentation.md#newproducerconfigs)


## Kafka Output Configuration Options [v7.0.0-plugins-outputs-kafka-options]

This plugin supports the following configuration options plus the [Common options](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`acks`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-acks) | [string](logstash://reference/configuration-file-structure.md#string), one of `["0", "1", "all"]` | No |
| [`batch_size`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-batch_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`bootstrap_servers`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-bootstrap_servers) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`buffer_memory`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-buffer_memory) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`client_id`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-client_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`compression_type`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-compression_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "gzip", "snappy", "lz4"]` | No |
| [`jaas_path`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-jaas_path) | a valid filesystem path | No |
| [`kerberos_config`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-kerberos_config) | a valid filesystem path | No |
| [`key_serializer`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-key_serializer) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`linger_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-linger_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_request_size`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-max_request_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`message_key`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-message_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_fetch_timeout_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-metadata_fetch_timeout_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`metadata_max_age_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-metadata_max_age_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`receive_buffer_bytes`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-receive_buffer_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`reconnect_backoff_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-reconnect_backoff_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`request_timeout_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-request_timeout_ms) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`retries`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-retries) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_backoff_ms`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-retry_backoff_ms) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`sasl_kerberos_service_name`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-sasl_kerberos_service_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sasl_mechanism`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-sasl_mechanism) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`security_protocol`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-security_protocol) | [string](logstash://reference/configuration-file-structure.md#string), one of `["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]` | No |
| [`send_buffer_bytes`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-send_buffer_bytes) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_key_password`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_key_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_location`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_keystore_location) | a valid filesystem path | No |
| [`ssl_keystore_password`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_type`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_keystore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_truststore_location`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_truststore_location) | a valid filesystem path | No |
| [`ssl_truststore_password`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_type`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-ssl_truststore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`topic_id`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-topic_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`value_serializer`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-value_serializer) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-common-options) for a list of options supported by all output plugins.

 

### `acks` [v7.0.0-plugins-outputs-kafka-acks]

* Value can be any of: `0`, `1`, `all`
* Default value is `"1"`

The number of acknowledgments the producer requires the leader to have received before considering a request complete.

acks=0,   the producer will not wait for any acknowledgment from the server at all. acks=1,   This will mean the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers. acks=all, This means the leader will wait for the full set of in-sync replicas to acknowledge the record.


### `batch_size` [v7.0.0-plugins-outputs-kafka-batch_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `16384`

The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes.


### `bootstrap_servers` [v7.0.0-plugins-outputs-kafka-bootstrap_servers]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost:9092"`

This is for bootstrapping and the producer will only use it for getting metadata (topics, partitions and replicas). The socket connections for sending the actual data will be established based on the broker information returned in the metadata. The format is `host1:port1,host2:port2`, and the list can be a subset of brokers or a VIP pointing to a subset of brokers.


### `buffer_memory` [v7.0.0-plugins-outputs-kafka-buffer_memory]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `33554432`

The total bytes of memory the producer can use to buffer records waiting to be sent to the server.


### `client_id` [v7.0.0-plugins-outputs-kafka-client_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The id string to pass to the server when making requests. The purpose of this is to be able to track the source of requests beyond just ip/port by allowing a logical application name to be included with the request


### `compression_type` [v7.0.0-plugins-outputs-kafka-compression_type]

* Value can be any of: `none`, `gzip`, `snappy`, `lz4`
* Default value is `"none"`

The compression type for all data generated by the producer. The default is none (i.e. no compression). Valid values are none, gzip, or snappy.


### `jaas_path` [v7.0.0-plugins-outputs-kafka-jaas_path]

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


### `kerberos_config` [v7.0.0-plugins-outputs-kafka-kerberos_config]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Optional path to kerberos config file. This is krb5.conf style as detailed in [https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.md)


### `key_serializer` [v7.0.0-plugins-outputs-kafka-key_serializer]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringSerializer"`

Serializer class for the key of the message


### `linger_ms` [v7.0.0-plugins-outputs-kafka-linger_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The producer groups together any records that arrive in between request transmissions into a single batched request. Normally this occurs only under load when records arrive faster than they can be sent out. However in some circumstances the client may want to reduce the number of requests even under moderate load. This setting accomplishes this by adding a small amount of artificial delay—that is, rather than immediately sending out a record the producer will wait for up to the given delay to allow other records to be sent so that the sends can be batched together.


### `max_request_size` [v7.0.0-plugins-outputs-kafka-max_request_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1048576`

The maximum size of a request


### `message_key` [v7.0.0-plugins-outputs-kafka-message_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The key for the message


### `metadata_fetch_timeout_ms` [v7.0.0-plugins-outputs-kafka-metadata_fetch_timeout_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60000`

the timeout setting for initial metadata request to fetch topic metadata.


### `metadata_max_age_ms` [v7.0.0-plugins-outputs-kafka-metadata_max_age_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `300000`

the max time in milliseconds before a metadata refresh is forced.


### `receive_buffer_bytes` [v7.0.0-plugins-outputs-kafka-receive_buffer_bytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `32768`

The size of the TCP receive buffer to use when reading data


### `reconnect_backoff_ms` [v7.0.0-plugins-outputs-kafka-reconnect_backoff_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

The amount of time to wait before attempting to reconnect to a given host when a connection fails.


### `request_timeout_ms` [v7.0.0-plugins-outputs-kafka-request_timeout_ms]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted.


### `retries` [v7.0.0-plugins-outputs-kafka-retries]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

Setting a value greater than zero will cause the client to resend any record whose send fails with a potentially transient error.


### `retry_backoff_ms` [v7.0.0-plugins-outputs-kafka-retry_backoff_ms]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100`

The amount of time to wait before attempting to retry a failed produce request to a given topic partition.


### `sasl_kerberos_service_name` [v7.0.0-plugins-outputs-kafka-sasl_kerberos_service_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The Kerberos principal name that Kafka broker runs as. This can be defined either in Kafka’s JAAS config or in Kafka’s config.


### `sasl_mechanism` [v7.0.0-plugins-outputs-kafka-sasl_mechanism]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"GSSAPI"`

[SASL mechanism](http://kafka.apache.org/documentation.md#security_sasl) used for client connections. This may be any mechanism for which a security provider is available. GSSAPI is the default mechanism.


### `security_protocol` [v7.0.0-plugins-outputs-kafka-security_protocol]

* Value can be any of: `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT`, `SASL_SSL`
* Default value is `"PLAINTEXT"`

Security protocol to use, which can be either of PLAINTEXT,SSL,SASL_PLAINTEXT,SASL_SSL


### `send_buffer_bytes` [v7.0.0-plugins-outputs-kafka-send_buffer_bytes]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `131072`

The size of the TCP send buffer to use when sending data.


### `ssl_key_password` [v7.0.0-plugins-outputs-kafka-ssl_key_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The password of the private key in the key store file.


### `ssl_keystore_location` [v7.0.0-plugins-outputs-kafka-ssl_keystore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore path.


### `ssl_keystore_password` [v7.0.0-plugins-outputs-kafka-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

If client authentication is required, this setting stores the keystore password


### `ssl_keystore_type` [v7.0.0-plugins-outputs-kafka-ssl_keystore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The keystore type.


### `ssl_truststore_location` [v7.0.0-plugins-outputs-kafka-ssl_truststore_location]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The JKS truststore path to validate the Kafka broker’s certificate.


### `ssl_truststore_password` [v7.0.0-plugins-outputs-kafka-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The truststore password


### `ssl_truststore_type` [v7.0.0-plugins-outputs-kafka-ssl_truststore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The truststore type.


### `topic_id` [v7.0.0-plugins-outputs-kafka-topic_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The topic to produce messages to


### `value_serializer` [v7.0.0-plugins-outputs-kafka-value_serializer]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"org.apache.kafka.common.serialization.StringSerializer"`

Serializer class for the value of the message



## Common options [v7.0.0-plugins-outputs-kafka-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v7-0-0-plugins-outputs-kafka.md#v7.0.0-plugins-outputs-kafka-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v7.0.0-plugins-outputs-kafka-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v7.0.0-plugins-outputs-kafka-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v7.0.0-plugins-outputs-kafka-id]

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



