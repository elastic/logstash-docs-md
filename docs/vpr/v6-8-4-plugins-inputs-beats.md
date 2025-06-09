---
navigation_title: "v6.8.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.8.4-plugins-inputs-beats.html
---

# Beats input plugin v6.8.4 [v6.8.4-plugins-inputs-beats]

The `input-elastic_agent` plugin is the next generation of the `input-beats` plugin. They currently share code and a [common codebase](https://github.com/logstash-plugins/logstash-input-beats).

* Plugin version: v6.8.4
* Released on: 2024-08-28
* [Changelog](https://github.com/logstash-plugins/logstash-input-beats/blob/v6.8.4/CHANGELOG.md)

For other versions, see the [overview list](input-beats-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_172]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-beats). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_172]

This input plugin enables Logstash to receive events from the Beats framework.

The following example shows how to configure Logstash to listen on port 5044 for incoming Beats connections and to index into Elasticsearch.

```
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

1. `%{[@metadata][beat]}` sets the first part of the index name to the value of the metadata field and `%{[@metadata][version]}` sets the second part to the Beat version. For example: metricbeat-6.1.6.

Events indexed into Elasticsearch with the Logstash configuration shown here will be similar to events directly indexed by Beats into Elasticsearch.

If ILM is not being used, set `index` to `%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}` instead so Logstash creates an index per day, based on the `@timestamp` value of the events coming from Beats.

### Memory usage [v6.8.4-plugins-inputs-beats-memory]

This plugin uses "off-heap" direct memory in addition to heap memory. By default, a JVM’s off-heap direct memory limit is the same as the heap size. For example, setting `-Xmx10G` without setting the direct memory limit will allocate `10GB` for heap and an additional `10GB` for direct memory, for a total of `20GB` allocated. You can set the amount of direct memory with `-XX:MaxDirectMemorySize` in [Logstash JVM Settings](https://www.elastic.co/guide/en/logstash/current/jvm-settings.html). Consider setting direct memory to half of the heap size. Setting direct memory too low decreases the performance of ingestion.

Be sure that heap and direct memory combined does not exceed the total memory available on the server to avoid an OutOfDirectMemoryError

### Multi-line events [v6.8.4-plugins-inputs-beats-multiline]

If you are shipping events that span multiple lines, you need to use the [configuration options available in Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html) to handle multiline events before sending the event data to Logstash. You cannot use the [Multiline codec plugin](https://www.elastic.co/guide/en/logstash/current/plugins-codecs-multiline.html) to handle multiline events. Doing so will result in the failure to start Logstash.

## Versioned indices [v6.8.4-plugins-inputs-beats-versioned-indexes]

To minimize the impact of future schema changes on your existing indices and mappings in Elasticsearch, configure the Elasticsearch output to write to versioned indices. The pattern that you specify for the `index` setting controls the index name:

```
index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
```

* `%{[@metadata][beat]}`

  Sets the first part of the index name to the value of the `beat` metadata field, for example, `filebeat`.

* `%{[@metadata][version]}`

  Sets the second part of the name to the Beat version, for example, `{logstash_version}`.

* `%{+YYYY.MM.dd}`

  Sets the third part of the name to a date based on the Logstash `@timestamp` field.

This configuration results in daily index names like `filebeat-{logstash_version}-2025-06-03`.

## Event enrichment and the Elastic Common Schema (ECS) [v6.8.4-plugins-inputs-beats-ecs_metadata]

When decoding Beats events, this plugin enriches each event with metadata about the event’s source, making this information available during further processing. You can use the [`enrich`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-enrich) option to activate or deactivate individual enrichment categories.

The location of these enrichment fields depends on whether [ECS compatibility mode](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ecs_compatibility) is enabled:

* When ECS compatibility is *enabled*, enrichment fields are added in an ECS-compatible structure.
* When ECS compatibility is *disabled*, enrichment fields are added in a way that is backward-compatible with this plugin, but is known to clash with the Elastic Common Schema.

**Enrichment category:`source_metadata`**

| ECS \`v1\`, \`v8\` | ECS \`disabled\` | Description |
| :- | :- | :- |
| \[@metadata]\[input]\[beats]\[host]\[name] | \[host] | *Name or address of the Beat host* |
| \[@metadata]\[input]\[beats]\[host]\[ip] | \[@metadata]\[ip\_address] | *IP address of the Beats client that connected to this input* |

**Enrichment category:`ssl_peer_metadata`**

| ECS \`v1\`, \`v8\` | ECS \`disabled\` | Description |
| :- | :- | :- |
| \[@metadata]\[tls\_peer]\[status] | \[@metadata]\[tls\_peer]\[status] | *Contains "verified" or "unverified" label; available when SSL is enabled.* |
| \[@metadata]\[input]\[beats]\[tls]\[version\_protocol] | \[@metadata]\[tls\_peer]\[protocol] | *Contains the TLS version used (such as `TLSv1.2`); available when SSL status is "verified"* |
| \[@metadata]\[input]\[beats]\[tls]\[client]\[subject] | \[@metadata]\[tls\_peer]\[subject] | *Contains the identity name of the remote end (such as `CN=artifacts-no-kpi.elastic.co`); available when SSL status is "verified"* |
| \[@metadata]\[input]\[beats]\[tls]\[cipher] | \[@metadata]\[tls\_peer]\[cipher\_suite] | *Contains the name of cipher suite used (such as `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`); available when SSL status is "verified"* |

**Enrichment category:`codec_metadata`**

| ECS \`v1\`, \`v8\` | ECS \`disabled\` | Description |
| :- | :- | :- |
| \[tag] | \[tag] | *Contains `beats_input_codec_XXX_applied` where `XXX` is the name of the codec* |
| \[event]\[original] | *N/A* | *When ECS is enabled, even if `[event][original]` field does not already exist on the event being processed, this plugin’s **default codec** ensures that the field is populated using the bytes as-processed.* |

## Beats input configuration options [v6.8.4-plugins-inputs-beats-options]

This plugin supports the following configuration options plus the [Common options](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_hostname`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-add_hostname) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`cipher_suites`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-cipher_suites) | [array](/lsr/value-types.md#array) | *Deprecated* |
| [`client_inactivity_timeout`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-client_inactivity_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ecs_compatibility`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`enrich`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-enrich) | [string](/lsr/value-types.md#string) | No |
| [`event_loop_threads`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-event_loop_threads) | [number](/lsr/value-types.md#number) | No |
| [`executor_threads`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-executor_threads) | [number](/lsr/value-types.md#number) | No |
| [`host`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-host) | [string](/lsr/value-types.md#string) | No |
| [`include_codec_tag`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-include_codec_tag) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`port`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-port) | [number](/lsr/value-types.md#number) | Yes |
| [`ssl`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`ssl_certificate`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate) | a valid filesystem path | No |
| [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) | [array](/lsr/value-types.md#array) | No |
| [`ssl_cipher_suites`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_cipher_suites) | [array](/lsr/value-types.md#array) | No |
| [`ssl_client_authentication`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_client_authentication) | [string](/lsr/value-types.md#string), one of `["none", "optional", "required"]` | No |
| [`ssl_enabled`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_enabled) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_handshake_timeout`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_handshake_timeout) | [number](/lsr/value-types.md#number) | No |
| [`ssl_key`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_key) | a valid filesystem path | No |
| [`ssl_key_passphrase`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_key_passphrase) | [password](/lsr/value-types.md#password) | No |
| [`ssl_peer_metadata`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_peer_metadata) | [boolean](/lsr/value-types.md#boolean) | *Deprecated* |
| [`ssl_supported_protocols`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_supported_protocols) | [array](/lsr/value-types.md#array) | No |
| [`ssl_verify_mode`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_verify_mode) | [string](/lsr/value-types.md#string), one of `["none", "peer", "force_peer"]` | *Deprecated* |
| [`tls_max_version`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-tls_max_version) | [number](/lsr/value-types.md#number) | *Deprecated* |
| [`tls_min_version`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-tls_min_version) | [number](/lsr/value-types.md#number) | *Deprecated* |

Also see [Common options](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-common-options) for a list of options supported by all input plugins.

### `add_hostname` [v6.8.4-plugins-inputs-beats-add_hostname]

Deprecated in 6.0.0.

The default value has been changed to `false`. In 7.0.0 this setting will be removed

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Flag to determine whether to add `host` field to event using the value supplied by the Beat in the `hostname` field.

### `cipher_suites` [v6.8.4-plugins-inputs-beats-cipher_suites]

Deprecated in 6.4.0.

Replaced by [`ssl_cipher_suites`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_cipher_suites)

* Value type is [array](/lsr/value-types.md#array)

The list of cipher suites to use, listed by priorities.

### `client_inactivity_timeout` [v6.8.4-plugins-inputs-beats-client_inactivity_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Close Idle clients after X seconds of inactivity.

### `ecs_compatibility` [v6.8.4-plugins-inputs-beats-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: unstructured connection metadata added at root level
  * `v1`: structured connection metadata added under ECS v1 compliant namespaces
  * `v8`: structured connection metadata added under ECS v8 compliant namespaces

* Default value depends on which version of Logstash is running:

  * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
  * Otherwise, the default value is `disabled`.

Refer to [ECS mapping](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ecs_metadata) for detailed information.

### `enrich` [v6.8.4-plugins-inputs-beats-enrich]

* Value type is [string](/lsr/value-types.md#string)

  * An [array](/lsr/value-types.md#array) can also be provided

  * Configures which enrichments are applied to each event

  * Default value is `[codec_metadata, source_metadata]` that may be extended in future versions of this plugin to include additional enrichments.

  * Supported values are:

    | Enrichment | Description |
    | :- | :- |
    | codec\_metadata | Information about how the codec transformed a sequence of bytes into this Event, such as *which* codec was used. Also, if no codec is explicitly specified, *excluding* `codec_metadata` from `enrich` will disable `ecs_compatibility` for this plugin. |
    | source\_metadata | Information about the *source* of the event, such as the IP address of the inbound connection this input received the event from |
    | ssl\_peer\_metadata | Detailed information about the *SSL peer* we received the event from, such as identity information from the SSL client certificate that was presented when establishing a connection to this input |
    | all | *alias* to include *all* available enrichments (including additional enrichments introduced in future versions of this plugin) |
    | none | *alias* to *exclude* all available enrichments. Note that, *explicitly* defining codec with this option will not disable the `ecs_compatibility`, instead it relies on pipeline or codec `ecs_compatibility` configuration. |

**Example:**

This configuration disables *all* enrichments:

```
input {
  beats {
    port => 5044
    enrich => none
  }
}
```

Or, to explicitly enable *only* `source_metadata` and `ssl_peer_metadata` (disabling all others):

```
input {
  beats {
    port => 5044
    enrich => [source_metadata, ssl_peer_metadata]
  }
}
```

### `event_loop_threads` [v6.8.4-plugins-inputs-beats-event_loop_threads]

* Value type is [number](/lsr/value-types.md#number)
* Defaults to 0.

When setting `0`, the actual default is `available_processors * 2`

This is an expert-level setting, and generally should not need to be set Beats plugin is implemented based on a non-blocking mechanism, requiring a number of event loop and executor threads. The event loop threads are responsible to communicate with clients (accept incoming connections, enqueue/dequeue tasks and respond) and executor threads handle tasks. This configuration intends to limit or increase the number of threads to be created for the event loop. See [`executor_threads`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-executor_threads) configuration if you need to set executor threads count.

### `executor_threads` [v6.8.4-plugins-inputs-beats-executor_threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is equal to the number of CPU cores (1 executor thread per CPU core).

The number of threads to be used to process incoming Beats requests. By default, the Beats input creates a number of threads equal to the number of CPU cores. These threads handle incoming connections, reading from established sockets, and executing most of the tasks related to network connection management. Parsing the Lumberjack protocol is offloaded to a dedicated thread pool.

Generally you don’t need to touch this setting. In case you are sending very large events and observing "OutOfDirectMemory" exceptions, you may want to reduce this number to half or 1/4 of the CPU cores. This change reduces the number of threads decompressing batches of data into direct memory. However, this will only be a mitigating tweak, as the proper solution may require resizing your Logstash deployment, either by increasing number of Logstash nodes or increasing the JVM’s Direct Memory.

### `host` [v6.8.4-plugins-inputs-beats-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

The IP address to listen on.

### `include_codec_tag` [v6.8.4-plugins-inputs-beats-include_codec_tag]

Deprecated in 6.5.0.

Replaced by [`enrich`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-enrich)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

### `port` [v6.8.4-plugins-inputs-beats-port]

* This is a required setting.
* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

The port to listen on.

### `ssl` [v6.8.4-plugins-inputs-beats-ssl]

Deprecated in 6.6.0.

Replaced by [`ssl_enabled`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_enabled)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Events are by default sent in plain text. You can enable encryption by setting `ssl` to true and configuring the `ssl_certificate` and `ssl_key` options.

### `ssl_certificate` [v6.8.4-plugins-inputs-beats-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use.

### `ssl_certificate_authorities` [v6.8.4-plugins-inputs-beats-ssl_certificate_authorities]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Validate client certificates against these authorities. You can define multiple files or paths. All the certificates will be read and added to the trust store. You need to configure the [`ssl_client_authentication`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_client_authentication) to `optional` or `required` to enable the verification.

### `ssl_cipher_suites` [v6.8.4-plugins-inputs-beats-ssl_cipher_suites]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `['TLS_AES_256_GCM_SHA384', 'TLS_AES_128_GCM_SHA256', 'TLS_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256']`

The list of cipher suites to use, listed by priorities. This default list applies for OpenJDK 11.0.14 and higher. For older JDK versions, the default list includes only suites supported by that version. For example, the ChaCha20 family of ciphers is not supported in older versions.

### `ssl_client_authentication` [v6.8.4-plugins-inputs-beats-ssl_client_authentication]

* Value can be any of: `none`, `optional`, `required`
* Default value is `"none"`

Controls the server’s behavior in regard to requesting a certificate from client connections: `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `none`, which disables the client authentication.

When mutual TLS is enabled (`required` or `optional`), the certificate presented by the client must be signed by trusted [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) (CAs). Please note that the server does not validate the client certificate CN (Common Name) or SAN (Subject Alternative Name).

This setting can be used only if [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) is set.

### `ssl_enabled` [v6.8.4-plugins-inputs-beats-ssl_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Events are by default sent in plain text. You can enable encryption by setting `ssl_enabled` to true and configuring the [`ssl_certificate`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate) and [`ssl_key`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_key) options.

### `ssl_handshake_timeout` [v6.8.4-plugins-inputs-beats-ssl_handshake_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10000`

Time in milliseconds for an incomplete ssl handshake to timeout

### `ssl_key` [v6.8.4-plugins-inputs-beats-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL key to use. This key must be in the PKCS8 format and PEM encoded. You can use the [openssl pkcs8](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs8.html) command to complete the conversion. For example, the command to convert a PEM encoded PKCS1 private key to a PEM encoded, non-encrypted PKCS8 key is:

```
openssl pkcs8 -inform PEM -in path/to/logstash.key -topk8 -nocrypt -outform PEM -out path/to/logstash.pkcs8.key
```

### `ssl_key_passphrase` [v6.8.4-plugins-inputs-beats-ssl_key_passphrase]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

SSL key passphrase to use.

### `ssl_peer_metadata` [v6.8.4-plugins-inputs-beats-ssl_peer_metadata]

Deprecated in 6.5.0.

Replaced by [`enrich`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-enrich)

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Enables storing client certificate information in event’s metadata.

This option is only valid when [`ssl_client_authentication`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_client_authentication) is set to `optional` or `required`.

### `ssl_supported_protocols` [v6.8.4-plugins-inputs-beats-ssl_supported_protocols]

* Value type is [array](/lsr/value-types.md#array)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the HTTP endpoint.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_verify_mode` [v6.8.4-plugins-inputs-beats-ssl_verify_mode]

Deprecated in 6.6.0.

Replaced by [`ssl_client_authentication`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_client_authentication)

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

By default, the server doesn’t do any client verification. If the [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) is configured, and no value or `none` is provided for this option, it defaults to `force_peer` instead of `none`.

`peer` will make the server ask the client to provide a certificate. If the client provides a certificate, it will be validated.

`force_peer` will make the server ask the client to provide a certificate. If the client doesn’t provide a certificate, the connection will be closed.

When mutual TLS is enabled (`peer` or `force_peer`), the certificate presented by the client must be signed by trusted [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) (CAs). Please note that the server does not validate the client certificate CN (Common Name) or SAN (Subject Alternative Name).

This setting can be used only if [`ssl_certificate_authorities`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_certificate_authorities) is set.

### `tls_max_version` [v6.8.4-plugins-inputs-beats-tls_max_version]

Deprecated in 6.4.0.

Replaced by [`ssl_supported_protocols`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_supported_protocols)

* Value type is [number](/lsr/value-types.md#number)

The maximum TLS version allowed for the encrypted connections. The value must be the one of the following: 1.1 for TLS 1.1, 1.2 for TLS 1.2, 1.3 for TLSv1.3

### `tls_min_version` [v6.8.4-plugins-inputs-beats-tls_min_version]

Deprecated in 6.4.0.

Replaced by [`ssl_supported_protocols`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-ssl_supported_protocols)

* Value type is [number](/lsr/value-types.md#number)

The minimum TLS version allowed for the encrypted connections. The value must be one of the following: 1.1 for TLS 1.1, 1.2 for TLS 1.2, 1.3 for TLS 1.3

## Common options [v6.8.4-plugins-inputs-beats-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v6.8.4-plugins-inputs-beats-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v6.8.4-plugins-inputs-beats-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v6.8.4-plugins-inputs-beats-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v6.8.4-plugins-inputs-beats-id]

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

### `tags` [v6.8.4-plugins-inputs-beats-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v6.8.4-plugins-inputs-beats-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.

The Beats shipper automatically sets the `type` field on the event. You cannot override this setting in the Logstash config. If you specify a setting for the [`type`](v6-8-4-plugins-inputs-beats.md#v6.8.4-plugins-inputs-beats-type) config option in Logstash, it is ignored.
