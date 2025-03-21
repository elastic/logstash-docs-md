---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-filters-anonymize.html
---

# Anonymize filter plugin v3.0.6 [v3.0.6-plugins-filters-anonymize]


* Plugin version: v3.0.6
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-anonymize/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](filter-anonymize-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1694]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-anonymize). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1672]

::::{admonition} Deprecated in 3.0.3.
:class: warning

We recommend that you use the [fingerprint filter plugin](logstash://reference/plugins-filters-fingerprint.md) instead.
::::


Anonymize fields by replacing values with a consistent hash.


## Anonymize Filter Configuration Options [v3.0.6-plugins-filters-anonymize-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`algorithm`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-algorithm) | [string](logstash://reference/configuration-file-structure.md#string), one of `["SHA1", "SHA256", "SHA384", "SHA512", "MD5", "MURMUR3", "IPV4_NETWORK"]` | Yes |
| [`fields`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-fields) | [array](logstash://reference/configuration-file-structure.md#array) | Yes |
| [`key`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-key) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-common-options) for a list of options supported by all filter plugins.

 

### `algorithm` [v3.0.6-plugins-filters-anonymize-algorithm]

* This is a required setting.
* Value can be any of: `SHA1`, `SHA256`, `SHA384`, `SHA512`, `MD5`, `MURMUR3`, `IPV4_NETWORK`
* Default value is `"SHA1"`

digest/hash type


### `fields` [v3.0.6-plugins-filters-anonymize-fields]

* This is a required setting.
* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

The fields to be anonymized


### `key` [v3.0.6-plugins-filters-anonymize-key]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Hashing key When using MURMUR3 the key is ignored but must still be set. When using IPV4_NETWORK key is the subnet prefix lentgh



## Common options [v3.0.6-plugins-filters-anonymize-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-6-plugins-filters-anonymize.md#v3.0.6-plugins-filters-anonymize-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.6-plugins-filters-anonymize-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      anonymize {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      anonymize {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.6-plugins-filters-anonymize-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      anonymize {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      anonymize {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.6-plugins-filters-anonymize-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-filters-anonymize-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 anonymize filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      anonymize {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.6-plugins-filters-anonymize-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.6-plugins-filters-anonymize-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      anonymize {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      anonymize {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.6-plugins-filters-anonymize-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      anonymize {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      anonymize {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



