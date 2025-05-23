---
navigation_title: "elastic_app_search"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash/current/plugins-outputs-elastic_app_search.html
---

# Elastic App Search output plugin [plugins-outputs-elastic_app_search]


* A component of the [elastic_enterprise_search integration plugin](plugins-integrations-elastic_enterprise_search.md)
* Integration version: v3.0.0
* Released on: 2023-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search/blob/v3.0.0/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](/vpr/output-elastic_app_search-index.md).

## Getting help [_getting_help_72]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-elastic_enterprise_search). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_71]

This output lets you send events to the [Elastic App Search](https://www.elastic.co/app-search) solution, both the [self-managed](https://www.elastic.co/downloads/app-search) or the [managed](https://www.elastic.co/cloud/app-search-service) service. On receiving a batch of events from the Logstash pipeline, the plugin converts the events into documents and uses the App Search bulk API to index multiple events in one request.

App Search doesn’t allow fields to begin with `@timestamp`. By default the `@timestamp` and `@version` fields will be removed from each event before the event is sent to App Search. If you want to keep the `@timestamp` field, you can use the [timestamp_destination](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-timestamp_destination) option to store the timestamp in a different field.

::::{note} 
This gem does not support codec customization.
::::



## AppSearch Output configuration options [plugins-outputs-elastic_app_search-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-api_key) | [password](value-types.md#password) | Yes |
| [`document_id`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-document_id) | [string](value-types.md#string) | No |
| [`engine`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-engine) | [string](value-types.md#string) | Yes |
| [`ssl_certificate_authorities`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_certificate_authorities) | list of [path](value-types.md#path) | No |
| [`ssl_cipher_suites`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_cipher_suites) | list of [string](value-types.md#string) | No |
| [`ssl_supported_protocols`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_supported_protocols) | [string](value-types.md#string) | No |
| [`ssl_truststore_password`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_truststore_password) | [password](value-types.md#password) | No |
| [`ssl_truststore_path`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_truststore_path) | [path](value-types.md#path) | No |
| [`ssl_truststore_type`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_truststore_type) | [string](value-types.md#string) | No |
| [`ssl_verification_mode`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_verification_mode) | [string](value-types.md#string), one of `["full", "none"]` | No |
| [`timestamp_destination`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-timestamp_destination) | [string](value-types.md#string) | No |
| [`url`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-url) | [string](value-types.md#string) | Yes |

Also see [Common options](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-common-options) for a list of options supported by all output plugins.

 

### `api_key` [plugins-outputs-elastic_app_search-api_key]

* Value type is [password](value-types.md#password)
* There is no default value

The private API Key with write permissions. Visit the App Search API keys reference [page](https://www.elastic.co/guide/en/app-search/current/authentication.html#authentication-api-keys) for more information.


### `document_id` [plugins-outputs-elastic_app_search-document_id]

* Value type is [string](value-types.md#string)
* There is no default value

The id for app search documents. This can be an interpolated value like `myapp-%{{sequence_id}}`. Reusing ids will cause documents to be rewritten.


### `engine` [plugins-outputs-elastic_app_search-engine]

* Value type is [string](value-types.md#string)
* There is no default value

The name of the search engine you created in App Search, an information repository that includes the indexed document records. The `engine` field supports [sprintf format](https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html#sprintf) to allow the engine name to be derived from a field value from each event, for example `engine-%{{engine_name}}`.

Invalid engine names cause ingestion to stop until the field value can be resolved into a valid engine name. This situation can happen if the interpolated field value resolves to a value without a matching engine, or, if the field is missing from the event and cannot be resolved at all.

::::{tip} 
Consider adding a "default" engine type in the configuration to catch errors if the field is missing from the event.
::::


Example:

```ruby
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


### `ssl_certificate_authorities` [plugins-outputs-elastic_app_search-ssl_certificate_authorities]

* Value type is a list of [path](value-types.md#path)
* There is no default value for this setting

The .cer or .pem files to validate the server’s certificate.

::::{note} 
You cannot use this setting and [`ssl_truststore_path`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_truststore_path) at the same time.
::::



### `ssl_cipher_suites` [plugins-outputs-elastic_app_search-ssl_cipher_suites]

* Value type is a list of [string](value-types.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.


### `ssl_supported_protocols` [plugins-outputs-elastic_app_search-ssl_supported_protocols]

* Value type is [string](value-types.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the Elasticsearch cluster.

For Java 8 `'TLSv1.3'` is supported only since ***8u262*** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

::::{note} 
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_truststore_password` [plugins-outputs-elastic_app_search-ssl_truststore_password]

* Value type is [password](value-types.md#password)
* There is no default value for this setting.

Set the truststore password


### `ssl_truststore_path` [plugins-outputs-elastic_app_search-ssl_truststore_path]

* Value type is [path](value-types.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either `.jks` or `.p12`.

::::{note} 
You cannot use this setting and [`ssl_certificate_authorities`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-ssl_certificate_authorities) at the same time.
::::



### `ssl_truststore_type` [plugins-outputs-elastic_app_search-ssl_truststore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the truststore filename.

The format of the truststore file. It must be either `jks` or `pkcs12`.


### `ssl_verification_mode` [plugins-outputs-elastic_app_search-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another party in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not_before and not_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.

::::{warning} 
Setting certificate verification to `none` disables many security benefits of SSL/TLS, which is very dangerous. For more information on disabling certificate verification please read [https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf)
::::



### `timestamp_destination` [plugins-outputs-elastic_app_search-timestamp_destination]

* Value type is [string](value-types.md#string)
* There is no default value

Where to move the value from the `@timestamp` field.

All Logstash events contain a `@timestamp` field. App Search doesn’t support fields starting with `@timestamp`, and by default, the `@timestamp` field will be deleted.

To keep the timestamp field, set this value to the name of the field where you want `@timestamp` copied.


### `url` [plugins-outputs-elastic_app_search-url]

* Value type is [string](value-types.md#string)
* Default value is `http://localhost:3002`

The value of the API endpoint in the form of a URL.



## Common options [plugins-outputs-elastic_app_search-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`enable_metric`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](plugins-outputs-elastic_app_search.md#plugins-outputs-elastic_app_search-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `enable_metric` [plugins-outputs-elastic_app_search-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-elastic_app_search-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 elastic_app_search outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  elastic_app_search {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




