---
navigation_title: "v1.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.2-plugins-filters-emoji.html
---

# Emoji filter plugin v1.0.2 [v1.0.2-plugins-filters-emoji]

* Plugin version: v1.0.2
* Released on: 2017-08-15
* [Changelog](https://github.com/logstash-plugins/logstash-filter-emoji/blob/v1.0.2/CHANGELOG.md)

For other versions, see the [overview list](filter-emoji-index.md "Versioned emoji filter plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_1867]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-emoji). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_1845]

This plugin maps the severity names or numeric codes as defined in [RFC 3164](https://tools.ietf.org/html/rfc3164#section-4.1.1) and [RFC 5424](https://tools.ietf.org/html/rfc5424#section-6.2.1) to the emoji as defined in the configuration.

### Emoji Filter Configuration Options [v1.0.2-plugins-filters-emoji-options]

This plugin supports the following configuration options plus the [Common options](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`fallback`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-fallback "fallback") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`field`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-field "field") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | Yes |
| [`override`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-override "override") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`sev_alert`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_alert "sev_alert") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_critical`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_critical "sev_critical") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_debug`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_debug "sev_debug") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_emergency`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_emergency "sev_emergency") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_error`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_error "sev_error") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_info`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_info "sev_info") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_notice`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_notice "sev_notice") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`sev_warning`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-sev_warning "sev_warning") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`target`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-target "target") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

Also see [Common options](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-common-options "Common options") for a list of options supported by all filter plugins.

 

#### `fallback` [v1.0.2-plugins-filters-emoji-fallback]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

In case no match is found in the event, this will add a default emoji, which will always populate `target`, if the match failed.

For example, if we have configured `fallback => "`❓`"`, using this dictionary:

```
    foo: 👤
```

Then, if logstash received an event with the field `foo` set to 👤, the target field would be set to 👤. However, if logstash received an event with `foo` set to `nope`, then the target field would still be populated, but with the value of ❓. This configuration can be dynamic and include parts of the event using the `%{field}` syntax.

#### `field` [v1.0.2-plugins-filters-emoji-field]

* This is a required setting.
* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

The name of the logstash event field containing the value to be compared for a match by the emoji filter (e.g. `severity`).

If this field is an array, only the first value will be used.

#### `override` [v1.0.2-plugins-filters-emoji-override]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

If the target field already exists, this configuration item specifies whether the filter should skip being rewritten as an emoji (default) or overwrite the target field value with the emoji value.

#### `sev_alert` [v1.0.2-plugins-filters-emoji-sev_alert]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"🚨"`

`sev_alert` selects the emoji/unicode character for Alert severity

#### `sev_critical` [v1.0.2-plugins-filters-emoji-sev_critical]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"🔥"`

`sev_critical` selects the emoji/unicode character for Critical severity

#### `sev_debug` [v1.0.2-plugins-filters-emoji-sev_debug]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"🐛"`

`sev_debug` selects the emoji/unicode character for Debug severity

#### `sev_emergency` [v1.0.2-plugins-filters-emoji-sev_emergency]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"💥"`

`sev_emergency` selects the emoji/unicode character for Emergency severity

#### `sev_error` [v1.0.2-plugins-filters-emoji-sev_error]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"❌"`

`sev_error` selects the emoji/unicode character for Error severity

#### `sev_info` [v1.0.2-plugins-filters-emoji-sev_info]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"ℹ️"`

`sev_info` selects the emoji/unicode character for Informational severity

#### `sev_notice` [v1.0.2-plugins-filters-emoji-sev_notice]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"👀"`

`sev_notice` selects the emoji/unicode character for Notice severity

#### `sev_warning` [v1.0.2-plugins-filters-emoji-sev_warning]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"⚠️"`

`sev_warning` selects the emoji/unicode character for Warning severity

#### `target` [v1.0.2-plugins-filters-emoji-target]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"emoji"`

The target field you wish to populate with the emoji. The default is a field named `emoji`. Set this to the same value as the source (`field`) if you want to do a substitution, in this case filter will allways succeed. This will overwrite the old value of the source field!

### Common options [v1.0.2-plugins-filters-emoji-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-add_field "add_field") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`add_tag`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-add_tag "add_tag") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`enable_metric`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`periodic_flush`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-periodic_flush "periodic_flush") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`remove_field`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-remove_field "remove_field") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`remove_tag`](v1-0-2-plugins-filters-emoji.md#v1.0.2-plugins-filters-emoji-remove_tag "remove_tag") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |

#### `add_field` [v1.0.2-plugins-filters-emoji-add_field]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      emoji {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      emoji {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

#### `add_tag` [v1.0.2-plugins-filters-emoji-add_tag]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      emoji {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      emoji {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

#### `enable_metric` [v1.0.2-plugins-filters-emoji-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v1.0.2-plugins-filters-emoji-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 emoji filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      emoji {
        id => "ABC"
      }
    }
```

#### `periodic_flush` [v1.0.2-plugins-filters-emoji-periodic_flush]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

#### `remove_field` [v1.0.2-plugins-filters-emoji-remove_field]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      emoji {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      emoji {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

#### `remove_tag` [v1.0.2-plugins-filters-emoji-remove_tag]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      emoji {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      emoji {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
