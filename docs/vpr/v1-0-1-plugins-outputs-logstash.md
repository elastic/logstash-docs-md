---
navigation_title: "v1.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.1-plugins-outputs-logstash.html
---

# Logstash output plugin v1.0.1 [v1.0.1-plugins-outputs-logstash]

* A component of the [logstash integration plugin](integration-logstash-index.md)
* Integration version: v1.0.1
* Released on: 2023-11-16
* [Changelog](https://github.com/logstash-plugins/logstash-integration-logstash/blob/v1.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-logstash-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1434]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-logstash). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1424]

Send events to a [Logstash input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-logstash.html) in a pipeline that may be in another process or on another host. You must have a TCP route to the port (defaults to 9800) on an interface that the downstream input is bound to.

Sending events to *any* destination other than a `logstash-input` plugin is neither advised nor supported. We will maintain cross-compatibility with any two supported versions of output/input pair and reserve the right to change details such as protocol and encoding.

### Minimum Configuration [v1.0.1-plugins-outputs-logstash-minimum-config]

| SSL Enabled | SSL Disabled |
| :- | :- |
| output {<br> logstash {<br> hosts => "10.0.0.123:9801"<br> }<br>} | output {<br> logstash {<br> hosts => "10.0.0.123:9801"<br> ssl\_enabled<br> => false<br> }<br>} |

### Configuration Concepts [v1.0.1-plugins-outputs-logstash-config-connecting]

Configure this output plugin to connect to a [Logstash input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-logstash.html) by specifying its `hosts`. Depending on the downstream plugin’s configuration, you may need to also configure the target port, SSL, and/or credentials.

### Security: SSL Trust [v1.0.1-plugins-outputs-logstash-config-ssl-trust]

When communicating over SSL, this plugin establishes trust of the server it connects to before transmitting credentials or events.

It does so by ensuring that the responding server presents a currently-valid certificate with identity claims matching host it is connecting to, signed by a trusted signing authority, along with proof-of-possession of the associated private key material.

The system trust store is used by default. You can provide an *alternate* source of trust with *ONE OF*:

* A PEM-formatted list of trusted certificate authorities (see [`ssl_certificate_authorities`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_certificate_authorities))
* A PKCS12- or JKS-formatted truststore (see [`ssl_truststore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_path))

### Security: SSL Identity [v1.0.1-plugins-outputs-logstash-config-ssl-identity]

If the downstream input plugin is configured to request or require client authentication, you can configure this plugin to provide its proof-of-identity with *ONE OF*:

* JKS- or PKCS12-formatted Keystore (see [`ssl_keystore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_path))
* PKCS8-formatted Certificate/Key pair (see [`ssl_certificate`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_certificate))

### Security: Credentials [v1.0.1-plugins-outputs-logstash-config-credentials]

If the downstream `logstash-input` plugin is configured to require `username` and `password`, you will need to configure this output with a matching [`username`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-username) and [`password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-password).

when SSL is disabled, data and credentials will be transmitted in clear-text.

## Logstash Output Configuration Options [v1.0.1-plugins-outputs-logstash-options]

This plugin supports the following configuration options plus the [Common options](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`hosts`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-hosts) | list of [string](/lsr/value-types.md#string) | Yes |
| [`password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_enabled`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_enabled) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_certificate`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_certificate) | [path](/lsr/value-types.md#path) | No |
| [`ssl_certificate_authorities`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_certificate_authorities) | list of [path](/lsr/value-types.md#path) | No |
| [`ssl_key`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_key) | [path](/lsr/value-types.md#path) | No |
| [`ssl_keystore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_path) | [path](/lsr/value-types.md#path) | No |
| [`ssl_keystore_password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_truststore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_path) | [path](/lsr/value-types.md#path) | No |
| [`ssl_truststore_password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_verification_mode`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_verification_mode) | [string](/lsr/value-types.md#string), one of `["full", "none"]` | No |
| [`username`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-username) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-common-options) for a list of options supported by all output plugins.

### `hosts` [v1.0.1-plugins-outputs-logstash-hosts]

* Value type is list of [string](/lsr/value-types.md#string)

* There is no default value for this setting.

* Constraints:

  * When using IPv6, IP address must be in an enclosed in brackets.
  * When a port is not provided, the default `9800` is used.

The addresses of one or more downstream \`input\`s to connect to.

Host can be any of IPv4, IPv6 (in enclosed bracket) or host name, examples:

* `"127.0.0.1"`
* `"127.0.0.1:9801"`
* `"ds.example.com"`
* `"ds.example.com:9802"`
* `"[::1]"`
* `"[::1]:9803"`
* `"[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"`
* `"[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:9804"`

Plugin balances incoming load among the `hosts`. For more information, visit [Logstash integration plugin](https://www.elastic.co/guide/en/logstash/current/plugins-integrations-logstash.html) *Load Balancing* section.

When connecting, communication to downstream input Logstash is secured with SSL unless configured otherwise.

Disabling SSL is dangerous

The security of this plugin relies on SSL to avoid leaking credentials and to avoid running illegitimate ingest pipeline definitions.

when using SSL, the server that responds must present a certificated with identity claim matching this host name or ip address.

### `password` [v1.0.1-plugins-outputs-logstash-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.
* Required when [`username`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-username) is configured.

Password for password-based authentication.

When the downstream input plugin is configured with a `username` and `password`, you must also configure upstream outputs with a matching `username`/`password` pair.

### `ssl_enabled` [v1.0.1-plugins-outputs-logstash-ssl_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Logstash-to-Logstash communication is secured by default. When the downstream input plugin disables SSL, it must also be disabled here.

You can disable SSL with `+ssl_enabled => false+`. When disabled, setting any `ssl_*` configuration causes configuration failure.

### `ssl_certificate` [v1.0.1-plugins-outputs-logstash-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* When present, [`ssl_key`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_key) is also required.
* Cannot be combined with configurations that disable SSL.

Path to a PEM-encoded certificate or certificate chain with which to identify this plugin to connecting downstream input.

### `ssl_certificate_authorities` [v1.0.1-plugins-outputs-logstash-ssl_certificate_authorities]

* Value type is a [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* Cannot be combined with configurations that disable SSL.
* Cannot be combined with [`+ssl_verification_mode => none+`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_verification_mode).

One or more PEM-encoded files defining certificate authorities for use in downstream input authentication. This setting can be used to *override* the system trust store for verifying the SSL certificate presented by downstream input.

### `ssl_key` [v1.0.1-plugins-outputs-logstash-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_certificate)
* Cannot be combined with configurations that disable SSL.

A path to an PEM-encoded *unencrypted* PKCS8 SSL certificate key.

### `ssl_keystore_path` [v1.0.1-plugins-outputs-logstash-ssl_keystore_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* When present, [`ssl_keystore_password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_password) is also required.
* Cannot be combined with configurations that disable SSL.

A path to a JKS- or PKCS12-formatted keystore with which to identify this plugin to the downstream input. The provided identity will be used if the downstream input enables [SSL client authentication](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-config-ssl-trust).

### `ssl_keystore_password` [v1.0.1-plugins-outputs-logstash-ssl_keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_keystore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_path)
* Cannot be combined with configurations that disable SSL.

Password for the [`ssl_keystore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_keystore_path)

### `ssl_truststore_path` [v1.0.1-plugins-outputs-logstash-ssl_truststore_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.
* When present, [`ssl_truststore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_path) is also required.
* Cannot be combined with configurations that disable SSL.
* Cannot be combined with [`+ssl_verification_mode => none+`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_verification_mode).

A path to a JKS- or PKCS12-formatted truststore with which to validate the identity claims of the downstream input. The provided identity will be used if the downstream input enables [SSL client authentication](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-config-ssl-trust).

### `ssl_truststore_password` [v1.0.1-plugins-outputs-logstash-ssl_truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_truststore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_path)
* Cannot be combined with configurations that disable SSL.

Password for the [`ssl_truststore_path`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-ssl_truststore_path)

### `ssl_verification_mode` [v1.0.1-plugins-outputs-logstash-ssl_verification_mode]

* Value type is [string](/lsr/value-types.md#string)

* The supported modes are:

  * `full`: verifies that a certificate provided by the client has an identity claim matching [`hosts`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-hosts), is signed by a trusted authority (CA), is within its valid date range, and that the client has possession of the associated key.
  * `none`: performs no validation of the presented certificate

* The default value is `full`.

* Cannot be combined with configurations that disable SSL.

When communicating over SSL, this setting controls how the downstream input’s certificate is verified.

### `username` [v1.0.1-plugins-outputs-logstash-username]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* When present, [`password`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-password) is also required.

Username for password-based authentication.

When the downstream input plugin is configured with a `username` and `password`, you must also configure upstream outputs with a matching `username`/`password` pair.

when SSL is disabled, credentials will be transmitted in clear-text.

## Common options [v1.0.1-plugins-outputs-logstash-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`enable_metric`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-1-plugins-outputs-logstash.md#v1.0.1-plugins-outputs-logstash-id) | [string](/lsr/value-types.md#string) | No |

### `enable_metric` [v1.0.1-plugins-outputs-logstash-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.1-plugins-outputs-logstash-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 logstash outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  logstash {
    id => "my_plugin_id"
  }
}
```
