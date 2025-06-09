---
navigation_title: "v1.4.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.4.2-plugins-filters-http.html
---

# HTTP filter plugin v1.4.2 [v1.4.2-plugins-filters-http]

* Plugin version: v1.4.2
* Released on: 2023-03-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-http/blob/v1.4.2/CHANGELOG.md)

For other versions, see the [overview list](filter-http-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1954]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1932]

The HTTP filter provides integration with external web services/REST APIs.

## Compatibility with the Elastic Common Schema (ECS) [v1.4.2-plugins-filters-http-ecs]

The plugin includes sensible defaults that change based on [ECS compatibility mode](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ecs_compatibility). When targeting an ECS version, headers are set as `@metadata` and the `target_body` is a required option. See [`target_body`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_body), and [`target_headers`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_headers).

## HTTP Filter Configuration Options [v1.4.2-plugins-filters-http-options]

This plugin supports the following configuration options plus the [Common options](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`body`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-body) | String, Array or Hash | No |
| [`body_format`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-body_format) | [string](/lsr/value-types.md#string) | No |
| [`ecs_compatibility`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`headers`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-headers) | [hash](/lsr/value-types.md#hash) | No |
| [`query`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-query) | [hash](/lsr/value-types.md#hash) | No |
| [`target_body`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_body) | [string](/lsr/value-types.md#string) | No |
| [`target_headers`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_headers) | [string](/lsr/value-types.md#string) | No |
| [`url`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-url) | [string](/lsr/value-types.md#string) | Yes |
| [`verb`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-verb) | [string](/lsr/value-types.md#string) | No |

There are also multiple configuration options related to the HTTP connectivity:

| Setting | Input type | Required |
| :- | :- | :- |
| [`automatic_retries`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-automatic_retries) | [number](/lsr/value-types.md#number) | No |
| [`cacert`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-cacert) | a valid filesystem path | No |
| [`client_cert`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-client_cert) | a valid filesystem path | No |
| [`client_key`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-client_key) | a valid filesystem path | No |
| [`connect_timeout`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-connect_timeout) | [number](/lsr/value-types.md#number) | No |
| [`cookies`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-cookies) | [boolean](/lsr/value-types.md#boolean) | No |
| [`follow_redirects`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-follow_redirects) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keepalive`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-keepalive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keystore`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-keystore) | a valid filesystem path | No |
| [`keystore_password`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`keystore_type`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-keystore_type) | [string](/lsr/value-types.md#string) | No |
| [`password`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-password) | [password](/lsr/value-types.md#password) | No |
| [`pool_max`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-pool_max) | [number](/lsr/value-types.md#number) | No |
| [`pool_max_per_route`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-pool_max_per_route) | [number](/lsr/value-types.md#number) | No |
| [`proxy`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-proxy) | [string](/lsr/value-types.md#string) | No |
| [`request_timeout`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-request_timeout) | [number](/lsr/value-types.md#number) | No |
| [`retry_non_idempotent`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-retry_non_idempotent) | [boolean](/lsr/value-types.md#boolean) | No |
| [`socket_timeout`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-socket_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ssl_supported_protocols`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ssl_supported_protocols) | [string](/lsr/value-types.md#string) | No |
| [`ssl_verification_mode`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ssl_verification_mode) | [string](/lsr/value-types.md#string) | No |
| [`truststore`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-truststore) | a valid filesystem path | No |
| [`truststore_password`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`truststore_type`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`user`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-user) | [string](/lsr/value-types.md#string) | no |
| [`validate_after_inactivity`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-validate_after_inactivity) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-common-options) for a list of options supported by all filter plugins.

### `body` [v1.4.2-plugins-filters-http-body]

* Value type can be a [string](/lsr/value-types.md#string), [number](/lsr/value-types.md#number), [array](/lsr/value-types.md#array) or [hash](/lsr/value-types.md#hash)
* There is no default value

The body of the HTTP request to be sent.

### `body_format` [v1.4.2-plugins-filters-http-body_format]

* Value type can be either `"json"` or `"text"`
* Default value is `"text"`

If set to `"json"` the body will be serialized as JSON. Otherwise it is sent as is.

### `ecs_compatibility` [v1.4.2-plugins-filters-http-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: does not use ECS-compatible field names (for example, response headers target `headers` field by default)
  * `v1`, `v8`: avoids field names that might conflict with Elastic Common Schema (for example, headers are added as metadata)

* Default value depends on which version of Logstash is running:

  * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
  * Otherwise, the default value is `disabled`.

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current). The value of this setting affects the *default* value of [`target_body`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_body) and [`target_headers`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-target_headers).

### `headers` [v1.4.2-plugins-filters-http-headers]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value

The HTTP headers to be sent in the request. Both the names of the headers and their values can reference values from event fields.

### `query` [v1.4.2-plugins-filters-http-query]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value

Define the query string parameters (key-value pairs) to be sent in the HTTP request.

### `target_body` [v1.4.2-plugins-filters-http-target_body]

* Value type is [hash](/lsr/value-types.md#hash)

* Default value depends on whether [`ecs_compatibility`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ecs_compatibility) is enabled:

  * ECS Compatibility disabled: \`"\[body]"
  * ECS Compatibility enabled: no default value, needs to be specified explicitly

Define the target field for placing the body of the HTTP response.

### `target_headers` [v1.4.2-plugins-filters-http-target_headers]

* Value type is [hash](/lsr/value-types.md#hash)

* Default value depends on whether [`ecs_compatibility`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-ecs_compatibility) is enabled:

  * ECS Compatibility disabled: `"[headers]"`
  * ECS Compatibility enabled: `"[@metadata][filter][http][response][headers]"`

Define the target field for placing the headers of the HTTP response.

### `url` [v1.4.2-plugins-filters-http-url]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The URL to send the request to. The value can be fetched from event fields.

### `verb` [v1.4.2-plugins-filters-http-verb]

* Value type can be either `"GET"`, `"HEAD"`, `"PATCH"`, `"DELETE"`, `"POST"`, `"PUT"`
* Default value is `"GET"`

The verb to be used for the HTTP request.

## HTTP Filter Connectivity Options [v1.4.2-plugins-filters-http-connectivity-options]

### `automatic_retries` [v1.4.2-plugins-filters-http-automatic_retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

How many times should the client retry a failing URL. We highly recommend NOT setting this value to zero if keepalive is enabled. Some servers incorrectly end keepalives early requiring a retry! Note: if `retry_non_idempotent` is set only GET, HEAD, PUT, DELETE, OPTIONS, and TRACE requests will be retried.

### `cacert` [v1.4.2-plugins-filters-http-cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom X.509 CA (.pem certs) specify the path to that here

### `client_cert` [v1.4.2-plugins-filters-http-client_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’d like to use a client certificate (note, most people don’t want this) set the path to the x509 cert here

### `client_key` [v1.4.2-plugins-filters-http-client_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’re using a client certificate specify the path to the encryption key here

### `connect_timeout` [v1.4.2-plugins-filters-http-connect_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for a connection to be established. Default is `10s`

### `cookies` [v1.4.2-plugins-filters-http-cookies]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Enable cookie support. With this enabled the client will persist cookies across requests as a normal web browser would. Enabled by default

### `follow_redirects` [v1.4.2-plugins-filters-http-follow_redirects]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Should redirects be followed? Defaults to `true`

### `keepalive` [v1.4.2-plugins-filters-http-keepalive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Turn this on to enable HTTP keepalive support. We highly recommend setting `automatic_retries` to at least one with this to fix interactions with broken keepalive implementations.

### `keystore` [v1.4.2-plugins-filters-http-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom keystore (`.jks`) specify that here. This does not work with .pem keys!

### `keystore_password` [v1.4.2-plugins-filters-http-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the keystore password here. Note, most .jks files created with keytool require a password!

### `keystore_type` [v1.4.2-plugins-filters-http-keystore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the keystore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `password` [v1.4.2-plugins-filters-http-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to be used in conjunction with the username for HTTP authentication.

### `pool_max` [v1.4.2-plugins-filters-http-pool_max]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50`

Max number of concurrent connections. Defaults to `50`

### `pool_max_per_route` [v1.4.2-plugins-filters-http-pool_max_per_route]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `25`

Max number of concurrent connections to a single host. Defaults to `25`

### `proxy` [v1.4.2-plugins-filters-http-proxy]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

If you’d like to use an HTTP proxy . This supports multiple configuration syntaxes:

1. Proxy host in form: `http://proxy.org:1234`
2. Proxy host in form: `{host => "proxy.org", port => 80, scheme => 'http', user => 'username@host', password => 'password'}`
3. Proxy host in form: `{url => 'http://proxy.org:1234', user => 'username@host', password => 'password'}`

### `request_timeout` [v1.4.2-plugins-filters-http-request_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Timeout (in seconds) for the entire request.

### `retry_non_idempotent` [v1.4.2-plugins-filters-http-retry_non_idempotent]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If `automatic_retries` is enabled this will cause non-idempotent HTTP verbs (such as POST) to be retried.

### `socket_timeout` [v1.4.2-plugins-filters-http-socket_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for data on the socket. Default is `10s`

### `ssl_supported_protocols` [v1.4.2-plugins-filters-http-ssl_supported_protocols]

* Value type is [string](/lsr/value-types.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the HTTP endpoint.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_verification_mode` [v1.4.2-plugins-filters-http-ssl_verification_mode]

* Value type is [string](/lsr/value-types.md#string)
* Supported values are: `full`, `none`
* Default value is `full`

Controls the verification of server certificates. The `full` option verifies that the provided certificate is signed by a trusted authority (CA) and also that the server’s hostname (or IP address) matches the names identified within the certificate.

The `none` setting performs no verification of the server’s certificate. This mode disables many of the security benefits of SSL/TLS and should only be used after cautious consideration. It is primarily intended as a temporary diagnostic mechanism when attempting to resolve TLS errors. Using `none` in production environments is strongly discouraged.

### `truststore` [v1.4.2-plugins-filters-http-truststore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom truststore (`.jks`) specify that here. This does not work with .pem certs!

### `truststore_password` [v1.4.2-plugins-filters-http-truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the truststore password here. Note, most .jks files created with keytool require a password!

### `truststore_type` [v1.4.2-plugins-filters-http-truststore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the truststore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `user` [v1.4.2-plugins-filters-http-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username to use with HTTP authentication for ALL requests. Note that you can also set this per-URL. If you set this you must also set the `password` option.

### `validate_after_inactivity` [v1.4.2-plugins-filters-http-validate_after_inactivity]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `200`

How long to wait before checking for a stale connection to determine if a keepalive request is needed. Consider setting this value lower than the default, possibly to 0, if you get connection errors regularly.

This client is based on Apache Commons. Here’s how the [Apache Commons documentation](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity\(int\)) describes this option: "Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool."

## Common options [v1.4.2-plugins-filters-http-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-4-2-plugins-filters-http.md#v1.4.2-plugins-filters-http-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.4.2-plugins-filters-http-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      http {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      http {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.4.2-plugins-filters-http-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      http {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      http {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.4.2-plugins-filters-http-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.4.2-plugins-filters-http-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      http {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.4.2-plugins-filters-http-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.4.2-plugins-filters-http-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      http {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      http {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.4.2-plugins-filters-http-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      http {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      http {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
