---
navigation_title: "v5.2.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.2.0-plugins-outputs-redis.html
---

# Redis output plugin v5.2.0 [v5.2.0-plugins-outputs-redis]


* Plugin version: v5.2.0
* Released on: 2024-06-04
* [Changelog](https://github.com/logstash-plugins/logstash-output-redis/blob/v5.2.0/CHANGELOG.md)

For other versions, see the [overview list](output-redis-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1504]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-redis). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1494]

This output will send events to a Redis queue using RPUSH. The RPUSH command is supported in Redis v0.0.7+. Using PUBLISH to a channel requires at least v1.3.8+. While you may be able to make these Redis versions work, the best performance and stability will be found in more recent stable versions.  Versions 2.6.0+ are recommended.

For more information, see [the Redis homepage](http://redis.io/)


## Redis Output Configuration Options [v5.2.0-plugins-outputs-redis-options]

This plugin supports the following configuration options plus the [Common options](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`batch`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-batch) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`batch_events`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-batch_events) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`batch_timeout`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-batch_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`congestion_interval`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-congestion_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`congestion_threshold`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-congestion_threshold) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`data_type`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-data_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["list", "channel"]` | Yes |
| [`db`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-db) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-host) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`key`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-key) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`password`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`reconnect_interval`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-reconnect_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`shuffle_hosts`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-shuffle_hosts) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_certificate) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_certificate_authorities`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_certificate_authorities) | list of [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_cipher_suites`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_cipher_suites) | list of [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_enabled`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_key) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_supported_protocols`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_supported_protocols) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_verification_mode`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-ssl_verification_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["full", "none"]` | No |
| [`timeout`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-common-options) for a list of options supported by all output plugins.

 

### `batch` [v5.2.0-plugins-outputs-redis-batch]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Set to true if you want Redis to batch up values and send 1 RPUSH command instead of one command per value to push on the list.  Note that this only works with `data_type="list"` mode right now.

If true, we send an RPUSH every "batch_events" events or "batch_timeout" seconds (whichever comes first). Only supported for `data_type` is "list".


### `batch_events` [v5.2.0-plugins-outputs-redis-batch_events]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`

If batch is set to true, the number of events we queue up for an RPUSH.


### `batch_timeout` [v5.2.0-plugins-outputs-redis-batch_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

If batch is set to true, the maximum amount of time between RPUSH commands when there are pending events to flush.


### `congestion_interval` [v5.2.0-plugins-outputs-redis-congestion_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

How often to check for congestion. Default is one second. Zero means to check on every event.


### `congestion_threshold` [v5.2.0-plugins-outputs-redis-congestion_threshold]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

In case Redis `data_type` is `list` and has more than `@congestion_threshold` items, block until someone consumes them and reduces congestion, otherwise if there are no consumers Redis will run out of memory, unless it was configured with OOM protection. But even with OOM protection, a single Redis list can block all other users of Redis, until Redis CPU consumption reaches the max allowed RAM size. A default value of 0 means that this limit is disabled. Only supported for `list` Redis `data_type`.


### `data_type` [v5.2.0-plugins-outputs-redis-data_type]

* Value can be any of: `list`, `channel`
* There is no default value for this setting.

Either list or channel.  If `data_type` is list, then we will set RPUSH to key. If `data_type` is channel, then we will PUBLISH to `key`.


### `db` [v5.2.0-plugins-outputs-redis-db]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The Redis database number.


### `host` [v5.2.0-plugins-outputs-redis-host]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["127.0.0.1"]`

The hostname(s) of your Redis server(s). Ports may be specified on any hostname, which will override the global port config. If the hosts list is an array, Logstash will pick one random host to connect to, if that host is disconnected it will then pick another.

For example:

```ruby
    "127.0.0.1"
    ["127.0.0.1", "127.0.0.2"]
    ["127.0.0.1:6380", "127.0.0.1"]
```


### `key` [v5.2.0-plugins-outputs-redis-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of a Redis list or channel. Dynamic names are valid here, for example `logstash-%{{type}}`.


### `password` [v5.2.0-plugins-outputs-redis-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password to authenticate with.  There is no authentication by default.


### `port` [v5.2.0-plugins-outputs-redis-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `6379`

The default port to connect on. Can be overridden on any hostname.


### `ssl` [v5.2.0-plugins-outputs-redis-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL support.


### `reconnect_interval` [v5.2.0-plugins-outputs-redis-reconnect_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Interval for reconnecting to failed Redis connections


### `shuffle_hosts` [v5.2.0-plugins-outputs-redis-shuffle_hosts]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Shuffle the host list during Logstash startup.


### `ssl_certificate` [v5.2.0-plugins-outputs-redis-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path to certificate in PEM format. This certificate will be presented to the other part of the TLS connection.


### `ssl_certificate_authorities` [v5.2.0-plugins-outputs-redis-ssl_certificate_authorities]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Validate the certificate chain against these authorities. You can define multiple files. All the certificates will be read and added to the trust store. The system CA path is automatically included.


### `ssl_cipher_suites` [v5.2.0-plugins-outputs-redis-ssl_cipher_suites]

* Value type is a list of [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.


### `ssl_enabled` [v5.2.0-plugins-outputs-redis-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable SSL (must be set for other `ssl_` options to take effect).


### `ssl_key` [v5.2.0-plugins-outputs-redis-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key path


### `ssl_key_passphrase` [v5.2.0-plugins-outputs-redis-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* Default value is `nil`

SSL key passphrase


### `ssl_supported_protocols` [v5.2.0-plugins-outputs-redis-ssl_supported_protocols]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a secure connection.

::::{note}
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_verification_mode` [v5.2.0-plugins-outputs-redis-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another part in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not_before and not_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.


### `timeout` [v5.2.0-plugins-outputs-redis-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Redis initial connection timeout in seconds.



## Common options [v5.2.0-plugins-outputs-redis-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v5-2-0-plugins-outputs-redis.md#v5.2.0-plugins-outputs-redis-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v5.2.0-plugins-outputs-redis-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v5.2.0-plugins-outputs-redis-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v5.2.0-plugins-outputs-redis-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 redis outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  redis {
    id => "my_plugin_id"
  }
}
```



