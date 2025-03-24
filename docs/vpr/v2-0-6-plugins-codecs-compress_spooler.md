---
navigation_title: "v2.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.6-plugins-codecs-compress_spooler.html
---

# Compress_spooler codec plugin v2.0.6 [v2.0.6-plugins-codecs-compress_spooler]


* Plugin version: v2.0.6
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-codec-compress_spooler/blob/v2.0.6/CHANGELOG.md)

For other versions, see the [overview list](codec-compress_spooler-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2280]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-compress_spooler). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2258]

The compress_spooler codec.


## Compress_spooler Codec Configuration Options [v2.0.6-plugins-codecs-compress_spooler-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`compress_level`](v2-0-6-plugins-codecs-compress_spooler.md#v2.0.6-plugins-codecs-compress_spooler-compress_level) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`min_flush_time`](v2-0-6-plugins-codecs-compress_spooler.md#v2.0.6-plugins-codecs-compress_spooler-min_flush_time) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`spool_size`](v2-0-6-plugins-codecs-compress_spooler.md#v2.0.6-plugins-codecs-compress_spooler-spool_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |

 

### `compress_level` [v2.0.6-plugins-codecs-compress_spooler-compress_level]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `6`


### `min_flush_time` [v2.0.6-plugins-codecs-compress_spooler-min_flush_time]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

The amount of time in seconds since last flush before a flush is forced, on the next event. Values smaller than 0 disables time based flushing.


### `spool_size` [v2.0.6-plugins-codecs-compress_spooler-spool_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`



