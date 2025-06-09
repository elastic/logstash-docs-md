---
navigation_title: "v4.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.2-plugins-filters-cipher.html
---

# Cipher filter plugin v4.0.2 [v4.0.2-plugins-filters-cipher]

* Plugin version: v4.0.2
* Released on: 2022-02-11
* [Changelog](https://github.com/logstash-plugins/logstash-filter-cipher/blob/v4.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-cipher-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1725]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-cipher). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1703]

This filter parses a source and apply a cipher or decipher before storing it in the target.

Prior to version 4.0.1, this plugin was not thread-safe and could not safely be used with multiple pipeline workers.

## Cipher Filter Configuration Options [v4.0.2-plugins-filters-cipher-options]

This plugin supports the following configuration options plus the [Common options](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`algorithm`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-algorithm) | [string](/lsr/value-types.md#string) | Yes |
| [`base64`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-base64) | [boolean](/lsr/value-types.md#boolean) | No |
| [`cipher_padding`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-cipher_padding) | [string](/lsr/value-types.md#string) | No |
| [`iv_random_length`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-iv_random_length) | [number](/lsr/value-types.md#number) | No |
| [`key`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key) | [string](/lsr/value-types.md#string) | No |
| [`key_pad`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key_pad) | [string](/lsr/value-types.md#string) | No |
| [`key_size`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key_size) | [number](/lsr/value-types.md#number) | No |
| [`max_cipher_reuse`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-max_cipher_reuse) | [number](/lsr/value-types.md#number) | No |
| [`mode`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode) | [string](/lsr/value-types.md#string) | Yes |
| [`source`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-source) | [string](/lsr/value-types.md#string) | No |
| [`target`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-common-options) for a list of options supported by all filter plugins.

### `algorithm` [v4.0.2-plugins-filters-cipher-algorithm]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The cipher algorithm to use for encryption and decryption operations.

A list of supported algorithms depends on the versions of Logstash, JRuby, and Java this plugin is running in, but can be obtained by running:

```
    cd $LOGSTASH_HOME # <-- your Logstash distribution root
    bin/ruby -ropenssl -e 'puts OpenSSL::Cipher.ciphers'
```

### `base64` [v4.0.2-plugins-filters-cipher-base64]

* Value type is [boolean](/lsr/value-types.md#boolean)

* Default value is `true`

* Unless this option is disabled:

  * When [`mode => encrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the source ciphertext will be `base64`-decoded before it is deciphered.
  * When [`mode => decrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the result ciphertext will be `base64`-encoded before it is stored.

### `cipher_padding` [v4.0.2-plugins-filters-cipher-cipher_padding]

* Value type is [string](/lsr/value-types.md#string)

  * `0`: means `false`
  * `1`: means `true`

* There is no default value for this setting.

Enables or disables padding in encryption operations.

In encryption operations with block-ciphers, the input plaintext must be an *exact* multiple of the cipher’s block-size unless padding is enabled.

Disabling padding by setting this value to `0` will cause this plugin to fail to encrypt any input plaintext that doesn’t strictly adhere to the [`algorithm`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-algorithm)'s block size requirements.

```
    filter { cipher { cipher_padding => 0 }}
```

### `iv_random_length` [v4.0.2-plugins-filters-cipher-iv_random_length]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

In encryption operations, this plugin generates a random Initialization Vector (IV) per encryption operation. This is a standard best-practice to ensure that the resulting ciphertexts cannot be compared to infer equivalence of the source plaintext. This unique IV is then *prepended* to the resulting ciphertext before it is stored, ensuring it is available to any process that needs to decrypt it.

In decryption operations, the IV is assumed to have been prepended to the ciphertext, so this plugin needs to know the length of the IV in order to split the input appropriately.

The size of the IV is generally dependent on which [`algorithm`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-algorithm) is used. AES Algorithms generally use a 16-byte IV:

```
    filter { cipher { iv_random_length => 16 }}
```

### `key` [v4.0.2-plugins-filters-cipher-key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The key to use for encryption and decryption operations.

Please read the [UnlimitedStrengthCrypto topic](https://github.com/jruby/jruby/wiki/UnlimitedStrengthCrypto) in the [jruby](https://github.com/jruby/jruby) github repo if you see a runtime error that resembles:

`java.security.InvalidKeyException: Illegal key size: possibly you need to install Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files for your JRE`

### `key_pad` [v4.0.2-plugins-filters-cipher-key_pad]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"\u0000"`

The character used to pad the key to the required [`key_size`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key_size).

### `key_size` [v4.0.2-plugins-filters-cipher-key_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `16`

The cipher’s required key size, which depends on which [`algorithm`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-algorithm) you are using. If a [`key`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key) is specified with a shorter value, it will be padded with [`key_pad`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-key_pad).

Example, for AES-128, we must have 16 char long key. AES-256 = 32 chars

```
    filter { cipher { key_size => 16 }
```

### `max_cipher_reuse` [v4.0.2-plugins-filters-cipher-max_cipher_reuse]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

If this value is set, the internal Cipher instance will be re-used up to `max_cipher_reuse` times before it is re-created from scratch. This is an option for efficiency where lots of data is being encrypted and decrypted using this filter. This lets the filter avoid creating new Cipher instances over and over for each encrypt/decrypt operation.

This is optional, the default is no re-use of the Cipher instance and max\_cipher\_reuse = 1 by default

```
    filter { cipher { max_cipher_reuse => 1000 }}
```

### `mode` [v4.0.2-plugins-filters-cipher-mode]

* This is a required setting.

* Value type is [string](/lsr/value-types.md#string)

  * `encrypt`: encrypts a plaintext value into IV + ciphertext
  * `decrypt`: decrypts an IV + ciphertext value into plaintext

* There is no default value for this setting.

### `source` [v4.0.2-plugins-filters-cipher-source]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The name of the source field.

* When [`mode => encrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the `source` should be a field containing plaintext
* When [`mode => decrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the `source` should be a field containing IV + ciphertext

Example, to use the `message` field (default) :

```
    filter { cipher { source => "message" } }
```

### `target` [v4.0.2-plugins-filters-cipher-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The name of the target field to put the result:

* When [`mode => encrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the IV + ciphertext result will be stored in the `target` field
* When [`mode => decrypt`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-mode), the plaintext result will be stored in the `target` field

Example, to place the result into crypt:

```
    filter { cipher { target => "crypt" } }
```

## Common options [v4.0.2-plugins-filters-cipher-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v4-0-2-plugins-filters-cipher.md#v4.0.2-plugins-filters-cipher-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v4.0.2-plugins-filters-cipher-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      cipher {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      cipher {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v4.0.2-plugins-filters-cipher-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      cipher {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      cipher {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v4.0.2-plugins-filters-cipher-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.2-plugins-filters-cipher-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 cipher filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      cipher {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v4.0.2-plugins-filters-cipher-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v4.0.2-plugins-filters-cipher-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      cipher {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      cipher {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v4.0.2-plugins-filters-cipher-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      cipher {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      cipher {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
