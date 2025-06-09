---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-codecs-dots.html
---

# Dots codec plugin v3.0.5 [v3.0.5-plugins-codecs-dots]

* Plugin version: v3.0.5
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-codec-dots/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](codec-dots-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2323]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-dots). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2301]

This codec generates a dot(`.`) to represent each Event it processes. This is typically used with `stdout` output to provide feedback on the terminal. It is also used to measure Logstash’s throughtput with the `pv` command.
