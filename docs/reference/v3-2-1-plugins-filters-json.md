---
navigation_title: "v3.2.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.1-plugins-filters-json.html
---

# JSON filter plugin v3.2.1 [v3.2.1-plugins-filters-json]


* Plugin version: v3.2.1
* Released on: 2023-12-18
* [Changelog](https://github.com/logstash-plugins/logstash-filter-json/blob/v3.2.1/CHANGELOG.md)

For other versions, see the [overview list](filter-json-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2042]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-json). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2020]

This is a JSON parsing filter. It takes an existing field which contains JSON and expands it into an actual data structure within the Logstash event.

By default, it will place the parsed JSON in the root (top level) of the Logstash event, but this filter can be configured to place the JSON into any arbitrary event field, using the `target` configuration.

This plugin has a few fallback scenarios when something bad happens during the parsing of the event. If the JSON parsing fails on the data, the event will be untouched and it will be tagged with `_jsonparsefailure`; you can then use conditionals to clean the data. You can configure this tag with the `tag_on_failure` option.

If the parsed data contains a `@timestamp` field, the plugin will try to use it for the events `@timestamp`, and if the parsing fails, the field will be renamed to `_@timestamp` and the event will be tagged with a `_timestampparsefailure`.


## Event Metadata and the Elastic Common Schema (ECS) [v3.2.1-plugins-filters-json-ecs_metadata]

The plugin behaves the same regardless of ECS compatibility, except giving a warning when ECS is enabled and `target` isn’t set.

::::{tip}
Set the `target` option to avoid potential schema conflicts.
::::



## JSON Filter Configuration Options [v3.2.1-plugins-filters-json-options]

This plugin supports the following configuration options plus the [Common options](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`ecs_compatibility`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`skip_on_invalid_json`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-skip_on_invalid_json) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`source`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-source) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`tag_on_failure`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`target`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-common-options) for a list of options supported by all filter plugins.

 

### `ecs_compatibility` [v3.2.1-plugins-filters-json-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: does not use ECS-compatible field names
    * `v1`: Elastic Common Schema compliant behavior (warns when `target` isn’t set)


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). See [Event Metadata and the Elastic Common Schema (ECS)](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-ecs_metadata) for detailed information.


### `skip_on_invalid_json` [v3.2.1-plugins-filters-json-skip_on_invalid_json]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Allows for skipping the filter on invalid JSON (this allows you to handle JSON and non-JSON data without warnings)


### `source` [v3.2.1-plugins-filters-json-source]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The configuration for the JSON filter:

```ruby
    source => source_field
```

For example, if you have JSON data in the `message` field:

```ruby
    filter {
      json {
        source => "message"
      }
    }
```

The above would parse the JSON from the `message` field.


### `tag_on_failure` [v3.2.1-plugins-filters-json-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_jsonparsefailure"]`

Append values to the `tags` field when there has been no successful match


### `target` [v3.2.1-plugins-filters-json-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Define the target field for placing the parsed data. If this setting is omitted, the JSON data will be stored at the root (top level) of the event.

For example, if you want the data to be put in the `doc` field:

```ruby
    filter {
      json {
        target => "doc"
      }
    }
```

JSON in the value of the `source` field will be expanded into a data structure in the `target` field.

::::{note}
if the `target` field already exists, it will be overwritten!
::::




## Common options [v3.2.1-plugins-filters-json-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-2-1-plugins-filters-json.md#v3.2.1-plugins-filters-json-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.2.1-plugins-filters-json-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      json {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      json {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.2.1-plugins-filters-json-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      json {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      json {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.2.1-plugins-filters-json-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.2.1-plugins-filters-json-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 json filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      json {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.2.1-plugins-filters-json-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.2.1-plugins-filters-json-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      json {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      json {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.2.1-plugins-filters-json-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      json {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      json {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



