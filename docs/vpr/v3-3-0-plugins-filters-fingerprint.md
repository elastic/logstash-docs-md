---
navigation_title: "v3.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.0-plugins-filters-fingerprint.html
---

# Fingerprint filter plugin v3.3.0 [v3.3.0-plugins-filters-fingerprint]


* Plugin version: v3.3.0
* Released on: 2021-06-08
* [Changelog](https://github.com/logstash-plugins/logstash-filter-fingerprint/blob/v3.3.0/CHANGELOG.md)

For other versions, see the [overview list](filter-fingerprint-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1858]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-fingerprint). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1836]

Create consistent hashes (fingerprints) of one or more fields and store the result in a new field.

You can use this plugin to create consistent document ids when  events are inserted into Elasticsearch. This approach means that existing documents can be updated instead of creating new documents.

::::{note}
When the `method` option is set to `UUID` the result won’t be a consistent hash but a random [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). To generate UUIDs, prefer the [uuid filter](/lsr/plugins-filters-uuid.md).
::::



## Event Metadata and the Elastic Common Schema (ECS) [v3.3.0-plugins-filters-fingerprint-ecs_metadata]

This plugin adds a hash value to event as an identifier. You can configure the `target` option to change the output field.

When ECS compatibility is disabled, the hash value is stored in the `fingerprint` field. When ECS is enabled, the value is stored in the `[event][hash]` field.

Here’s how ECS compatibility mode affects output.

|  ECS disabled |  ECS v1 | Availability | Description |
| --- | --- | --- | --- |
|  fingerprint |  [event][hash] | *Always* | *a hash value of event* |


## Fingerprint Filter Configuration Options [v3.3.0-plugins-filters-fingerprint-options]

This plugin supports the following configuration options plus the [Common options](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`base64encode`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-base64encode) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`concatenate_sources`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-concatenate_sources) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`concatenate_all_fields`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-concatenate_all_fields) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ecs_compatibility`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`method`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-method) | [string](logstash://reference/configuration-file-structure.md#string), one of `["SHA1", "SHA256", "SHA384", "SHA512", "MD5", "MURMUR3", "IPV4_NETWORK", "UUID", "PUNCTUATION"]` | Yes |
| [`source`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-source) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`target`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-common-options) for a list of options supported by all filter plugins.

 

### `base64encode` [v3.3.0-plugins-filters-fingerprint-base64encode]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When set to `true`, the `SHA1`, `SHA256`, `SHA384`, `SHA512` and `MD5` fingerprint methods will produce base64 encoded rather than hex encoded strings.


### `concatenate_sources` [v3.3.0-plugins-filters-fingerprint-concatenate_sources]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When set to `true` and `method` isn’t `UUID` or `PUNCTUATION`, the plugin concatenates the names and values of all fields given in the `source` option into one string (like the old checksum filter) before doing the fingerprint computation.

If `false` and multiple source fields are given, the target field will be single fingerprint of the last source field.

**Example: `concatenate_sources`=false**

This example produces a single fingerprint that is computed from "birthday," the last source field.

```ruby
fingerprint {
  source => ["user_id", "siblings", "birthday"]
}
```

The output is:

```ruby
"fingerprint" => "6b6390a4416131f82b6ffb509f6e779e5dd9630f".
```

**Example: `concatenate_sources`=false with array**

If the last source field is an array, you get an array of fingerprints.

In this example, "siblings" is an array ["big brother", "little sister", "little brother"].

```ruby
fingerprint {
  source => ["user_id", "siblings"]
}
```

The output is:

```ruby
 "fingerprint" => [
        [0] "8a8a9323677f4095fcf0c8c30b091a0133b00641",
        [1] "2ce11b313402e0e9884e094409f8d9fcf01337c2",
        [2] "adc0b90f9391a82098c7b99e66a816e9619ad0a7"
    ],
```


### `concatenate_all_fields` [v3.3.0-plugins-filters-fingerprint-concatenate_all_fields]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When set to `true` and `method` isn’t `UUID` or `PUNCTUATION`, the plugin concatenates the names and values of all fields of the event into one string (like the old checksum filter) before doing the fingerprint computation. If `false` and at least one source field is given, the target field will be an array with fingerprints of the source fields given.


### `ecs_compatibility` [v3.3.0-plugins-filters-fingerprint-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: unstructured data added at root level
    * `v1`: uses `[event][hash]` fields that are compatible with Elastic Common Schema


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). See [Event Metadata and the Elastic Common Schema (ECS)](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-ecs_metadata) for detailed information.


### `key` [v3.3.0-plugins-filters-fingerprint-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

When used with the `IPV4_NETWORK` method fill in the subnet prefix length. With other methods, optionally fill in the HMAC key.


### `method` [v3.3.0-plugins-filters-fingerprint-method]

* This is a required setting.
* Value can be any of: `SHA1`, `SHA256`, `SHA384`, `SHA512`, `MD5`, `MURMUR3`, `IPV4_NETWORK`, `UUID`, `PUNCTUATION`
* Default value is `"SHA1"`

The fingerprint method to use.

If set to `SHA1`, `SHA256`, `SHA384`, `SHA512`, or `MD5` and a key is set, the cryptographic hash function with the same name will be used to generate the fingerprint. When a key set, the keyed-hash (HMAC) digest function will be used.

If set to `MURMUR3` the non-cryptographic 64 bit MurmurHash function will be used.

If set to `IPV4_NETWORK` the input data needs to be a IPv4 address and the hash value will be the masked-out address using the number of bits specified in the `key` option. For example, with "1.2.3.4" as the input and `key` set to 16, the hash becomes "1.2.0.0".

If set to `PUNCTUATION`, all non-punctuation characters will be removed from the input string.

If set to `UUID`, a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) will be generated. The result will be random and thus not a consistent hash.


### `source` [v3.3.0-plugins-filters-fingerprint-source]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `"message"`

The name(s) of the source field(s) whose contents will be used to create the fingerprint. If an array is given, see the `concatenate_sources` option.


### `target` [v3.3.0-plugins-filters-fingerprint-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"fingerprint"` when ECS is disabled
* Default value is `"[event][hash]"` when ECS is enabled

The name of the field where the generated fingerprint will be stored. Any current contents of that field will be overwritten.



## Common options [v3.3.0-plugins-filters-fingerprint-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-3-0-plugins-filters-fingerprint.md#v3.3.0-plugins-filters-fingerprint-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.3.0-plugins-filters-fingerprint-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      fingerprint {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      fingerprint {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.3.0-plugins-filters-fingerprint-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      fingerprint {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      fingerprint {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.3.0-plugins-filters-fingerprint-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.3.0-plugins-filters-fingerprint-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 fingerprint filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      fingerprint {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.3.0-plugins-filters-fingerprint-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.3.0-plugins-filters-fingerprint-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      fingerprint {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      fingerprint {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.3.0-plugins-filters-fingerprint-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      fingerprint {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      fingerprint {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
