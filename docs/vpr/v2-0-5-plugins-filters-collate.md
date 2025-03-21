---
navigation_title: "v2.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.5-plugins-filters-collate.html
---

# Collate filter plugin v2.0.5 [v2.0.5-plugins-filters-collate]


* Plugin version: v2.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-collate/blob/v2.0.5/CHANGELOG.md)

For other versions, see the [overview list](filter-collate-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1724]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-collate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1702]

Collate events by time or count.

The original goal of this filter was to merge the logs from different sources by the time of log, for example, in real-time log collection, logs can be collated by amount of 3000 logs or can be collated in 30 seconds.

The config looks like this:

```ruby
    filter {
      collate {
        count => 3000
        interval => "30s"
        order => "ascending"
      }
    }
```


## Collate Filter Configuration Options [v2.0.5-plugins-filters-collate-options]

This plugin supports the following configuration options plus the [Common options](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`count`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-count) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`interval`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-interval) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`order`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-order) | [string](logstash://reference/configuration-file-structure.md#string), one of `["ascending", "descending"]` | No |

Also see [Common options](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-common-options) for a list of options supported by all filter plugins.

 

### `count` [v2.0.5-plugins-filters-collate-count]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

How many logs should be collated.


### `interval` [v2.0.5-plugins-filters-collate-interval]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1m"`

The `interval` is the time window which how long the logs should be collated. (default `1m`)


### `order` [v2.0.5-plugins-filters-collate-order]

* Value can be any of: `ascending`, `descending`
* Default value is `"ascending"`

The `order` collated events should appear in.



## Common options [v2.0.5-plugins-filters-collate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v2-0-5-plugins-filters-collate.md#v2.0.5-plugins-filters-collate-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v2.0.5-plugins-filters-collate-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      collate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      collate {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v2.0.5-plugins-filters-collate-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      collate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      collate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v2.0.5-plugins-filters-collate-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.0.5-plugins-filters-collate-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 collate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      collate {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v2.0.5-plugins-filters-collate-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v2.0.5-plugins-filters-collate-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      collate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      collate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v2.0.5-plugins-filters-collate-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      collate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      collate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



