---
navigation_title: "v3.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.1-plugins-outputs-exec.html
---

# Exec output plugin v3.1.1 [v3.1.1-plugins-outputs-exec]

* Plugin version: v3.1.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-exec/blob/v3.1.1/CHANGELOG.md)

For other versions, see the [overview list](output-exec-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1231]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-exec). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1224]

The exec output will run a command for each event received. Ruby’s `system()` function will be used, i.e. the command string will be passed to a shell. You can use `%{name}` and other dynamic strings in the command to pass select fields from the event to the child process. Example:

```
    output {
      if [type] == "abuse" {
        exec {
          command => "iptables -A INPUT -s %{clientip} -j DROP"
        }
      }
    }
```

If you want it non-blocking you should use `&` or `dtach` or other such techniques. There is no timeout for the commands being run so misbehaving commands could otherwise stall the Logstash pipeline indefinitely.

Exercise great caution with `%{name}` field placeholders. The contents of the field will be included verbatim without any sanitization, i.e. any shell metacharacters from the field values will be passed straight to the shell.

## Exec Output Configuration Options [v3.1.1-plugins-outputs-exec-options]

This plugin supports the following configuration options plus the [Common options](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`command`](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-command) | [string](/lsr/value-types.md#string) | Yes |
| [`quiet`](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-quiet) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-common-options) for a list of options supported by all output plugins.

### `command` [v3.1.1-plugins-outputs-exec-command]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Command line to execute via subprocess. Use `dtach` or `screen` to make it non blocking. This value can include `%{name}` and other dynamic strings.

### `quiet` [v3.1.1-plugins-outputs-exec-quiet]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

display the result of the command to the terminal

## Common options [v3.1.1-plugins-outputs-exec-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-1-plugins-outputs-exec.md#v3.1.1-plugins-outputs-exec-id) | [string](/lsr/value-types.md#string) | No |

### `codec` [v3.1.1-plugins-outputs-exec-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.1.1-plugins-outputs-exec-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.1-plugins-outputs-exec-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 exec outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  exec {
    id => "my_plugin_id"
  }
}
```
