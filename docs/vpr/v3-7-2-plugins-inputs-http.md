---
navigation_title: "v3.7.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.7.2-plugins-inputs-http.html
---

# Http input plugin v3.7.2 [v3.7.2-plugins-inputs-http]


* Plugin version: v3.7.2
* Released on: 2023-06-29
* [Changelog](https://github.com/logstash-plugins/logstash-input-http/blob/v3.7.2/CHANGELOG.md)

For other versions, see the [overview list](input-http-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_471]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_465]

Using this input you can receive single or multiline events over http(s). Applications can send an HTTP request to the endpoint started by this input and Logstash will convert it into an event for subsequent processing. Users can pass plain text, JSON, or any formatted data and use a corresponding codec with this input. For Content-Type `application/json` the `json` codec is used, but for all other data formats, `plain` codec is used.

This input can also be used to receive webhook requests to integrate with other services and applications. By taking advantage of the vast plugin ecosystem available in Logstash you can trigger actionable events right from your application.


## Event Metadata and the Elastic Common Schema (ECS) [v3.7.2-plugins-inputs-http-ecs_metadata]

In addition to decoding the events, this input will add HTTP headers containing connection information to each event. When ECS compatibility is disabled, the headers are stored in the `headers` field, which has the potential to create confusion and schema conflicts downstream. When ECS is enabled, we can ensure a pipeline maintains access to this metadata throughout the event’s lifecycle without polluting the top-level namespace.

Here’s how ECS compatibility mode affects output.

|  ECS `disabled` |  ECS `v1`,`v8` | Availability | Description |
| --- | --- | --- | --- |
|  [host] |  [host][ip] | *Always* | *Host IP address* |
|  [headers] |  [@metadata][input][http][request][headers] | *Always* | *Complete HTTP headers* |
|  [headers][http_version] |  [http][version] | *Always* | *HTTP version* |
|  [headers][http_user_agent] |  [user_agent][original] | *Always* | *client user agent* |
|  [headers][http_host] |  [url][domain] and [url][port] | *Always* | *host domain and port* |
|  [headers][request_method] |  [http][method] | *Always* | *HTTP method* |
|  [headers][request_path] |  [url][path] | *Always* | *Query path* |
|  [headers][content_length] |  [http][request][body][bytes] | *Always* | *Request content length* |
|  [headers][content_type] |  [http][request][mime_type] | *Always* | *Request mime type* |


## Blocking Behavior [_blocking_behavior_8]

The HTTP protocol doesn’t deal well with long running requests. This plugin will either return a 429 (busy) error when Logstash is backlogged, or it will time out the request.

If a 429 error is encountered clients should sleep, backing off exponentially with some random jitter, then retry their request.

This plugin will block if the Logstash queue is blocked and there are available HTTP input threads. This will cause most HTTP clients to time out. Sent events will still be processed in this case. This behavior is not optimal and will be changed in a future release. In the future, this plugin will always return a 429 if the queue is busy, and will not time out in the event of a busy queue.


## Security [_security_8]

This plugin supports standard HTTP basic authentication headers to identify the requester. You can pass in a username, password combination while sending data to this input

You can also setup SSL and send data securely over https, with multiple options such as validating the client’s certificate.


## Codec settings [v3.7.2-plugins-inputs-http-codec-settings]

This plugin has two configuration options for codecs: `codec` and `additional_codecs`.

Values in `additional_codecs` are prioritized over those specified in the `codec` option. That is, the default `codec` is applied only if no codec for the request’s content-type is found in the `additional_codecs` setting.


## Http Input Configuration Options [v3.7.2-plugins-inputs-http-options]

This plugin supports the following configuration options plus the [Common options](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`additional_codecs`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-additional_codecs) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`cipher_suites`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-cipher_suites) | [array](logstash://reference/configuration-file-structure.md#array) | *Deprecated* |
| [`ecs_compatibility`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`keystore`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-keystore) | [path](logstash://reference/configuration-file-structure.md#path) | *Deprecated* |
| [`keystore_password`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | *Deprecated* |
| [`password`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_pending_requests`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-max_pending_requests) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`response_headers`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-response_headers) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`response_code`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-response_code) | [number](logstash://reference/configuration-file-structure.md#number), one of `[200, 201, 202, 204]` | No |
| [`ssl`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | *Deprecated* |
| [`ssl_certificate`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_certificate_authorities) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_cipher_suites`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_cipher_suites) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_client_authentication`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_client_authentication) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "optional", "required"]` | No |
| [`ssl_enabled`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_handshake_timeout`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_handshake_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_key`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_password`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_path`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_keystore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_supported_protocols`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_supported_protocols) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_verify_mode`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_verify_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "peer", "force_peer"]` | *Deprecated* |
| [`threads`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-threads) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`tls_max_version`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-tls_max_version) | [number](logstash://reference/configuration-file-structure.md#number) | *Deprecated* |
| [`tls_min_version`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-tls_min_version) | [number](logstash://reference/configuration-file-structure.md#number) | *Deprecated* |
| [`user`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`verify_mode`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-verify_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "peer", "force_peer"]` | *Deprecated* |

Also see [Common options](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-common-options) for a list of options supported by all input plugins.

 

### `additional_codecs` [v3.7.2-plugins-inputs-http-additional_codecs]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{"application/json"=>"json"}`

Apply specific codecs for specific content types. The default codec will be applied only after this list is checked and no codec for the request’s content-type is found


### `cipher_suites` [v3.7.2-plugins-inputs-http-cipher_suites]

::::{admonition} Deprecated in 3.6.0.
:class: warning

Replaced by [`ssl_cipher_suites`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_cipher_suites)
::::


* Value type is [array](logstash://reference/configuration-file-structure.md#array)

The list of cipher suites to use, listed by priorities.


### `ecs_compatibility` [v3.7.2-plugins-inputs-http-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: unstructured connection metadata added at root level
    * `v1`,`v8`: headers added under `[@metadata][http][header]`. Some are copied to structured ECS fields `http`, `url`, `user_agent` and `host`


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). See [Event Metadata and the Elastic Common Schema (ECS)](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ecs_metadata) for detailed information.

**Sample output: ECS disabled**

```text
{
    "@version" => "1",
    "headers" => {
           "request_path" => "/twitter/tweet/1",
            "http_accept" => "*/*",
           "http_version" => "HTTP/1.1",
         "request_method" => "PUT",
              "http_host" => "localhost:8080",
        "http_user_agent" => "curl/7.64.1",
         "content_length" => "5",
           "content_type" => "application/x-www-form-urlencoded"
    },
    "@timestamp" => 2021-05-28T19:27:28.609Z,
    "host" => "127.0.0.1",
    "message" => "hello"
}
```

**Sample output: ECS enabled**

```text
{
    "@version" => "1",
    "user_agent" => {
        "original" => "curl/7.64.1"
    },
    "http" => {
        "method" => "PUT",
        "request" => {
            "mime_type" => "application/x-www-form-urlencoded",
            "body" => {
                "bytes" => "5"
            }
        },
        "version" => "HTTP/1.1"
    },
    "url" => {
          "port" => "8080",
        "domain" => "snmp1",
          "path" => "/twitter/tweet/1"
    },
    "@timestamp" => 2021-05-28T23:32:38.222Z,
    "host" => {
        "ip" => "127.0.0.1"
    },
    "message" => "hello",
}
```


### `host` [v3.7.2-plugins-inputs-http-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"0.0.0.0"`

The host or ip to bind


### `keystore` [v3.7.2-plugins-inputs-http-keystore]

::::{admonition} Deprecated in 3.7.0.
:class: warning

Use [`ssl_keystore_path`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_keystore_path) instead
::::


* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The JKS keystore to validate the client’s certificates


### `keystore_password` [v3.7.2-plugins-inputs-http-keystore_password]

::::{admonition} Deprecated in 3.7.0.
:class: warning

Use [`ssl_keystore_password`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_keystore_password) instead
::::


* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the keystore password


### `password` [v3.7.2-plugins-inputs-http-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password for basic authorization


### `port` [v3.7.2-plugins-inputs-http-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `8080`

The TCP port to bind to


### `max_content_length` [v3.7.2-plugins-inputs-http-max_content_length]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is 104857600

The max content of an HTTP request in bytes. It defaults to 100mb.


### `max_pending_requests` [v3.7.2-plugins-inputs-http-max_pending_requests]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is 200

Maximum number of incoming requests to store in a temporary queue before being processed by worker threads. If a request arrives and the queue is full a 429 response will be returned immediately. This queue exists to deal with micro bursts of events and to improve overall throughput, so it should be changed very carefully as it can lead to memory pressure and impact performance. If you need to deal both periodic or unforeseen spikes in incoming requests consider enabling the Persistent Queue for the logstash pipeline.


### `response_code` [v3.7.2-plugins-inputs-http-response_code]

* Value can be any of: 200, 201, 202, 204
* Default value is `200`

The HTTP return code if the request is processed successfully.

Other return codes may happen in the case of an error condition, such as invalid credentials (401), internal errors (503) or backpressure (429).

If 204 (No Content) is set, the response body will not be sent in the response.


### `response_headers` [v3.7.2-plugins-inputs-http-response_headers]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{"Content-Type"=>"text/plain"}`

specify a custom set of response headers


### `remote_host_target_field` [v3.7.2-plugins-inputs-http-remote_host_target_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"host"` when ECS is disabled
* Default value is `[host][ip]` when ECS is enabled

specify a target field for the client host of the http request


### `request_headers_target_field` [v3.7.2-plugins-inputs-http-request_headers_target_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"headers"` when ECS is disabled
* Default value is `[@metadata][http][header]` when ECS is enabled

specify target field for the client host of the http request


### `ssl` [v3.7.2-plugins-inputs-http-ssl]

::::{admonition} Deprecated in 3.7.0.
:class: warning

Replaced by [`ssl_enabled`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_enabled)
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Events are, by default, sent in plain text. You can enable encryption by setting `ssl` to true and configuring the `ssl_certificate` and `ssl_key` options.


### `ssl_certificate` [v3.7.2-plugins-inputs-http-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate to use.


### `ssl_certificate_authorities` [v3.7.2-plugins-inputs-http-ssl_certificate_authorities]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store. You need to configure the [`ssl_client_authentication`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_client_authentication) to `optional` or `required` to enable the verification.


### `ssl_cipher_suites` [v3.7.2-plugins-inputs-http-ssl_cipher_suites]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `['TLS_AES_256_GCM_SHA384', 'TLS_AES_128_GCM_SHA256', 'TLS_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256']`

The list of cipher suites to use, listed by priorities. This default list applies for OpenJDK 11.0.14 and higher. For older JDK versions, the default list includes only suites supported by that version. For example, the ChaCha20 family of ciphers is not supported in older versions.


### `ssl_client_authentication` [v3.7.2-plugins-inputs-http-ssl_client_authentication]

* Value can be any of: `none`, `optional`, `required`
* Default value is `"none"`

Controls the server’s behavior in regard to requesting a certificate from client connections: `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `none`, which disables the client authentication.

::::{note}
This setting can be used only if [`ssl_certificate_authorities`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_certificate_authorities) is set.
::::



### `ssl_enabled` [v3.7.2-plugins-inputs-http-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Events are, by default, sent in plain text. You can enable encryption by setting `ssl_enabled` to true and configuring the [`ssl_certificate`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_certificate) and [`ssl_key`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_key) options.


### `ssl_handshake_timeout` [v3.7.2-plugins-inputs-http-ssl_handshake_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout


### `ssl_key` [v3.7.2-plugins-inputs-http-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL key to use. NOTE: This key need to be in the PKCS8 format, you can convert it with [OpenSSL](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs8.html) for more information.


### `ssl_key_passphrase` [v3.7.2-plugins-inputs-http-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

SSL key passphrase to use.


### `ssl_keystore_path` [v3.7.2-plugins-inputs-http-ssl_keystore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The JKS keystore to validate the client’s certificates


### `ssl_keystore_password` [v3.7.2-plugins-inputs-http-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the JKS keystore password


### `ssl_supported_protocols` [v3.7.2-plugins-inputs-http-ssl_supported_protocols]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the HTTP endpoint.

For Java 8 `'TLSv1.3'` is supported  only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

::::{note}
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_verify_mode` [v3.7.2-plugins-inputs-http-ssl_verify_mode]

::::{admonition} Deprecated in 3.7.0.
:class: warning

Replaced by [`ssl_client_authentication`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_client_authentication)
::::


* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

By default the server doesn’t do any client verification.

`peer` will make the server ask the client to provide a certificate. If the client provides a certificate, it will be validated.

`force_peer` will make the server ask the client to provide a certificate. If the client doesn’t provide a certificate, the connection will be closed.

This option needs to be used with [`ssl_certificate_authorities`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_certificate_authorities) and a defined list of CAs.


### `threads` [v3.7.2-plugins-inputs-http-threads]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is number of processors

Number of threads to use for both accepting connections and handling requests


### `tls_max_version` [v3.7.2-plugins-inputs-http-tls_max_version]

::::{warning}
Deprecated in 3.6.0.
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)

The maximum TLS version allowed for the encrypted connections. The value must be the one of the following: 1.1 for TLS 1.1, 1.2 for TLS 1.2, 1.3 for TLSv1.3


### `tls_min_version` [v3.7.2-plugins-inputs-http-tls_min_version]

::::{warning}
Deprecated in 3.6.0.
::::


* Value type is [number](logstash://reference/configuration-file-structure.md#number)

The minimum TLS version allowed for the encrypted connections. The value must be one of the following: 1.1 for TLS 1.1, 1.2 for TLS 1.2, 1.3 for TLSv1.3


### `user` [v3.7.2-plugins-inputs-http-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username for basic authorization


### `verify_mode` [v3.7.2-plugins-inputs-http-verify_mode]

::::{admonition} Deprecated in 3.6.0.
:class: warning

Replaced by [`ssl_verify_mode`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-ssl_verify_mode)
::::


* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

Set the client certificate verification method. Valid methods: none, peer, force_peer



## Common options [v3.7.2-plugins-inputs-http-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-7-2-plugins-inputs-http.md#v3.7.2-plugins-inputs-http-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.7.2-plugins-inputs-http-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.7.2-plugins-inputs-http-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.7.2-plugins-inputs-http-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.7.2-plugins-inputs-http-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  http {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.7.2-plugins-inputs-http-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.7.2-plugins-inputs-http-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
