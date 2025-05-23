---
navigation_title: "v3.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.1.3-plugins-filters-dns.html
---

# Dns filter plugin v3.1.3 [v3.1.3-plugins-filters-dns]


* Plugin version: v3.1.3
* Released on: 2020-01-06
* [Changelog](https://github.com/logstash-plugins/logstash-filter-dns/blob/v3.1.3/CHANGELOG.md)

For other versions, see the [overview list](filter-dns-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1762]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-dns). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1740]

The DNS filter performs a lookup (either an A record/CNAME record lookup or a reverse lookup at the PTR record) on records specified under the `reverse` arrays or respectively under the `resolve` arrays.

The config should look like this:

```ruby
    filter {
      dns {
        reverse => [ "source_host", "field_with_address" ]
        resolve => [ "field_with_fqdn" ]
        action => "replace"
      }
    }
```

This filter, like all filters, only processes 1 event at a time, so the use of this plugin can significantly slow down your pipeline’s throughput if you have a high latency network. By way of example, if each DNS lookup takes 2 milliseconds, the maximum throughput you can achieve with a single filter worker is 500 events per second (1000 milliseconds / 2 milliseconds).


## Dns Filter Configuration Options [v3.1.3-plugins-filters-dns-options]

This plugin supports the following configuration options plus the [Common options](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`action`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-action) | [string](logstash://reference/configuration-file-structure.md#string), one of `["append", "replace"]` | No |
| [`failed_cache_size`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-failed_cache_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`failed_cache_ttl`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-failed_cache_ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`hit_cache_size`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-hit_cache_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`hit_cache_ttl`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-hit_cache_ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`hostsfile`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-hostsfile) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`max_retries`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-max_retries) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`nameserver`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-nameserver) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`resolve`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-resolve) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`reverse`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-reverse) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`timeout`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-common-options) for a list of options supported by all filter plugins.

 

### `action` [v3.1.3-plugins-filters-dns-action]

* Value can be any of: `append`, `replace`
* Default value is `"append"`

Determine what action to do: append or replace the values in the fields specified under `reverse` and `resolve`.


### `failed_cache_size` [v3.1.3-plugins-filters-dns-failed_cache_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

cache size for failed requests


### `failed_cache_ttl` [v3.1.3-plugins-filters-dns-failed_cache_ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

how long to cache failed requests (in seconds)


### `hit_cache_size` [v3.1.3-plugins-filters-dns-hit_cache_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

set the size of cache for successful requests


### `hit_cache_ttl` [v3.1.3-plugins-filters-dns-hit_cache_ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

how long to cache successful requests (in seconds)


### `hostsfile` [v3.1.3-plugins-filters-dns-hostsfile]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Use custom hosts file(s). For example: `["/var/db/my_custom_hosts"]`


### `max_retries` [v3.1.3-plugins-filters-dns-max_retries]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `2`

number of times to retry a failed resolve/reverse


### `nameserver` [v3.1.3-plugins-filters-dns-nameserver]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash), and is composed of:

    * a required `address` key, whose value is either a [string](logstash://reference/configuration-file-structure.md#string) or an [array](logstash://reference/configuration-file-structure.md#array), representing one or more nameserver ip addresses
    * an optional `search` key, whose value is either a [string](logstash://reference/configuration-file-structure.md#string) or an [array](logstash://reference/configuration-file-structure.md#array), representing between one and six search domains (e.g., with search domain `com`, a query for `example` will match DNS entries for `example.com`)
    * an optional `ndots` key, used in conjunction with `search`, whose value is a [number](logstash://reference/configuration-file-structure.md#number), representing the minimum number of dots in a domain name being resolved that will *prevent* the search domains from being used (default `1`; this option is rarely needed)

* For backward-compatibility, values of [string](logstash://reference/configuration-file-structure.md#string) and [array](logstash://reference/configuration-file-structure.md#array) are also accepted, representing one or more nameserver ip addresses *without* search domains.
* There is no default value for this setting.

Use custom nameserver(s). For example:

```ruby
    filter {
      dns {
        nameserver => {
          address => ["8.8.8.8", "8.8.4.4"]
          search  => ["internal.net"]
        }
      }
    }
```

If `nameserver` is not specified then `/etc/resolv.conf` will be read to configure the resolver using the `nameserver`, `domain`, `search` and `ndots` directives in `/etc/resolv.conf`.


### `resolve` [v3.1.3-plugins-filters-dns-resolve]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Forward resolve one or more fields.


### `reverse` [v3.1.3-plugins-filters-dns-reverse]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Reverse resolve one or more fields.


### `timeout` [v3.1.3-plugins-filters-dns-timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0.5`

`resolv` calls will be wrapped in a timeout instance



## Common options [v3.1.3-plugins-filters-dns-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-1-3-plugins-filters-dns.md#v3.1.3-plugins-filters-dns-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.1.3-plugins-filters-dns-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      dns {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      dns {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.1.3-plugins-filters-dns-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      dns {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      dns {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.1.3-plugins-filters-dns-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.1.3-plugins-filters-dns-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 dns filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      dns {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.1.3-plugins-filters-dns-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.1.3-plugins-filters-dns-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      dns {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      dns {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.1.3-plugins-filters-dns-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      dns {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      dns {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



