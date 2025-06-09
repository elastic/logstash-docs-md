---
navigation_title: "v3.2.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.2.3-plugins-filters-useragent.html
---

# Useragent filter plugin v3.2.3 [v3.2.3-plugins-filters-useragent]

* Plugin version: v3.2.3
* Released on: 2018-09-24
* [Changelog](https://github.com/logstash-plugins/logstash-filter-useragent/blob/v3.2.3/CHANGELOG.md)

For other versions, see the [overview list](filter-useragent-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2216]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-useragent). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2194]

Parse user agent strings into structured data based on BrowserScope data

UserAgent filter, adds information about user agent like family, operating system, version, and device

Logstash releases ship with the regexes.yaml database made available from ua-parser with an Apache 2.0 license. For more details on ua-parser, see <https://github.com/tobie/ua-parser/>.

## Useragent Filter Configuration Options [v3.2.3-plugins-filters-useragent-options]

This plugin supports the following configuration options plus the [Common options](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`lru_cache_size`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-lru_cache_size) | [number](/lsr/value-types.md#number) | No |
| [`prefix`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-prefix) | [string](/lsr/value-types.md#string) | No |
| [`regexes`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-regexes) | [string](/lsr/value-types.md#string) | No |
| [`source`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-source) | [string](/lsr/value-types.md#string) | Yes |
| [`target`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-common-options) for a list of options supported by all filter plugins.

### `lru_cache_size` [v3.2.3-plugins-filters-useragent-lru_cache_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1000`

UA parsing is surprisingly expensive. This filter uses an LRU cache to take advantage of the fact that user agents are often found adjacent to one another in log files and rarely have a random distribution. The higher you set this the more likely an item is to be in the cache and the faster this filter will run. However, if you set this too high you can use more memory than desired.

Experiment with different values for this option to find the best performance for your dataset.

This MUST be set to a value > 0. There is really no reason to not want this behavior, the overhead is minimal and the speed gains are large.

It is important to note that this config value is global. That is to say all instances of the user agent filter share the same cache. The last declared cache size will *win*. The reason for this is that there would be no benefit to having multiple caches for different instances at different points in the pipeline, that would just increase the number of cache misses and waste memory.

### `prefix` [v3.2.3-plugins-filters-useragent-prefix]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

A string to prepend to all of the extracted keys

### `regexes` [v3.2.3-plugins-filters-useragent-regexes]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

`regexes.yaml` file to use

If not specified, this will default to the `regexes.yaml` that ships with logstash.

You can find the latest version of this here: <https://github.com/ua-parser/uap-core/blob/master/regexes.yaml>

### `source` [v3.2.3-plugins-filters-useragent-source]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field containing the user agent string. If this field is an array, only the first value will be used.

### `target` [v3.2.3-plugins-filters-useragent-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the field to assign user agent data into.

If not specified user agent data will be stored in the root of the event.

## Common options [v3.2.3-plugins-filters-useragent-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-2-3-plugins-filters-useragent.md#v3.2.3-plugins-filters-useragent-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.2.3-plugins-filters-useragent-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      useragent {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      useragent {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.2.3-plugins-filters-useragent-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      useragent {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      useragent {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.2.3-plugins-filters-useragent-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.2.3-plugins-filters-useragent-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 useragent filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      useragent {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.2.3-plugins-filters-useragent-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.2.3-plugins-filters-useragent-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      useragent {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      useragent {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.2.3-plugins-filters-useragent-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      useragent {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      useragent {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
