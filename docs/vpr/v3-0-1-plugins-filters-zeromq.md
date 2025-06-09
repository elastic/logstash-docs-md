---
navigation_title: "v3.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.1-plugins-filters-zeromq.html
---

# Zeromq filter plugin v3.0.1 [v3.0.1-plugins-filters-zeromq]

* Plugin version: v3.0.1
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-zeromq/blob/v3.0.1/CHANGELOG.md)

For other versions, see the [overview list](filter-zeromq-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2242]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-zeromq). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2220]

ZeroMQ filter. This is the best way to send an event externally for filtering It works much like an exec filter would by sending the event "offsite" for processing and waiting for a response

The protocol here is: \* REQ sent with JSON-serialized logstash event \* REP read expected to be the full JSON *filtered* event \* - if reply read is an empty string, it will cancel the event.

Note that this is a limited subset of the zeromq functionality in inputs and outputs. The only topology that makes sense here is: REQ/REP. bunde

## Zeromq Filter Configuration Options [v3.0.1-plugins-filters-zeromq-options]

This plugin supports the following configuration options plus the [Common options](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_tag_on_timeout`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-add_tag_on_timeout) | [string](/lsr/value-types.md#string) | No |
| [`address`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-address) | [string](/lsr/value-types.md#string) | No |
| [`field`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-field) | [string](/lsr/value-types.md#string) | No |
| [`mode`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-mode) | [string](/lsr/value-types.md#string), one of `["server", "client"]` | No |
| [`retries`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-retries) | [number](/lsr/value-types.md#number) | No |
| [`sentinel`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-sentinel) | [string](/lsr/value-types.md#string) | No |
| [`sockopt`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-sockopt) | [hash](/lsr/value-types.md#hash) | No |
| [`timeout`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-timeout) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-common-options) for a list of options supported by all filter plugins.

### `add_tag_on_timeout` [v3.0.1-plugins-filters-zeromq-add_tag_on_timeout]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"zeromqtimeout"`

tag to add if zeromq timeout expires before getting back an answer. If set to "" then no tag will be added.

### `address` [v3.0.1-plugins-filters-zeromq-address]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"tcp://127.0.0.1:2121"`

0mq socket address to connect or bind Please note that inproc:// will not work with logstash as we use a context per thread By default, filters connect

### `field` [v3.0.1-plugins-filters-zeromq-field]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The field to send off-site for processing If this is unset, the whole event will be sent

### `mode` [v3.0.1-plugins-filters-zeromq-mode]

* Value can be any of: `server`, `client`
* Default value is `"client"`

0mq mode server mode binds/listens client mode connects

### `retries` [v3.0.1-plugins-filters-zeromq-retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3`

number of retries, used for both sending and receiving messages. for sending, retries should return instantly. for receiving, the total blocking time is up to retries X timeout, which by default is 3 X 500 = 1500ms

### `sentinel` [v3.0.1-plugins-filters-zeromq-sentinel]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

A sentinel value to signal the filter to cancel the event If the peer returns the sentinel value, the event will be cancelled

### `sockopt` [v3.0.1-plugins-filters-zeromq-sockopt]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

0mq socket options This exposes zmq\_setsockopt for advanced tuning see <http://api.zeromq.org/2-1:zmq-setsockopt> for details

This is where you would set values like: ZMQ::HWM - high water mark ZMQ::IDENTITY - named queues ZMQ::SWAP\_SIZE - space for disk overflow ZMQ::SUBSCRIBE - topic filters for pubsub

example: sockopt ⇒ \["ZMQ::HWM", 50, "ZMQ::IDENTITY", "my\_named\_queue"]

### `timeout` [v3.0.1-plugins-filters-zeromq-timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `500`

timeout in milliseconds on which to wait for a reply.

## Common options [v3.0.1-plugins-filters-zeromq-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-0-1-plugins-filters-zeromq.md#v3.0.1-plugins-filters-zeromq-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.0.1-plugins-filters-zeromq-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      zeromq {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      zeromq {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.0.1-plugins-filters-zeromq-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      zeromq {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      zeromq {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.0.1-plugins-filters-zeromq-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.1-plugins-filters-zeromq-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 zeromq filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      zeromq {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.0.1-plugins-filters-zeromq-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.0.1-plugins-filters-zeromq-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      zeromq {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      zeromq {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.0.1-plugins-filters-zeromq-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      zeromq {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      zeromq {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
