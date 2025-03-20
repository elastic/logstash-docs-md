---
navigation_title: "v3.1.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.1-plugins-filters-syslog_pri.html
---

# Syslog_pri filter plugin v3.1.1 [v3.1.1-plugins-filters-syslog_pri]


* Plugin version: v3.1.1
* Released on: 2021-11-10
* [Changelog](https://github.com/logstash-plugins/logstash-filter-syslog_pri/blob/v3.1.1/CHANGELOG.md)

For other versions, see the [overview list](filter-syslog_pri-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2143]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-syslog_pri). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2121]

Filter plugin for logstash to parse the `PRI` field from the front of a Syslog (RFC3164) message.  If no priority is set, it will default to 13 (per RFC).

This filter is based on the original `syslog.rb` code shipped with logstash.


## Syslog_pri Filter Configuration Options [v3.1.1-plugins-filters-syslog_pri-options]

This plugin supports the following configuration options plus the [Common options](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`ecs_compatibility`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`facility_labels`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-facility_labels) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`severity_labels`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-severity_labels) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`syslog_pri_field_name`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-syslog_pri_field_name) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`use_labels`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-use_labels) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-common-options) for a list of options supported by all filter plugins.

 

### `ecs_compatibility` [v3.1.1-plugins-filters-syslog_pri-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: does not use ECS-compatible field names (for example, `syslog_severity_code` for syslog severity)
    * `v1`, `v8`: uses fields that are compatible with Elastic Common Schema (for example, `[log][syslog][severity][code]`)

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`.


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)](ecs://docs/reference/index.md)). The value of this setting affects the *default* value of [`syslog_pri_field_name`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-syslog_pri_field_name).


### `facility_labels` [v3.1.1-plugins-filters-syslog_pri-facility_labels]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["kernel", "user-level", "mail", "daemon", "security/authorization", "syslogd", "line printer", "network news", "uucp", "clock", "security/authorization", "ftp", "ntp", "log audit", "log alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]`

Labels for facility levels. This comes from RFC3164.


### `severity_labels` [v3.1.1-plugins-filters-syslog_pri-severity_labels]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["emergency", "alert", "critical", "error", "warning", "notice", "informational", "debug"]`

Labels for severity levels. This comes from RFC3164.


### `syslog_pri_field_name` [v3.1.1-plugins-filters-syslog_pri-syslog_pri_field_name]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: `"syslog_pri"`
    * ECS Compatibility enabled: `"[log][syslog][priority]"`


Name of field which passes in the extracted PRI part of the syslog message


### `use_labels` [v3.1.1-plugins-filters-syslog_pri-use_labels]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

set the status to experimental/beta/stable Add human-readable names after parsing severity and facility from PRI



## Common options [v3.1.1-plugins-filters-syslog_pri-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-1-1-plugins-filters-syslog_pri.md#v3.1.1-plugins-filters-syslog_pri-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.1.1-plugins-filters-syslog_pri-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      syslog_pri {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      syslog_pri {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.1.1-plugins-filters-syslog_pri-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      syslog_pri {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      syslog_pri {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.1.1-plugins-filters-syslog_pri-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.1-plugins-filters-syslog_pri-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 syslog_pri filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      syslog_pri {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.1.1-plugins-filters-syslog_pri-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.1.1-plugins-filters-syslog_pri-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      syslog_pri {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      syslog_pri {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.1.1-plugins-filters-syslog_pri-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      syslog_pri {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      syslog_pri {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



