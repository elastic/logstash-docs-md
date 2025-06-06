---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-redmine.html
---

# Redmine output plugin v3.0.3 [v3.0.3-plugins-outputs-redmine]

* Plugin version: v3.0.3
* Released on: 2017-11-13
* [Changelog](https://github.com/logstash-plugins/logstash-output-redmine/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-redmine-index.md "Versioned redmine output plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1523]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-redmine). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1513]

The redmine output is used to create a ticket via the API redmine.

It send a POST request in a JSON format and use TOKEN authentication

 — Exemple of use — 

```
 output {
   redmine {
     url => "http://redmineserver.tld"
     token => 'token'
     project_id => 200
     tracker_id => 1
     status_id => 3
     priority_id => 2
     subject => "Error ... detected"
   }
 }
```

### Redmine Output Configuration Options [v3.0.3-plugins-outputs-redmine-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`assigned_to_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-assigned_to_id "assigned_to_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`categorie_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-categorie_id "categorie_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`description`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-description "description") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`fixed_version_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-fixed_version_id "fixed_version_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`parent_issue_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-parent_issue_id "parent_issue_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`priority_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-priority_id "priority_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | Yes |
| [`project_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-project_id "project_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | Yes |
| [`ssl`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-ssl "ssl") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`status_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-status_id "status_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | Yes |
| [`subject`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-subject "subject") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`token`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-token "token") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`tracker_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-tracker_id "tracker_id") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | Yes |
| [`url`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-url "url") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |

Also see [Common options](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-common-options "Common options") for a list of options supported by all output plugins.

 

#### `assigned_to_id` [v3.0.3-plugins-outputs-redmine-assigned_to_id]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `nil`

redmine issue assigned\_to not required for post\_issue

#### `categorie_id` [v3.0.3-plugins-outputs-redmine-categorie_id]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `nil`

not required for post\_issue

#### `description` [v3.0.3-plugins-outputs-redmine-description]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"%{message}"`

redmine issue description required

#### `fixed_version_id` [v3.0.3-plugins-outputs-redmine-fixed_version_id]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `nil`

redmine issue fixed\_version\_id

#### `parent_issue_id` [v3.0.3-plugins-outputs-redmine-parent_issue_id]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `nil`

redmine issue parent\_issue\_id not required for post\_issue

#### `priority_id` [v3.0.3-plugins-outputs-redmine-priority_id]

* This is a required setting.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

redmine issue priority\_id required

#### `project_id` [v3.0.3-plugins-outputs-redmine-project_id]

* This is a required setting.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

redmine issue projet\_id required

#### `ssl` [v3.0.3-plugins-outputs-redmine-ssl]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

#### `status_id` [v3.0.3-plugins-outputs-redmine-status_id]

* This is a required setting.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

redmine issue status\_id required

#### `subject` [v3.0.3-plugins-outputs-redmine-subject]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"%{host}"`

redmine issue subject required

#### `token` [v3.0.3-plugins-outputs-redmine-token]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

redmine token user used for authentication

#### `tracker_id` [v3.0.3-plugins-outputs-redmine-tracker_id]

* This is a required setting.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

redmine issue tracker\_id required

#### `url` [v3.0.3-plugins-outputs-redmine-url]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

host of redmine app value format : *<http://urlofredmine.tld>* - Not add */issues* at end

### Common options [v3.0.3-plugins-outputs-redmine-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`codec`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `codec` [v3.0.3-plugins-outputs-redmine-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v3.0.3-plugins-outputs-redmine-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v3.0.3-plugins-outputs-redmine-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 redmine outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
output {
  redmine {
    id => "my_plugin_id"
  }
}
```
