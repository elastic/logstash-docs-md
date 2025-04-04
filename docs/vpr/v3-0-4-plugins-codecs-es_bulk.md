---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-codecs-es_bulk.html
---

# Es_bulk codec plugin v3.0.4 [v3.0.4-plugins-codecs-es_bulk]


* Plugin version: v3.0.4
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-es_bulk/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](codec-es_bulk-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2302]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-es_bulk). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2280]

This codec will decode the [Elasticsearch bulk format](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-bulk.html) into individual events, plus metadata into the `@metadata` field.

Encoding is not supported at this time as the Elasticsearch output submits Logstash events in bulk format.


