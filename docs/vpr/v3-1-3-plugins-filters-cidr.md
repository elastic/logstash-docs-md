---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-filters-cidr.html
---

# Cidr filter plugin v3.1.3 [v3.1.3-plugins-filters-cidr]

* Plugin version: v3.1.3
* Released on: 2019-09-18
* [Changelog](https://github.com/logstash-plugins/logstash-filter-cidr/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](filter-cidr-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1720]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-cidr). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1698]

The CIDR filter is for checking IP addresses in events against a list of network blocks that might contain it. Multiple addresses can be checked against multiple networks, any match succeeds. Upon success additional tags and/or fields can be added to the event.

## Cidr Filter Configuration Options [v3.1.3-plugins-filters-cidr-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`address`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-address) | [array](/lsr/value-types.md#array) | No |
| [`network`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-network) | [array](/lsr/value-types.md#array) | No |
| [`network_path`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-network_path) | a valid filesystem path | No |
| [`refresh_interval`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-refresh_interval) | [number](/lsr/value-types.md#number) | No |
| [`separator`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-separator) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-common-options) for a list of options supported by all filter plugins.

### `address` [v3.1.3-plugins-filters-cidr-address]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

The IP address(es) to check with. Example:

```
    filter {
      cidr {
        add_tag => [ "testnet" ]
        address => [ "%{src_ip}", "%{dst_ip}" ]
        network => [ "192.0.2.0/24" ]
      }
    }
```

### `network` [v3.1.3-plugins-filters-cidr-network]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

The IP network(s) to check against. Example:

```
    filter {
      cidr {
        add_tag => [ "linklocal" ]
        address => [ "%{clientip}" ]
        network => [ "169.254.0.0/16", "fe80::/64" ]
      }
    }
```

### `network_path` [v3.1.3-plugins-filters-cidr-network_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The full path of the external file containing the networks the filter should check with. Networks are separated by a separator character defined in `separator`.

```
    192.168.1.0/24
    192.167.0.0/16
NOTE: It is an error to specify both `network` and `network_path`.
```

### `refresh_interval` [v3.1.3-plugins-filters-cidr-refresh_interval]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `600`

When using an external file, this setting will indicate how frequently (in seconds) Logstash will check the file for updates.

### `separator` [v3.1.3-plugins-filters-cidr-separator]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `\n`

Separator character used for parsing networks from the external file specified by `network_path`. Defaults to newline `\n` character.

## Common options [v3.1.3-plugins-filters-cidr-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-1-3-plugins-filters-cidr.md#v3.1.3-plugins-filters-cidr-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.1.3-plugins-filters-cidr-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      cidr {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      cidr {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.1.3-plugins-filters-cidr-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      cidr {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      cidr {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.1.3-plugins-filters-cidr-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.1.3-plugins-filters-cidr-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 cidr filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      cidr {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.1.3-plugins-filters-cidr-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.1.3-plugins-filters-cidr-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      cidr {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      cidr {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.1.3-plugins-filters-cidr-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      cidr {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      cidr {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
