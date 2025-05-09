---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-ruby.html
---

# Ruby filter plugin v3.0.3 [v3.0.3-plugins-filters-ruby]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-ruby/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-ruby-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2129]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-ruby). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2107]

Execute ruby code.

For example, to cancel 90% of events, you can do this:

```ruby
    filter {
      ruby {
        # Cancel 90% of events
        code => "event.cancel if rand <= 0.90"
      }
    }
```

If you need to create additional events, it cannot be done as in other filters where you would use `yield`, you must use a specific syntax `new_event_block.call(event)` like in this example duplicating the input event

```ruby
filter {
  ruby {
    code => "new_event_block.call(event.clone)"
  }
}
```


## Ruby Filter Configuration Options [v3.0.3-plugins-filters-ruby-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`code`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-code) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`init`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-init) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-common-options) for a list of options supported by all filter plugins.

 

### `code` [v3.0.3-plugins-filters-ruby-code]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The code to execute for every event. You will have an `event` variable available that is the event itself. See the [Event API](logstash://reference/event-api.md) for more information.


### `init` [v3.0.3-plugins-filters-ruby-init]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Any code to execute at logstash startup-time



## Common options [v3.0.3-plugins-filters-ruby-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-ruby.md#v3.0.3-plugins-filters-ruby-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-ruby-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      ruby {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      ruby {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.3-plugins-filters-ruby-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      ruby {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      ruby {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.3-plugins-filters-ruby-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-filters-ruby-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 ruby filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      ruby {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.3-plugins-filters-ruby-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.3-plugins-filters-ruby-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      ruby {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      ruby {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.3-plugins-filters-ruby-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      ruby {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      ruby {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



