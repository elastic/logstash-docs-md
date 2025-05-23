---
navigation_title: "v3.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.3-plugins-filters-translate.html
---

# Translate filter plugin v3.0.3 [v3.0.3-plugins-filters-translate]


* Plugin version: v3.0.3
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-translate/blob/v3.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-translate-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2169]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-translate). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2147]

A general search and replace tool that uses a configured hash and/or a file to determine replacement values. Currently supported are YAML, JSON, and CSV files.

The dictionary entries can be specified in one of two ways: First, the `dictionary` configuration item may contain a hash representing the mapping. Second, an external file (readable by logstash) may be specified in the `dictionary_path` configuration item. These two methods may not be used in conjunction; it will produce an error.

Operationally, if the event field specified in the `field` configuration matches the EXACT contents of a dictionary entry key (or matches a regex if `regex` configuration item has been enabled), the field’s value will be substituted with the matched key’s value from the dictionary.

By default, the translate filter will replace the contents of the maching event field (in-place). However, by using the `destination` configuration item, you may also specify a target event field to populate with the new translated value.

Alternatively, for simple string search and replacements for just a few values you might consider using the gsub function of the mutate filter.


## Translate Filter Configuration Options [v3.0.3-plugins-filters-translate-options]

This plugin supports the following configuration options plus the [Common options](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`destination`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-destination) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`dictionary`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-dictionary) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`dictionary_path`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-dictionary_path) | a valid filesystem path | No |
| [`exact`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-exact) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`fallback`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-fallback) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-field) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`override`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-override) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`refresh_interval`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-refresh_interval) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`regex`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-regex) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-common-options) for a list of options supported by all filter plugins.

 

### `destination` [v3.0.3-plugins-filters-translate-destination]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"translation"`

The destination field you wish to populate with the translated code. The default is a field named `translation`. Set this to the same value as source if you want to do a substitution, in this case filter will allways succeed. This will clobber the old value of the source field!


### `dictionary` [v3.0.3-plugins-filters-translate-dictionary]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

The dictionary to use for translation, when specified in the logstash filter configuration item (i.e. do not use the `@dictionary_path` file).

Example:

```ruby
    filter {
      translate {
        dictionary => [ "100", "Continue",
                        "101", "Switching Protocols",
                        "merci", "thank you",
                        "old version", "new version" ]
      }
    }
```

::::{note}
It is an error to specify both `dictionary` and `dictionary_path`.
::::



### `dictionary_path` [v3.0.3-plugins-filters-translate-dictionary_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The full path of the external dictionary file. The format of the table should be a standard YAML, JSON, or CSV. Make sure you specify any integer-based keys in quotes. For example, the YAML file should look something like this:

```ruby
    "100": Continue
    "101": Switching Protocols
    merci: gracias
    old version: new version
```

::::{note}
it is an error to specify both `dictionary` and `dictionary_path`.
::::


The currently supported formats are YAML, JSON, and CSV. Format selection is based on the file extension: `json` for JSON, `yaml` or `yml` for YAML, and `csv` for CSV. The JSON format only supports simple key/value, unnested objects. The CSV format expects exactly two columns, with the first serving as the original text, and the second column as the replacement.


### `exact` [v3.0.3-plugins-filters-translate-exact]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

When `exact => true`, the translate filter will populate the destination field with the exact contents of the dictionary value. When `exact => false`, the filter will populate the destination field with the result of any existing destination field’s data, with the translated value substituted in-place.

For example, consider this simple translation.yml, configured to check the `data` field:

```ruby
    foo: bar
```

If logstash receives an event with the `data` field set to `foo`, and `exact => true`, the destination field will be populated with the string `bar`. If `exact => false`, and logstash receives the same event, the destination field will be also set to `bar`. However, if logstash receives an event with the `data` field set to `foofing`, the destination field will be set to `barfing`.

Set both `exact => true` AND `regex => `true` if you would like to match using dictionary keys as regular expressions. A large dictionary could be expensive to match in this case.


### `fallback` [v3.0.3-plugins-filters-translate-fallback]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

In case no translation occurs in the event (no matches), this will add a default translation string, which will always populate `field`, if the match failed.

For example, if we have configured `fallback => "no match"`, using this dictionary:

```ruby
    foo: bar
```

Then, if logstash received an event with the field `foo` set to `bar`, the destination field would be set to `bar`. However, if logstash received an event with `foo` set to `nope`, then the destination field would still be populated, but with the value of `no match`. This configuration can be dynamic and include parts of the event using the `%{{field}}` syntax.


### `field` [v3.0.3-plugins-filters-translate-field]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the logstash event field containing the value to be compared for a match by the translate filter (e.g. `message`, `host`, `response_code`).

If this field is an array, only the first value will be used.


### `override` [v3.0.3-plugins-filters-translate-override]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If the destination (or target) field already exists, this configuration item specifies whether the filter should skip translation (default) or overwrite the target field value with the new translation value.


### `refresh_interval` [v3.0.3-plugins-filters-translate-refresh_interval]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `300`

When using a dictionary file, this setting will indicate how frequently (in seconds) logstash will check the dictionary file for updates.


### `regex` [v3.0.3-plugins-filters-translate-regex]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If you’d like to treat dictionary keys as regular expressions, set `exact => true`. Note: this is activated only when `exact => true`.



## Common options [v3.0.3-plugins-filters-translate-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-0-3-plugins-filters-translate.md#v3.0.3-plugins-filters-translate-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.0.3-plugins-filters-translate-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      translate {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      translate {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.0.3-plugins-filters-translate-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      translate {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      translate {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.0.3-plugins-filters-translate-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.3-plugins-filters-translate-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 translate filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      translate {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.0.3-plugins-filters-translate-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.0.3-plugins-filters-translate-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      translate {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      translate {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.0.3-plugins-filters-translate-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      translate {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      translate {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



