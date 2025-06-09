---
navigation_title: "v2.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v2.0.6-plugins-filters-cipher.html
---

# Cipher filter plugin v2.0.6 [v2.0.6-plugins-filters-cipher]

* Plugin version: v2.0.6
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-filter-cipher/blob/v2.0.6/CHANGELOG.md)

For other versions, see the [overview list](filter-cipher-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1733]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-cipher). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1711]

This filter parses a source and apply a cipher or decipher before storing it in the target.

## Cipher Filter Configuration Options [v2.0.6-plugins-filters-cipher-options]

This plugin supports the following configuration options plus the [Common options](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`algorithm`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-algorithm) | [string](/lsr/value-types.md#string) | Yes |
| [`base64`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-base64) | [boolean](/lsr/value-types.md#boolean) | No |
| [`cipher_padding`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-cipher_padding) | [string](/lsr/value-types.md#string) | No |
| [`iv_random_length`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-iv_random_length) | [number](/lsr/value-types.md#number) | No |
| [`key`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-key) | [string](/lsr/value-types.md#string) | No |
| [`key_pad`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-key_pad) | <<,>> | No |
| [`key_size`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-key_size) | [number](/lsr/value-types.md#number) | No |
| [`max_cipher_reuse`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-max_cipher_reuse) | [number](/lsr/value-types.md#number) | No |
| [`mode`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-mode) | [string](/lsr/value-types.md#string) | Yes |
| [`source`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-source) | [string](/lsr/value-types.md#string) | No |
| [`target`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-target) | [string](/lsr/value-types.md#string) | No |

Also see [Common options](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-common-options) for a list of options supported by all filter plugins.

### `algorithm` [v2.0.6-plugins-filters-cipher-algorithm]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The cipher algorithm

A list of supported algorithms can be obtained by

```
    puts OpenSSL::Cipher.ciphers
```

### `base64` [v2.0.6-plugins-filters-cipher-base64]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Do we have to perform a `base64` decode or encode?

If we are decrypting, `base64` decode will be done before. If we are encrypting, `base64` will be done after.

### `cipher_padding` [v2.0.6-plugins-filters-cipher-cipher_padding]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Cipher padding to use. Enables or disables padding.

By default encryption operations are padded using standard block padding and the padding is checked and removed when decrypting. If the pad parameter is zero then no padding is performed, the total amount of data encrypted or decrypted must then be a multiple of the block size or an error will occur.

See EVP\_CIPHER\_CTX\_set\_padding for further information.

We are using Openssl jRuby which uses default padding to PKCS5Padding If you want to change it, set this parameter. If you want to disable it, Set this parameter to 0

```
    filter { cipher { cipher_padding => 0 }}
```

### `iv` (DEPRECATED) [v2.0.6-plugins-filters-cipher-iv]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The initialization vector to use (statically hard-coded). For a random IV see the iv\_random\_length property

If iv\_random\_length is set, it takes precedence over any value set for "iv"

The cipher modes CBC, CFB, OFB and CTR all need an "initialization vector", or short, IV. ECB mode is the only mode that does not require an IV, but there is almost no legitimate use case for this mode because of the fact that it does not sufficiently hide plaintext patterns.

For AES algorithms set this to a 16 byte string.

```
    filter { cipher { iv => "1234567890123456" }}
```

Deprecated: Please use `iv_random_length` instead

### `iv_random_length` [v2.0.6-plugins-filters-cipher-iv_random_length]

* Value type is [number](/lsr/value-types.md#number)
* There is no default value for this setting.

Force an random IV to be used per encryption invocation and specify the length of the random IV that will be generated via:

```
OpenSSL::Random.random_bytes(int_length)
```

If iv\_random\_length is set, it takes precedence over any value set for "iv"

Enabling this will force the plugin to generate a unique random IV for each encryption call. This random IV will be prepended to the encrypted result bytes and then base64 encoded. On decryption "iv\_random\_length" must also be set to utilize this feature. Random IV’s are better than statically hardcoded IVs

For AES algorithms you can set this to a 16

```
    filter { cipher { iv_random_length => 16 }}
```

### `key` [v2.0.6-plugins-filters-cipher-key]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

The key to use

If you encounter an error message at runtime containing the following:

"java.security.InvalidKeyException: Illegal key size: possibly you need to install Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files for your JRE"

Please read the following: <https://github.com/jruby/jruby/wiki/UnlimitedStrengthCrypto>

### `key_pad` [v2.0.6-plugins-filters-cipher-key_pad]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"\u0000"`

The character used to pad the key

### `key_size` [v2.0.6-plugins-filters-cipher-key_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `16`

The key size to pad

It depends of the cipher algorithm. If your key doesn’t need padding, don’t set this parameter

Example, for AES-128, we must have 16 char long key. AES-256 = 32 chars

```
    filter { cipher { key_size => 16 }
```

### `max_cipher_reuse` [v2.0.6-plugins-filters-cipher-max_cipher_reuse]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

If this is set the internal Cipher instance will be re-used up to @max\_cipher\_reuse times before being reset() and re-created from scratch. This is an option for efficiency where lots of data is being encrypted and decrypted using this filter. This lets the filter avoid creating new Cipher instances over and over for each encrypt/decrypt operation.

This is optional, the default is no re-use of the Cipher instance and max\_cipher\_reuse = 1 by default

```
    filter { cipher { max_cipher_reuse => 1000 }}
```

### `mode` [v2.0.6-plugins-filters-cipher-mode]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Encrypting or decrypting some data

Valid values are encrypt or decrypt

### `source` [v2.0.6-plugins-filters-cipher-source]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The field to perform filter

Example, to use the @message field (default) :

```
    filter { cipher { source => "message" } }
```

### `target` [v2.0.6-plugins-filters-cipher-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"message"`

The name of the container to put the result

Example, to place the result into crypt :

```
    filter { cipher { target => "crypt" } }
```

## Common options [v2.0.6-plugins-filters-cipher-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v2-0-6-plugins-filters-cipher.md#v2.0.6-plugins-filters-cipher-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v2.0.6-plugins-filters-cipher-add_field]

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

### `add_tag` [v2.0.6-plugins-filters-cipher-add_tag]

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

### `enable_metric` [v2.0.6-plugins-filters-cipher-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v2.0.6-plugins-filters-cipher-id]

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

### `periodic_flush` [v2.0.6-plugins-filters-cipher-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v2.0.6-plugins-filters-cipher-remove_field]

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

### `remove_tag` [v2.0.6-plugins-filters-cipher-remove_tag]

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
