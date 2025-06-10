---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-codecs-es_bulk.html
---

# Es_bulk codec plugin v3.0.7 [v3.0.7-plugins-codecs-es_bulk]

* Plugin version: v3.0.7
* Released on: 2019-02-04
* [Changelog](https://github.com/logstash-plugins/logstash-codec-es_bulk/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](codec-es_bulk-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2335]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-es_bulk). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2313]

This codec will decode the [Elasticsearch bulk format](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-bulk.html) into individual events, plus metadata into the `@metadata` field.

Encoding is not supported at this time as the Elasticsearch output submits Logstash events in bulk format.

## Codec settings in the `logstash-input-http` plugin [v3.0.7-plugins-codecs-es_bulk-codec-settings]

The [input-http](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-http.html) plugin has two configuration options for codecs: `codec` and `additional_codecs`.

Values in `additional_codecs` are prioritized over those specified in the `codec` option. That is, the default `codec` is applied only if no codec for the request’s content-type is found in the `additional_codecs` setting.
