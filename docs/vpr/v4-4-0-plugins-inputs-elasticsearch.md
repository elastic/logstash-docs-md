---
navigation_title: "v4.4.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.4.0-plugins-inputs-elasticsearch.html
---

# Elasticsearch input plugin v4.4.0 [v4.4.0-plugins-inputs-elasticsearch]

* Plugin version: v4.4.0
* Released on: 2019-12-09
* [Changelog](https://github.com/logstash-plugins/logstash-input-elasticsearch/blob/v4.4.0/CHANGELOG.md)

For other versions, see the [overview list](input-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_358]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_358]

Compatibility Note

Starting with Elasticsearch 5.3, there’s an [HTTP setting](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html) called `http.content_type.required`. If this option is set to `true`, and you are using Logstash 2.4 through 5.2, you need to update the Elasticsearch input plugin to version 4.0.2 or higher.

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

## Scheduling [_scheduling_40]

Input from this plugin can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ).

Examples:

| | |
| :- | :- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).

## Elasticsearch Input Configuration Options [v4.4.0-plugins-inputs-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`ca_file`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-ca_file) | a valid filesystem path | No |
| [`docinfo`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-docinfo) | [boolean](/lsr/value-types.md#boolean) | No |
| [`docinfo_fields`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-docinfo_fields) | [array](/lsr/value-types.md#array) | No |
| [`docinfo_target`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-docinfo_target) | [string](/lsr/value-types.md#string) | No |
| [`hosts`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-hosts) | [array](/lsr/value-types.md#array) | No |
| [`index`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-index) | [string](/lsr/value-types.md#string) | No |
| [`password`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-password) | [password](/lsr/value-types.md#password) | No |
| [`query`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-query) | [string](/lsr/value-types.md#string) | No |
| [`schedule`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-schedule) | [string](/lsr/value-types.md#string) | No |
| [`scroll`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-scroll) | [string](/lsr/value-types.md#string) | No |
| [`size`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-size) | [number](/lsr/value-types.md#number) | No |
| [`slices`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-slices) | [number](/lsr/value-types.md#number) | No |
| [`ssl`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`user`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-user) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-common-options) for a list of options supported by all input plugins.

### `ca_file` [v4.4.0-plugins-inputs-elasticsearch-ca_file]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

SSL Certificate Authority file in PEM encoded format, must also include any chain certificates as necessary.

### `docinfo` [v4.4.0-plugins-inputs-elasticsearch-docinfo]

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

Starting with Logstash 6.0, the `document_type` option is deprecated due to the [removal of types in Logstash 6.0](https://www.elastic.co/guide/en/elasticsearch/reference/6.0/removal-of-types.html). It will be removed in the next major version of Logstash.

### `docinfo_fields` [v4.4.0-plugins-inputs-elasticsearch-docinfo_fields]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_index", "_type", "_id"]`

If document metadata storage is requested by enabling the `docinfo` option, this option lists the metadata fields to save in the current event. See [Meta-Fields](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-fields.html) in the Elasticsearch documentation for more information.

### `docinfo_target` [v4.4.0-plugins-inputs-elasticsearch-docinfo_target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"@metadata"`

If document metadata storage is requested by enabling the `docinfo` option, this option names the field under which to store the metadata fields as subfields.

### `hosts` [v4.4.0-plugins-inputs-elasticsearch-hosts]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

List of one or more Elasticsearch hosts to use for querying. Each host can be either IP, HOST, IP:port, or HOST:port. The port defaults to 9200.

### `index` [v4.4.0-plugins-inputs-elasticsearch-index]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"logstash-*"`

The index or alias to search. See [Multi Indices documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/multi-index.html) in the Elasticsearch documentation for more information on how to reference multiple indices.

### `password` [v4.4.0-plugins-inputs-elasticsearch-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

The password to use together with the username in the `user` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.

### `query` [v4.4.0-plugins-inputs-elasticsearch-query]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `'{ "sort": [ "_doc" ] }'`

The query to be executed. Read the [Elasticsearch query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/query-dsl.html) for more information.

### `schedule` [v4.4.0-plugins-inputs-elasticsearch-schedule]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "\* \* \* \* \*" (execute query every minute, on the minute)

There is no schedule by default. If no schedule is given, then the statement is run exactly once.

### `scroll` [v4.4.0-plugins-inputs-elasticsearch-scroll]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"1m"`

This parameter controls the keepalive time in seconds of the scrolling request and initiates the scrolling process. The timeout applies per round trip (i.e. between the previous scroll request, to the next).

### `size` [v4.4.0-plugins-inputs-elasticsearch-size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1000`

This allows you to set the maximum number of hits returned per scroll.

### `slices` [v4.4.0-plugins-inputs-elasticsearch-slices]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value.
* Sensible values range from 2 to about 8.

In some cases, it is possible to improve overall throughput by consuming multiple distinct slices of a query simultaneously using [sliced scrolls](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/search-request-body.html#sliced-scroll), especially if the pipeline is spending significant time waiting on Elasticsearch to provide results.

If set, the `slices` parameter tells the plugin how many slices to divide the work into, and will produce events from the slices in parallel until all of them are done scrolling.

The Elasticsearch manual indicates that there can be *negative* performance implications to both the query and the Elasticsearch cluster when a scrolling query uses more slices than shards in the index.

If the `slices` parameter is left unset, the plugin will *not* inject slice instructions into the query.

### `ssl` [v4.4.0-plugins-inputs-elasticsearch-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If enabled, SSL will be used when communicating with the Elasticsearch server (i.e. HTTPS will be used instead of plain HTTP).

### `user` [v4.4.0-plugins-inputs-elasticsearch-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The username to use together with the password in the `password` option when authenticating to the Elasticsearch server. If set to an empty string authentication will be disabled.

## Common options [v4.4.0-plugins-inputs-elasticsearch-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v4-4-0-plugins-inputs-elasticsearch.md#v4.4.0-plugins-inputs-elasticsearch-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v4.4.0-plugins-inputs-elasticsearch-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v4.4.0-plugins-inputs-elasticsearch-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.4.0-plugins-inputs-elasticsearch-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.4.0-plugins-inputs-elasticsearch-id]

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

### `tags` [v4.4.0-plugins-inputs-elasticsearch-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v4.4.0-plugins-inputs-elasticsearch-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
