---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-prune.html
---

# Prune filter plugin v3.0.3 [v3.0.3-plugins-filters-prune]


* Plugin version: v3.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-prune/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-prune-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2111]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-prune). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2089]

The prune filter is for removing fields from events based on whitelists or blacklist of field names or their values (names and values can also be regular expressions).

This can e.g. be useful if you have a [json](/lsr/plugins-filters-json.md) or [kv](/lsr/plugins-filters-kv.md) filter that creates a number of fields with names that you don’t necessarily know the names of beforehand, and you only want to keep a subset of them.

Usage help: To specify a exact field name or value use the regular expression syntax `^some_name_or_value$`. Example usage: Input data `{ "msg":"hello world", "msg_short":"hw" }`

```ruby
    filter {
      prune {
        whitelist_names => [ "msg" ]
      }
    }
Allows both `"msg"` and `"msg_short"` through.
```

While:

```ruby
    filter {
      prune {
        whitelist_names => ["^msg$"]
      }
    }
Allows only `"msg"` through.
```

Logstash stores an event’s `tags` as a field which is subject to pruning. Remember to `whitelist_names => [ "^tags$" ]` to maintain `tags` after pruning or use `blacklist_values => [ "^tag_name$" ]` to eliminate a specific `tag`.

::::{note}
This filter currently only support operations on top-level fields, i.e. whitelisting and blacklisting of subfields based on name or value does not work.
::::



## Prune Filter Configuration Options [v3.0.3-plugins-filters-prune-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`blacklist_names`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-blacklist_names) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`blacklist_values`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-blacklist_values) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`interpolate`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-interpolate) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`whitelist_names`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-whitelist_names) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`whitelist_values`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-whitelist_values) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |

Also see [Common options](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-common-options) for a list of options supported by all filter plugins.

 

### `blacklist_names` [v3.0.3-plugins-filters-prune-blacklist_names]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["%{[^}]+}"]`

Exclude fields whose names match specified regexps, by default exclude unresolved `%{{field}}` strings.

```ruby
    filter {
      prune {
        blacklist_names => [ "method", "(referrer|status)", "${some}_field" ]
      }
    }
```


### `blacklist_values` [v3.0.3-plugins-filters-prune-blacklist_values]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Exclude specified fields if their values match one of the supplied regular expressions. In case field values are arrays, each array item is matched against the regular expressions and matching array items will be excluded.

```ruby
    filter {
      prune {
        blacklist_values => [ "uripath", "/index.php",
                              "method", "(HEAD|OPTIONS)",
                              "status", "^[^2]" ]
      }
    }
```


### `interpolate` [v3.0.3-plugins-filters-prune-interpolate]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Trigger whether configuration fields and values should be interpolated for dynamic values (when resolving `%{{some_field}}`). Probably adds some performance overhead. Defaults to false.


### `whitelist_names` [v3.0.3-plugins-filters-prune-whitelist_names]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Include only fields only if their names match specified regexps, default to empty list which means include everything.

```ruby
    filter {
      prune {
        whitelist_names => [ "method", "(referrer|status)", "${some}_field" ]
      }
    }
```


### `whitelist_values` [v3.0.3-plugins-filters-prune-whitelist_values]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Include specified fields only if their values match one of the supplied regular expressions. In case field values are arrays, each array item is matched against the regular expressions and only matching array items will be included.

```ruby
    filter {
      prune {
        whitelist_values => [ "uripath", "/index.php",
                              "method", "(GET|POST)",
                              "status", "^[^2]" ]
      }
    }
```



## Common options [v3.0.3-plugins-filters-prune-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-prune.md#v3.0.3-plugins-filters-prune-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-prune-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      prune {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      prune {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.3-plugins-filters-prune-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      prune {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      prune {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.3-plugins-filters-prune-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-filters-prune-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 prune filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      prune {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.3-plugins-filters-prune-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.3-plugins-filters-prune-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      prune {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      prune {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.3-plugins-filters-prune-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      prune {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      prune {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



