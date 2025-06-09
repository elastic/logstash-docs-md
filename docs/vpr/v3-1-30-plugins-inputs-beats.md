---
navigation_title: "v3.1.30"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.30-plugins-inputs-beats.html
---

# Beats input plugin v3.1.30 [v3.1.30-plugins-inputs-beats]

* Plugin version: v3.1.30
* Released on: 2018-03-13
* [Changelog](https://github.com/logstash-plugins/logstash-input-beats/blob/v3.1.30/CHANGELOG.md)

For other versions, see the [overview list](input-beats-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_253]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-beats). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_253]

This input plugin enables Logstash to receive events from the [Elastic Beats](https://www.elastic.co/products/beats) framework.

The following example shows how to configure Logstash to listen on port 5044 for incoming Beats connections and to index into Elasticsearch:

```
input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => "localhost:9200"
    manage_template => false
    index => "%{[@metadata][beat]}-%{+YYYY.MM.dd}"
    document_type => "%{[@metadata][type]}"
  }
}
```

The Beats shipper automatically sets the `type` field on the event. You cannot override this setting in the Logstash config. If you specify a setting for the [`type`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-type) config option in Logstash, it is ignored.

If you are shipping events that span multiple lines, you need to use the [configuration options available in Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html) to handle multiline events before sending the event data to Logstash. You cannot use the [multiline codec plugin](https://www.elastic.co/guide/en/logstash/current/plugins-codecs-multiline.html) codec to handle multiline events. Doing so will result in the failure to start Logstash.

## Beats Input Configuration Options [v3.1.30-plugins-inputs-beats-options]

This plugin supports the following configuration options plus the [Common options](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`cipher_suites`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-cipher_suites) | [array](/lsr/value-types.md#array) | No |
| [`client_inactivity_timeout`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-client_inactivity_timeout) | [number](/lsr/value-types.md#number) | No |
| [`host`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-host) | [string](/lsr/value-types.md#string) | No |
| [`include_codec_tag`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-include_codec_tag) | [boolean](/lsr/value-types.md#boolean) | No |
| [`port`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-port) | [number](/lsr/value-types.md#number) | Yes |
| [`ssl`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_certificate`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_handshake_timeout`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_handshake_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ssl_key`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verify_mode`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-ssl_verify_mode) | [string](/lsr/value-types.md#string), one of `["none", "peer", "force_peer"]` | No |
| [`tls_max_version`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-tls_max_version) | [number](/lsr/value-types.md#number) | No |
| [`tls_min_version`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-tls_min_version) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-common-options) for a list of options supported by all input plugins.

### `cipher_suites` [v3.1.30-plugins-inputs-beats-cipher_suites]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `java.lang.String[TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256]@459cfcca`

The list of ciphers suite to use, listed by priorities.

### `client_inactivity_timeout` [v3.1.30-plugins-inputs-beats-client_inactivity_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Close Idle clients after X seconds of inactivity.

### `congestion_threshold` (DEPRECATED) [v3.1.30-plugins-inputs-beats-congestion_threshold]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](/lsr/value-types.md#number)
* Default value is `5`

The number of seconds before we raise a timeout. This option is useful to control how much time to wait if something is blocking the pipeline.

### `host` [v3.1.30-plugins-inputs-beats-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The IP address to listen on.

### `include_codec_tag` [v3.1.30-plugins-inputs-beats-include_codec_tag]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

### `port` [v3.1.30-plugins-inputs-beats-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

The port to listen on.

### `ssl` [v3.1.30-plugins-inputs-beats-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Events are by default sent in plain text. You can enable encryption by setting `ssl` to true and configuring the `ssl_certificate` and `ssl_key` options.

### `ssl_certificate` [v3.1.30-plugins-inputs-beats-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use.

### `ssl_certificate_authorities` [v3.1.30-plugins-inputs-beats-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store. You need to configure the `ssl_verify_mode` to `peer` or `force_peer` to enable the verification.

### `ssl_handshake_timeout` [v3.1.30-plugins-inputs-beats-ssl_handshake_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout

### `ssl_key` [v3.1.30-plugins-inputs-beats-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key to use. NOTE: This key need to be in the PKCS8 format, you can convert it with [OpenSSL](https://www.openssl.org/docs/man1.1.0/apps/pkcs8.html) for more information.

### `ssl_key_passphrase` [v3.1.30-plugins-inputs-beats-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

SSL key passphrase to use.

### `ssl_verify_mode` [v3.1.30-plugins-inputs-beats-ssl_verify_mode]

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

By default the server doesn’t do any client verification.

`peer` will make the server ask the client to provide a certificate. If the client provides a certificate, it will be validated.

`force_peer` will make the server ask the client to provide a certificate. If the client doesn’t provide a certificate, the connection will be closed.

This option needs to be used with `ssl_certificate_authorities` and a defined list of CAs.

### `target_field_for_codec` (DEPRECATED) [v3.1.30-plugins-inputs-beats-target_field_for_codec]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

This is the default field to which the specified codec will be applied.

### `tls_max_version` [v3.1.30-plugins-inputs-beats-tls_max_version]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1.2`

The maximum TLS version allowed for the encrypted connections. The value must be the one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2

### `tls_min_version` [v3.1.30-plugins-inputs-beats-tls_min_version]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

The minimum TLS version allowed for the encrypted connections. The value must be one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2

## Common options [v3.1.30-plugins-inputs-beats-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.1.30-plugins-inputs-beats-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.1.30-plugins-inputs-beats-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.30-plugins-inputs-beats-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.30-plugins-inputs-beats-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 beats inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  beats {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.1.30-plugins-inputs-beats-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.1.30-plugins-inputs-beats-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.

The Beats shipper automatically sets the `type` field on the event. You cannot override this setting in the Logstash config. If you specify a setting for the [`type`](v3-1-30-plugins-inputs-beats.md#v3.1.30-plugins-inputs-beats-type) config option in Logstash, it is ignored.
