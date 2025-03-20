---
navigation_title: "v4.18.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.18.0-plugins-inputs-elasticsearch.html
---

# Elasticsearch input plugin v4.18.0 [v4.18.0-plugins-inputs-elasticsearch]


* Plugin version: v4.18.0
* Released on: 2023-09-29
* [Changelog](https://github.com/logstash-plugins/logstash-input-elasticsearch/blob/v4.18.0/CHANGELOG.md)

For other versions, see the [overview list](input-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_317]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_317]

Read from an Elasticsearch cluster, based on search query results. This is useful for replaying test logs, reindexing, etc. You can periodically schedule ingestion using a cron syntax (see `schedule` setting) or run the query one time to load data into Logstash.

Example:

```ruby
    input {
      # Read all documents from Elasticsearch matching the given query
      elasticsearch {
        hosts => "localhost"
        query => '{ "query": { "match": { "statuscode": 200 } }, "sort": [ "_doc" ] }'
      }
    }
```

This would create an Elasticsearch query with the following format:

```json
    curl 'http://localhost:9200/logstash-*/_search?&scroll=1m&size=1000' -d '{
      "query": {
        "match": {
          "statuscode": 200
        }
      },
      "sort": [ "_doc" ]
    }'
```


## Scheduling [_scheduling_11]

Input from this plugin can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ).

Examples:

|     |     |
| --- | --- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).


## Authentication [v4.18.0-plugins-inputs-elasticsearch-auth]

Authentication to a secure Elasticsearch cluster is possible using *one* of the following options:

* [`user`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-user) AND [`password`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-password)
* [`cloud_auth`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-cloud_auth)
* [`api_key`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-api_key)


## Authorization [v4.18.0-plugins-inputs-elasticsearch-autz]

Authorization to a secure Elasticsearch cluster requires `read` permission at index level and `monitoring` permissions at cluster level. The `monitoring` permission at cluster level is necessary to perform periodic connectivity checks.


## Compatibility with the Elastic Common Schema (ECS) [v4.18.0-plugins-inputs-elasticsearch-ecs]

When ECS compatibility is disabled, `docinfo_target` uses the `"@metadata"` field as a default, with ECS enabled the plugin uses a naming convention `"[@metadata][input][elasticsearch]"` as a default target for placing document information.

The plugin logs a warning when ECS is enabled and `target` isn’t set.

::::{tip}
Set the `target` option to avoid potential schema conflicts.
::::



## Elasticsearch Input configuration options [v4.18.0-plugins-inputs-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-common-options) and the [Elasticsearch Input deprecated configuration options](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-deprecated-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ca_trusted_fingerprint`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ca_trusted_fingerprint) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`cloud_auth`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-cloud_auth) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`cloud_id`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-cloud_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`connect_timeout_seconds`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-connect_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`docinfo`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-docinfo) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`docinfo_fields`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-docinfo_fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`docinfo_target`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-docinfo_target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ecs_compatibility`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`hosts`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`index`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-index) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`proxy`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-proxy) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`query`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-query) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`request_timeout_seconds`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-request_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`schedule`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-schedule) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`scroll`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-scroll) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`size`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`slices`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-slices) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_certificate`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_certificate_authorities`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) | list of [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_cipher_suites`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_cipher_suites) | list of [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_enabled`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_key) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_password`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_path`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_type`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_supported_protocols`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_supported_protocols) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_truststore_password`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_path`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_truststore_type`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_verification_mode`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_verification_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["full", "none"]` | No |
| [`socket_timeout_seconds`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-socket_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`target`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-target) | [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html) | No |
| [`retries`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-retries) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`user`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-common-options) for a list of options supported by all input plugins.

 

### `api_key` [v4.18.0-plugins-inputs-elasticsearch-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Authenticate using Elasticsearch API key. Note that this option also requires enabling the [`ssl_enabled`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_enabled) option.

Format is `id:api_key` where `id` and `api_key` are as returned by the Elasticsearch [Create API key API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key).


### `ca_trusted_fingerprint` [v4.18.0-plugins-inputs-elasticsearch-ca_trusted_fingerprint]

* Value type is [string](logstash://reference/configuration-file-structure.md#string), and must contain exactly 64 hexadecimal characters.
* There is no default value for this setting.
* Use of this option *requires* Logstash 8.3+

The SHA-256 fingerprint of an SSL Certificate Authority to trust, such as the autogenerated self-signed CA for an Elasticsearch cluster.


### `cloud_auth` [v4.18.0-plugins-inputs-elasticsearch-cloud_auth]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Cloud authentication string ("<username>:<password>" format) is an alternative for the `user`/`password` pair.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `cloud_id` [v4.18.0-plugins-inputs-elasticsearch-cloud_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Cloud ID, from the Elastic Cloud web console. If set `hosts` should not be used.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `connect_timeout_seconds` [v4.18.0-plugins-inputs-elasticsearch-connect_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

The maximum amount of time, in seconds, to wait while establishing a connection to Elasticsearch. Connect timeouts tend to occur when Elasticsearch or an intermediate proxy is overloaded with requests and has exhausted its connection pool.


### `docinfo` [v4.18.0-plugins-inputs-elasticsearch-docinfo]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If set, include Elasticsearch document information such as index, type, and the id in the event.

It might be important to note, with regards to metadata, that if you’re ingesting documents with the intent to re-index them (or just update them) that the `action` option in the elasticsearch output wants to know how to handle those things. It can be dynamically assigned with a field added to the metadata.

Example

```ruby
    input {
      elasticsearch {
        hosts => "es.production.mysite.org"
        index => "mydata-2018.09.*"
        query => '{ "query": { "query_string": { "query": "*" } } }'
        size => 500
        scroll => "5m"
        docinfo => true
        docinfo_target => "[@metadata][doc]"
      }
    }
    output {
      elasticsearch {
        index => "copy-of-production.%{[@metadata][doc][_index]}"
        document_type => "%{[@metadata][doc][_type]}"
        document_id => "%{[@metadata][doc][_id]}"
      }
    }
```

If set, you can use metadata information in the [`add_field`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-add_field) common option.

Example

```ruby
    input {
      elasticsearch {
        docinfo => true
        docinfo_target => "[@metadata][doc]"
        add_field => {
          identifier => "%{[@metadata][doc][_index]}:%{[@metadata][doc][_type]}:%{[@metadata][doc][_id]}"
        }
      }
    }
```


### `docinfo_fields` [v4.18.0-plugins-inputs-elasticsearch-docinfo_fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_index", "_type", "_id"]`

If document metadata storage is requested by enabling the `docinfo` option, this option lists the metadata fields to save in the current event. See [Meta-Fields](elasticsearch://reference/elasticsearch/mapping-reference/document-metadata-fields.md) in the Elasticsearch documentation for more information.


### `docinfo_target` [v4.18.0-plugins-inputs-elasticsearch-docinfo_target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: `"@metadata"`
    * ECS Compatibility enabled: `"[@metadata][input][elasticsearch]"`


If document metadata storage is requested by enabling the `docinfo` option, this option names the field under which to store the metadata fields as subfields.


### `ecs_compatibility` [v4.18.0-plugins-inputs-elasticsearch-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: CSV data added at root level
    * `v1`,`v8`: Elastic Common Schema compliant behavior

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)).


### `hosts` [v4.18.0-plugins-inputs-elasticsearch-hosts]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

List of one or more Elasticsearch hosts to use for querying. Each host can be either IP, HOST, IP:port, or HOST:port. The port defaults to 9200.


### `index` [v4.18.0-plugins-inputs-elasticsearch-index]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash-*"`

The index or alias to search. See [Multi Indices documentation](elasticsearch://reference/elasticsearch/rest-apis/api-conventions.md) in the Elasticsearch documentation for more information on how to reference multiple indices.


### `password` [v4.18.0-plugins-inputs-elasticsearch-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The password to use together with the username in the `user` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.


### `proxy` [v4.18.0-plugins-inputs-elasticsearch-proxy]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. An empty string is treated as if proxy was not set, this is useful when using environment variables e.g. `proxy => '${LS_PROXY:}'`.


### `query` [v4.18.0-plugins-inputs-elasticsearch-query]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `'{ "sort": [ "_doc" ] }'`

The query to be executed. Read the [Elasticsearch query DSL documentation](elasticsearch://reference/query-languages/querydsl.md) for more information.


### `request_timeout_seconds` [v4.18.0-plugins-inputs-elasticsearch-request_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

The maximum amount of time, in seconds, for a single request to Elasticsearch. Request timeouts tend to occur when an individual page of data is very large, such as when it contains large-payload documents and/or the [`size`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-size) has been specified as a large value.


### `retries` [v4.18.0-plugins-inputs-elasticsearch-retries]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The number of times to re-run the query after the first failure. If the query fails after all retries, it logs an error message. The default is 0 (no retry). This value should be equal to or greater than zero.

::::{note}
Partial failures - such as errors in a subset of all slices - can result in the entire query being retried, which can lead to duplication of data. Avoiding this would require Logstash to store the entire result set of a query in memory which is often not possible.
::::



### `schedule` [v4.18.0-plugins-inputs-elasticsearch-schedule]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "* * * * *" (execute query every minute, on the minute)

There is no schedule by default. If no schedule is given, then the statement is run exactly once.


### `scroll` [v4.18.0-plugins-inputs-elasticsearch-scroll]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1m"`

This parameter controls the keepalive time in seconds of the scrolling request and initiates the scrolling process. The timeout applies per round trip (i.e. between the previous scroll request, to the next).


### `size` [v4.18.0-plugins-inputs-elasticsearch-size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

This allows you to set the maximum number of hits returned per scroll.


### `slices` [v4.18.0-plugins-inputs-elasticsearch-slices]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value.
* Sensible values range from 2 to about 8.

In some cases, it is possible to improve overall throughput by consuming multiple distinct slices of a query simultaneously using [sliced scrolls](elasticsearch://reference/elasticsearch/rest-apis/paginate-search-results.md#slice-scroll), especially if the pipeline is spending significant time waiting on Elasticsearch to provide results.

If set, the `slices` parameter tells the plugin how many slices to divide the work into, and will produce events from the slices in parallel until all of them are done scrolling.

::::{note}
The Elasticsearch manual indicates that there can be *negative* performance implications to both the query and the Elasticsearch cluster when a scrolling query uses more slices than shards in the index.
::::


If the `slices` parameter is left unset, the plugin will *not* inject slice instructions into the query.


### `ssl_certificate` [v4.18.0-plugins-inputs-elasticsearch-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL certificate to use to authenticate the client. This certificate should be an OpenSSL-style X.509 certificate file.

::::{note}
This setting can be used only if [`ssl_key`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_key) is set.
::::



### `ssl_certificate_authorities` [v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_authorities]

* Value type is a list of [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting

The `.cer` or `.pem` files to validate the server’s certificate.

::::{note}
You cannot use this setting and [`ssl_truststore_path`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_path) at the same time.
::::



### `ssl_cipher_suites` [v4.18.0-plugins-inputs-elasticsearch-ssl_cipher_suites]

* Value type is a list of [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.


### `ssl_enabled` [v4.18.0-plugins-inputs-elasticsearch-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Enable SSL/TLS secured communication to Elasticsearch cluster. Leaving this unspecified will use whatever scheme is specified in the URLs listed in [`hosts`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-hosts) or extracted from the [`cloud_id`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-cloud_id). If no explicit protocol is specified plain HTTP will be used.


### `ssl_key` [v4.18.0-plugins-inputs-elasticsearch-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

OpenSSL-style RSA private key that corresponds to the [`ssl_certificate`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate).

::::{note}
This setting can be used only if [`ssl_certificate`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate) is set.
::::



### `ssl_keystore_password` [v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the keystore password


### `ssl_keystore_path` [v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The keystore used to present a certificate to the server. It can be either `.jks` or `.p12`

::::{note}
You cannot use this setting and [`ssl_certificate`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate) at the same time.
::::



### `ssl_keystore_type` [v4.18.0-plugins-inputs-elasticsearch-ssl_keystore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the keystore filename.

The format of the keystore file. It must be either `jks` or `pkcs12`.


### `ssl_supported_protocols` [v4.18.0-plugins-inputs-elasticsearch-ssl_supported_protocols]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the Elasticsearch cluster.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

::::{note}
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_truststore_password` [v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Set the truststore password.


### `ssl_truststore_path` [v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either .jks or .p12.

::::{note}
You cannot use this setting and [`ssl_certificate_authorities`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) at the same time.
::::



### `ssl_truststore_type` [v4.18.0-plugins-inputs-elasticsearch-ssl_truststore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the truststore filename.

The format of the truststore file. It must be either `jks` or `pkcs12`.


### `ssl_verification_mode` [v4.18.0-plugins-inputs-elasticsearch-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another party in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not_before and not_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.

::::{warning}
Setting certificate verification to `none` disables many security benefits of SSL/TLS, which is very dangerous. For more information on disabling certificate verification please read [https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf](https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf)
::::



### `socket_timeout_seconds` [v4.18.0-plugins-inputs-elasticsearch-socket_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

The maximum amount of time, in seconds, to wait on an incomplete response from Elasticsearch while no additional data has been appended. Socket timeouts usually occur while waiting for the first byte of a response, such as when executing a particularly complex query.


### `target` [v4.18.0-plugins-inputs-elasticsearch-target]

* Value type is [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html)
* There is no default value for this setting.

Without a `target`, events are created from each hit’s `_source` at the root level. When the `target` is set to a field reference, the `_source` of the hit is placed in the target field instead.

This option can be useful to avoid populating unknown fields when a downstream schema such as ECS is enforced. It is also possible to target an entry in the event’s metadata, which will be available during event processing but not exported to your outputs (e.g., `target \=> "[@metadata][_source]"`).


### `user` [v4.18.0-plugins-inputs-elasticsearch-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The username to use together with the password in the `password` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.



## Elasticsearch Input deprecated configuration options [v4.18.0-plugins-inputs-elasticsearch-deprecated-options]

This plugin supports the following deprecated configurations.

::::{warning}
Deprecated options are subject to removal in future releases.
::::


| Setting | Input type | Replaced by |
| --- | --- | --- |
| [`ca_file`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ca_file) | a valid filesystem path | [`ssl_certificate_authorities`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) |
| [`ssl`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | [`ssl_enabled`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_enabled) |
| [`ssl_certificate_verification`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_verification) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | [`ssl_verification_mode`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_verification_mode) |

### `ca_file` [v4.18.0-plugins-inputs-elasticsearch-ca_file]

::::{admonition} Deprecated in 4.17.0.
:class: warning

Replaced by [`ssl_certificate_authorities`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_authorities)
::::


* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL Certificate Authority file in PEM encoded format, must also include any chain certificates as necessary.


### `ssl` [v4.18.0-plugins-inputs-elasticsearch-ssl]

::::{admonition} Deprecated in 4.17.0.
:class: warning

Replaced by [`ssl_enabled`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_enabled)
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If enabled, SSL will be used when communicating with the Elasticsearch server (i.e. HTTPS will be used instead of plain HTTP).


### `ssl_certificate_verification` [v4.18.0-plugins-inputs-elasticsearch-ssl_certificate_verification]

::::{admonition} Deprecated in 4.17.0.
:class: warning

Replaced by [`ssl_verification_mode`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-ssl_verification_mode)
::::


* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Option to validate the server’s certificate. Disabling this severely compromises security. When certificate validation is disabled, this plugin implicitly trusts the machine resolved at the given address without validating its proof-of-identity. In this scenario, the plugin can transmit credentials to or process data from an untrustworthy man-in-the-middle or other compromised infrastructure. More information on the importance of certificate verification: **https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf**.



## Common options [v4.18.0-plugins-inputs-elasticsearch-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v4-18-0-plugins-inputs-elasticsearch.md#v4.18.0-plugins-inputs-elasticsearch-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v4.18.0-plugins-inputs-elasticsearch-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v4.18.0-plugins-inputs-elasticsearch-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.18.0-plugins-inputs-elasticsearch-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.18.0-plugins-inputs-elasticsearch-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elasticsearch inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  elasticsearch {
    id => "my_plugin_id"
  }
}
```


### `tags` [v4.18.0-plugins-inputs-elasticsearch-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v4.18.0-plugins-inputs-elasticsearch-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
