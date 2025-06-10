---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-outputs-elastic_app_search.html
---

# Elastic App Search output plugin v3.0.1 [v3.0.1-plugins-outputs-elastic_app_search]

* A component of the [elastic\_enterprise\_search integration plugin](integration-elastic_enterprise_search-index.md)
* Integration version: v3.0.1
* Released on: 2025-01-03
* [Changelog](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](output-elastic_app_search-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1102]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1095]

This output lets you send events to the [Elastic App Search](https://www.elastic.co/app-search) solution, both the [self-managed](https://www.elastic.co/downloads/app-search) or the [managed](https://www.elastic.co/cloud/app-search-service) service. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the App Search bulk API to index multiple events in one request.

App Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to App Search. If you want to keep the `@timestamp` field, you can use the [timestamp\_destination](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-timestamp_destination) option to store the timestamp in a different field.

This gem does not support codec customization.

## AppSearch Output configuration options [v3.0.1-plugins-outputs-elastic_app_search-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`api_key`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-api_key) | [password](/lsr/value-types.md#password) | Yes |
| [`document_id`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-document_id) | [string](/lsr/value-types.md#string) | No |
| [`engine`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-engine) | [string](/lsr/value-types.md#string) | Yes |
| [`ssl_certificate_authorities`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_certificate_authorities) | list of [path](/lsr/value-types.md#path) | No |
| [`ssl_cipher_suites`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_cipher_suites) | list of [string](/lsr/value-types.md#string) | No |
| [`ssl_supported_protocols`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_supported_protocols) | [string](/lsr/value-types.md#string) | No |
| [`ssl_truststore_password`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_truststore_path`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_path) | [path](/lsr/value-types.md#path) | No |
| [`ssl_truststore_type`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`ssl_verification_mode`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_verification_mode) | [string](/lsr/value-types.md#string), one of `["full", "none"]` | No |
| [`timestamp_destination`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-timestamp_destination) | [string](/lsr/value-types.md#string) | No |
| [`url`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-url) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-common-options) for a list of options supported by all output plugins.

### `api_key` [v3.0.1-plugins-outputs-elastic_app_search-api_key]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value

The private API Key with write permissions. Visit the App Search API keys reference \[page]\(<https://www.elastic.co/guide/en/app-search/current/authentication.html#authentication-api-keys>) for more information.

### `document_id` [v3.0.1-plugins-outputs-elastic_app_search-document_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The id for app search documents. This can be an interpolated value like `myapp-%{sequence_id}`. Reusing ids will cause documents to be rewritten.

### `engine` [v3.0.1-plugins-outputs-elastic_app_search-engine]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

The name of the search engine you created in App Search, an information repository that includes the indexed document records. The `engine` field supports [sprintf format](https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html#sprintf) to allow the engine name to be derived from a field value from each event, for example `engine-%{engine_name}`.

Invalid engine names cause ingestion to stop until the field value can be resolved into a valid engine name. This situation can happen if the interpolated field value resolves to a value without a matching engine, or, if the field is missing from the event and cannot be resolved at all.

Consider adding a "default" engine type in the configuration to catch errors if the field is missing from the event.

Example:

```
input {
  stdin {
    codec => json
  }
}

filter {
  if ![engine_name] {
    mutate {
      add_field => {"engine_name" => "default"}
    }
  }
}

output {
  elastic_app_search {
    engine => "engine_%{[engine_name]}"
  }
}
```

### `ssl_certificate_authorities` [v3.0.1-plugins-outputs-elastic_app_search-ssl_certificate_authorities]

* Value type is a list of [path](/lsr/value-types.md#path)
* There is no default value for this setting

The .cer or .pem files to validate the server’s certificate.

You cannot use this setting and [`ssl_truststore_path`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_path) at the same time.

### `ssl_cipher_suites` [v3.0.1-plugins-outputs-elastic_app_search-ssl_cipher_suites]

* Value type is a list of [string](/lsr/value-types.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.

### `ssl_supported_protocols` [v3.0.1-plugins-outputs-elastic_app_search-ssl_supported_protocols]

* Value type is [string](/lsr/value-types.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the Elasticsearch cluster.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_truststore_password` [v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the truststore password

### `ssl_truststore_path` [v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either `.jks` or `.p12`.

You cannot use this setting and [`ssl_certificate_authorities`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-ssl_certificate_authorities) at the same time.

### `ssl_truststore_type` [v3.0.1-plugins-outputs-elastic_app_search-ssl_truststore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the truststore filename.

The format of the truststore file. It must be either `jks` or `pkcs12`.

### `ssl_verification_mode` [v3.0.1-plugins-outputs-elastic_app_search-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another party in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not\_before and not\_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.

Setting certificate verification to `none` disables many security benefits of SSL/TLS, which is very dangerous. For more information on disabling certificate verification please read <https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf>

### `timestamp_destination` [v3.0.1-plugins-outputs-elastic_app_search-timestamp_destination]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. App Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.

### `url` [v3.0.1-plugins-outputs-elastic_app_search-url]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `http://localhost:3002`

The value of the API endpoint in the form of a URL.

## Common options [v3.0.1-plugins-outputs-elastic_app_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`enable_metric`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-1-plugins-outputs-elastic_app_search.md#v3.0.1-plugins-outputs-elastic_app_search-id) | [string](/lsr/value-types.md#string) | No |

### `enable_metric` [v3.0.1-plugins-outputs-elastic_app_search-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.1-plugins-outputs-elastic_app_search-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic\_app\_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  elastic_app_search {
    id => "my_plugin_id"
  }
}
```
