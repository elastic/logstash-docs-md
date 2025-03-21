---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-filters-sleep.html
---

# Sleep filter plugin v3.0.6 [v3.0.6-plugins-filters-sleep]


* Plugin version: v3.0.6
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-sleep/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](filter-sleep-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2131]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-sleep). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2109]

Sleep a given amount of time. This will cause logstash to stall for the given amount of time. This is useful for rate limiting, etc.


## Sleep Filter Configuration Options [v3.0.6-plugins-filters-sleep-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`every`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-every) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`replay`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-replay) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`time`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-time) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-common-options) for a list of options supported by all filter plugins.

 

### `every` [v3.0.6-plugins-filters-sleep-every]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `1`

Sleep on every N’th. This option is ignored in replay mode.

Example:

```ruby
    filter {
      sleep {
        time => "1"   # Sleep 1 second
        every => 10   # on every 10th event
      }
    }
```


### `replay` [v3.0.6-plugins-filters-sleep-replay]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enable replay mode.

Replay mode tries to sleep based on timestamps in each event.

The amount of time to sleep is computed by subtracting the previous event’s timestamp from the current event’s timestamp. This helps you replay events in the same timeline as original.

If you specify a `time` setting as well, this filter will use the `time` value as a speed modifier. For example, a `time` value of 2 will replay at double speed, while a value of 0.25 will replay at 1/4th speed.

For example:

```ruby
    filter {
      sleep {
        time => 2
        replay => true
      }
    }
```

The above will sleep in such a way that it will perform replay 2-times faster than the original time speed.


### `time` [v3.0.6-plugins-filters-sleep-time]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The length of time to sleep, in seconds, for every event.

This can be a number (eg, 0.5), or a string (eg, `%{{foo}}`) The second form (string with a field value) is useful if you have an attribute of your event that you want to use to indicate the amount of time to sleep.

Example:

```ruby
    filter {
      sleep {
        # Sleep 1 second for every event.
        time => "1"
      }
    }
```



## Common options [v3.0.6-plugins-filters-sleep-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-6-plugins-filters-sleep.md#v3.0.6-plugins-filters-sleep-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.6-plugins-filters-sleep-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      sleep {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      sleep {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.6-plugins-filters-sleep-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      sleep {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      sleep {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.6-plugins-filters-sleep-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-filters-sleep-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 sleep filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      sleep {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.6-plugins-filters-sleep-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.6-plugins-filters-sleep-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      sleep {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      sleep {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.6-plugins-filters-sleep-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      sleep {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      sleep {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



