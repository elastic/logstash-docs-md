---
navigation_title: "v4.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.2-plugins-filters-throttle.html
---

# Throttle filter plugin v4.0.2 [v4.0.2-plugins-filters-throttle]

* Plugin version: v4.0.2
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-throttle/blob/v4.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-throttle-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2180]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-throttle). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2158]

The throttle filter is for throttling the number of events. The filter is configured with a lower bound, the "before\_count", and upper bound, the "after\_count", and a period of time. All events passing through the filter will be counted based on their key and the event timestamp. As long as the count is less than the "before\_count" or greater than the "after\_count", the event will be "throttled" which means the filter will be considered successful and any tags or fields will be added (or removed).

The plugin is thread-safe and properly tracks past events.

For example, if you wanted to throttle events so you only receive an event after 2 occurrences and you get no more than 3 in 10 minutes, you would use the configuration:

```
    period => 600
    max_age => 1200
    before_count => 3
    after_count => 5
```

Which would result in:

```
event 1 - throttled (successful filter, period start)
event 2 - throttled (successful filter)
event 3 - not throttled
event 4 - not throttled
event 5 - not throttled
event 6 - throttled (successful filter)
event 7 - throttled (successful filter)
event x - throttled (successful filter)
period end
event 1 - throttled (successful filter, period start)
event 2 - throttled (successful filter)
event 3 - not throttled
event 4 - not throttled
event 5 - not throttled
event 6 - throttled (successful filter)
...
```

Another example is if you wanted to throttle events so you only receive 1 event per hour, you would use the configuration:

```
    period => 3600
    max_age => 7200
    before_count => -1
    after_count => 1
```

Which would result in:

```
event 1 - not throttled (period start)
event 2 - throttled (successful filter)
event 3 - throttled (successful filter)
event 4 - throttled (successful filter)
event x - throttled (successful filter)
period end
event 1 - not throttled (period start)
event 2 - throttled (successful filter)
event 3 - throttled (successful filter)
event 4 - throttled (successful filter)
...
```

A common use case would be to use the throttle filter to throttle events before 3 and after 5 while using multiple fields for the key and then use the drop filter to remove throttled events. This configuration might appear as:

```
    filter {
      throttle {
        before_count => 3
        after_count => 5
        period => 3600
        max_age => 7200
        key => "%{host}%{message}"
        add_tag => "throttled"
      }
      if "throttled" in [tags] {
        drop { }
      }
    }
```

Another case would be to store all events, but only email non-throttled events so the op’s inbox isn’t flooded with emails in the event of a system error. This configuration might appear as:

```
    filter {
      throttle {
        before_count => 3
        after_count => 5
        period => 3600
        max_age => 7200
        key => "%{message}"
        add_tag => "throttled"
      }
    }
    output {
      if "throttled" not in [tags] {
        email {
          from => "logstash@mycompany.com"
          subject => "Production System Alert"
          to => "ops@mycompany.com"
          via => "sendmail"
          body => "Alert on %{host} from path %{path}:\n\n%{message}"
          options => { "location" => "/usr/sbin/sendmail" }
        }
      }
      elasticsearch_http {
        host => "localhost"
        port => "19200"
      }
    }
```

When an event is received, the event key is stored in a key\_cache. The key references a timeslot\_cache. The event is allocated to a timeslot (created dynamically) based on the timestamp of the event. The timeslot counter is incremented. When the next event is received (same key), within the same "period", it is allocated to the same timeslot. The timeslot counter is incremented once again.

The timeslot expires if the maximum age has been exceeded. The age is calculated based on the latest event timestamp and the max\_age configuration option.

```
---[::.. DESIGN ..::]---
```

`- [key_cache] -` `-- [timeslot_cache] --` | | | @created: 1439839636 | | @latest: 1439839836 | \[a.b.c] ⇒ `----------------------` | \[1439839636] ⇒ 1 | | \[1439839736] ⇒ 3 | | \[1439839836] ⇒ 2 | `----------------------`

```
                   +-- [timeslot_cache] --+
                   | @created: eeeeeeeeee |
                   | @latest:  llllllllll |
   [x.y.z]  =>     +----------------------+
                   | [0000000060] => x    |
                   | [0000000120] => y    |
|               |  | [..........] => N    |
+---------------+  +----------------------+
```

Frank de Jong (@frapex) Mike Pilone (@mikepilone)

only update if greater than current

## Throttle Filter Configuration Options [v4.0.2-plugins-filters-throttle-options]

This plugin supports the following configuration options plus the [Common options](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`after_count`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-after_count) | [number](/lsr/value-types.md#number) | No |
| [`before_count`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-before_count) | [number](/lsr/value-types.md#number) | No |
| [`key`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-key) | [string](/lsr/value-types.md#string) | Yes |
| [`max_age`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-max_age) | [number](/lsr/value-types.md#number) | No |
| [`max_counters`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-max_counters) | [number](/lsr/value-types.md#number) | No |
| [`period`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-period) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-common-options) for a list of options supported by all filter plugins.

### `after_count` [v4.0.2-plugins-filters-throttle-after_count]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `-1`

Events greater than this count will be throttled. Setting this value to -1, the default, will cause no events to be throttled based on the upper bound.

### `before_count` [v4.0.2-plugins-filters-throttle-before_count]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `-1`

Events less than this count will be throttled. Setting this value to -1, the default, will cause no events to be throttled based on the lower bound.

### `key` [v4.0.2-plugins-filters-throttle-key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The key used to identify events. Events with the same key are grouped together. Field substitutions are allowed, so you can combine multiple fields.

### `max_age` [v4.0.2-plugins-filters-throttle-max_age]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3600`

The maximum age of a timeslot. Higher values allow better tracking of an asynchronous flow of events, but require more memory. As a rule of thumb you should set this value to at least twice the period. Or set this value to period + maximum time offset between unordered events with the same key. Values below the specified period give unexpected results if unordered events are processed simultaneously.

### `max_counters` [v4.0.2-plugins-filters-throttle-max_counters]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `100000`

The maximum number of counters to store before decreasing the maximum age of a timeslot. Setting this value to -1 will prevent an upper bound with no constraint on the number of counters. This configuration value should only be used as a memory control mechanism and can cause early counter expiration if the value is reached. It is recommended to leave the default value and ensure that your key is selected such that it limits the number of counters required (i.e. don’t use UUID as the key).

### `period` [v4.0.2-plugins-filters-throttle-period]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"60"`

The period in seconds after the first occurrence of an event until a new timeslot is created. This period is tracked per unique key and per timeslot. Field substitutions are allowed in this value. This allows you to specify that certain kinds of events throttle for a specific period of time.

## Common options [v4.0.2-plugins-filters-throttle-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-0-2-plugins-filters-throttle.md#v4.0.2-plugins-filters-throttle-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.0.2-plugins-filters-throttle-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      throttle {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      throttle {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.0.2-plugins-filters-throttle-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      throttle {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      throttle {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.0.2-plugins-filters-throttle-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.2-plugins-filters-throttle-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 throttle filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      throttle {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.0.2-plugins-filters-throttle-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.0.2-plugins-filters-throttle-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      throttle {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      throttle {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.0.2-plugins-filters-throttle-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      throttle {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      throttle {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
