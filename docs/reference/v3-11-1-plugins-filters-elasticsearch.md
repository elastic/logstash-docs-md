---
navigation_title: "v3.11.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.11.1-plugins-filters-elasticsearch.html
---

# Elasticsearch filter plugin v3.11.1 [v3.11.1-plugins-filters-elasticsearch]


* Plugin version: v3.11.1
* Released on: 2022-02-08
* [Changelog](https://github.com/logstash-plugins/logstash-filter-elasticsearch/blob/v3.11.1/CHANGELOG.md)

For other versions, see the [overview list](filter-elasticsearch-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1821]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-elasticsearch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1799]

Search Elasticsearch for a previous log event and copy some fields from it into the current event. Below are two complete examples of how this filter might be used.

The first example uses the legacy *query* parameter where the user is limited to an Elasticsearch query_string. Whenever logstash receives an "end" event, it uses this elasticsearch filter to find the matching "start" event based on some operation identifier. Then it copies the `@timestamp` field from the "start" event into a new field on the "end" event.  Finally, using a combination of the "date" filter and the "ruby" filter, we calculate the time duration in hours between the two events.

```ruby
if [type] == "end" {
   elasticsearch {
      hosts => ["es-server"]
      query => "type:start AND operation:%{[opid]}"
      fields => { "@timestamp" => "started" }
   }

   date {
      match => ["[started]", "ISO8601"]
      target => "[started]"
   }

   ruby {
      code => "event.set('duration_hrs', (event.get('@timestamp') - event.get('started')) / 3600)"
   }
}
```

The example below reproduces the above example but utilises the query_template. This query_template represents a full Elasticsearch query DSL and supports the standard Logstash field substitution syntax.  The example below issues the same query as the first example but uses the template shown.

```ruby
if [type] == "end" {
      elasticsearch {
         hosts => ["es-server"]
         query_template => "template.json"
         fields => { "@timestamp" => "started" }
      }

      date {
         match => ["[started]", "ISO8601"]
         target => "[started]"
      }

      ruby {
         code => "event.set('duration_hrs', (event.get('@timestamp') - event.get('started')) / 3600)"
      }
}
```

template.json:

```json
{
  "size": 1,
  "sort" : [ { "@timestamp" : "desc" } ],
  "query": {
    "query_string": {
      "query": "type:start AND operation:%{[opid]}"
    }
  },
  "_source": ["@timestamp"]
}
```

As illustrated above, through the use of *opid*, fields from the Logstash events can be referenced within the template. The template will be populated per event prior to being used to query Elasticsearch.

Notice also that when you use `query_template`, the Logstash attributes `result_size` and `sort` will be ignored. They should be specified directly in the JSON template, as shown in the example above.


## Authentication [v3.11.1-plugins-filters-elasticsearch-auth]

Authentication to a secure Elasticsearch cluster is possible using *one* of the following options:

* [`user`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-user) AND [`password`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-password)
* [`cloud_auth`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-cloud_auth)
* [`api_key`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-api_key)


## Authorization [v3.11.1-plugins-filters-elasticsearch-autz]

Authorization to a secure Elasticsearch cluster requires `read` permission at index level and `monitoring` permissions at cluster level. The `monitoring` permission at cluster level is necessary to perform periodic connectivity checks.


## Elasticsearch Filter Configuration Options [v3.11.1-plugins-filters-elasticsearch-options]

This plugin supports the following configuration options plus the [Common options](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`aggregation_fields`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-aggregation_fields) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`api_key`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ca_file`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-ca_file) | a valid filesystem path | No |
| [`cloud_auth`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-cloud_auth) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`cloud_id`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-cloud_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`docinfo_fields`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-docinfo_fields) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`enable_sort`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-enable_sort) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`fields`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`hosts`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`index`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-index) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`proxy`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-proxy) | [uri](logstash://reference/configuration-file-structure.md#uri) | No |
| [`query`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-query) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`query_template`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-query_template) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`result_size`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-result_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`sort`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-sort) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`tag_on_failure`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`user`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-common-options) for a list of options supported by all filter plugins.

 

### `aggregation_fields` [v3.11.1-plugins-filters-elasticsearch-aggregation_fields]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Hash of aggregation names to copy from elasticsearch response into Logstash event fields

Example:

```ruby
    filter {
      elasticsearch {
        aggregation_fields => {
          "my_agg_name" => "my_ls_field"
        }
      }
    }
```


### `api_key` [v3.11.1-plugins-filters-elasticsearch-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Authenticate using Elasticsearch API key. Note that this option also requires enabling the `ssl` option.

Format is `id:api_key` where `id` and `api_key` are as returned by the Elasticsearch [Create API key API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key).


### `ca_file` [v3.11.1-plugins-filters-elasticsearch-ca_file]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

SSL Certificate Authority file


### `cloud_auth` [v3.11.1-plugins-filters-elasticsearch-cloud_auth]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Cloud authentication string ("<username>:<password>" format) is an alternative for the `user`/`password` pair.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `cloud_id` [v3.11.1-plugins-filters-elasticsearch-cloud_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Cloud ID, from the Elastic Cloud web console. If set `hosts` should not be used.

For more info, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `docinfo_fields` [v3.11.1-plugins-filters-elasticsearch-docinfo_fields]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Hash of docinfo fields to copy from old event (found via elasticsearch) into new event

Example:

```ruby
    filter {
      elasticsearch {
        docinfo_fields => {
          "_id" => "document_id"
          "_index" => "document_index"
        }
      }
    }
```


### `enable_sort` [v3.11.1-plugins-filters-elasticsearch-enable_sort]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Whether results should be sorted or not


### `fields` [v3.11.1-plugins-filters-elasticsearch-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `{}`

An array of fields to copy from the old event (found via elasticsearch) into the new event, currently being processed.

In the following example, the values of `@timestamp` and `event_id` on the event found via elasticsearch are copied to the current event’s `started` and `start_id` fields, respectively:

```ruby
fields => {
  "@timestamp" => "started"
  "event_id" => "start_id"
}
```


### `hosts` [v3.11.1-plugins-filters-elasticsearch-hosts]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["localhost:9200"]`

List of elasticsearch hosts to use for querying.


### `index` [v3.11.1-plugins-filters-elasticsearch-index]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Comma-delimited list of index names to search; use `_all` or empty string to perform the operation on all indices. Field substitution (e.g. `index-name-%{{date_field}}`) is available


### `password` [v3.11.1-plugins-filters-elasticsearch-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Basic Auth - password


### `proxy` [v3.11.1-plugins-filters-elasticsearch-proxy]

* Value type is [uri](logstash://reference/configuration-file-structure.md#uri)
* There is no default value for this setting.

Set the address of a forward HTTP proxy. An empty string is treated as if proxy was not set, and is useful when using environment variables e.g. `proxy => '${LS_PROXY:}'`.


### `query` [v3.11.1-plugins-filters-elasticsearch-query]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Elasticsearch query string. More information is available in the [Elasticsearch query string documentation](elasticsearch://reference/query-languages/query-dsl-query-string-query.md#query-string-syntax).


### `query_template` [v3.11.1-plugins-filters-elasticsearch-query_template]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

File path to elasticsearch query in DSL format. More information is available in the [Elasticsearch query documentation](elasticsearch://reference/query-languages/querydsl.md).


### `result_size` [v3.11.1-plugins-filters-elasticsearch-result_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

How many results to return


### `sort` [v3.11.1-plugins-filters-elasticsearch-sort]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"@timestamp:desc"`

Comma-delimited list of `<field>:<direction>` pairs that define the sort order


### `ssl` [v3.11.1-plugins-filters-elasticsearch-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

SSL


### `tag_on_failure` [v3.11.1-plugins-filters-elasticsearch-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_elasticsearch_lookup_failure"]`

Tags the event on failure to look up previous log event information. This can be used in later analysis.


### `user` [v3.11.1-plugins-filters-elasticsearch-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Basic Auth - username



## Common options [v3.11.1-plugins-filters-elasticsearch-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-11-1-plugins-filters-elasticsearch.md#v3.11.1-plugins-filters-elasticsearch-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.11.1-plugins-filters-elasticsearch-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      elasticsearch {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      elasticsearch {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.11.1-plugins-filters-elasticsearch-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      elasticsearch {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      elasticsearch {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.11.1-plugins-filters-elasticsearch-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.11.1-plugins-filters-elasticsearch-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elasticsearch filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      elasticsearch {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.11.1-plugins-filters-elasticsearch-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.11.1-plugins-filters-elasticsearch-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      elasticsearch {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      elasticsearch {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.11.1-plugins-filters-elasticsearch-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      elasticsearch {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      elasticsearch {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



