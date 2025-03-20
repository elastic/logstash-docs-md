---
navigation_title: "v1.0.3"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.3-plugins-filters-jdbc_streaming.html
---

# Jdbc_streaming filter plugin v1.0.3 [v1.0.3-plugins-filters-jdbc_streaming]


* Plugin version: v1.0.3
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-filter-jdbc_streaming/blob/v1.0.3/CHANGELOG.md)

For other versions, see the [overview list](filter-jdbc_streaming-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2039]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-jdbc_streaming). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2017]

This filter executes a SQL query and store the result set in the field specified as `target`. It will cache the results locally in an LRU cache with expiry

For example you can load a row based on an id from in the event

```ruby
filter {
  jdbc_streaming {
    jdbc_driver_library => "/path/to/mysql-connector-java-5.1.34-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => ""jdbc:mysql://localhost:3306/mydatabase"
    jdbc_user => "me"
    jdbc_password => "secret"
    statement => "select * from WORLD.COUNTRY WHERE Code = :code"
    parameters => { "code" => "country_code"}
    target => "country_details"
  }
}
```


## Jdbc_streaming Filter Configuration Options [v1.0.3-plugins-filters-jdbc_streaming-options]

This plugin supports the following configuration options plus the [Common options](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`cache_expiration`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-cache_expiration) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`cache_size`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-cache_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`default_hash`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-default_hash) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`jdbc_connection_string`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_connection_string) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_driver_class`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_driver_class) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_driver_library`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_driver_library) | a valid filesystem path | No |
| [`jdbc_password`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`jdbc_user`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`jdbc_validate_connection`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_validate_connection) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`jdbc_validation_timeout`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-jdbc_validation_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`parameters`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-parameters) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`statement`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-statement) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`tag_on_default_use`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-tag_on_default_use) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`tag_on_failure`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`target`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-target) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`use_cache`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-use_cache) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-common-options) for a list of options supported by all filter plugins.

 

### `cache_expiration` [v1.0.3-plugins-filters-jdbc_streaming-cache_expiration]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5.0`

The minimum number of seconds any entry should remain in the cache, defaults to 5 seconds A numeric value, you can use decimals for example `{ "cache_expiration" => 0.25 }` If there are transient jdbc errors the cache will store empty results for a given parameter set and bypass the jbdc lookup, this merges the default_hash into the event, until the cache entry expires, then the jdbc lookup will be tried again for the same parameters Conversely, while the cache contains valid results any external problem that would cause jdbc errors, will not be noticed for the cache_expiration period.


### `cache_size` [v1.0.3-plugins-filters-jdbc_streaming-cache_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `500`

The maximum number of cache entries are stored, defaults to 500 entries The least recently used entry will be evicted


### `default_hash` [v1.0.3-plugins-filters-jdbc_streaming-default_hash]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Define a default object to use when lookup fails to return a matching row. ensure that the key names of this object match the columns from the statement


### `jdbc_connection_string` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_connection_string]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC connection string


### `jdbc_driver_class` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_driver_class]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC driver class to load, for example "oracle.jdbc.OracleDriver" or "org.apache.derby.jdbc.ClientDriver"


### `jdbc_driver_library` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_driver_library]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Tentative of abstracting JDBC logic to a mixin for potential reuse in other plugins (input/output) This method is called when someone includes this module Add these methods to the *base* given. JDBC driver library path to third party driver library.


### `jdbc_password` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

JDBC password


### `jdbc_user` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC user


### `jdbc_validate_connection` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_validate_connection]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Connection pool configuration. Validate connection before use.


### `jdbc_validation_timeout` [v1.0.3-plugins-filters-jdbc_streaming-jdbc_validation_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `3600`

Connection pool configuration. How often to validate a connection (in seconds)


### `parameters` [v1.0.3-plugins-filters-jdbc_streaming-parameters]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Hash of query parameter, for example `{ "id" => "id_field" }`


### `statement` [v1.0.3-plugins-filters-jdbc_streaming-statement]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Statement to execute. To use parameters, use named parameter syntax, for example "SELECT * FROM MYTABLE WHERE ID = :id"


### `tag_on_default_use` [v1.0.3-plugins-filters-jdbc_streaming-tag_on_default_use]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_jdbcstreamingdefaultsused"]`

Append values to the `tags` field if no record was found and default values were used


### `tag_on_failure` [v1.0.3-plugins-filters-jdbc_streaming-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_jdbcstreamingfailure"]`

Append values to the `tags` field if sql error occured


### `target` [v1.0.3-plugins-filters-jdbc_streaming-target]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Define the target field to store the extracted result(s) Field is overwritten if exists


### `use_cache` [v1.0.3-plugins-filters-jdbc_streaming-use_cache]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Enable or disable caching, boolean true or false, defaults to true



## Common options [v1.0.3-plugins-filters-jdbc_streaming-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v1-0-3-plugins-filters-jdbc_streaming.md#v1.0.3-plugins-filters-jdbc_streaming-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v1.0.3-plugins-filters-jdbc_streaming-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      jdbc_streaming {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      jdbc_streaming {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v1.0.3-plugins-filters-jdbc_streaming-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      jdbc_streaming {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      jdbc_streaming {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v1.0.3-plugins-filters-jdbc_streaming-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.3-plugins-filters-jdbc_streaming-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jdbc_streaming filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      jdbc_streaming {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v1.0.3-plugins-filters-jdbc_streaming-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v1.0.3-plugins-filters-jdbc_streaming-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      jdbc_streaming {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      jdbc_streaming {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v1.0.3-plugins-filters-jdbc_streaming-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      jdbc_streaming {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      jdbc_streaming {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



