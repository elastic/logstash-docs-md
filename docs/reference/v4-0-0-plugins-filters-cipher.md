---
navigation_title: "v4.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.0-plugins-filters-cipher.html
---

# Cipher filter plugin v4.0.0 [v4.0.0-plugins-filters-cipher]


* Plugin version: v4.0.0
* Released on: 2019-01-11
* [Changelog](https://github.com/logstash-plugins/logstash-filter-cipher/blob/v4.0.0/CHANGELOG.md)

For other versions, see the [overview list](filter-cipher-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1710]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-cipher). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1688]

This filter parses a source and apply a cipher or decipher before storing it in the target.


## Cipher Filter Configuration Options [v4.0.0-plugins-filters-cipher-options]

This plugin supports the following configuration options plus the [Common options](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`algorithm`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-algorithm) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`base64`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-base64) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`cipher_padding`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-cipher_padding) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`iv_random_length`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-iv_random_length) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`key`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`key_pad`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-key_pad) | <<,>> | No |
| [`key_size`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-key_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`max_cipher_reuse`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-max_cipher_reuse) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`mode`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-mode) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`source`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-source) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`target`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-common-options) for a list of options supported by all filter plugins.

 

### `algorithm` [v4.0.0-plugins-filters-cipher-algorithm]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The cipher algorithm

A list of supported algorithms can be obtained by

```ruby
    puts OpenSSL::Cipher.ciphers
```


### `base64` [v4.0.0-plugins-filters-cipher-base64]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Do we have to perform a `base64` decode or encode?

If we are decrypting, `base64` decode will be done before. If we are encrypting, `base64` will be done after.


### `cipher_padding` [v4.0.0-plugins-filters-cipher-cipher_padding]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Cipher padding to use. Enables or disables padding.

By default encryption operations are padded using standard block padding and the padding is checked and removed when decrypting. If the pad parameter is zero then no padding is performed, the total amount of data encrypted or decrypted must then be a multiple of the block size or an error will occur.

See EVP_CIPHER_CTX_set_padding for further information.

We are using Openssl jRuby which uses default padding to PKCS5Padding If you want to change it, set this parameter. If you want to disable it, Set this parameter to 0

```ruby
    filter { cipher { cipher_padding => 0 }}
```


### `iv_random_length` [v4.0.0-plugins-filters-cipher-iv_random_length]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

Force an random IV to be used per encryption invocation and specify the length of the random IV that will be generated via:

```
OpenSSL::Random.random_bytes(int_length)
```
If iv_random_length is set, it takes precedence over any value set for "iv"

Enabling this will force the plugin to generate a unique random IV for each encryption call. This random IV will be prepended to the encrypted result bytes and then base64 encoded. On decryption "iv_random_length" must also be set to utilize this feature. Random IV’s are better than statically hardcoded IVs

For AES algorithms you can set this to a 16

```ruby
    filter { cipher { iv_random_length => 16 }}
```


### `key` [v4.0.0-plugins-filters-cipher-key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The key to use

::::{note}
If you encounter an error message at runtime containing the following:
::::


"java.security.InvalidKeyException: Illegal key size: possibly you need to install Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files for your JRE"

Please read the following: [https://github.com/jruby/jruby/wiki/UnlimitedStrengthCrypto](https://github.com/jruby/jruby/wiki/UnlimitedStrengthCrypto)


### `key_pad` [v4.0.0-plugins-filters-cipher-key_pad]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"\u0000"`

The character used to pad the key


### `key_size` [v4.0.0-plugins-filters-cipher-key_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `16`

The key size to pad

It depends of the cipher algorithm. If your key doesn’t need padding, don’t set this parameter

Example, for AES-128, we must have 16 char long key. AES-256 = 32 chars

```ruby
    filter { cipher { key_size => 16 }
```


### `max_cipher_reuse` [v4.0.0-plugins-filters-cipher-max_cipher_reuse]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

If this is set the internal Cipher instance will be re-used up to @max_cipher_reuse times before being reset() and re-created from scratch. This is an option for efficiency where lots of data is being encrypted and decrypted using this filter. This lets the filter avoid creating new Cipher instances over and over for each encrypt/decrypt operation.

This is optional, the default is no re-use of the Cipher instance and max_cipher_reuse = 1 by default

```ruby
    filter { cipher { max_cipher_reuse => 1000 }}
```


### `mode` [v4.0.0-plugins-filters-cipher-mode]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Encrypting or decrypting some data

Valid values are encrypt or decrypt


### `source` [v4.0.0-plugins-filters-cipher-source]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The field to perform filter

Example, to use the @message field (default) :

```ruby
    filter { cipher { source => "message" } }
```


### `target` [v4.0.0-plugins-filters-cipher-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"message"`

The name of the container to put the result

Example, to place the result into crypt :

```ruby
    filter { cipher { target => "crypt" } }
```



## Common options [v4.0.0-plugins-filters-cipher-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v4-0-0-plugins-filters-cipher.md#v4.0.0-plugins-filters-cipher-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v4.0.0-plugins-filters-cipher-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      cipher {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v4.0.0-plugins-filters-cipher-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      cipher {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      cipher {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v4.0.0-plugins-filters-cipher-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.0.0-plugins-filters-cipher-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 cipher filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      cipher {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v4.0.0-plugins-filters-cipher-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v4.0.0-plugins-filters-cipher-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      cipher {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      cipher {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v4.0.0-plugins-filters-cipher-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      cipher {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      cipher {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



