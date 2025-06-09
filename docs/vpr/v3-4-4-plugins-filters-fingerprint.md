---
navigation_title: "v3.4.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.4.4-plugins-filters-fingerprint.html
---

# Fingerprint filter plugin v3.4.4 [v3.4.4-plugins-filters-fingerprint]

* Plugin version: v3.4.4
* Released on: 2024-03-19
* [Changelog](https://github.com/logstash-plugins/logstash-filter-fingerprint/blob/v3.4.4/CHANGELOG.md)

For other versions, see the [overview list](filter-fingerprint-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1875]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-fingerprint). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1853]

Create consistent hashes (fingerprints) of one or more fields and store the result in a new field.

You can use this plugin to create consistent document ids when events are inserted into Elasticsearch. This approach means that existing documents can be updated instead of creating new documents.

When the `method` option is set to `UUID` the result won’t be a consistent hash but a random [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). To generate UUIDs, prefer the [uuid filter](https://www.elastic.co/guide/en/logstash/current/plugins-filters-uuid.html).

## Event Metadata and the Elastic Common Schema (ECS) [v3.4.4-plugins-filters-fingerprint-ecs_metadata]

This plugin adds a hash value to event as an identifier. You can configure the `target` option to change the output field.

When ECS compatibility is disabled, the hash value is stored in the `fingerprint` field. When ECS is enabled, the value is stored in the `[event][hash]` field.

Here’s how ECS compatibility mode affects output.

| ECS disabled | ECS v1 | Availability | Description |
| :- | :- | :- | :- |
| fingerprint | \[event]\[hash] | *Always* | *a hash value of event* |

## Fingerprint Filter Configuration Options [v3.4.4-plugins-filters-fingerprint-options]

This plugin supports the following configuration options plus the [Common options](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`base64encode`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-base64encode) | [boolean](/lsr/value-types.md#boolean) | No |
| [`concatenate_sources`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-concatenate_sources) | [boolean](/lsr/value-types.md#boolean) | No |
| [`concatenate_all_fields`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-concatenate_all_fields) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ecs_compatibility`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-ecs_compatibility) | [string](/lsr/value-types.md#string) | No |
| [`key`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-key) | [password](/lsr/value-types.md#password) | No |
| [`method`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-method) | [string](/lsr/value-types.md#string), one of `["SHA1", "SHA256", "SHA384", "SHA512", "MD5", "MURMUR3", "MURMUR3_128", IPV4_NETWORK", "UUID", "PUNCTUATION"]` | Yes |
| [`source`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-source) | [array](/lsr/value-types.md#array) | No |
| [`target`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-common-options) for a list of options supported by all filter plugins.

### `base64encode` [v3.4.4-plugins-filters-fingerprint-base64encode]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

When set to `true`, the `SHA1`, `SHA256`, `SHA384`, `SHA512`, `MD5` and `MURMUR3_128` fingerprint methods will produce base64 encoded rather than hex encoded strings.

### `concatenate_sources` [v3.4.4-plugins-filters-fingerprint-concatenate_sources]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

When set to `true` and `method` isn’t `UUID` or `PUNCTUATION`, the plugin concatenates the names and values of all fields given in the `source` option into one string (like the old checksum filter) before doing the fingerprint computation.

If `false` and multiple source fields are given, the target field will be single fingerprint of the last source field.

**Example: `concatenate_sources`=false**

This example produces a single fingerprint that is computed from "birthday," the last source field.

```
fingerprint {
  source => ["user_id", "siblings", "birthday"]
}
```

The output is:

```
"fingerprint" => "6b6390a4416131f82b6ffb509f6e779e5dd9630f".
```

**Example: `concatenate_sources`=false with array**

If the last source field is an array, you get an array of fingerprints.

In this example, "siblings" is an array \["big brother", "little sister", "little brother"].

```
fingerprint {
  source => ["user_id", "siblings"]
}
```

The output is:

```
 "fingerprint" => [
        [0] "8a8a9323677f4095fcf0c8c30b091a0133b00641",
        [1] "2ce11b313402e0e9884e094409f8d9fcf01337c2",
        [2] "adc0b90f9391a82098c7b99e66a816e9619ad0a7"
    ],
```

### `concatenate_all_fields` [v3.4.4-plugins-filters-fingerprint-concatenate_all_fields]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

When set to `true` and `method` isn’t `UUID` or `PUNCTUATION`, the plugin concatenates the names and values of all fields of the event into one string (like the old checksum filter) before doing the fingerprint computation. If `false` and at least one source field is given, the target field will be an array with fingerprints of the source fields given.

### `ecs_compatibility` [v3.4.4-plugins-filters-fingerprint-ecs_compatibility]

* Value type is [string](/lsr/value-types.md#string)

* Supported values are:

  * `disabled`: unstructured data added at root level
  * `v1`: uses `[event][hash]` fields that are compatible with Elastic Common Schema

Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current). See [Event Metadata and the Elastic Common Schema (ECS)](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-ecs_metadata) for detailed information.

### `key` [v3.4.4-plugins-filters-fingerprint-key]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

When used with the `IPV4_NETWORK` method fill in the subnet prefix length. With other methods, optionally fill in the HMAC key.

### `method` [v3.4.4-plugins-filters-fingerprint-method]

* This is a required setting.
* Value can be any of: `SHA1`, `SHA256`, `SHA384`, `SHA512`, `MD5`, `MURMUR3`, `MURMUR3_128`, `IPV4_NETWORK`, `UUID`, `PUNCTUATION`
* Default value is `"SHA1"`

The fingerprint method to use.

If set to `SHA1`, `SHA256`, `SHA384`, `SHA512`, or `MD5` and a key is set, the corresponding cryptographic hash function and the keyed-hash (HMAC) digest function are used to generate the fingerprint.

If set to `MURMUR3` or `MURMUR3_128` the non-cryptographic MurmurHash function (either the 32-bit or 128-bit implementation, respectively) will be used.

If set to `IPV4_NETWORK` the input data needs to be a IPv4 address and the hash value will be the masked-out address using the number of bits specified in the `key` option. For example, with "1.2.3.4" as the input and `key` set to 16, the hash becomes "1.2.0.0".

If set to `PUNCTUATION`, all non-punctuation characters will be removed from the input string.

If set to `UUID`, a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) will be generated. The result will be random and thus not a consistent hash.

### `source` [v3.4.4-plugins-filters-fingerprint-source]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `"message"`

The name(s) of the source field(s) whose contents will be used to create the fingerprint. If an array is given, see the `concatenate_sources` option.

### `target` [v3.4.4-plugins-filters-fingerprint-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"fingerprint"` when ECS is disabled
* Default value is `"[event][hash]"` when ECS is enabled

The name of the field where the generated fingerprint will be stored. Any current contents of that field will be overwritten.

## Common options [v3.4.4-plugins-filters-fingerprint-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v3-4-4-plugins-filters-fingerprint.md#v3.4.4-plugins-filters-fingerprint-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v3.4.4-plugins-filters-fingerprint-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      fingerprint {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v3.4.4-plugins-filters-fingerprint-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      fingerprint {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      fingerprint {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v3.4.4-plugins-filters-fingerprint-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.4.4-plugins-filters-fingerprint-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 fingerprint filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      fingerprint {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v3.4.4-plugins-filters-fingerprint-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v3.4.4-plugins-filters-fingerprint-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      fingerprint {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      fingerprint {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v3.4.4-plugins-filters-fingerprint-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      fingerprint {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      fingerprint {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
