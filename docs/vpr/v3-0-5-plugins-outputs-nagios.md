---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-outputs-nagios.html
---

# Nagios output plugin v3.0.5 [v3.0.5-plugins-outputs-nagios]

* Plugin version: v3.0.5
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-output-nagios/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](output-nagios-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1462]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-nagios). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1452]

The Nagios output is used for sending passive check results to Nagios via the Nagios command file. This output currently supports Nagios 3.

For this output to work, your event *must* have the following Logstash event fields:

* `nagios_host`
* `nagios_service`

These Logstash event fields are supported, but optional:

* `nagios_annotation`
* `nagios_level` (overrides `nagios_level` configuration option)

There are two configuration options:

* `commandfile` - The location of the Nagios external command file. Defaults to */var/lib/nagios3/rw/nagios.cmd*

* `nagios_level` - Specifies the level of the check to be sent. Defaults to CRITICAL and can be overriden by setting the "nagios\_level" field to one of "OK", "WARNING", "CRITICAL", or "UNKNOWN"

  ```
      output{
        if [message] =~ /(error|ERROR|CRITICAL)/ {
          nagios {
            # your config here
          }
        }
      }
  ```

## Nagios Output Configuration Options [v3.0.5-plugins-outputs-nagios-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`commandfile`](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-commandfile) | <<,>> | No |
| [`nagios_level`](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-nagios_level) | [string](/lsr/value-types.md#string), one of `["0", "1", "2", "3"]` | No |

Also see [Common options](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-common-options) for a list of options supported by all output plugins.

### `commandfile` [v3.0.5-plugins-outputs-nagios-commandfile]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"/var/lib/nagios3/rw/nagios.cmd"`

The full path to your Nagios command file.

### `nagios_level` [v3.0.5-plugins-outputs-nagios-nagios_level]

* Value can be any of: `0`, `1`, `2`, `3`
* Default value is `"2"`

The Nagios check level. Should be one of 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN. Defaults to 2 - CRITICAL.

## Common options [v3.0.5-plugins-outputs-nagios-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-5-plugins-outputs-nagios.md#v3.0.5-plugins-outputs-nagios-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.0.5-plugins-outputs-nagios-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.5-plugins-outputs-nagios-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.5-plugins-outputs-nagios-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 nagios outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  nagios {
    id => "my_plugin_id"
  }
}
```
