---
navigation_title: "v3.3.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.2-plugins-inputs-http.html
---

# Http input plugin v3.3.2 [v3.3.2-plugins-inputs-http]

* Plugin version: v3.3.2
* Released on: 2019-12-04
* [Changelog](https://github.com/logstash-plugins/logstash-input-http/blob/v3.3.2/CHANGELOG.md)

For other versions, see the [overview list](input-http-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_508]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_502]

Using this input you can receive single or multiline events over http(s). Applications can send an HTTP request to the endpoint started by this input and Logstash will convert it into an event for subsequent processing. Users can pass plain text, JSON, or any formatted data and use a corresponding codec with this input. For Content-Type `application/json` the `json` codec is used, but for all other data formats, `plain` codec is used.

This input can also be used to receive webhook requests to integrate with other services and applications. By taking advantage of the vast plugin ecosystem available in Logstash you can trigger actionable events right from your application.

## Blocking Behavior [_blocking_behavior_32]

The HTTP protocol doesn’t deal well with long running requests. This plugin will either return a 429 (busy) error when Logstash is backlogged, or it will time out the request.

If a 429 error is encountered clients should sleep, backing off exponentially with some random jitter, then retry their request.

This plugin will block if the Logstash queue is blocked and there are available HTTP input threads. This will cause most HTTP clients to time out. Sent events will still be processed in this case. This behavior is not optimal and will be changed in a future release. In the future, this plugin will always return a 429 if the queue is busy, and will not time out in the event of a busy queue.

## Security [_security_32]

This plugin supports standard HTTP basic authentication headers to identify the requester. You can pass in a username, password combination while sending data to this input

You can also setup SSL and send data securely over https, with multiple options such as validating the client’s certificate.

## Codec settings [v3.3.2-plugins-inputs-http-codec-settings]

This plugin has two configuration options for codecs: `codec` and `additional_codecs`.

Values in `additional_codecs` are prioritized over those specified in the `codec` option. That is, the default `codec` is applied only if no codec for the request’s content-type is found in the `additional_codecs` setting.

## Http Input Configuration Options [v3.3.2-plugins-inputs-http-options]

This plugin supports the following configuration options plus the [Common options](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`additional_codecs`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-additional_codecs) | [hash](/lsr/value-types.md#hash) | No |
| [`cipher_suites`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-cipher_suites) | [array](/lsr/value-types.md#array) | No |
| [`host`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-host) | [string](/lsr/value-types.md#string) | No |
| [`keystore`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-keystore) | [path](/lsr/value-types.md#path) | No |
| [`keystore_password`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`password`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-port) | [number](/lsr/value-types.md#number) | No |
| [`max_pending_requests`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-max_pending_requests) | [number](/lsr/value-types.md#number) | No |
| [`response_headers`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-response_headers) | [hash](/lsr/value-types.md#hash) | No |
| [`response_code`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-response_code) | [number](/lsr/value-types.md#number), one of `[200, 201, 202, 204]` | No |
| [`ssl`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_certificate`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_handshake_timeout`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_handshake_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ssl_key`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verify_mode`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-ssl_verify_mode) | [string](/lsr/value-types.md#string), one of `["none", "peer", "force_peer"]` | No |
| [`threads`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-threads) | [number](/lsr/value-types.md#number) | No |
| [`tls_max_version`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-tls_max_version) | [number](/lsr/value-types.md#number) | No |
| [`tls_min_version`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-tls_min_version) | [number](/lsr/value-types.md#number) | No |
| [`user`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-user) | [string](/lsr/value-types.md#string) | No |
| [`verify_mode`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-verify_mode) | [string](/lsr/value-types.md#string), one of `["none", "peer", "force_peer"]` | No |

Also see [Common options](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-common-options) for a list of options supported by all input plugins.

### `additional_codecs` [v3.3.2-plugins-inputs-http-additional_codecs]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"application/json"=>"json"}`

Apply specific codecs for specific content types. The default codec will be applied only after this list is checked and no codec for the request’s content-type is found

### `cipher_suites` [v3.3.2-plugins-inputs-http-cipher_suites]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `java.lang.String[TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256]@459cfcca`

The list of ciphers suite to use, listed by priorities.

### `host` [v3.3.2-plugins-inputs-http-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The host or ip to bind

### `keystore` [v3.3.2-plugins-inputs-http-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* This option is deprecated

The JKS keystore to validate the client’s certificates

Note: This option is deprecated and it will be removed in the next major version of Logstash. Use `ssl_certificate` and `ssl_key` instead.

### `keystore_password` [v3.3.2-plugins-inputs-http-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.
* This option is deprecated

Set the truststore password

Note: This option is deprecated and it will be removed in the next major version of Logstash. Use `ssl_certificate` and `ssl_key` instead.

### `password` [v3.3.2-plugins-inputs-http-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password for basic authorization

### `port` [v3.3.2-plugins-inputs-http-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `8080`

The TCP port to bind to

### `max_content_length` [v3.3.2-plugins-inputs-http-max_content_length]

* Value type is [number](/lsr/value-types.md#number)
* Default value is 104857600

The max content of an HTTP request in bytes. It defaults to 100mb.

### `max_pending_requests` [v3.3.2-plugins-inputs-http-max_pending_requests]

* Value type is [number](/lsr/value-types.md#number)
* Default value is 200

Maximum number of incoming requests to store in a temporary queue before being processed by worker threads. If a request arrives and the queue is full a 429 response will be returned immediately. This queue exists to deal with micro bursts of events and to improve overall throughput, so it should be changed very carefully as it can lead to memory pressure and impact performance. If you need to deal both periodic or unforeseen spikes in incoming requests consider enabling the Persistent Queue for the logstash pipeline.

### `response_code` [v3.3.2-plugins-inputs-http-response_code]

* Value can be any of: 200, 201, 202, 204
* Default value is `200`

The HTTP return code if the request is processed successfully.

Other return codes may happen in the case of an error condition, such as invalid credentials (401), internal errors (503) or backpressure (429).

If 204 (No Content) is set, the response body will not be sent in the response.

### `response_headers` [v3.3.2-plugins-inputs-http-response_headers]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"Content-Type"=>"text/plain"}`

specify a custom set of response headers

### `remote_host_target_field` [v3.3.2-plugins-inputs-http-remote_host_target_field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"host"`

specify a target field for the client host of the http request

### `request_headers_target_field` [v3.3.2-plugins-inputs-http-request_headers_target_field]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"headers"`

specify target field for the client host of the http request

### `ssl` [v3.3.2-plugins-inputs-http-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Events are by default sent in plain text. You can enable encryption by setting `ssl` to true and configuring the `ssl_certificate` and `ssl_key` options.

### `ssl_certificate` [v3.3.2-plugins-inputs-http-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use.

### `ssl_certificate_authorities` [v3.3.2-plugins-inputs-http-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store. You need to configure the `ssl_verify_mode` to `peer` or `force_peer` to enable the verification.

### `ssl_handshake_timeout` [v3.3.2-plugins-inputs-http-ssl_handshake_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout

### `ssl_key` [v3.3.2-plugins-inputs-http-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key to use. NOTE: This key need to be in the PKCS8 format, you can convert it with [OpenSSL](https://www.openssl.org/docs/man1.1.0/apps/pkcs8.html) for more information.

### `ssl_key_passphrase` [v3.3.2-plugins-inputs-http-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

SSL key passphrase to use.

### `ssl_verify_mode` [v3.3.2-plugins-inputs-http-ssl_verify_mode]

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

By default the server doesn’t do any client verification.

`peer` will make the server ask the client to provide a certificate. If the client provides a certificate, it will be validated.

`force_peer` will make the server ask the client to provide a certificate. If the client doesn’t provide a certificate, the connection will be closed.

This option needs to be used with `ssl_certificate_authorities` and a defined list of CAs.

### `threads` [v3.3.2-plugins-inputs-http-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is number of processors

Number of threads to use for both accepting connections and handling requests

### `tls_max_version` [v3.3.2-plugins-inputs-http-tls_max_version]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1.2`

The maximum TLS version allowed for the encrypted connections. The value must be the one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2

### `tls_min_version` [v3.3.2-plugins-inputs-http-tls_min_version]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

The minimum TLS version allowed for the encrypted connections. The value must be one of the following: 1.0 for TLS 1.0, 1.1 for TLS 1.1, 1.2 for TLS 1.2

### `user` [v3.3.2-plugins-inputs-http-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username for basic authorization

### `verify_mode` [v3.3.2-plugins-inputs-http-verify_mode]

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`
* This option is deprecated

Set the client certificate verification method. Valid methods: none, peer, force\_peer

Note: This option is deprecated and it will be removed in the next major version of Logstash. Use `ssl_verify_mode` instead.

## Common options [v3.3.2-plugins-inputs-http-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-3-2-plugins-inputs-http.md#v3.3.2-plugins-inputs-http-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.3.2-plugins-inputs-http-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.3.2-plugins-inputs-http-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.3.2-plugins-inputs-http-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.3.2-plugins-inputs-http-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  http {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.3.2-plugins-inputs-http-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.3.2-plugins-inputs-http-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
