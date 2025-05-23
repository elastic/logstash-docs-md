---
navigation_title: "v1.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.0-plugins-filters-memcached.html
---

# Memcached filter plugin v1.0.0 [v1.0.0-plugins-filters-memcached]


* Plugin version: v1.0.0
* Released on: 2019-02-04
* [Changelog](https://github.com/logstash-plugins/logstash-filter-memcached/blob/v1.0.0/CHANGELOG.md)

For other versions, see the [overview list](filter-memcached-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2075]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-memcached). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2053]

The Memcached filter provides integration with external data in Memcached.

It currently provides the following facilities: - `get`: get values for one or more memcached keys and inject them into the event at the provided paths - `set`: set values from the event to the corresponding memcached keys


## Memcached Filter Configuration Options [v1.0.0-plugins-filters-memcached-options]

This plugin supports the following configuration options plus the [Common options](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`hosts`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`namespace`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-namespace) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`get`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-get) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`set`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-set) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`ttl`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-common-options) for a list of options supported by all filter plugins.

 

### `hosts` [v1.0.0-plugins-filters-memcached-hosts]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `localhost`

The `hosts` parameter accepts an array of addresses corresponding to memcached instances.

Hosts can be specified via FQDN (e.g., `example.com`), an IPV4 address (e.g., `123.45.67.89`), or an IPV6 address (e.g. `::1` or `2001:0db8:85a3:0000:0000:8a2e:0370:7334`). If your memcached host uses a non-standard port, the port can be specified by appending a colon (`:`) and the port number; to include a port with an IPv6 address, the address must first be wrapped in square-brackets (`[` and `]`), e.g., `[::1]:11211`.

If more than one host is specified, requests will be distributed to the given hosts using a modulus of the CRC-32 checksum of each key.


### `namespace` [v1.0.0-plugins-filters-memcached-namespace]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

If specified, prefix all memcached keys with the given string followed by a colon (`:`); this is useful if all keys being used by this plugin share a common prefix.

EXAMPLE:

In the following configuration, we would GET `fruit:banana` and `fruit:apple` from memcached:

```
filter {
  memcached {
    namespace => "fruit"
    get => {
      "banana" => "[fruit-stats][banana]"
      "apple"  => "[fruit-stats][apple]
    }
  }
}
```


### `get` [v1.0.0-plugins-filters-memcached-get]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

If specified, get the values for the given keys from memcached, and store them in the corresponding fields on the event.

* keys are interpolated (e.g., if the event has a field `foo` with value `bar`, the key `sand/%{{foo}}` will evaluate to `sand/bar`)
* fields can be nested references

```
filter {
  memcached {
    get => {
      "memcached-key-1" => "field1"
      "memcached-key-2" => "[nested][field2]"
    }
  }
}
```


### `set` [v1.0.0-plugins-filters-memcached-set]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

If specified, extracts the values from the given event fields, and sets the corresponding keys to those values in memcached with the configured [ttl](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-ttl)

* keys are interpolated (e.g., if the event has a field `foo` with value `bar`, the key `sand/%{{foo}}` will evaluate to `sand/bar`)
* fields can be nested references

```
filter {
  memcached {
    set => {
      "field1"           => "memcached-key-1"
      "[nested][field2]" => "memcached-key-2"
    }
  }
}
```


### `ttl` [v1.0.0-plugins-filters-memcached-ttl]

For usages of this plugin that persist data to memcached (e.g., [`set`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-set)), the time-to-live in seconds

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* The default value is `0` (no expiry)



## Common options [v1.0.0-plugins-filters-memcached-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v1-0-0-plugins-filters-memcached.md#v1.0.0-plugins-filters-memcached-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v1.0.0-plugins-filters-memcached-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      memcached {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      memcached {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v1.0.0-plugins-filters-memcached-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      memcached {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      memcached {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v1.0.0-plugins-filters-memcached-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.0-plugins-filters-memcached-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 memcached filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      memcached {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v1.0.0-plugins-filters-memcached-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v1.0.0-plugins-filters-memcached-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      memcached {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      memcached {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v1.0.0-plugins-filters-memcached-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      memcached {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      memcached {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



