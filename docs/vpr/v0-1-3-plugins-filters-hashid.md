---
navigation_title: "v0.1.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.1.3-plugins-filters-hashid.html
---

# Hashid filter plugin v0.1.3 [v0.1.3-plugins-filters-hashid]

* Plugin version: v0.1.3
* Released on: 2017-08-21
* [Changelog](https://github.com/logstash-plugins/logstash-filter-hashid/blob/v0.1.3/CHANGELOG.md)

For other versions, see the [overview list](filter-hashid-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1947]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-hashid). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1925]

This filter allow you to generate predictable, string encoded hashed keys based om event contents and timestamp. This can be used to avoid getting duplicate records indexed into Elasticsearch.

Hashed keys to be generated based on full or partial hashes and has the ability to prefix these keys based on the event timestamp in order to make then largely ordered by timestamp, which tend to lead to increased indexing performance for event based use cases where data is being indexed in near real time.

When used with the timestamp prefix enabled, it should ideally be run after the date filter has run and populated the @timestamp field.

## Hashid Filter Configuration Options [v0.1.3-plugins-filters-hashid-options]

This plugin supports the following configuration options plus the [Common options](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_timestamp_prefix`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-add_timestamp_prefix) | [boolean](/lsr/value-types.md#boolean) | No |
| [`hash_bytes_used`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-hash_bytes_used) | [number](/lsr/value-types.md#number) | No |
| [`key`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-key) | [string](/lsr/value-types.md#string) | No |
| [`method`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-method) | [string](/lsr/value-types.md#string), one of `["SHA1", "SHA256", "SHA384", "SHA512", "MD5"]` | No |
| [`source`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-source) | [array](/lsr/value-types.md#array) | No |
| [`target`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-common-options) for a list of options supported by all filter plugins.

### `add_timestamp_prefix` [v0.1.3-plugins-filters-hashid-add_timestamp_prefix]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Use the timestamp to generate an ID prefix

### `hash_bytes_used` [v0.1.3-plugins-filters-hashid-hash_bytes_used]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

If full hash generated is not to be used, this parameter specifies how many bytes that should be used If not specified, the full hash will be used

### `key` [v0.1.3-plugins-filters-hashid-key]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"hashid"`

Encryption key to be used when generating cryptographic hashes

### `method` [v0.1.3-plugins-filters-hashid-method]

* Value can be any of: `SHA1`, `SHA256`, `SHA384`, `SHA512`, `MD5`
* Default value is `"MD5"`

Hash function to use

### `source` [v0.1.3-plugins-filters-hashid-source]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["message"]`

Source field(s) to base the hash calculation on

### `target` [v0.1.3-plugins-filters-hashid-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"hashid"`

Target field. Will overwrite current value of a field if it exists.

## Common options [v0.1.3-plugins-filters-hashid-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v0-1-3-plugins-filters-hashid.md#v0.1.3-plugins-filters-hashid-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v0.1.3-plugins-filters-hashid-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      hashid {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      hashid {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v0.1.3-plugins-filters-hashid-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      hashid {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      hashid {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v0.1.3-plugins-filters-hashid-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v0.1.3-plugins-filters-hashid-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 hashid filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      hashid {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v0.1.3-plugins-filters-hashid-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v0.1.3-plugins-filters-hashid-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      hashid {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      hashid {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v0.1.3-plugins-filters-hashid-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      hashid {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      hashid {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
