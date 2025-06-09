---
navigation_title: "v3.1.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.4-plugins-filters-ruby.html
---

# Ruby filter plugin v3.1.4 [v3.1.4-plugins-filters-ruby]

* Plugin version: v3.1.4
* Released on: 2018-03-16
* [Changelog](https://github.com/logstash-plugins/logstash-filter-ruby/blob/v3.1.4/CHANGELOG.md)

For other versions, see the [overview list](filter-ruby-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2153]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-ruby). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2131]

Execute ruby code. This filter accepts inline ruby code or a ruby file. The two options are mutually exclusive and have slightly different ways of working, which are described below.

### Inline ruby code [_inline_ruby_code_3]

To inline ruby in your filter, place all code in the `code` option. This code will be executed for every event the filter receives. You can also place ruby code in the `init` option - it will be executed only once during the plugin’s register phase.

For example, to cancel 90% of events, you can do this:

```
    filter {
      ruby {
        # Cancel 90% of events
        code => "event.cancel if rand <= 0.90"
      }
    }
```

If you need to create additional events, you must use a specific syntax `new_event_block.call(event)` like in this example duplicating the input event

```
filter {
  ruby {
    code => "new_event_block.call(event.clone)"
  }
}
```

### Using a Ruby script file [_using_a_ruby_script_file_3]

As the inline code can become complex and hard to structure inside of a text string in `code`, it’s then preferrable to place the Ruby code in a .rb file, using the `path` option.

```
    filter {
      ruby {
        # Cancel 90% of events
        path => "/etc/logstash/drop_percentage.rb"
        script_params => { "percentage" => 0.9 }
      }
    }
```

The ruby script file should define the following methods:

* `register(params)`: An optional register method that receives the key/value hash passed in the `script_params` configuration option
* `filter(event)`: A mandatory Ruby method that accepts a Logstash event and must return an array of events

Below is an example implementation of the `drop_percentage.rb` ruby script that drops a configurable percentage of events:

```
# the value of `params` is the value of the hash passed to `script_params`
# in the logstash configuration
def register(params)
	@drop_percentage = params["percentage"]
end

# the filter method receives an event and must return a list of events.
# Dropping an event means not including it in the return array,
# while creating new ones only requires you to add a new instance of
# LogStash::Event to the returned array
def filter(event)
	if rand >= @drop_percentage
		return [event]
	else
		return [] # return empty array to cancel event
	end
end
```

### Testing the ruby script [_testing_the_ruby_script_5]

To validate the behaviour of the `filter` method you implemented, the Ruby filter plugin provides an inline test framework where you can assert expectations. The tests you define will run when the pipeline is created and will prevent it from starting if a test fails.

You can also verify if the tests pass using the logstash `-t` flag.

For example above, you can write at the bottom of the `drop_percentage.rb` ruby script the following test:

```
def register(params)
  # ..
end

def filter(event)
  # ..
end

test "drop percentage 100%" do
  parameters do
    { "percentage" => 1 }
  end

  in_event { { "message" => "hello" } }

  expect("drops the event") do |events|
    events.size == 0
  end
end
```

We can now test that the ruby script we’re using is implemented correctly:

```
% bin/logstash -e "filter { ruby { path => '/etc/logstash/drop_percentage.rb' script_params => { 'drop_percentage' => 0.5 } } }" -t
[2017-10-13T13:44:29,723][INFO ][logstash.filters.ruby.script] Test run complete {:script_path=>"/etc/logstash/drop_percentage.rb", :results=>{:passed=>1, :failed=>0, :errored=>0}}
Configuration OK
[2017-10-13T13:44:29,887][INFO ][logstash.runner          ] Using config.test_and_exit mode. Config Validation Result: OK. Exiting Logstash
```

## Ruby Filter Configuration Options [v3.1.4-plugins-filters-ruby-options]

This plugin supports the following configuration options plus the [Common options](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`code`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-code) | [string](/lsr/value-types.md#string) | No |
| [`init`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-init) | [string](/lsr/value-types.md#string) | No |
| [`path`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-path) | [string](/lsr/value-types.md#string) | No |
| [`script_params`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-script_params) | [hash](/lsr/value-types.md#hash),{} | No |
| [`tag_on_exception`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-tag_on_exception) | [string](/lsr/value-types.md#string),\_rubyexception | No |

Also see [Common options](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-common-options) for a list of options supported by all filter plugins.

### `code` [v3.1.4-plugins-filters-ruby-code]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* This setting cannot be used together with `path`.

The code to execute for every event. You will have an `event` variable available that is the event itself. See the [Event API](https://www.elastic.co/guide/en/logstash/current/event-api.html) for more information.

### `init` [v3.1.4-plugins-filters-ruby-init]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Any code to execute at logstash startup-time

### `path` [v3.1.4-plugins-filters-ruby-path]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.
* This setting cannot be used together with `code`.

The path of the ruby script file that implements the `filter` method.

### `script_params` [v3.1.4-plugins-filters-ruby-script_params]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

A key/value hash with parameters that are passed to the register method of your ruby script file defined in `path`.

### `tag_on_exception` [v3.1.4-plugins-filters-ruby-tag_on_exception]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `_rubyexception`

Tag to add to events in case the ruby code (either inline or file based) causes an exception.

## Common options [v3.1.4-plugins-filters-ruby-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-1-4-plugins-filters-ruby.md#v3.1.4-plugins-filters-ruby-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.1.4-plugins-filters-ruby-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      ruby {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.1.4-plugins-filters-ruby-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      ruby {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      ruby {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.1.4-plugins-filters-ruby-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.4-plugins-filters-ruby-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 ruby filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      ruby {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.1.4-plugins-filters-ruby-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.1.4-plugins-filters-ruby-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      ruby {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      ruby {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.1.4-plugins-filters-ruby-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      ruby {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      ruby {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
