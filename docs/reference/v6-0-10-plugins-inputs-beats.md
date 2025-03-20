---
navigation_title: "v6.0.10"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.0.10-plugins-inputs-beats.html
---

# Beats input plugin v6.0.10 [v6.0.10-plugins-inputs-beats]


* Plugin version: v6.0.10
* Released on: 2020-05-12
* [Changelog](https://github.com/logstash-plugins/logstash-input-beats/blob/v6.0.10/CHANGELOG.md)

For other versions, see the [overview list](input-beats-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_200]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-beats). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_200]

This input plugin enables Logstash to receive events from the [Elastic Beats](https://www.elastic.co/products/beats) framework.

The following example shows how to configure Logstash to listen on port 5044 for incoming Beats connections and to index into Elasticsearch.

```json
input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "%{[@metadata][beat]}-%{[@metadata][version]}" <1>
  }
}
```

1. `%{[@metadata][beat]}` sets the first part of the index name to the value of the `beat` metadata field and `%{[@metadata][version]}` sets the second part to the Beat’s version. For example: metricbeat-7.4.0.


Events indexed into Elasticsearch with the Logstash configuration shown here will be similar to events directly indexed by Beats into Elasticsearch.

::::{note}
If ILM is not being used, set `index` to `%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}` instead so Logstash creates an index per day, based on the `@timestamp` value of the events coming from Beats.
::::


::::{important}
If you are shipping events that span multiple lines, you need to use the [configuration options available in Filebeat](beats://docs/reference/filebeat/multiline-examples.md) to handle multiline events before sending the event data to Logstash. You cannot use the [Multiline codec plugin](logstash://reference/plugins-codecs-multiline.md) to handle multiline events. Doing so will result in the failure to start Logstash.
::::



## Versioned Beats Indices [v6.0.10-plugins-inputs-beats-versioned-indexes]

To minimize the impact of future schema changes on your existing indices and mappings in Elasticsearch, configure the Elasticsearch output to write to versioned indices. The pattern that you specify for the `index` setting controls the index name:

```yaml
index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
```

`%{[@metadata][beat]}`
:   Sets the first part of the index name to the value of the `beat` metadata field, for example, `filebeat`.

`%{[@metadata][version]}`
:   Sets the second part of the name to the Beat version, for example, `{{logstash_version}}`.

`%{+YYYY.MM.dd}`
:   Sets the third part of the name to a date based on the Logstash `@timestamp` field.

This configuration results in daily index names like `filebeat-{{logstash_version}}-2025-01-30`.


## Beats Input Configuration Options [v6.0.10-plugins-inputs-beats-options]

This plugin supports the following configuration options plus the [Common options](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_hostname`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-add_hostname) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`cipher_suites`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-cipher_suites) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`client_inactivity_timeout`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-client_inactivity_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`host`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`include_codec_tag`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-include_codec_tag) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`port`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`ssl`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_certificate_authorities) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_handshake_timeout`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_handshake_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_key`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verify_mode`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_verify_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "peer", "force_peer"]` | No |
| [`ssl_peer_metadata`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-ssl_peer_metadata) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`tls_max_version`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-tls_max_version) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`tls_min_version`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-tls_min_version) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-common-options) for a list of options supported by all input plugins.

 

### `add_hostname` [v6.0.10-plugins-inputs-beats-add_hostname]

::::{admonition} Deprecated in 6.0.0.
:class: warning

The default value has been changed to `false`. In 7.0.0 this setting will be removed
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Flag to determine whether to add `host` field to event using the value supplied by the beat in the `hostname` field.


### `cipher_suites` [v6.0.10-plugins-inputs-beats-cipher_suites]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `java.lang.String[TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256]@459cfcca`

The list of ciphers suite to use, listed by priorities.


### `client_inactivity_timeout` [v6.0.10-plugins-inputs-beats-client_inactivity_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Close Idle clients after X seconds of inactivity.


### `host` [v6.0.10-plugins-inputs-beats-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

The IP address to listen on.


### `include_codec_tag` [v6.0.10-plugins-inputs-beats-include_codec_tag]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`


### `port` [v6.0.10-plugins-inputs-beats-port]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The port to listen on.


### `ssl` [v6.0.10-plugins-inputs-beats-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Events are by default sent in plain text. You can enable encryption by setting `ssl` to true and configuring the `ssl_certificate` and `ssl_key` options.


### `ssl_certificate` [v6.0.10-plugins-inputs-beats-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate to use.


### `ssl_certificate_authorities` [v6.0.10-plugins-inputs-beats-ssl_certificate_authorities]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store. You need to configure the `ssl_verify_mode` to `peer` or `force_peer` to enable the verification.


### `ssl_handshake_timeout` [v6.0.10-plugins-inputs-beats-ssl_handshake_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout


### `ssl_key` [v6.0.10-plugins-inputs-beats-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key to use. NOTE: This key need to be in the PKCS8 format, you can convert it with [OpenSSL](https://www.openssl.org/docs/man1.1.0/apps/pkcs8.md) for more information.


### `ssl_key_passphrase` [v6.0.10-plugins-inputs-beats-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

SSL key passphrase to use.


### `ssl_verify_mode` [v6.0.10-plugins-inputs-beats-ssl_verify_mode]

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

By default the server doesn’t do any client verification.

`peer` will make the server ask the client to provide a certificate. If the client provides a certificate, it will be validated.

`force_peer` will make the server ask the client to provide a certificate. If the client doesn’t provide a certificate, the connection will be closed.

This option needs to be used with `ssl_certificate_authorities` and a defined list of CAs.


### `ssl_peer_metadata` [v6.0.10-plugins-inputs-beats-ssl_peer_metadata]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enables storing client certificate information in event’s metadata.

This option is only valid when `ssl_verify_mode` is set to `peer` or `force_peer`.


### `tls_max_version` [v6.0.10-plugins-inputs-beats-tls_max_version]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1.2`

The maximum TLS version allowed for the encrypted connections. The value must be the one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2


### `tls_min_version` [v6.0.10-plugins-inputs-beats-tls_min_version]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

The minimum TLS version allowed for the encrypted connections. The value must be one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2



## Common options [v6.0.10-plugins-inputs-beats-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v6.0.10-plugins-inputs-beats-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v6.0.10-plugins-inputs-beats-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v6.0.10-plugins-inputs-beats-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v6.0.10-plugins-inputs-beats-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 beats inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  beats {
    id => "my_plugin_id"
  }
}
```


### `tags` [v6.0.10-plugins-inputs-beats-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v6.0.10-plugins-inputs-beats-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.

::::{note}
The Beats shipper automatically sets the `type` field on the event. You cannot override this setting in the Logstash config. If you specify a setting for the [`type`](v6-0-10-plugins-inputs-beats.md#v6.0.10-plugins-inputs-beats-type) config option in Logstash, it is ignored.
::::




