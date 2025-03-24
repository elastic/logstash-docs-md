---
navigation_title: "v3.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.2-plugins-outputs-jira.html
---

# Jira output plugin v3.0.2 [v3.0.2-plugins-outputs-jira]


* Plugin version: v3.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-output-jira/blob/v3.0.2/CHANGELOG.md)

For other versions, see the [overview list](output-jira-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1331]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-jira). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1321]

This output allows you to use Logstash to parse and structure your logs and ship structured event data to JIRA.

Structured event data will be added to the JIRA issue as *Description* field value.

Example JSON-encoded event:

```yaml
    {
      "message": "Hello JIRA!",
      "@version": "1",
      "@timestamp": "2015-06-04T10:23:30.279Z",
      "type": "syslog",
      "host": "192.168.1.42",
      "syslog_pri": "11",
      "syslog_timestamp": "Jun  4 14:23:30",
      "syslog_host": "myhost",
      "program": "root",
      "syslog_severity_code": 3,
      "syslog_facility_code": 1,
      "syslog_facility": "user-level",
      "syslog_severity": "error"
    }
```

Example JIRA issue created the event above:

```shell
    Type:        Task
    Priority:    2 - Major
    Status:      TO DO
    Resolution:  Unresolved
    Summary:     [logstash] Hello JIRA!
    Description:
        ---
        message: Hello JIRA!
        '@version': '1'
        '@timestamp': 2015-06-04 10:23:30.279000000 Z
        type: syslog
        host: 192.168.1.42
        syslog_pri: '11'
        syslog_timestamp: Jun 4 14:23:30
        syslog_host: myhost
        program: root
        syslog_severity_code: 3
        syslog_facility_code: 1
        syslog_facility: user-level
        syslog_severity: error
```

To use this output you’ll need to ensure that your JIRA instance allows REST calls.

This output uses `jiralicious` as the bridge to JIRA By Martin Cleaver, Blended Perspectives with a lot of help from *electrical* in #logstash.

Origin [https://groups.google.com/forum/#!msg/logstash-users/exgrB4iQ-mw/R34apku5nXsJ](https://groups.google.com/forum/#!msg/logstash-users/exgrB4iQ-mw/R34apku5nXsJ) and [https://botbot.me/freenode/logstash/msg/4169496/](https://botbot.me/freenode/logstash/msg/4169496/) via [https://gist.github.com/electrical/4660061e8fff11cdcf37#file-jira-rb](https://gist.github.com/electrical/4660061e8fff11cdcf37#file-jira-rb).


## Jira Output Configuration Options [v3.0.2-plugins-outputs-jira-options]

This plugin supports the following configuration options plus the [Common options](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`assignee`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-assignee) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`host`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-host) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`issuetypeid`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-issuetypeid) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`password`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-password) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`priority`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-priority) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`projectid`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-projectid) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`reporter`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-reporter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`summary`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-summary) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`username`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-username) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-common-options) for a list of options supported by all output plugins.

 

### `assignee` [v3.0.2-plugins-outputs-jira-assignee]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JIRA Reporter


### `host` [v3.0.2-plugins-outputs-jira-host]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The hostname to send logs to. This should target your JIRA server and has to have the REST interface enabled.


### `issuetypeid` [v3.0.2-plugins-outputs-jira-issuetypeid]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JIRA Issuetype number


### `password` [v3.0.2-plugins-outputs-jira-password]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.


### `priority` [v3.0.2-plugins-outputs-jira-priority]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JIRA Priority


### `projectid` [v3.0.2-plugins-outputs-jira-projectid]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Javalicious has no proxy support JIRA Project number


### `reporter` [v3.0.2-plugins-outputs-jira-reporter]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JIRA Reporter


### `summary` [v3.0.2-plugins-outputs-jira-summary]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JIRA Summary

Truncated and appended with *…​* if longer than 255 characters.


### `username` [v3.0.2-plugins-outputs-jira-username]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.



## Common options [v3.0.2-plugins-outputs-jira-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-2-plugins-outputs-jira.md#v3.0.2-plugins-outputs-jira-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.2-plugins-outputs-jira-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.2-plugins-outputs-jira-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.2-plugins-outputs-jira-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 jira outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  jira {
    id => "my_plugin_id"
  }
}
```



