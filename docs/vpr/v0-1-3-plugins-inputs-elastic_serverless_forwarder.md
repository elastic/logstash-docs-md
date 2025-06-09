---
navigation_title: "v0.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.1.3-plugins-inputs-elastic_serverless_forwarder.html
---

# Elastic Serverless Forwarder input plugin v0.1.3 [v0.1.3-plugins-inputs-elastic_serverless_forwarder]

* Plugin version: v0.1.3
* Released on: 2023-09-14
* [Changelog](https://github.com/logstash-plugins/logstash-input-elastic_serverless_forwarder/blob/v0.1.3/CHANGELOG.md)

For other versions, see the [overview list](input-elastic_serverless_forwarder-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_311]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-elastic_serverless_forwarder). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_311]

Using this input you can receive events from Elastic Serverless Forwarder over http(s) connections to the configured [`port`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-port).

### Minimum Configuration [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ext-field]

| SSL Enabled | SSL Disabled |
| :- | :- |
| input {<br> elastic\_serverless\_forwarder {<br> port => 8080<br> ssl\_certificate => "/path/to/logstash.crt"<br> ssl\_key => "/path/to/logstash.key"<br> }<br>} | input {<br> elastic\_serverless\_forwarder {<br> port => 8080<br> ssl\_enabled => false<br> }<br>} |

**Technical Preview**

This Elastic Serverless Forwarder input plugin is part of a *Technical Preview*, which means that both configuration options and implementation details are subject to change in minor releases without being preceded by deprecation warnings.

Before upgrading this plugin or Logstash itself, please pay special attention to this plugin’s [CHANGELOG.md](https://github.com/logstash-plugins/logstash-input-elastic_serverless_forwarder/blob/main/CHANGELOG.md) to avoid being caught by surprise.

## Enrichment [v0.1.3-plugins-inputs-elastic_serverless_forwarder-enrichment]

This input provides *minimal enrichment* on events, and avoids including information about itself, the client from which it received the data, or about the original event as-decoded from the request.

Senders are advised to use care with respect to fields that are [reserved in Logstash](https://www.elastic.co/guide/en/logstash/current/processing.html#reserved-fields). ESF sends the Logstash-required `@timestamp` field by default, but if this value is missing it will be populated with the current time.

## Security [v0.1.3-plugins-inputs-elastic_serverless_forwarder-security]

This plugin has SSL on-by-default.

At a minimum, you will need to either configure the plugin to present its identity, or disable SSL.

Additionally, you may wish to authenticate clients using SSL client authentication, and/or authenticate requests using HTTP Basic authentication as described below.

### SSL Identity [_ssl_identity_3]

In order to establish SSL with a client, this input plugin will need to present an SSL certificate that the client trusts, and have access to the associated key. These are configurable with [`ssl_certificate`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate), [`ssl_key`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key), and optionally [`ssl_key_passphrase`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key_passphrase).

### SSL Client Authentication [_ssl_client_authentication_3]

By default, this plugin does not request certificates from clients during SSL negotiation.

It can be configured to either request or require client certificates using [`ssl_client_authentication`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_client_authentication), which often also requires configuring it with a list of [`ssl_certificate_authorities`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate_authorities) to trust. When validating a certificate that is presented, [`ssl_verification_mode`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_verification_mode) controls how certificates are verified.

ESF does not currently support *presenting* client certificates, so requesting or requiring clients to present identity is only useful when combined with an SSL-terminating proxy.

### SSL Advanced Configuration [_ssl_advanced_configuration_3]

This plugin exposes several advanced SSL configurations:

* [`ssl_cipher_suites`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_cipher_suites)
* [`ssl_supported_protocols`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_supported_protocols)
* [`ssl_handshake_timeout`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_handshake_timeout)

### HTTP Basic Authentication [_http_basic_authentication_3]

You can configure this plugin to authenticate requests using HTTP Basic authentication by configuring [`auth_basic_username`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_username) and [`auth_basic_password`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_password).

Basic Authentication is not a substitute for SSL, as it provides neither secrecy nor security on its own. When used with SSL disabled, HTTP Basic credentials are transmitted in effectively clear-text and can be easily recovered by an adversary.

## Elastic Serverless Forwarder Input Configuration Options [v0.1.3-plugins-inputs-elastic_serverless_forwarder-options]

This plugin supports the following configuration options plus the [Common options](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`auth_basic_username`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_username) | [string](/lsr/value-types.md#string) | No |
| [`auth_basic_password`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_password) | [password](/lsr/value-types.md#password) | No |
| [`host`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-host) | [string](/lsr/value-types.md#string) | No |
| [`port`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-port) | [number](/lsr/value-types.md#number) | No |
| [`ssl`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`ssl_certificate`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_client_authentication`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_client_authentication) | [string](/lsr/value-types.md#string), one of `["none", "optional", "required"]` | No |
| [`ssl_cipher_suites`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_cipher_suites) | [array](/lsr/value-types.md#array) | No |
| [`ssl_enabled`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_enabled) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_handshake_timeout`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_handshake_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ssl_key`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_supported_protocols`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_supported_protocols) | [array](/lsr/value-types.md#array) | No |
| [`ssl_verification_mode`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_verification_mode) | [string](/lsr/value-types.md#string), one of `["certificate"]` | No |

Also see [Common options](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-common-options) for a list of options supported by all input plugins.

### `auth_basic_password` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password for HTTP basic authorization. Requires [`auth_basic_username`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_username).

### `auth_basic_username` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_username]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username for basic authorization. Requires [`auth_basic_password`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-auth_basic_password).

### `host` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"` (all available interfaces)

The host or ip to bind

### `port` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `8080`

The TCP port to bind to

### `ssl` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl]

Deprecated in 0.1.3.

Replaced by [`ssl_enabled`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_enabled)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Events are by default sent over SSL, which requires configuring this plugin to present an identity certificate using [`ssl_certificate`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate) and key using [`ssl_key`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key).

You can disable SSL with `+ssl => false+`.

### `ssl_certificate` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use. This certificate *MUST* be PEM-formatted, and *MAY* contain a chain of certificates starting with the certificate that identifies itself, followed by zero or more ordered intermediates optionally ending with the root signing authority. Providing a complete chain allows clients to trust our certificate if their configuration allows them to trust one of our intermediates.

### `ssl_certificate_authorities` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store.

If you wish to perform client authentication, you need to set `ssl_client_authentication` to `optional` or `required`.

### `ssl_cipher_suites` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_cipher_suites]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `['TLS_AES_256_GCM_SHA384', 'TLS_AES_128_GCM_SHA256', 'TLS_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256']`

The list of cipher suites to use, listed by priorities.

This is an advanced SSL configuration.

This default list applies for OpenJDK 11.0.14 and higher. For older JDK versions, the default list includes only suites supported by that version. For example, the ChaCha20 family of ciphers is not supported in older versions.

### `ssl_client_authentication` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_client_authentication]

* Value can be any of:

  * `none`: do not request client’s certificate, or validate certificates that are presented
  * `optional`: request client’s certificate, and validate it against our trust authorities *if-and-only-if* it is presented
  * `required`: require a valid certificate from the client that is signed by a trusted certificate authority

* Default value is `"none"`

By default the server doesn’t do any client authentication. This means that connections from clients are *private* when SSL is enabled, but that this input will allow SSL connections from *any* client. If you wish to configure this plugin to reject connections from untrusted hosts, you will need to configure this plugin to authenticate clients, and may also need to configure it with a list of `ssl_certificate_authorities`.

### `ssl_enabled` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Events are, by default, sent over SSL, which requires configuring this plugin to present an identity certificate using [`ssl_certificate`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_certificate) and key using [`ssl_key`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key).

You can disable SSL with `+ssl_enabled => false+`.

### `ssl_handshake_timeout` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_handshake_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout

This is an advanced SSL configuration.

### `ssl_key` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key to use.

This key need to be in the PKCS8 format, you can convert it with [OpenSSL](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs8.html) for more information.

### `ssl_key_passphrase` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

SSL key passphrase to use.

### `ssl_supported_protocols` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_supported_protocols]

* Value type is [array](/lsr/value-types.md#array)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the HTTP endpoint.

This is an advanced SSL configuration.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_verification_mode` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_verification_mode]

* Value type is [string](/lsr/value-types.md#string)

* There is only one currently-supported mode:

  * `certificate`: verifies that a certificate provided by the client is signed by a trusted authority (CA), is within its valid date range, and that the client has possession of the associated key, but does *not* perform hostname validation.

- The default value is `certificate`.

When [`ssl_client_authentication`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-ssl_client_authentication) causes a client to present a certificate, this setting controls how that certificate is verified.

Client identity is not typically validated using SSL because the receiving server only has access to the client’s outbound-ip, which is not always constant and is frequently not represented in the certificate’s subject or subjectAltNames extensions. For more information, see [RFC2818 § 3.2 (HTTP over TLS—Client Identity)](https://www.rfc-editor.org/rfc/rfc2818#section-3.1)

## Common options [v0.1.3-plugins-inputs-elastic_serverless_forwarder-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`enable_metric`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v0-1-3-plugins-inputs-elastic_serverless_forwarder.md#v0.1.3-plugins-inputs-elastic_serverless_forwarder-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `enable_metric` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elastic\_serverless\_forwarder inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  elastic_serverless_forwarder {
    id => "my_plugin_id"
  }
}
```

### `tags` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v0.1.3-plugins-inputs-elastic_serverless_forwarder-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
