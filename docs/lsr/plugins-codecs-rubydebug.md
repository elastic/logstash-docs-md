---
navigation_title: "rubydebug"
---

# Rubydebug codec plugin [plugins-codecs-rubydebug]


* Plugin version: v3.1.0
* Released on: 2020-07-08
* [Changelog](https://github.com/logstash-plugins/logstash-codec-rubydebug/blob/v3.1.0/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/codec-rubydebug-index.md).

## Getting help [_getting_help_197]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-rubydebug). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_195]

The rubydebug codec will output your Logstash event data using the Ruby Amazing Print library.


## Rubydebug Codec Configuration Options [plugins-codecs-rubydebug-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`metadata`](plugins-codecs-rubydebug.md#plugins-codecs-rubydebug-metadata) | [boolean](introduction.md#boolean) | No |

 

### `metadata` [plugins-codecs-rubydebug-metadata]

* Value type is [boolean](introduction.md#boolean)
* Default value is `false`

Should the event’s metadata be included?



