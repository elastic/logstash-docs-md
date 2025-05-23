---
navigation_title: "v2.7.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.7.1-plugins-filters-aggregate.html
---

# Aggregate filter plugin v2.7.1 [v2.7.1-plugins-filters-aggregate]


* Plugin version: v2.7.1
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-aggregate/blob/v2.7.1/CHANGELOG.md)

For other versions, see the [overview list](filter-aggregate-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1684]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-aggregate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [v2.7.1-plugins-filters-aggregate-description]

The aim of this filter is to aggregate information available among several events (typically log lines) belonging to a same task, and finally push aggregated information into final task event.

You should be very careful to set Logstash filter workers to 1 (`-w 1` flag) for this filter to work correctly otherwise events may be processed out of sequence and unexpected results will occur.


## Example #1 [v2.7.1-plugins-filters-aggregate-example1]

* with these given logs :

```ruby
 INFO - 12345 - TASK_START - start
 INFO - 12345 - SQL - sqlQuery1 - 12
 INFO - 12345 - SQL - sqlQuery2 - 34
 INFO - 12345 - TASK_END - end
```

* you can aggregate "sql duration" for the whole task with this configuration :

```ruby
 filter {
   grok {
     match => [ "message", "%{LOGLEVEL:loglevel} - %{NOTSPACE:taskid} - %{NOTSPACE:logger} - %{WORD:label}( - %{INT:duration:int})?" ]
   }

   if [logger] == "TASK_START" {
     aggregate {
       task_id => "%{taskid}"
       code => "map['sql_duration'] = 0"
       map_action => "create"
     }
   }

   if [logger] == "SQL" {
     aggregate {
       task_id => "%{taskid}"
       code => "map['sql_duration'] += event.get('duration')"
       map_action => "update"
     }
   }

   if [logger] == "TASK_END" {
     aggregate {
       task_id => "%{taskid}"
       code => "event.set('sql_duration', map['sql_duration'])"
       map_action => "update"
       end_of_task => true
       timeout => 120
     }
   }
 }
```

* the final event then looks like :

```ruby
{
  "message" => "INFO - 12345 - TASK_END - end message",
  "sql_duration" => 46
}
```

the field `sql_duration` is added and contains the sum of all sql queries durations.


## Example #2 : no start event [v2.7.1-plugins-filters-aggregate-example2]

* If you have the same logs than example #1, but without a start log :

```ruby
 INFO - 12345 - SQL - sqlQuery1 - 12
 INFO - 12345 - SQL - sqlQuery2 - 34
 INFO - 12345 - TASK_END - end
```

* you can also aggregate "sql duration" with a slightly different configuration :

```ruby
 filter {
   grok {
     match => [ "message", "%{LOGLEVEL:loglevel} - %{NOTSPACE:taskid} - %{NOTSPACE:logger} - %{WORD:label}( - %{INT:duration:int})?" ]
   }

   if [logger] == "SQL" {
     aggregate {
       task_id => "%{taskid}"
       code => "map['sql_duration'] ||= 0 ; map['sql_duration'] += event.get('duration')"
     }
   }

   if [logger] == "TASK_END" {
     aggregate {
       task_id => "%{taskid}"
       code => "event.set('sql_duration', map['sql_duration'])"
       end_of_task => true
       timeout => 120
     }
   }
 }
```

* the final event is exactly the same than example #1
* the key point is the "||=" ruby operator. It allows to initialize *sql_duration* map entry to 0 only if this map entry is not already initialized


## Example #3 : no end event [v2.7.1-plugins-filters-aggregate-example3]

Third use case: You have no specific end event.

A typical case is aggregating or tracking user behaviour. We can track a user by its ID through the events, however once the user stops interacting, the events stop coming in. There is no specific event indicating the end of the user’s interaction.

In this case, we can enable the option *push_map_as_event_on_timeout* to enable pushing the aggregation map as a new event when a timeout occurs. In addition, we can enable *timeout_code* to execute code on the populated timeout event. We can also add *timeout_task_id_field* so we can correlate the task_id, which in this case would be the user’s ID.

* Given these logs:

```ruby
INFO - 12345 - Clicked One
INFO - 12345 - Clicked Two
INFO - 12345 - Clicked Three
```

* You can aggregate the amount of clicks the user did like this:

```ruby
filter {
  grok {
    match => [ "message", "%{LOGLEVEL:loglevel} - %{NOTSPACE:user_id} - %{GREEDYDATA:msg_text}" ]
  }

  aggregate {
    task_id => "%{user_id}"
    code => "map['clicks'] ||= 0; map['clicks'] += 1;"
    push_map_as_event_on_timeout => true
    timeout_task_id_field => "user_id"
    timeout => 600 # 10 minutes timeout
    timeout_tags => ['_aggregatetimeout']
    timeout_code => "event.set('several_clicks', event.get('clicks') > 1)"
  }
}
```

* After ten minutes, this will yield an event like:

```json
{
  "user_id": "12345",
  "clicks": 3,
  "several_clicks": true,
    "tags": [
       "_aggregatetimeout"
    ]
}
```


## Example #4 : no end event and tasks come one after the other [v2.7.1-plugins-filters-aggregate-example4]

Fourth use case : like example #3, you have no specific end event, but also, tasks come one after the other.

That is to say : tasks are not interlaced. All task1 events come, then all task2 events come, …​

In that case, you don’t want to wait task timeout to flush aggregation map.

* A typical case is aggregating results from jdbc input plugin.
* Given that you have this SQL query : `SELECT country_name, town_name FROM town`
* Using jdbc input plugin, you get these 3 events from :

```json
  { "country_name": "France", "town_name": "Paris" }
  { "country_name": "France", "town_name": "Marseille" }
  { "country_name": "USA", "town_name": "New-York" }
```

* And you would like these 2 result events to push them into elasticsearch :

```json
  { "country_name": "France", "towns": [ {"town_name": "Paris"}, {"town_name": "Marseille"} ] }
  { "country_name": "USA", "towns": [ {"town_name": "New-York"} ] }
```

* You can do that using `push_previous_map_as_event` aggregate plugin option :

```ruby
   filter {
     aggregate {
       task_id => "%{country_name}"
       code => "
         map['country_name'] = event.get('country_name')
         map['towns'] ||= []
         map['towns'] << {'town_name' => event.get('town_name')}
         event.cancel()
       "
       push_previous_map_as_event => true
       timeout => 3
     }
   }
```

* The key point is that each time aggregate plugin detects a new `country_name`, it pushes previous aggregate map as a new Logstash event, and then creates a new empty map for the next country
* When 5s timeout comes, the last aggregate map is pushed as a new event
* Finally, initial events (which are not aggregated) are dropped because useless (thanks to `event.cancel()`)


## Example #5 : no end event and push events as soon as possible [v2.7.1-plugins-filters-aggregate-example5]

Fifth use case: like example #3, there is no end event.

Events keep comming for an indefinite time and you want to push the aggregation map as soon as possible after the last user interaction without waiting for the `timeout`.

This allows to have the aggregated events pushed closer to real time.

A typical case is aggregating or tracking user behaviour.

We can track a user by its ID through the events, however once the user stops interacting, the events stop coming in.

There is no specific event indicating the end of the user’s interaction.

The user ineraction will be considered as ended when no events for the specified user (task_id) arrive after the specified inactivity_timeout`.

If the user continues interacting for longer than `timeout` seconds (since first event), the aggregation map will still be deleted and pushed as a new event when timeout occurs.

The difference with example #3 is that the events will be pushed as soon as the user stops interacting for `inactivity_timeout` seconds instead of waiting for the end of `timeout` seconds since first event.

In this case, we can enable the option *push_map_as_event_on_timeout* to enable pushing the aggregation map as a new event when inactivity timeout occurs.

In addition, we can enable *timeout_code* to execute code on the populated timeout event.

We can also add *timeout_task_id_field* so we can correlate the task_id, which in this case would be the user’s ID.

* Given these logs:

```ruby
INFO - 12345 - Clicked One
INFO - 12345 - Clicked Two
INFO - 12345 - Clicked Three
```

* You can aggregate the amount of clicks the user did like this:

```ruby
filter {
 grok {
   match => [ "message", "%{LOGLEVEL:loglevel} - %{NOTSPACE:user_id} - %{GREEDYDATA:msg_text}" ]
 }
 aggregate {
   task_id => "%{user_id}"
   code => "map['clicks'] ||= 0; map['clicks'] += 1;"
   push_map_as_event_on_timeout => true
   timeout_task_id_field => "user_id"
   timeout => 3600 # 1 hour timeout, user activity will be considered finished one hour after the first event, even if events keep comming
   inactivity_timeout => 300 # 5 minutes timeout, user activity will be considered finished if no new events arrive 5 minutes after the last event
   timeout_tags => ['_aggregatetimeout']
   timeout_code => "event.set('several_clicks', event.get('clicks') > 1)"
 }
}
```

* After five minutes of inactivity or one hour since first event, this will yield an event like:

```json
{
 "user_id": "12345",
 "clicks": 3,
 "several_clicks": true,
   "tags": [
      "_aggregatetimeout"
   ]
}
```


## How it works [v2.7.1-plugins-filters-aggregate-howitworks]

* the filter needs a "task_id" to correlate events (log lines) of a same task
* at the task beginning, filter creates a map, attached to task_id
* for each event, you can execute code using *event* and *map* (for instance, copy an event field to map)
* in the final event, you can execute a last code (for instance, add map data to final event)
* after the final event, the map attached to task is deleted (thanks to `end_of_task => true`)
* an aggregate map is tied to one task_id value which is tied to one task_id pattern. So if you have 2 filters with different task_id patterns, even if you have same task_id value, they won’t share the same aggregate map.
* in one filter configuration, it is recommanded to define a timeout option to protect the feature against unterminated tasks. It tells the filter to delete expired maps
* if no timeout is defined, by default, all maps older than 1800 seconds are automatically deleted
* all timeout options have to be defined in only one aggregate filter per task_id pattern (per pipeline). Timeout options are : timeout, inactivity_timeout, timeout_code, push_map_as_event_on_timeout, push_previous_map_as_event, timeout_task_id_field, timeout_tags
* if `code` execution raises an exception, the error is logged and event is tagged *_aggregateexception*


## Use Cases [v2.7.1-plugins-filters-aggregate-usecases]

* extract some cool metrics from task logs and push them into task final log event (like in example #1 and #2)
* extract error information in any task log line, and push it in final task event (to get a final event with all error information if any)
* extract all back-end calls as a list, and push this list in final task event (to get a task profile)
* extract all http headers logged in several lines to push this list in final task event (complete http request info)
* for every back-end call, collect call details available on several lines, analyse it and finally tag final back-end call log line (error, timeout, business-warning, …​)
* Finally, task id can be any correlation id matching your need : it can be a session id, a file path, …​


## Aggregate Filter Configuration Options [v2.7.1-plugins-filters-aggregate-options]

This plugin supports the following configuration options plus the [Common options](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`aggregate_maps_path`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-aggregate_maps_path) | [string](logstash://reference/configuration-file-structure.md#string), a valid filesystem path | No |
| [`code`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-code) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`end_of_task`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-end_of_task) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`inactivity_timeout`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-inactivity_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`map_action`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-map_action) | [string](logstash://reference/configuration-file-structure.md#string), one of `["create", "update", "create_or_update"]` | No |
| [`push_map_as_event_on_timeout`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-push_map_as_event_on_timeout) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`push_previous_map_as_event`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-push_previous_map_as_event) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`task_id`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-task_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`timeout`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`timeout_code`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-timeout_code) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`timeout_tags`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-timeout_tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`timeout_task_id_field`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-timeout_task_id_field) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-common-options) for a list of options supported by all filter plugins.

 

### `aggregate_maps_path` [v2.7.1-plugins-filters-aggregate-aggregate_maps_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The path to file where aggregate maps are stored when Logstash stops and are loaded from when Logstash starts.

If not defined, aggregate maps will not be stored at Logstash stop and will be lost. Must be defined in only one aggregate filter per pipeline (as aggregate maps are shared at pipeline level).

Example:

```ruby
    filter {
      aggregate {
        aggregate_maps_path => "/path/to/.aggregate_maps"
      }
    }
```


### `code` [v2.7.1-plugins-filters-aggregate-code]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The code to execute to update map, using current event.

Or on the contrary, the code to execute to update event, using current map.

You will have a *map* variable and an *event* variable available (that is the event itself).

Example:

```ruby
    filter {
      aggregate {
        code => "map['sql_duration'] += event.get('duration')"
      }
    }
```


### `end_of_task` [v2.7.1-plugins-filters-aggregate-end_of_task]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Tell the filter that task is ended, and therefore, to delete aggregate map after code execution.


### `inactivity_timeout` [v2.7.1-plugins-filters-aggregate-inactivity_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

The amount of seconds (since the last event) after which a task is considered as expired.

When timeout occurs for a task, its aggregate map is evicted.

If *push_map_as_event_on_timeout* or *push_previous_map_as_event* is set to true, the task aggregation map is pushed as a new Logstash event.

`inactivity_timeout` can be defined for each "task_id" pattern.

`inactivity_timeout` must be lower than `timeout`.


### `map_action` [v2.7.1-plugins-filters-aggregate-map_action]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"create_or_update"`

Tell the filter what to do with aggregate map.

`"create"`: create the map, and execute the code only if map wasn’t created before

`"update"`: doesn’t create the map, and execute the code only if map was created before

`"create_or_update"`: create the map if it wasn’t created before, execute the code in all cases


### `push_map_as_event_on_timeout` [v2.7.1-plugins-filters-aggregate-push_map_as_event_on_timeout]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When this option is enabled, each time a task timeout is detected, it pushes task aggregation map as a new Logstash event. This enables to detect and process task timeouts in Logstash, but also to manage tasks that have no explicit end event.


### `push_previous_map_as_event` [v2.7.1-plugins-filters-aggregate-push_previous_map_as_event]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When this option is enabled, each time aggregate plugin detects a new task id, it pushes previous aggregate map as a new Logstash event, and then creates a new empty map for the next task.

::::{warning}
this option works fine only if tasks come one after the other. It means : all task1 events, then all task2 events, etc…​
::::



### `task_id` [v2.7.1-plugins-filters-aggregate-task_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The expression defining task ID to correlate logs.

This value must uniquely identify the task.

Example:

```ruby
    filter {
      aggregate {
        task_id => "%{type}%{my_task_id}"
      }
    }
```


### `timeout` [v2.7.1-plugins-filters-aggregate-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1800`

The amount of seconds (since the first event) after which a task is considered as expired.

When timeout occurs for a task, its aggregate map is evicted.

If *push_map_as_event_on_timeout* or *push_previous_map_as_event* is set to true, the task aggregation map is pushed as a new Logstash event.

Timeout can be defined for each "task_id" pattern.


### `timeout_code` [v2.7.1-plugins-filters-aggregate-timeout_code]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The code to execute to complete timeout generated event, when `'push_map_as_event_on_timeout'` or `'push_previous_map_as_event'` is set to true. The code block will have access to the newly generated timeout event that is pre-populated with the aggregation map.

If `'timeout_task_id_field'` is set, the event is also populated with the task_id value

Example:

```ruby
    filter {
      aggregate {
        timeout_code => "event.set('state', 'timeout')"
      }
    }
```


### `timeout_tags` [v2.7.1-plugins-filters-aggregate-timeout_tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Defines tags to add when a timeout event is generated and yield

Example:

```ruby
    filter {
      aggregate {
        timeout_tags => ["aggregate_timeout']
      }
    }
```


### `timeout_task_id_field` [v2.7.1-plugins-filters-aggregate-timeout_task_id_field]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This option indicates the timeout generated event’s field for the "task_id" value. The task id will then be set into the timeout event. This can help correlate which tasks have been timed out.

For example, with option `timeout_task_id_field => "my_id"` ,when timeout task id is `"12345"`, the generated timeout event will contain `'my_id' => '12345'`.

By default, if this option is not set, task id value won’t be set into timeout generated event.



## Common options [v2.7.1-plugins-filters-aggregate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v2-7-1-plugins-filters-aggregate.md#v2.7.1-plugins-filters-aggregate-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v2.7.1-plugins-filters-aggregate-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      aggregate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      aggregate {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v2.7.1-plugins-filters-aggregate-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      aggregate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      aggregate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v2.7.1-plugins-filters-aggregate-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v2.7.1-plugins-filters-aggregate-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 aggregate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      aggregate {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v2.7.1-plugins-filters-aggregate-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v2.7.1-plugins-filters-aggregate-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      aggregate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      aggregate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v2.7.1-plugins-filters-aggregate-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      aggregate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      aggregate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



