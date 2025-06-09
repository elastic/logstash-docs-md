---
navigation_title: "v5.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.1.0-plugins-inputs-elasticsearch.html
---

# Elasticsearch input plugin v5.1.0 [v5.1.0-plugins-inputs-elasticsearch]

* Plugin version: v5.1.0
* Released on: 2025-04-07
* [Changelog](https://github.com/logstash-plugins/logstash-input-elasticsearch/blob/v5.1.0/CHANGELOG.md)

For other versions, see the [overview list](input-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_316]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_316]

Read from an Elasticsearch cluster, based on search query results. This is useful for replaying test logs, reindexing, etc. You can periodically schedule ingestion using a cron syntax (see `schedule` setting) or run the query one time to load data into Logstash.

Example:

```
    input {
      # Read all documents from Elasticsearch matching the given query
      elasticsearch {
        hosts => "localhost"
        query => '{ "query": { "match": { "statuscode": 200 } }, "sort": [ "_doc" ] }'
      }
    }
```

This would create an Elasticsearch query with the following format:

```
    curl 'http://localhost:9200/logstash-*/_search?&scroll=1m&size=1000' -d '{
      "query": {
        "match": {
          "statuscode": 200
        }
      },
      "sort": [ "_doc" ]
    }'
```

## Scheduling [v5.1.0-plugins-inputs-elasticsearch-scheduling]

Input from this plugin can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ).

Examples:

| | |
| :- | :- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).

## Authentication [v5.1.0-plugins-inputs-elasticsearch-auth]

Authentication to a secure Elasticsearch cluster is possible using *one* of the following options:

* [`user`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-user) AND [`password`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-password)
* [`cloud_auth`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-cloud_auth)
* [`api_key`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-api_key)

## Authorization [v5.1.0-plugins-inputs-elasticsearch-autz]

Authorization to a secure Elasticsearch cluster requires `read` permission at index level and `monitoring` permissions at cluster level. The `monitoring` permission at cluster level is necessary to perform periodic connectivity checks.

## Compatibility with the Elastic Common Schema (ECS) [v5.1.0-plugins-inputs-elasticsearch-ecs]

When ECS compatibility is disabled, `docinfo_target` uses the `"@metadata"` field as a default, with ECS enabled the plugin uses a naming convention `"[@metadata][input][elasticsearch]"` as a default target for placing document information.

The plugin logs a warning when ECS is enabled and `target` isn’t set.

Set the `target` option to avoid potential schema conflicts.

## Failure handling [v5.1.0-plugins-inputs-elasticsearch-failure-handling]

When this input plugin cannot create a structured `Event` from a hit result, it will instead create an `Event` that is tagged with `_elasticsearch_input_failure` whose `[event][original]` is a JSON-encoded string representation of the entire hit.

Common causes are:

* When the hit result contains top-level fields that are [reserved in Logstash](https://www.elastic.co/guide/en/logstash/current/processing.html#reserved-fields) but do not have the expected shape. Use the [`target`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-target) directive to avoid conflicts with the top-level namespace.
* When [`docinfo`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-docinfo) is enabled and the docinfo fields cannot be merged into the hit result. Combine [`target`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-target) and [`docinfo_target`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-docinfo_target) to avoid conflict.

## Tracking a field’s value across runs [v5.1.0-plugins-inputs-elasticsearch-cursor]

**Technical Preview: Tracking a field’s value**

The feature that allows tracking a field’s value across runs is in *Technical Preview*. Configuration options and implementation details are subject to change in minor releases without being preceded by deprecation warnings.

Some uses cases require tracking the value of a particular field between two jobs. Examples include:

* avoiding the need to re-process the entire result set of a long query after an unplanned restart
* grabbing only new data from an index instead of processing the entire set on each job.

The Elasticsearch input plugin provides the [`tracking_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field) and [`tracking_field_seed`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field_seed) options. When [`tracking_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field) is set, the plugin records the value of that field for the last document retrieved in a run into a file. (The file location defaults to [`last_run_metadata_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-last_run_metadata_path).)

You can then inject this value in the query using the placeholder `:last_value`. The value will be injected into the query before execution, and then updated after the query completes if new data was found.

This feature works best when:

* the query sorts by the tracking field,
* the timestamp field is added by Elasticsearch, and
* the field type has enough resolution so that two events are unlikely to have the same value.

Consider using a tracking field whose type is [date nanoseconds](https://www.elastic.co/guide/en/elasticsearch/reference/current/date_nanos.html). If the tracking field is of this data type, you can use an extra placeholder called `:present` to inject the nano-second based value of "now-30s". This placeholder is useful as the right-hand side of a range filter, allowing the collection of new data but leaving partially-searchable bulk request data to the next scheduled job.

### Sample configuration: Track field value across runs [v5.1.0-plugins-inputs-elasticsearch-tracking-sample]

This section contains a series of steps to help you set up the "tailing" of data being written to a set of indices, using a date nanosecond field added by an Elasticsearch ingest pipeline and the `tracking_field` capability of this plugin.

1. Create ingest pipeline that adds Elasticsearch’s `_ingest.timestamp` field to the documents as `event.ingested`:

   ```
       PUT _ingest/pipeline/my-pipeline
       {
         "processors": [
                 {
               "script": {
                 "lang": "painless",
                 "source": "ctx.putIfAbsent(\"event\", [:]); ctx.event.ingested = metadata().now.format(DateTimeFormatter.ISO_INSTANT);"
               }
             }
         ]
       }
   ```

2) Create an index mapping where the tracking field is of date nanosecond type and invokes the defined pipeline:

   ```
       PUT /_template/my_template
       {
         "index_patterns": ["test-*"],
         "settings": {
           "index.default_pipeline": "my-pipeline",
         },
         "mappings": {
           "properties": {
             "event": {
               "properties": {
                 "ingested": {
                   "type": "date_nanos",
                   "format": "strict_date_optional_time_nanos"
                 }
               }
             }
           }
         }
       }
   ```

3. Define a query that looks at all data of the indices, sorted by the tracking field, and with a range filter since the last value seen until present:

   ```
   {
     "query": {
       "range": {
         "event.ingested": {
           "gt": ":last_value",
           "lt": ":present"
         }
       }
     },
     "sort": [
       {
         "event.ingested": {
           "order": "asc",
           "format": "strict_date_optional_time_nanos",
           "numeric_type": "date_nanos"
         }
       }
     ]
   }
   ```

4) Configure the Elasticsearch input to query the indices with the query defined above, every minute, and track the `event.ingested` field:

   ```
       input {
         elasticsearch {
           id => tail_test_index
           hosts => [ 'https://..']
           api_key => '....'
           index => 'test-*'
           query => '{ "query": { "range": { "event.ingested": { "gt": ":last_value", "lt": ":present"}}}, "sort": [ { "event.ingested": {"order": "asc", "format": "strict_date_optional_time_nanos", "numeric_type" : "date_nanos" } } ] }'
           tracking_field => "[event][ingested]"
           slices => 5 # optional use of slices to speed data processing, should be equal to or less than number of primary shards
           schedule => '* * * * *' # every minute
           schedule_overlap => false # don't accumulate jobs if one takes longer than 1 minute
         }
       }
   ```

With this sample setup, new documents are indexed into a `test-*` index. The next scheduled run:

* selects all new documents since the last observed value of the tracking field,
* uses [Point in time (PIT)](https://www.elastic.co/guide/en/elasticsearch/reference/current/point-in-time-api.html#point-in-time-api) + [Search after](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html#search-after) to paginate through all the data, and
* updates the value of the field at the end of the pagination.

## Elasticsearch Input configuration options [v5.1.0-plugins-inputs-elasticsearch-options]

This plugin supports these configuration options plus the [Common options](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-common-options) described later.

As of version `5.0.0` of this plugin, a number of previously deprecated settings related to SSL have been removed. Please check out [Elasticsearch Input Obsolete Configuration Options](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-obsolete-options) for details.

| Setting | Input type | Required |
| :- | :- | :- |
| [`api_key`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-api_key) | [password](/lsr/value-types.md#password) | No |
| [`ca_trusted_fingerprint`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ca_trusted_fingerprint) | [string](/lsr/value-types.md#string) | No |
| [`cloud_auth`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-cloud_auth) | [password](/lsr/value-types.md#password) | No |
| [`cloud_id`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-cloud_id) | [string](/lsr/value-types.md#string) | No |
| [`connect_timeout_seconds`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-connect_timeout_seconds) | [number](/lsr/value-types.md#number) | No |
| [`custom_headers`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-custom_headers) | [hash](/lsr/value-types.md#hash) | No |
| [`docinfo`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-docinfo) | [boolean](/lsr/value-types.md#boolean) | No |
| [`docinfo_fields`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-docinfo_fields) | [array](/lsr/value-types.md#array) | No |
| [`docinfo_target`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-docinfo_target) | [string](/lsr/value-types.md#string) | No |
| [`ecs_compatibility`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`hosts`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-hosts) | [array](/lsr/value-types.md#array) | No |
| [`index`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-index) | [string](/lsr/value-types.md#string) | No |
| [`last_run_metadata_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-last_run_metadata_path) | [string](/lsr/value-types.md#string) | No |
| [`password`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-password) | [password](/lsr/value-types.md#password) | No |
| [`proxy`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-proxy) | [uri](/lsr/value-types.md#uri) | No |
| [`query`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-query) | [string](/lsr/value-types.md#string) | No |
| [`response_type`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-response_type) | [string](/lsr/value-types.md#string), one of `["hits","aggregations"]` | No |
| [`request_timeout_seconds`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-request_timeout_seconds) | [number](/lsr/value-types.md#number) | No |
| [`schedule`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-schedule) | [string](/lsr/value-types.md#string) | No |
| [`schedule_overlap`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-schedule_overlap) | [boolean](/lsr/value-types.md#boolean) | No |
| [`scroll`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-scroll) | [string](/lsr/value-types.md#string) | No |
| [`search_api`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-search_api) | [string](/lsr/value-types.md#string), one of `["auto", "search_after", "scroll"]` | No |
| [`size`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-size) | [number](/lsr/value-types.md#number) | No |
| [`slices`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-slices) | [number](/lsr/value-types.md#number) | No |
| [`ssl_certificate`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate) | [path](/lsr/value-types.md#path) | No |
| [`ssl_certificate_authorities`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) | list of [path](/lsr/value-types.md#path) | No |
| [`ssl_cipher_suites`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_cipher_suites) | list of [string](/lsr/value-types.md#string) | No |
| [`ssl_enabled`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_enabled) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ssl_key`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_key) | [path](/lsr/value-types.md#path) | No |
| [`ssl_keystore_password`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_keystore_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_path) | [path](/lsr/value-types.md#path) | No |
| [`ssl_keystore_type`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_type) | [string](/lsr/value-types.md#string) | No |
| [`ssl_supported_protocols`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_supported_protocols) | [string](/lsr/value-types.md#string) | No |
| [`ssl_truststore_password`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`ssl_truststore_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_path) | [path](/lsr/value-types.md#path) | No |
| [`ssl_truststore_type`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`ssl_verification_mode`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_verification_mode) | [string](/lsr/value-types.md#string), one of `["full", "none"]` | No |
| [`socket_timeout_seconds`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-socket_timeout_seconds) | [number](/lsr/value-types.md#number) | No |
| [`target`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-target) | [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html) | No |
| [`tracking_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field) | [string](/lsr/value-types.md#string) | No |
| [`tracking_field_seed`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field_seed) | [string](/lsr/value-types.md#string) | No |
| [`retries`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-retries) | [number](/lsr/value-types.md#number) | No |
| [`user`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-user) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-common-options) for a list of options supported by all input plugins.

### `api_key` [v5.1.0-plugins-inputs-elasticsearch-api_key]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Authenticate using Elasticsearch API key. Note that this option also requires enabling the [`ssl_enabled`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_enabled) option.

Format is `id:api_key` where `id` and `api_key` are as returned by the Elasticsearch [Create API key API](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html).

### `ca_trusted_fingerprint` [v5.1.0-plugins-inputs-elasticsearch-ca_trusted_fingerprint]

* Value type is [string](/lsr/value-types.md#string), and must contain exactly 64 hexadecimal characters.
* There is no default value for this setting.
* Use of this option *requires* Logstash 8.3+

The SHA-256 fingerprint of an SSL Certificate Authority to trust, such as the autogenerated self-signed CA for an Elasticsearch cluster.

### `cloud_auth` [v5.1.0-plugins-inputs-elasticsearch-cloud_auth]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Cloud authentication string ("\<username>:\<password>" format) is an alternative for the `user`/`password` pair.

For more info, check out the [Logstash-to-Cloud documentation](https://www.elastic.co/guide/en/logstash/current/connecting-to-cloud.html).

### `cloud_id` [v5.1.0-plugins-inputs-elasticsearch-cloud_id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Cloud ID, from the Elastic Cloud web console. If set `hosts` should not be used.

For more info, check out the [Logstash-to-Cloud documentation](https://www.elastic.co/guide/en/logstash/current/connecting-to-cloud.html).

### `connect_timeout_seconds` [v5.1.0-plugins-inputs-elasticsearch-connect_timeout_seconds]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

The maximum amount of time, in seconds, to wait while establishing a connection to Elasticsearch. Connect timeouts tend to occur when Elasticsearch or an intermediate proxy is overloaded with requests and has exhausted its connection pool.

### `custom_headers` [v5.1.0-plugins-inputs-elasticsearch-custom_headers]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is empty

Pass a set of key value pairs as the headers sent in each request to an elasticsearch node. The headers will be used for any kind of request. These custom headers will override any headers previously set by the plugin such as the User Agent or Authorization headers.

### `docinfo` [v5.1.0-plugins-inputs-elasticsearch-docinfo]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If set, include Elasticsearch document information such as index, type, and the id in the event.

It might be important to note, with regards to metadata, that if you’re ingesting documents with the intent to re-index them (or just update them) that the `action` option in the elasticsearch output wants to know how to handle those things. It can be dynamically assigned with a field added to the metadata.

Example

```
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

If set, you can use metadata information in the [`add_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-add_field) common option.

Example

```
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

### `docinfo_fields` [v5.1.0-plugins-inputs-elasticsearch-docinfo_fields]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_index", "_type", "_id"]`

If document metadata storage is requested by enabling the `docinfo` option, this option lists the metadata fields to save in the current event. See [Meta-Fields](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-fields.html) in the Elasticsearch documentation for more information.

### `docinfo_target` [v5.1.0-plugins-inputs-elasticsearch-docinfo_target]

* Value type is [string](/lsr/value-types.md#string)

* Default value depends on whether [`ecs_compatibility`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ecs_compatibility) is enabled:

  * ECS Compatibility disabled: `"@metadata"`
  * ECS Compatibility enabled: `"[@metadata][input][elasticsearch]"`

If document metadata storage is requested by enabling the `docinfo` option, this option names the field under which to store the metadata fields as subfields.

### `ecs_compatibility` [v5.1.0-plugins-inputs-elasticsearch-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: CSV data added at root level
  * `v1`,`v8`: Elastic Common Schema compliant behavior

* Default value depends on which version of Logstash is running:

  * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
  * Otherwise, the default value is `disabled`

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current).

### `hosts` [v5.1.0-plugins-inputs-elasticsearch-hosts]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

List of one or more Elasticsearch hosts to use for querying. Each host can be either IP, HOST, IP:port, or HOST:port. The port defaults to 9200.

### `index` [v5.1.0-plugins-inputs-elasticsearch-index]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash-*"`

The index or alias to search. Check out [Multi Indices documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/api-conventions.html#api-multi-index) in the Elasticsearch documentation for info on referencing multiple indices.

### `last_run_metadata_path` [v5.1.0-plugins-inputs-elasticsearch-last_run_metadata_path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The path to store the last observed value of the tracking field, when used. By default this file is stored as `<path.data>/plugins/inputs/elasticsearch/<pipeline_id>/last_run_value`.

This setting should point to file, not a directory, and Logstash must have read+write access to this file.

### `password` [v5.1.0-plugins-inputs-elasticsearch-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

The password to use together with the username in the `user` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.

### `proxy` [v5.1.0-plugins-inputs-elasticsearch-proxy]

* Value type is [uri](/lsr/value-types.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. An empty string is treated as if proxy was not set, this is useful when using environment variables e.g. `proxy => '${LS_PROXY:}'`.

### `query` [v5.1.0-plugins-inputs-elasticsearch-query]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `'{ "sort": [ "_doc" ] }'`

The query to be executed. Read the [Elasticsearch query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) for more information.

When [`search_api`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-search_api) resolves to `search_after` and the query does not specify `sort`, the default sort `'{ "sort": { "_shard_doc": "asc" } }'` will be added to the query. Please refer to the [Elasticsearch search\_after](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html#search-after) parameter to know more.

### `response_type` [v5.1.0-plugins-inputs-elasticsearch-response_type]

* Value can be any of: `hits`, `aggregations`
* Default value is `hits`

Which part of the result to transform into Logstash events when processing the response from the query. The default `hits` will generate one event per returned document (i.e. "hit"). When set to `aggregations`, a single Logstash event will be generated with the contents of the `aggregations` object of the query’s response. In this case the `hits` object will be ignored. The parameter `size` will be always be set to 0 regardless of the default or user-defined value set in this plugin.

### `request_timeout_seconds` [v5.1.0-plugins-inputs-elasticsearch-request_timeout_seconds]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

The maximum amount of time, in seconds, for a single request to Elasticsearch. Request timeouts tend to occur when an individual page of data is very large, such as when it contains large-payload documents and/or the [`size`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-size) has been specified as a large value.

### `retries` [v5.1.0-plugins-inputs-elasticsearch-retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

The number of times to re-run the query after the first failure. If the query fails after all retries, it logs an error message. The default is 0 (no retry). This value should be equal to or greater than zero.

Partial failures - such as errors in a subset of all slices - can result in the entire query being retried, which can lead to duplication of data. Avoiding this would require Logstash to store the entire result set of a query in memory which is often not possible.

### `schedule` [v5.1.0-plugins-inputs-elasticsearch-schedule]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "\* \* \* \* \*" (execute query every minute, on the minute)

There is no schedule by default. If no schedule is given, then the statement is run exactly once.

### `schedule_overlap` [v5.1.0-plugins-inputs-elasticsearch-schedule_overlap]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Whether to allow queuing of a scheduled run if a run is occurring. While this is ideal for ensuring a new run happens immediately after the previous on finishes if there is a lot of work to do, but given the queue is unbounded it may lead to an out of memory over long periods of time if the queue grows continuously.

When in doubt, set `schedule_overlap` to false (it may become the default value in the future).

### `scroll` [v5.1.0-plugins-inputs-elasticsearch-scroll]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"1m"`

This parameter controls the keepalive time in seconds of the scrolling request and initiates the scrolling process. The timeout applies per round trip (i.e. between the previous scroll request, to the next).

### `search_api` [v5.1.0-plugins-inputs-elasticsearch-search_api]

* Value can be any of: `auto`, `search_after`, `scroll`
* Default value is `auto`

With `auto` the plugin uses the `search_after` parameter for Elasticsearch version `8.0.0` or higher, otherwise the `scroll` API is used instead.

`search_after` uses [point in time](https://www.elastic.co/guide/en/elasticsearch/reference/current/point-in-time-api.html#point-in-time-api) and sort value to search. The query requires at least one `sort` field, as described in the [`query`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-query) parameter.

`scroll` uses [scroll](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html#scroll-search-results) API to search, which is no longer recommended.

### `size` [v5.1.0-plugins-inputs-elasticsearch-size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1000`

This allows you to set the maximum number of hits returned per scroll.

### `slices` [v5.1.0-plugins-inputs-elasticsearch-slices]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value.
* Sensible values range from 2 to about 8.

In some cases, it is possible to improve overall throughput by consuming multiple distinct slices of a query simultaneously using [sliced scrolls](https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html#slice-scroll), especially if the pipeline is spending significant time waiting on Elasticsearch to provide results.

If set, the `slices` parameter tells the plugin how many slices to divide the work into, and will produce events from the slices in parallel until all of them are done scrolling.

The Elasticsearch manual indicates that there can be *negative* performance implications to both the query and the Elasticsearch cluster when a scrolling query uses more slices than shards in the index.

If the `slices` parameter is left unset, the plugin will *not* inject slice instructions into the query.

### `ssl_certificate` [v5.1.0-plugins-inputs-elasticsearch-ssl_certificate]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL certificate to use to authenticate the client. This certificate should be an OpenSSL-style X.509 certificate file.

This setting can be used only if [`ssl_key`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_key) is set.

### `ssl_certificate_authorities` [v5.1.0-plugins-inputs-elasticsearch-ssl_certificate_authorities]

* Value type is a list of [path](/lsr/value-types.md#path)
* There is no default value for this setting

The `.cer` or `.pem` files to validate the server’s certificate.

You cannot use this setting and [`ssl_truststore_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_path) at the same time.

### `ssl_cipher_suites` [v5.1.0-plugins-inputs-elasticsearch-ssl_cipher_suites]

* Value type is a list of [string](/lsr/value-types.md#string)
* There is no default value for this setting

The list of cipher suites to use, listed by priorities. Supported cipher suites vary depending on the Java and protocol versions.

### `ssl_enabled` [v5.1.0-plugins-inputs-elasticsearch-ssl_enabled]

* Value type is [boolean](/lsr/value-types.md#boolean)
* There is no default value for this setting.

Enable SSL/TLS secured communication to Elasticsearch cluster. Leaving this unspecified will use whatever scheme is specified in the URLs listed in [`hosts`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-hosts) or extracted from the [`cloud_id`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-cloud_id). If no explicit protocol is specified plain HTTP will be used.

When not explicitly set, SSL will be automatically enabled if any of the specified hosts use HTTPS.

### `ssl_key` [v5.1.0-plugins-inputs-elasticsearch-ssl_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

OpenSSL-style RSA private key that corresponds to the [`ssl_certificate`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate).

This setting can be used only if [`ssl_certificate`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate) is set.

### `ssl_keystore_password` [v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the keystore password

### `ssl_keystore_path` [v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The keystore used to present a certificate to the server. It can be either `.jks` or `.p12`

You cannot use this setting and [`ssl_certificate`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate) at the same time.

### `ssl_keystore_type` [v5.1.0-plugins-inputs-elasticsearch-ssl_keystore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the keystore filename.

The format of the keystore file. It must be either `jks` or `pkcs12`.

### `ssl_supported_protocols` [v5.1.0-plugins-inputs-elasticsearch-ssl_supported_protocols]

* Value type is [string](/lsr/value-types.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the Elasticsearch cluster.

For Java 8 `'TLSv1.3'` is supported only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK\_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.

### `ssl_truststore_password` [v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the truststore password.

### `ssl_truststore_path` [v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The truststore to validate the server’s certificate. It can be either .jks or .p12.

You cannot use this setting and [`ssl_certificate_authorities`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) at the same time.

### `ssl_truststore_type` [v5.1.0-plugins-inputs-elasticsearch-ssl_truststore_type]

* Value can be any of: `jks`, `pkcs12`
* If not provided, the value will be inferred from the truststore filename.

The format of the truststore file. It must be either `jks` or `pkcs12`.

### `ssl_verification_mode` [v5.1.0-plugins-inputs-elasticsearch-ssl_verification_mode]

* Value can be any of: `full`, `none`
* Default value is `full`

Defines how to verify the certificates presented by another party in the TLS connection:

`full` validates that the server certificate has an issue date that’s within the not\_before and not\_after dates; chains to a trusted Certificate Authority (CA), and has a hostname or IP address that matches the names within the certificate.

`none` performs no certificate validation.

Setting certificate verification to `none` disables many security benefits of SSL/TLS, which is very dangerous. For more information on disabling certificate verification please read <https://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf>

### `socket_timeout_seconds` [v5.1.0-plugins-inputs-elasticsearch-socket_timeout_seconds]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

The maximum amount of time, in seconds, to wait on an incomplete response from Elasticsearch while no additional data has been appended. Socket timeouts usually occur while waiting for the first byte of a response, such as when executing a particularly complex query.

### `target` [v5.1.0-plugins-inputs-elasticsearch-target]

* Value type is [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html)
* There is no default value for this setting.

Without a `target`, events are created from each hit’s `_source` at the root level. When the `target` is set to a field reference, the `_source` of the hit is placed in the target field instead.

This option can be useful to avoid populating unknown fields when a downstream schema such as ECS is enforced. It is also possible to target an entry in the event’s metadata, which will be available during event processing but not exported to your outputs (e.g., `target \=> "[@metadata][_source]"`).

### `tracking_field` [v5.1.0-plugins-inputs-elasticsearch-tracking_field]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Which field from the last event of a previous run will be used a cursor value for the following run. The value of this field is injected into each query if the query uses the placeholder `:last_value`. For the first query after a pipeline is started, the value used is either read from [`last_run_metadata_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-last_run_metadata_path) file, or taken from [`tracking_field_seed`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field_seed) setting.

Note: The tracking value is updated after each page is read and at the end of each Point in Time. In case of a crash the last saved value will be used so some duplication of data can occur. For this reason the use of unique document IDs for each event is recommended in the downstream destination.

### `tracking_field_seed` [v5.1.0-plugins-inputs-elasticsearch-tracking_field_seed]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"1970-01-01T00:00:00.000000000Z"`

The starting value for the [`tracking_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tracking_field) if there is no [`last_run_metadata_path`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-last_run_metadata_path) already. This field defaults to the nanosecond precision ISO8601 representation of `epoch`, or "1970-01-01T00:00:00.000000000Z", given nano-second precision timestamps are the most reliable data format to use for this feature.

### `user` [v5.1.0-plugins-inputs-elasticsearch-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The username to use together with the password in the `password` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.

## Elasticsearch Input Obsolete Configuration Options [v5.1.0-plugins-inputs-elasticsearch-obsolete-options]

As of version `5.0.0` of this plugin, some configuration options have been replaced. The plugin will fail to start if it contains any of these obsolete options.

| Setting | Replaced by |
| :- | :- |
| ca\_file | [`ssl_certificate_authorities`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_certificate_authorities) |
| ssl | [`ssl_enabled`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_enabled) |
| ssl\_certificate\_verification | [`ssl_verification_mode`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-ssl_verification_mode) |

## Common options [v5.1.0-plugins-inputs-elasticsearch-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v5-1-0-plugins-inputs-elasticsearch.md#v5.1.0-plugins-inputs-elasticsearch-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v5.1.0-plugins-inputs-elasticsearch-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v5.1.0-plugins-inputs-elasticsearch-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.1.0-plugins-inputs-elasticsearch-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.1.0-plugins-inputs-elasticsearch-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elasticsearch inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  elasticsearch {
    id => "my_plugin_id"
  }
}
```

### `tags` [v5.1.0-plugins-inputs-elasticsearch-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v5.1.0-plugins-inputs-elasticsearch-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
