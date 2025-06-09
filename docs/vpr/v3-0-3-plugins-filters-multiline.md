---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-multiline.html
---

# Multiline filter plugin v3.0.3 [v3.0.3-plugins-filters-multiline]


* Plugin version: v3.0.3
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-multiline/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-multiline-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2090]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-multiline). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2068]

This filter will collapse multiline messages from a single source into one Logstash event.

The original goal of this filter was to allow joining of multi-line messages from files into a single event. For example - joining java exception and stacktrace messages into a single event.

::::{note}
This filter will not work with multiple worker threads `-w 2` on the logstash command line.
::::


The config looks like this:

```ruby
    filter {
      multiline {
        pattern => "pattern, a regexp"
        negate => boolean
        what => "previous" or "next"
      }
    }
```

The `pattern` should be a regexp ([grok](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html) patterns are supported) which matches what you believe to be an indicator that the field is part of an event consisting of multiple lines of log data.

The `what` must be `previous` or `next` and indicates the relation to the multi-line event.

The `negate` can be `true` or `false` (defaults to `false`). If `true`, a message not matching the pattern will constitute a match of the multiline filter and the `what` will be applied. (vice-versa is also true)

For example, Java stack traces are multiline and usually have the message starting at the far-left, with each subsequent line indented. Do this:

```ruby
    filter {
      multiline {
        pattern => "^\s"
        what => "previous"
      }
    }
```

This says that any line starting with whitespace belongs to the previous line.

Another example is C line continuations (backslash). Here’s how to do that:

```ruby
    filter {
      multiline {
        pattern => "\\$"
        what => "next"
      }
    }
```

This says that any line ending with a backslash should be combined with the following line.


## Multiline Filter Configuration Options [v3.0.3-plugins-filters-multiline-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`allow_duplicates`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-allow_duplicates) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`max_age`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-max_age) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`negate`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-negate) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`pattern`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-pattern) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`patterns_dir`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-patterns_dir) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`source`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`stream_identity`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-stream_identity) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`what`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-what) | [string](logstash://reference/configuration-file-structure.md#string), one of `["previous", "next"]` | Yes |

Also see [Common options](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-common-options) for a list of options supported by all filter plugins.

 

### `allow_duplicates` [v3.0.3-plugins-filters-multiline-allow_duplicates]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Allow duplcate values on the source field.


### `max_age` [v3.0.3-plugins-filters-multiline-max_age]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

The maximum age an event can be (in seconds) before it is automatically flushed.


### `negate` [v3.0.3-plugins-filters-multiline-negate]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Negate the regexp pattern (*if not matched*)


### `pattern` [v3.0.3-plugins-filters-multiline-pattern]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The expression to match. The same matching engine as the [grok filter](/lsr/plugins-filters-grok.md) is used, so the expression can contain a plain regular expression or one that also contains grok patterns.


### `patterns_dir` [v3.0.3-plugins-filters-multiline-patterns_dir]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Logstash ships by default with a bunch of patterns, so you don’t necessarily need to define this yourself unless you are adding additional patterns.

Pattern files are plain text with format:

```ruby
    NAME PATTERN
```

For example:

```ruby
    NUMBER \d+
```


### `source` [v3.0.3-plugins-filters-multiline-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The field name to execute the pattern match on.


### `stream_identity` [v3.0.3-plugins-filters-multiline-stream_identity]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"%{{host}}.%{{path}}.%{{type}}"`

The stream identity is how the multiline filter determines which stream an event belongs to. This is generally used for differentiating, say, events coming from multiple files in the same file input, or multiple connections coming from a tcp input.

The default value here is usually what you want, but there are some cases where you want to change it. One such example is if you are using a tcp input with only one client connecting at any time. If that client reconnects (due to error or client restart), then logstash will identify the new connection as a new stream and break any multiline goodness that may have occurred between the old and new connection. To solve this use case, you can use `%{@source_host}.%{@type}` instead.


### `what` [v3.0.3-plugins-filters-multiline-what]

* This is a required setting.
* Value can be any of: `previous`, `next`
* There is no default value for this setting.

If the pattern matched, does event belong to the next or previous event?



## Common options [v3.0.3-plugins-filters-multiline-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-multiline.md#v3.0.3-plugins-filters-multiline-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-multiline-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      multiline {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      multiline {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.3-plugins-filters-multiline-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      multiline {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      multiline {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.3-plugins-filters-multiline-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-filters-multiline-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 multiline filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      multiline {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.3-plugins-filters-multiline-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.3-plugins-filters-multiline-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      multiline {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      multiline {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.3-plugins-filters-multiline-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      multiline {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      multiline {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



