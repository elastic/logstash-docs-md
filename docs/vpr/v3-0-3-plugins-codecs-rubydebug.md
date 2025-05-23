---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-codecs-rubydebug.html
---

# Rubydebug codec plugin v3.0.3 [v3.0.3-plugins-codecs-rubydebug]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-rubydebug/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](codec-rubydebug-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2415]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-rubydebug). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2393]

The rubydebug codec will output your Logstash event data using the Ruby Awesome Print library.


## Rubydebug Codec Configuration Options [v3.0.3-plugins-codecs-rubydebug-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`metadata`](v3-0-3-plugins-codecs-rubydebug.md#v3.0.3-plugins-codecs-rubydebug-metadata) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

 

### `metadata` [v3.0.3-plugins-codecs-rubydebug-metadata]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Should the event’s metadata be included?



