---
navigation_title: "v4.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.2-plugins-filters-elapsed.html
---

# Elapsed filter plugin v4.0.2 [v4.0.2-plugins-filters-elapsed]

* Plugin version: v4.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-elapsed/blob/v4.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-elapsed-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1803]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-elapsed). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1781]

The elapsed filter tracks a pair of start/end events and uses their timestamps to calculate the elapsed time between them.

The filter has been developed to track the execution time of processes and other long tasks.

The configuration looks like this:

```
    filter {
      elapsed {
        start_tag => "start event tag"
        end_tag => "end event tag"
        unique_id_field => "id field name"
        timeout => seconds
        new_event_on_match => true/false
      }
    }
```

The events managed by this filter must have some particular properties. The event describing the start of the task (the "start event") must contain a tag equal to `start_tag`. On the other side, the event describing the end of the task (the "end event") must contain a tag equal to `end_tag`. Both these two kinds of event need to own an ID field which identify uniquely that particular task. The name of this field is stored in `unique_id_field`.

You can use a Grok filter to prepare the events for the elapsed filter. An example of configuration can be:

```
    filter {
      grok {
        match => { "message" => "%{TIMESTAMP_ISO8601} START id: (?<task_id>.*)" }
        add_tag => [ "taskStarted" ]
      }
```

```
grok {
  match => { "message" => "%{TIMESTAMP_ISO8601} END id: (?<task_id>.*)" }
  add_tag => [ "taskTerminated" ]
}
```

```
  elapsed {
    start_tag => "taskStarted"
    end_tag => "taskTerminated"
    unique_id_field => "task_id"
  }
}
```

The elapsed filter collects all the "start events". If two, or more, "start events" have the same ID, only the first one is recorded, the others are discarded.

When an "end event" matching a previously collected "start event" is received, there is a match. The configuration property `new_event_on_match` tells where to insert the elapsed information: they can be added to the "end event" or a new "match event" can be created. Both events store the following information:

* the tags `elapsed` and `elapsed_match`
* the field `elapsed_time` with the difference, in seconds, between the two events timestamps
* an ID filed with the task ID
* the field `elapsed_timestamp_start` with the timestamp of the start event

If the "end event" does not arrive before "timeout" seconds, the "start event" is discarded and an "expired event" is generated. This event contains:

* the tags `elapsed` and `elapsed_expired_error`
* a field called `elapsed_time` with the age, in seconds, of the "start event"
* an ID filed with the task ID
* the field `elapsed_timestamp_start` with the timestamp of the "start event"

## Elapsed Filter Configuration Options [v4.0.2-plugins-filters-elapsed-options]

This plugin supports the following configuration options plus the [Common options](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`end_tag`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-end_tag) | [string](/lsr/value-types.md#string) | Yes |
| [`new_event_on_match`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-new_event_on_match) | [boolean](/lsr/value-types.md#boolean) | No |
| [`start_tag`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-start_tag) | [string](/lsr/value-types.md#string) | Yes |
| [`timeout`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-timeout) | [number](/lsr/value-types.md#number) | No |
| [`unique_id_field`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-unique_id_field) | [string](/lsr/value-types.md#string) | Yes |

Also see [Common options](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-common-options) for a list of options supported by all filter plugins.

### `end_tag` [v4.0.2-plugins-filters-elapsed-end_tag]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the tag identifying the "end event"

### `new_event_on_match` [v4.0.2-plugins-filters-elapsed-new_event_on_match]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

This property manage what to do when an "end event" matches a "start event". If it’s set to `false` (default value), the elapsed information are added to the "end event"; if it’s set to `true` a new "match event" is created.

### `start_tag` [v4.0.2-plugins-filters-elapsed-start_tag]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the tag identifying the "start event"

### `timeout` [v4.0.2-plugins-filters-elapsed-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1800`

The amount of seconds after an "end event" can be considered lost. The corresponding "start event" is discarded and an "expired event" is generated. The default value is 30 minutes (1800 seconds).

### `unique_id_field` [v4.0.2-plugins-filters-elapsed-unique_id_field]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The name of the field containing the task ID. This value must uniquely identify the task in the system, otherwise it’s impossible to match the couple of events.

## Common options [v4.0.2-plugins-filters-elapsed-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-0-2-plugins-filters-elapsed.md#v4.0.2-plugins-filters-elapsed-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.0.2-plugins-filters-elapsed-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      elapsed {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      elapsed {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.0.2-plugins-filters-elapsed-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      elapsed {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      elapsed {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.0.2-plugins-filters-elapsed-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.2-plugins-filters-elapsed-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elapsed filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      elapsed {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.0.2-plugins-filters-elapsed-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.0.2-plugins-filters-elapsed-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      elapsed {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      elapsed {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.0.2-plugins-filters-elapsed-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      elapsed {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      elapsed {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
