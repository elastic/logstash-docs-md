---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-codecs-compress_spooler.html
---

# Compress_spooler codec plugin v2.0.5 [v2.0.5-plugins-codecs-compress_spooler]

* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-compress_spooler/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](codec-compress_spooler-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2315]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-compress_spooler). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2293]

The compress\_spooler codec.

## Compress_spooler Codec Configuration Options [v2.0.5-plugins-codecs-compress_spooler-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`compress_level`](v2-0-5-plugins-codecs-compress_spooler.md#v2.0.5-plugins-codecs-compress_spooler-compress_level) | [number](/lsr/value-types.md#number) | No |
| [`min_flush_time`](v2-0-5-plugins-codecs-compress_spooler.md#v2.0.5-plugins-codecs-compress_spooler-min_flush_time) | [number](/lsr/value-types.md#number) | No |
| [`spool_size`](v2-0-5-plugins-codecs-compress_spooler.md#v2.0.5-plugins-codecs-compress_spooler-spool_size) | [number](/lsr/value-types.md#number) | No |

### `compress_level` [v2.0.5-plugins-codecs-compress_spooler-compress_level]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `6`

### `min_flush_time` [v2.0.5-plugins-codecs-compress_spooler-min_flush_time]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

The amount of time in seconds since last flush before a flush is forced, on the next event. Values smaller than 0 disables time based flushing.

### `spool_size` [v2.0.5-plugins-codecs-compress_spooler-spool_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50`
