---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-outputs-redmine.html
---

# Redmine output plugin v3.0.3 [v3.0.3-plugins-outputs-redmine]


* Plugin version: v3.0.3
* Released on: 2017-11-13
* [Changelog](https://github.com/logstash-plugins/logstash-output-redmine/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](output-redmine-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1514]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-redmine). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1504]

The redmine output is used to create a ticket via the API redmine.

It send a POST request in a JSON format and use TOKEN authentication

 — Exemple of use — 

```ruby
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


## Redmine Output Configuration Options [v3.0.3-plugins-outputs-redmine-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`assigned_to_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-assigned_to_id) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`categorie_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-categorie_id) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`description`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-description) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`fixed_version_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-fixed_version_id) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`parent_issue_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-parent_issue_id) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`priority_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-priority_id) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`project_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-project_id) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`ssl`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-ssl) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`status_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-status_id) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`subject`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-subject) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`token`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-token) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`tracker_id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-tracker_id) | [number](logstash://reference/configuration-file-structure.md#number) | Yes |
| [`url`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-url) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-common-options) for a list of options supported by all output plugins.

 

### `assigned_to_id` [v3.0.3-plugins-outputs-redmine-assigned_to_id]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `nil`

redmine issue assigned_to not required for post_issue


### `categorie_id` [v3.0.3-plugins-outputs-redmine-categorie_id]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `nil`

not required for post_issue


### `description` [v3.0.3-plugins-outputs-redmine-description]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{message}}"`

redmine issue description required


### `fixed_version_id` [v3.0.3-plugins-outputs-redmine-fixed_version_id]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `nil`

redmine issue fixed_version_id


### `parent_issue_id` [v3.0.3-plugins-outputs-redmine-parent_issue_id]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `nil`

redmine issue parent_issue_id not required for post_issue


### `priority_id` [v3.0.3-plugins-outputs-redmine-priority_id]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

redmine issue priority_id required


### `project_id` [v3.0.3-plugins-outputs-redmine-project_id]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

redmine issue projet_id required


### `ssl` [v3.0.3-plugins-outputs-redmine-ssl]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`


### `status_id` [v3.0.3-plugins-outputs-redmine-status_id]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

redmine issue status_id required


### `subject` [v3.0.3-plugins-outputs-redmine-subject]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `%{{host}}`

redmine issue subject required


### `token` [v3.0.3-plugins-outputs-redmine-token]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

redmine token user used for authentication


### `tracker_id` [v3.0.3-plugins-outputs-redmine-tracker_id]

* This is a required setting.
* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

redmine issue tracker_id required


### `url` [v3.0.3-plugins-outputs-redmine-url]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

host of redmine app value format : *http://urlofredmine.tld* - Not add */issues* at end



## Common options [v3.0.3-plugins-outputs-redmine-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-outputs-redmine.md#v3.0.3-plugins-outputs-redmine-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.3-plugins-outputs-redmine-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.3-plugins-outputs-redmine-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-outputs-redmine-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 redmine outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  redmine {
    id => "my_plugin_id"
  }
}
```



