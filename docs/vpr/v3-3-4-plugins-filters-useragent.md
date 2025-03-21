---
navigation_title: "v3.3.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.4-plugins-filters-useragent.html
---

# Useragent filter plugin v3.3.4 [v3.3.4-plugins-filters-useragent]


* Plugin version: v3.3.4
* Released on: 2023-03-13
* [Changelog](https://github.com/logstash-plugins/logstash-filter-useragent/blob/v3.3.4/CHANGELOG.md)

For other versions, see the [overview list](filter-useragent-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2183]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-useragent). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2161]

Parse user agent strings into structured data based on BrowserScope data

UserAgent filter, adds information about user agent like name, version, operating system, and device.

The plugin ships with the **regexes.yaml** database made available from ua-parser with an Apache 2.0 license. For more details on ua-parser, see [https://github.com/ua-parser/uap-core/](https://github.com/ua-parser/uap-core/).


## Compatibility with the Elastic Common Schema (ECS) [_compatibility_with_the_elastic_common_schema_ecs_82]

This plugin can be used to parse user-agent (UA) *into* fields compliant with the Elastic Common Schema. Here’s how [ECS compatibility mode](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-ecs_compatibility) affects output.

| ECS disabled | ECS v1, v8 | Description | Notes |
| --- | --- | --- | --- |
| [name] | [user_agent][name] | *Detected UA name* |  |
| [version]* | [user_agent][version] | *Detected UA version* | *Only available in ECS mode* |
| [major] | [@metadata][filter][user_agent][version][major] | *UA major version* | *Only as meta-data in ECS mode* |
| [minor] | [@metadata][filter][user_agent][version][minor] | *UA minor version* | *Only as meta-data in ECS mode* |
| [patch] | [@metadata][filter][user_agent][version][patch] | *UA patch version* | *Only as meta-data in ECS mode* |
| [os_name] | [user_agent][os][name] | *Detected operating-system name* |  |
| [os_version]* | [user_agent][os][version] | *Detected OS version* | *Only available in ECS mode* |
| [os_major] | [@metadata][filter][user_agent][os][version][major] | *OS major version* | *Only as meta-data in ECS mode* |
| [os_minor] | [@metadata][filter][user_agent][os][version][minor] | *OS minor version* | *Only as meta-data in ECS mode* |
| [os_patch] | [@metadata][filter][user_agent][os][version][patch] | *OS patch version* | *Only as meta-data in ECS mode* |
| [os_full] | [user_agent][os][full] | *Full operating-system name* |  |
| [device] | [user_agent][device][name] | *Device name* |  |

::::{note}
`[version]` and `[os_version]` fields were added in Logstash **7.14** and are not available by default in earlier versions.
::::


Example:

```ruby
    filter {
      useragent {
        source => 'message'
      }
    }
```

Given an event with the `message` field set as: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0` produces the following fields:

```ruby
    {
        "name"=>"Firefox",
        "version"=>"45.0", # since plugin version 3.3.0
        "major"=>"45",
        "minor"=>"0",
        "os_name"=>"Mac OS X",
        "os_version"=>"10.11", # since plugin version 3.3.0
        "os_full"=>"Mac OS X 10.11",
        "os_major"=>"10",
        "os_minor"=>"11",
        "device"=>"Mac"
    }
```

**and with ECS enabled:**

```ruby
    {
        "user_agent"=>{
            "name"=>"Firefox",
            "version"=>"45.0",
            "os"=>{
                "name"=>"Mac OS X",
                "version"=>"10.11",
                "full"=>"Mac OS X 10.11"
            },
            "device"=>{"name"=>"Mac"},
        }
    }
```


## Useragent Filter Configuration Options [v3.3.4-plugins-filters-useragent-options]

This plugin supports the following configuration options plus the [Common options](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`ecs_compatibility`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`lru_cache_size`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-lru_cache_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`prefix`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-prefix) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`regexes`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-regexes) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`source`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-source) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`target`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-common-options) for a list of options supported by all filter plugins.

 

### `ecs_compatibility` [v3.3.4-plugins-filters-useragent-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: does not use ECS-compatible field names (fields might be set at the root of the event)
    * `v1`, `v8`: uses fields that are compatible with Elastic Common Schema (for example, `[user_agent][version]`)

* Default value depends on which version of Logstash is running:

    * When Logstash provides a `pipeline.ecs_compatibility` setting, its value is used as the default
    * Otherwise, the default value is `disabled`.


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). The value of this setting affects the *default* value of [`target`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-target).


### `lru_cache_size` [v3.3.4-plugins-filters-useragent-lru_cache_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100000`

UA parsing is surprisingly expensive. This filter uses an LRU cache to take advantage of the fact that user agents are often found adjacent to one another in log files and rarely have a random distribution. The higher you set this the more likely an item is to be in the cache and the faster this filter will run. However, if you set this too high you can use more memory than desired.

Experiment with different values for this option to find the best performance for your dataset.

This MUST be set to a value > 0. There is really no reason to not want this behavior, the overhead is minimal and the speed gains are large.

It is important to note that this config value is global. That is to say all instances of the user agent filter share the same cache. The last declared cache size will *win*. The reason for this is that there would be no benefit to having multiple caches for different instances at different points in the pipeline, that would just increase the number of cache misses and waste memory.


### `prefix` [v3.3.4-plugins-filters-useragent-prefix]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

A string to prepend to all of the extracted keys


### `regexes` [v3.3.4-plugins-filters-useragent-regexes]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

If not specified, this will default to the `regexes.yaml` that ships with logstash. Otherwise use the provided `regexes.yaml` file.

You can find the latest version of this here: [https://github.com/ua-parser/uap-core/blob/master/regexes.yaml](https://github.com/ua-parser/uap-core/blob/master/regexes.yaml)


### `source` [v3.3.4-plugins-filters-useragent-source]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The field containing the user agent string. If this field is an array, only the first value will be used.


### `target` [v3.3.4-plugins-filters-useragent-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value depends on whether [`ecs_compatibility`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-ecs_compatibility) is enabled:

    * ECS Compatibility disabled: no default value for this setting
    * ECS Compatibility enabled: `"user_agent"`


The name of the field to assign user agent data into.

If not specified user agent data will be stored in the root of the event.



## Common options [v3.3.4-plugins-filters-useragent-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v3-3-4-plugins-filters-useragent.md#v3.3.4-plugins-filters-useragent-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v3.3.4-plugins-filters-useragent-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      useragent {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      useragent {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v3.3.4-plugins-filters-useragent-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      useragent {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      useragent {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v3.3.4-plugins-filters-useragent-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.3.4-plugins-filters-useragent-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 useragent filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      useragent {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v3.3.4-plugins-filters-useragent-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v3.3.4-plugins-filters-useragent-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      useragent {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      useragent {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v3.3.4-plugins-filters-useragent-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      useragent {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      useragent {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
