---
navigation_title: "v4.9.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.9.2-plugins-inputs-elasticsearch.html
---

# Elasticsearch input plugin v4.9.2 [v4.9.2-plugins-inputs-elasticsearch]


* Plugin version: v4.9.2
* Released on: 2021-08-12
* [Changelog](https://github.com/logstash-plugins/logstash-input-elasticsearch/blob/v4.9.2/CHANGELOG.md)

For other versions, see the [overview list](input-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_332]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_332]

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


## Scheduling [_scheduling_26]

Input from this plugin can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ).

Examples:

|     |     |
| --- | --- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).


## Authentication [v4.9.2-plugins-inputs-elasticsearch-auth]

Authentication to a secure Elasticsearch cluster is possible using *one* of the following options:

* [`user`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-user) AND [`password`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-password)
* [`cloud_auth`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-cloud_auth)
* [`api_key`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-api_key)


## Authorization [v4.9.2-plugins-inputs-elasticsearch-autz]

Authorization to a secure Elasticsearch cluster requires `read` permission at index level and `monitoring` permissions at cluster level. The `monitoring` permission at cluster level is necessary to perform periodic connectivity checks.


## Elasticsearch Input Configuration Options [v4.9.2-plugins-inputs-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ca_file`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-ca_file) | a valid filesystem path | No |
| [`cloud_auth`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-cloud_auth) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`cloud_id`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-cloud_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`connect_timeout_seconds`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-connect_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`docinfo`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-docinfo) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`docinfo_fields`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-docinfo_fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`docinfo_target`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-docinfo_target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`hosts`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`index`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-index) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`proxy`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-proxy) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`query`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-query) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`request_timeout_seconds`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-request_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`schedule`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-schedule) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`scroll`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-scroll) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`size`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`slices`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-slices) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`socket_timeout_seconds`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-socket_timeout_seconds) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`target`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-target) | [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html) | No |
| [`user`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-common-options) for a list of options supported by all input plugins.

 

### `api_key` [v4.9.2-plugins-inputs-elasticsearch-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Authenticate using Elasticsearch API key. Note that this option also requires enabling the `ssl` option.

Format is `id:api_key` where `id` and `api_key` are as returned by the Elasticsearch [Create API key API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key).


### `ca_file` [v4.9.2-plugins-inputs-elasticsearch-ca_file]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL Certificate Authority file in PEM encoded format, must also include any chain certificates as necessary.


### `cloud_auth` [v4.9.2-plugins-inputs-elasticsearch-cloud_auth]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Cloud authentication string ("<username>:<password>" format) is an alternative for the `user`/`password` pair.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `cloud_id` [v4.9.2-plugins-inputs-elasticsearch-cloud_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Cloud ID, from the Elastic Cloud web console. If set `hosts` should not be used.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `connect_timeout_seconds` [v4.9.2-plugins-inputs-elasticsearch-connect_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

The maximum amount of time, in seconds, to wait while establishing a connection to Elasticsearch. Connect timeouts tend to occur when Elasticsearch or an intermediate proxy is overloaded with requests and has exhausted its connection pool.


### `docinfo` [v4.9.2-plugins-inputs-elasticsearch-docinfo]

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
      }
    }
    output {
      elasticsearch {
        index => "copy-of-production.%{[@metadata][_index]}"
        document_type => "%{[@metadata][_type]}"
        document_id => "%{[@metadata][_id]}"
      }
    }
```

If set, you can use metadata information in the [`add_field`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-add_field) common option.

Example

```ruby
    input {
      elasticsearch {
        docinfo => true
        add_field => {
          identifier => "%{[@metadata][_index]}:%{[@metadata][_type]}:%{[@metadata][_id]}"
        }
      }
    }
```


### `docinfo_fields` [v4.9.2-plugins-inputs-elasticsearch-docinfo_fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_index", "_type", "_id"]`

If document metadata storage is requested by enabling the `docinfo` option, this option lists the metadata fields to save in the current event. See [Meta-Fields](elasticsearch://reference/elasticsearch/mapping-reference/document-metadata-fields.md) in the Elasticsearch documentation for more information.


### `docinfo_target` [v4.9.2-plugins-inputs-elasticsearch-docinfo_target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"@metadata"`

If document metadata storage is requested by enabling the `docinfo` option, this option names the field under which to store the metadata fields as subfields.


### `hosts` [v4.9.2-plugins-inputs-elasticsearch-hosts]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

List of one or more Elasticsearch hosts to use for querying. Each host can be either IP, HOST, IP:port, or HOST:port. The port defaults to 9200.


### `index` [v4.9.2-plugins-inputs-elasticsearch-index]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash-*"`

The index or alias to search. See [Multi Indices documentation](elasticsearch://reference/elasticsearch/rest-apis/api-conventions.md) in the Elasticsearch documentation for more information on how to reference multiple indices.


### `password` [v4.9.2-plugins-inputs-elasticsearch-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The password to use together with the username in the `user` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.


### `proxy` [v4.9.2-plugins-inputs-elasticsearch-proxy]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. An empty string is treated as if proxy was not set, this is useful when using environment variables e.g. `proxy => '${LS_PROXY:}'`.


### `query` [v4.9.2-plugins-inputs-elasticsearch-query]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `'{ "sort": [ "_doc" ] }'`

The query to be executed. Read the [Elasticsearch query DSL documentation](elasticsearch://reference/query-languages/querydsl.md) for more information.


### `request_timeout_seconds` [v4.9.2-plugins-inputs-elasticsearch-request_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

The maximum amount of time, in seconds, for a single request to Elasticsearch. Request timeouts tend to occur when an individual page of data is very large, such as when it contains large-payload documents and/or the [`size`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-size) has been specified as a large value.


### `schedule` [v4.9.2-plugins-inputs-elasticsearch-schedule]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "* * * * *" (execute query every minute, on the minute)

There is no schedule by default. If no schedule is given, then the statement is run exactly once.


### `scroll` [v4.9.2-plugins-inputs-elasticsearch-scroll]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1m"`

This parameter controls the keepalive time in seconds of the scrolling request and initiates the scrolling process. The timeout applies per round trip (i.e. between the previous scroll request, to the next).


### `size` [v4.9.2-plugins-inputs-elasticsearch-size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

This allows you to set the maximum number of hits returned per scroll.


### `slices` [v4.9.2-plugins-inputs-elasticsearch-slices]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value.
* Sensible values range from 2 to about 8.

In some cases, it is possible to improve overall throughput by consuming multiple distinct slices of a query simultaneously using [sliced scrolls](elasticsearch://reference/elasticsearch/rest-apis/paginate-search-results.md#slice-scroll), especially if the pipeline is spending significant time waiting on Elasticsearch to provide results.

If set, the `slices` parameter tells the plugin how many slices to divide the work into, and will produce events from the slices in parallel until all of them are done scrolling.

::::{note}
The Elasticsearch manual indicates that there can be *negative* performance implications to both the query and the Elasticsearch cluster when a scrolling query uses more slices than shards in the index.
::::


If the `slices` parameter is left unset, the plugin will *not* inject slice instructions into the query.


### `ssl` [v4.9.2-plugins-inputs-elasticsearch-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If enabled, SSL will be used when communicating with the Elasticsearch server (i.e. HTTPS will be used instead of plain HTTP).


### `socket_timeout_seconds` [v4.9.2-plugins-inputs-elasticsearch-socket_timeout_seconds]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

The maximum amount of time, in seconds, to wait on an incomplete response from Elasticsearch while no additional data has been appended. Socket timeouts usually occur while waiting for the first byte of a response, such as when executing a particularly complex query.


### `target` [v4.9.2-plugins-inputs-elasticsearch-target]

* Value type is [field reference](https://www.elastic.co/guide/en/logstash/current/field-references-deepdive.html)
* There is no default value for this setting.

Without a `target`, events are created from each hit’s `_source` at the root level. When the `target` is set to a field reference, the `_source` of the hit is placed in the target field instead.

This option can be useful to avoid populating unknown fields when a downstream schema such as ECS is enforced. It is also possible to target an entry in the event’s metadata, which will be available during event processing but not exported to your outputs (e.g., `target \=> "[@metadata][_source]"`).


### `user` [v4.9.2-plugins-inputs-elasticsearch-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The username to use together with the password in the `password` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.



## Common options [v4.9.2-plugins-inputs-elasticsearch-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v4-9-2-plugins-inputs-elasticsearch.md#v4.9.2-plugins-inputs-elasticsearch-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v4.9.2-plugins-inputs-elasticsearch-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v4.9.2-plugins-inputs-elasticsearch-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.9.2-plugins-inputs-elasticsearch-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.9.2-plugins-inputs-elasticsearch-id]

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


### `tags` [v4.9.2-plugins-inputs-elasticsearch-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v4.9.2-plugins-inputs-elasticsearch-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



