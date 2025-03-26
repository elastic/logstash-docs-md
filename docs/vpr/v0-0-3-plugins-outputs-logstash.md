---
navigation_title: "v0.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.0.3-plugins-outputs-logstash.html
---

# Logstash output plugin v0.0.3 [v0.0.3-plugins-outputs-logstash]


* A component of the [logstash integration plugin](integration-logstash-index.md)
* Integration version: v0.0.3
* Released on: 2023-09-29
* [Changelog](https://github.com/logstash-plugins/logstash-integration-logstash/blob/v0.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-logstash-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1427]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-logstash). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1417]

Send events to a [logstash input plugin](/lsr/plugins-inputs-logstash.md) in a pipeline that may be in another process or on another host. You must have a TCP route to the port on an interface that the downstream input is bound to.

::::{note}
Sending events to *any* destination other than [logstash input plugin](/lsr/plugins-inputs-logstash.md) is neither advised nor supported. We will maintain cross-compatibility with any two supported versions of output/input pair and reserve the right to change details such as protocol and encoding.
::::


### Minimum Configuration [v0.0.3-plugins-outputs-logstash-minimum-config]

| SSL Enabled | SSL Disabled |
| --- | --- |
| ```shell<br>output {<br>  logstash {<br>    host => "10.0.0.123"<br>    port => 8080<br>  }<br>}<br>```<br> | ```shell<br>output {<br>  logstash {<br>    host => "10.0.0.123"<br>    port => 8080<br>    ssl_enabled<br>         => false<br>  }<br>}<br>```<br> |


### Configuration Concepts [v0.0.3-plugins-outputs-logstash-config-connecting]

This output plugin needs to be configured to connect to a [logstash input plugin](/lsr/plugins-inputs-logstash.md) by specifying its [`host`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-host) and [`port`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-port). Depending on the downstream plugin’s configuration, you may need to also configure SSL and/or credentials.


### Security: SSL Trust [v0.0.3-plugins-outputs-logstash-config-ssl-trust]

When communicating over SSL, this plugin establishes trust of the server it connects to before transmitting credentials or events.

It does so by ensuring that the server presents a currently-valid certificate with identity claims matching the [`host`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-host) we are configured to connect to, signed by a trusted signing authority, along with proof-of-possession of the associated private key material.

The system trust store is used by default. You can provide an *alternate* source of trust with *ONE OF*:

* A PEM-formatted list of trusted certificate authorities (see [`ssl_certificate_authorities`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_certificate_authorities))
* A PKCS12- or JKS-formatted truststore (see [`ssl_truststore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_path))


### Security: SSL Identity [v0.0.3-plugins-outputs-logstash-config-ssl-identity]

If the downstream input plugin is configured to request or require client authentication, you can configure this plugin to provide its proof-of-identity with *ONE OF*:

* JKS- or PKCS12-formatted Keystore (see [`ssl_keystore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_path))
* PKCS8-formatted Certificate/Key pair (see [`ssl_certificate`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_certificate))


### Security: Credentials [v0.0.3-plugins-outputs-logstash-config-credentials]

If the downstream [logstash input plugin](/lsr/plugins-inputs-logstash.md) is configured to require [`username`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-username) and [`password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-password), you will need to configure this output with a matching [`username`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-username) and [`password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-password).

::::{note}
when SSL is disabled, data and credentials will be transmitted in clear-text.
::::




## Logstash Output Configuration Options [v0.0.3-plugins-outputs-logstash-options]

This plugin supports the following configuration options plus the [Common options](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-host) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-port) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`ssl_enabled`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_certificate`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_certificate) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_certificate_authorities`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_certificate_authorities) | list of [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_key`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_key) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_truststore_password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verification_mode`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_verification_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["full", "none"]` | No |
| [`username`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-common-options) for a list of options supported by all output plugins.

 

### `host` [v0.0.3-plugins-outputs-logstash-host]

* Value type is a [string](logstash://reference/configuration-file-structure.md#string) ip address or hostname
* There is no default value

Specify which host to connect to by providing its ip address or resolvable hostname.

::::{note}
when using SSL, the server that responds must present a certificated with identity claim matching this host name or ip address.
::::



### `port` [v0.0.3-plugins-outputs-logstash-port]

* Value type is a [number](logstash://reference/configuration-file-structure.md#number) port
* There is no default value

Specify which port to connect to.


### `password` [v0.0.3-plugins-outputs-logstash-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when [`username`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-username) is configured.

Password for password-based authentication.

When the downstream input plugin is configured with a `username` and `password`, you must also configure upstream outputs with a matching `username`/`password` pair.


### `ssl_enabled` [v0.0.3-plugins-outputs-logstash-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Logstash-to-Logstash communication is secured by default. When the downstream input plugin disables SSL, it must also be disabled here.

You can disable SSL with `+ssl_enabled => false+`. When disabled, setting any `ssl_*` configuration causes configuration failure.


### `ssl_certificate` [v0.0.3-plugins-outputs-logstash-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_key`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_key) is also required.
* Cannot be combined with configurations that disable SSL.

Path to a PEM-encoded certificate or certificate chain with which to identify this plugin to connecting downstream input.


### `ssl_certificate_authorities` [v0.0.3-plugins-outputs-logstash-ssl_certificate_authorities]

* Value type is a [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* Cannot be combined with configurations that disable SSL.
* Cannot be combined with [`+ssl_verification_mode => none+`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_verification_mode).

One or more PEM-encoded files defining certificate authorities for use in downstream input authentication. This setting can be used to *override* the system trust store for verifying the SSL certificate presented by downstream input.


### `ssl_key` [v0.0.3-plugins-outputs-logstash-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_certificate)
* Cannot be combined with configurations that disable SSL.

A path to an PEM-encoded *unencrypted* PKCS8 SSL certificate key.


### `ssl_keystore_path` [v0.0.3-plugins-outputs-logstash-ssl_keystore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_keystore_password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_password) is also required.
* Cannot be combined with configurations that disable SSL.

A path to a JKS- or PKCS12-formatted keystore with which to identify this plugin to the downstream input. The provided identity will be used if the downstream input enables [SSL client authentication](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-config-ssl-trust).


### `ssl_keystore_password` [v0.0.3-plugins-outputs-logstash-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_keystore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_path)
* Cannot be combined with configurations that disable SSL.

Password for the [`ssl_keystore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_keystore_path)


### `ssl_truststore_path` [v0.0.3-plugins-outputs-logstash-ssl_truststore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_truststore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_path) is also required.
* Cannot be combined with configurations that disable SSL.
* Cannot be combined with [`+ssl_verification_mode => none+`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_verification_mode).

A path to a JKS- or PKCS12-formatted truststore with which to validate the identity claims of the downstream input. The provided identity will be used if the downstream input enables [SSL client authentication](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-config-ssl-trust).


### `ssl_truststore_password` [v0.0.3-plugins-outputs-logstash-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_truststore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_path)
* Cannot be combined with configurations that disable SSL.

Password for the [`ssl_truststore_path`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-ssl_truststore_path)


### `ssl_verification_mode` [v0.0.3-plugins-outputs-logstash-ssl_verification_mode]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* The supported modes are:

    * `full`: verifies that a certificate provided by the client has an identity claim matching [`host`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-host), is signed by a trusted authority (CA), is within its valid date range, and that the client has possession of the associated key.
    * `none`: performs no validation of the presented certificate

* The default value is `full`.
* Cannot be combined with configurations that disable SSL.

When communicating over SSL, this setting controls how the downstream input’s certificate is verified.


### `username` [v0.0.3-plugins-outputs-logstash-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.
* When present, [`password`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-password) is also required.

Username for password-based authentication.

When the downstream input plugin is configured with a `username` and `password`, you must also configure upstream outputs with a matching `username`/`password` pair.

::::{note}
when SSL is disabled, credentials will be transmitted in clear-text.
::::




## Common options [v0.0.3-plugins-outputs-logstash-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`enable_metric`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v0-0-3-plugins-outputs-logstash.md#v0.0.3-plugins-outputs-logstash-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `enable_metric` [v0.0.3-plugins-outputs-logstash-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v0.0.3-plugins-outputs-logstash-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 logstash outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  logstash {
    id => "my_plugin_id"
  }
}
```



