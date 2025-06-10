---
navigation_title: "v5.2.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.2.4-plugins-outputs-http.html
---

# Http output plugin v5.2.4 [v5.2.4-plugins-outputs-http]

* Plugin version: v5.2.4
* Released on: 2019-01-30
* [Changelog](https://github.com/logstash-plugins/logstash-output-http/blob/v5.2.4/CHANGELOG.md)

For other versions, see the [overview list](output-http-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1312]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1305]

This output lets you send events to a generic HTTP(S) endpoint.

This output will execute up to *pool\_max* requests in parallel for performance. Consider this when tuning this plugin for performance.

Additionally, note that when parallel execution is used strict ordering of events is not guaranteed!

Beware, this gem does not yet support codecs. Please use the *format* option for now.

## Http Output Configuration Options [v5.2.4-plugins-outputs-http-options]

This plugin supports the following configuration options plus the [Common options](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`automatic_retries`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-automatic_retries) | [number](/lsr/value-types.md#number) | No |
| [`cacert`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-cacert) | a valid filesystem path | No |
| [`client_cert`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-client_cert) | a valid filesystem path | No |
| [`client_key`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-client_key) | a valid filesystem path | No |
| [`connect_timeout`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-connect_timeout) | [number](/lsr/value-types.md#number) | No |
| [`content_type`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-content_type) | [string](/lsr/value-types.md#string) | No |
| [`cookies`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-cookies) | [boolean](/lsr/value-types.md#boolean) | No |
| [`follow_redirects`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-follow_redirects) | [boolean](/lsr/value-types.md#boolean) | No |
| [`format`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-format) | [string](/lsr/value-types.md#string), one of `["json", "json_batch", "form", "message"]` | No |
| [`headers`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-headers) | [hash](/lsr/value-types.md#hash) | No |
| [`http_compression`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-http_compression) | [boolean](/lsr/value-types.md#boolean) | No |
| [`http_method`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-http_method) | [string](/lsr/value-types.md#string), one of `["put", "post", "patch", "delete", "get", "head"]` | Yes |
| [`ignorable_codes`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-ignorable_codes) | [number](/lsr/value-types.md#number) | No |
| [`keepalive`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-keepalive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keystore`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-keystore) | a valid filesystem path | No |
| [`keystore_password`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`keystore_type`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-keystore_type) | [string](/lsr/value-types.md#string) | No |
| [`mapping`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-mapping) | [hash](/lsr/value-types.md#hash) | No |
| [`message`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-message) | [string](/lsr/value-types.md#string) | No |
| [`pool_max`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-pool_max) | [number](/lsr/value-types.md#number) | No |
| [`pool_max_per_route`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-pool_max_per_route) | [number](/lsr/value-types.md#number) | No |
| [`proxy`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-proxy) | <<,>> | No |
| [`request_timeout`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-request_timeout) | [number](/lsr/value-types.md#number) | No |
| [`retry_failed`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-retry_failed) | [boolean](/lsr/value-types.md#boolean) | No |
| [`retry_non_idempotent`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-retry_non_idempotent) | [boolean](/lsr/value-types.md#boolean) | No |
| [`retryable_codes`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-retryable_codes) | [number](/lsr/value-types.md#number) | No |
| [`socket_timeout`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-socket_timeout) | [number](/lsr/value-types.md#number) | No |
| [`truststore`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-truststore) | a valid filesystem path | No |
| [`truststore_password`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`truststore_type`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`url`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-url) | [string](/lsr/value-types.md#string) | Yes |
| [`validate_after_inactivity`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-validate_after_inactivity) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-common-options) for a list of options supported by all output plugins.

### `automatic_retries` [v5.2.4-plugins-outputs-http-automatic_retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

How many times should the client retry a failing URL. We highly recommend NOT setting this value to zero if keepalive is enabled. Some servers incorrectly end keepalives early requiring a retry! Note: if `retry_non_idempotent` is set only GET, HEAD, PUT, DELETE, OPTIONS, and TRACE requests will be retried.

### `cacert` [v5.2.4-plugins-outputs-http-cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom X.509 CA (.pem certs) specify the path to that here

### `client_cert` [v5.2.4-plugins-outputs-http-client_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’d like to use a client certificate (note, most people don’t want this) set the path to the x509 cert here

### `client_key` [v5.2.4-plugins-outputs-http-client_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’re using a client certificate specify the path to the encryption key here

### `connect_timeout` [v5.2.4-plugins-outputs-http-connect_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for a connection to be established. Default is `10s`

### `content_type` [v5.2.4-plugins-outputs-http-content_type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Content type

If not specified, this defaults to the following:

* if format is "json", "application/json"
* if format is "json\_batch", "application/json". Each Logstash batch of events will be concatenated into a single array and sent in one request.
* if format is "form", "application/x-www-form-urlencoded"

### `cookies` [v5.2.4-plugins-outputs-http-cookies]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Enable cookie support. With this enabled the client will persist cookies across requests as a normal web browser would. Enabled by default

### `follow_redirects` [v5.2.4-plugins-outputs-http-follow_redirects]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Should redirects be followed? Defaults to `true`

### `format` [v5.2.4-plugins-outputs-http-format]

* Value can be any of: `json`, `json_batch`, `form`, `message`
* Default value is `"json"`

Set the format of the http body.

If json\_batch, each batch of events received by this output will be placed into a single JSON array and sent in one request. This is particularly useful for high throughput scenarios such as sending data between Logstash instaces.

If form, then the body will be the mapping (or whole event) converted into a query parameter string, e.g. `foo=bar&baz=fizz...`

If message, then the body will be the result of formatting the event according to message

Otherwise, the event is sent as json.

### `headers` [v5.2.4-plugins-outputs-http-headers]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Custom headers to use format is `headers => ["X-My-Header", "%{host}"]`

### `http_compression` [v5.2.4-plugins-outputs-http-http_compression]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enable request compression support. With this enabled the plugin will compress http requests using gzip.

### `http_method` [v5.2.4-plugins-outputs-http-http_method]

* This is a required setting.
* Value can be any of: `put`, `post`, `patch`, `delete`, `get`, `head`
* There is no default value for this setting.

The HTTP Verb. One of "put", "post", "patch", "delete", "get", "head"

### `ignorable_codes` [v5.2.4-plugins-outputs-http-ignorable_codes]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

If you would like to consider some non-2xx codes to be successes enumerate them here. Responses returning these codes will be considered successes

### `keepalive` [v5.2.4-plugins-outputs-http-keepalive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Turn this on to enable HTTP keepalive support. We highly recommend setting `automatic_retries` to at least one with this to fix interactions with broken keepalive implementations.

### `keystore` [v5.2.4-plugins-outputs-http-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom keystore (`.jks`) specify that here. This does not work with .pem keys!

### `keystore_password` [v5.2.4-plugins-outputs-http-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the keystore password here. Note, most .jks files created with keytool require a password!

### `keystore_type` [v5.2.4-plugins-outputs-http-keystore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the keystore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `mapping` [v5.2.4-plugins-outputs-http-mapping]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

This lets you choose the structure and parts of the event that are sent.

For example:

```
   mapping => {"foo" => "%{host}"
              "bar" => "%{type}"}
```

### `message` [v5.2.4-plugins-outputs-http-message]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

### `pool_max` [v5.2.4-plugins-outputs-http-pool_max]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50`

Max number of concurrent connections. Defaults to `50`

### `pool_max_per_route` [v5.2.4-plugins-outputs-http-pool_max_per_route]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `25`

Max number of concurrent connections to a single host. Defaults to `25`

### `proxy` [v5.2.4-plugins-outputs-http-proxy]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

If you’d like to use an HTTP proxy . This supports multiple configuration syntaxes:

1. Proxy host in form: `http://proxy.org:1234`
2. Proxy host in form: `{host => "proxy.org", port => 80, scheme => 'http', user => 'username@host', password => 'password'}`
3. Proxy host in form: `{url => 'http://proxy.org:1234', user => 'username@host', password => 'password'}`

### `request_timeout` [v5.2.4-plugins-outputs-http-request_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

This module makes it easy to add a very fully configured HTTP client to logstash based on \[Manticore]\(<https://github.com/cheald/manticore>). For an example of its usage see <https://github.com/logstash-plugins/logstash-input-http_poller> Timeout (in seconds) for the entire request

### `retry_failed` [v5.2.4-plugins-outputs-http-retry_failed]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Set this to false if you don’t want this output to retry failed requests

### `retry_non_idempotent` [v5.2.4-plugins-outputs-http-retry_non_idempotent]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If `automatic_retries` is enabled this will cause non-idempotent HTTP verbs (such as POST) to be retried.

### `retryable_codes` [v5.2.4-plugins-outputs-http-retryable_codes]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `[429, 500, 502, 503, 504]`

If encountered as response codes this plugin will retry these requests

### `socket_timeout` [v5.2.4-plugins-outputs-http-socket_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for data on the socket. Default is `10s`

### `truststore` [v5.2.4-plugins-outputs-http-truststore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom truststore (`.jks`) specify that here. This does not work with .pem certs!

### `truststore_password` [v5.2.4-plugins-outputs-http-truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the truststore password here. Note, most .jks files created with keytool require a password!

### `truststore_type` [v5.2.4-plugins-outputs-http-truststore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the truststore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `url` [v5.2.4-plugins-outputs-http-url]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

URL to use

### `validate_after_inactivity` [v5.2.4-plugins-outputs-http-validate_after_inactivity]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `200`

How long to wait before checking if the connection is stale before executing a request on a connection using keepalive. You may want to set this lower, possibly to 0 if you get connection errors regularly Quoting the Apache commons docs (this client is based Apache Commmons): *Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool.* See [these docs for more info](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity\(int\))

## Common options [v5.2.4-plugins-outputs-http-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-2-4-plugins-outputs-http.md#v5.2.4-plugins-outputs-http-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v5.2.4-plugins-outputs-http-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.2.4-plugins-outputs-http-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.2.4-plugins-outputs-http-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 http outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  http {
    id => "my_plugin_id"
  }
}
```
