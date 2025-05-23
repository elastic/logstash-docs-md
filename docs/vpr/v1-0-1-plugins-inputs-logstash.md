---
navigation_title: "v1.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.1-plugins-inputs-logstash.html
---

# Logstash input plugin v1.0.1 [v1.0.1-plugins-inputs-logstash]


* A component of the [logstash integration plugin](integration-logstash-index.md)
* Integration version: v1.0.1
* Released on: 2023-11-16
* [Changelog](https://github.com/logstash-plugins/logstash-integration-logstash/blob/v1.0.1/CHANGELOG.md)

For other versions, see the [overview list](input-logstash-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_706]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-logstash). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_699]

Listen for events that are sent by a [Logstash output plugin](/lsr/plugins-outputs-logstash.md) in a pipeline that may be in another process or on another host. The upstream output must have a TCP route to the port (defaults to 9800) on an interface that this plugin is bound to.

::::{note}
Sending events to this input by *any* means other than `plugins-outputs-logstash` is neither advised nor supported. We will maintain cross-compatibility with any two supported versions of output/input pair and reserve the right to change details such as protocol and encoding.
::::


### Minimum Configuration [v1.0.1-plugins-inputs-logstash-minimum-config]

#### SSL Enabled

```shell
input {
  logstash {
    ssl_keystore_path
         => "/path/to/logstash.p12"
    ssl_keystore_password
         => "${PASS}"
  }
}
```

#### SSL Disabled

```shell
input {
  logstash {
    ssl_enabled => false
  }
}
```


### Configuration Concepts [v1.0.1-plugins-inputs-logstash-config-binding]

This input plugin needs to be configured to bind to a TCP [`port`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-port), and can be constrained to bind to a particular interface by providing the IP to [`host`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-host).


### Security: SSL Identity [v1.0.1-plugins-inputs-logstash-config-ssl-identity]

Unless SSL is disabled, this plugin needs to be configured with identity material:

* JKS- or PKCS12-formatted Keystore (see [`ssl_keystore_path`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_path))
* PKCS8-formatted Certificate/Key pair (see [`ssl_certificate`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate))


### Security: SSL Trust [v1.0.1-plugins-inputs-logstash-config-ssl-trust]

When communicating over SSL, this plugin can be configured to either request or require that connecting clients present their own identity claims with [`ssl_client_authentication`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_client_authentication).

Certificates that are presented by clients are validated by default using the system trust store to ensure that they are currently-valid and trusted, and that the client can prove possession of its associated private key. You can provide an *alternate* source of trust with:

* A PEM-formatted list of trusted certificate authorities (see [`ssl_certificate_authorities`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate_authorities))

::::{note}
Client-certificate verification does *not* verify identity claims on the presented certificate, such as whether the certificate includes a Subject Alt Name matching the IP address from which the client is connecting.
::::



### Security: Credentials [v1.0.1-plugins-inputs-logstash-config-credentials]

You can also configure this plugin to require a specific username/password be provided by configuring [`username`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-username) and [`password`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-password). Doing so requires connecting `logstash-output` plugin clients to provide matching `username` and `password`.

::::{note}
when SSL is disabled, data and credentials will be received in clear-text.
::::




## Logstash Input Configuration Options [v1.0.1-plugins-inputs-logstash-options]

This plugin supports the following configuration options plus the [Common options](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`host`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`port`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_certificate`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_certificate_authorities`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate_authorities) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_client_authentication`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_client_authentication) | [string](logstash://reference/configuration-file-structure.md#string), one of `["none", "optional", "required"]` | No |
| [`ssl_enabled`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_key) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_password`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_path`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_key_passphrase`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`username`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-common-options) for a list of options supported by all input plugins.

 

### `host` [v1.0.1-plugins-inputs-logstash-host]

* Value type is a [string](logstash://reference/configuration-file-structure.md#string) ip address
* Default value is `0.0.0.0` (all interfaces)

Specify which interface to listen on by providing its ip address. By default, this input listens on all available interfaces.


### `password` [v1.0.1-plugins-inputs-logstash-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password for password-based authentication. Requires [`username`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-username).


### `port` [v1.0.1-plugins-inputs-logstash-port]

* Value type is a [number](logstash://reference/configuration-file-structure.md#number) port
* Default value is 9800

Specify which port to listen on.


### `ssl_certificate` [v1.0.1-plugins-inputs-logstash-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_key`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_key) and [`ssl_key_passphrase`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_key_passphrase) are also required.
* Cannot be combined with configurations that disable SSL.

Path to a PEM-encoded certificate or certificate chain with which to identify this plugin to connecting clients. The certificate *SHOULD* include identity claims about the ip address or hostname that clients use to establish a connection.


### `ssl_certificate_authorities` [v1.0.1-plugins-inputs-logstash-ssl_certificate_authorities]

* Value type is a list of [path](logstash://reference/configuration-file-structure.md#path)s
* There is no default value for this setting.
* Cannot be combined with configurations that disable SSL.
* Cannot be combined with [`+ssl_client_authentication => none+`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_client_authentication).

One or more PEM-encoded files defining certificate authorities for use in client authentication. This setting can be used to *override* the system trust store for verifying the SSL certificate presented by clients.


### `ssl_client_authentication` [v1.0.1-plugins-inputs-logstash-ssl_client_authentication]

* Value can be any of:

    * `none`: do not request client’s certificate, or validate certificates that are presented
    * `optional`: request client’s certificate, and validate it against our trust authorities *if-and-only-if* it is presented
    * `required`: require a valid certificate from the client that is signed by a trusted certificate authority

* Default value is `"none"`

By default the server doesn’t do any client authentication. This means that connections from clients are *private* when SSL is enabled, but that this input will allow SSL connections from *any* client. If you wish to configure this plugin to reject connections from untrusted hosts, you will need to configure this plugin to authenticate clients, and may also need to configure its [source of trust](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-config-ssl-trust).


### `ssl_enabled` [v1.0.1-plugins-inputs-logstash-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

SSL is enabled by default, which requires configuring this plugin to present its [identity](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-config-ssl-identity).

You can disable SSL with `+ssl_enabled => false+`. When disabled, setting any `ssl_*` configuration causes configuration failure.


### `ssl_key` [v1.0.1-plugins-inputs-logstash-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate).
* Cannot be combined with configurations that disable SSL.

A path to a PEM-encoded *encrypted* PKCS8 SSL certificate key.


### `ssl_keystore_password` [v1.0.1-plugins-inputs-logstash-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_keystore_path`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_path).
* Cannot be combined with configurations that disable SSL.

Password for the [`ssl_keystore_path`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_path)


### `ssl_keystore_path` [v1.0.1-plugins-inputs-logstash-ssl_keystore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_keystore_password`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_keystore_password) is also required.
* Cannot be combined with configurations that disable SSL.

A path to a JKS- or PKCS12-formatted keystore with which to identify this plugin to {{es}}.


### `ssl_key_passphrase` [v1.0.1-plugins-inputs-logstash-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_certificate).
* Cannot be combined with configurations that disable SSL.

A password or passphrase of the [`ssl_key`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-ssl_key).


### `username` [v1.0.1-plugins-inputs-logstash-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username for password-based authentication. When this input plugin is configured with a `username`, it also requires a `password`, and any upstream `logstash-output` plugin must also be configured with a matching `username`/`password` pair.

::::{note}
when SSL is disabled, credentials will be transmitted in clear-text.
::::




## Common options [v1.0.1-plugins-inputs-logstash-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`enable_metric`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v1-0-1-plugins-inputs-logstash.md#v1.0.1-plugins-inputs-logstash-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v1.0.1-plugins-inputs-logstash-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `enable_metric` [v1.0.1-plugins-inputs-logstash-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.1-plugins-inputs-logstash-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 logstash inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  logstash {
    id => "my_plugin_id"
  }
}
```


### `tags` [v1.0.1-plugins-inputs-logstash-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v1.0.1-plugins-inputs-logstash-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



