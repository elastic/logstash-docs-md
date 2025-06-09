---
navigation_title: "v5.1.10"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.1.10-plugins-filters-jdbc_streaming.html
---

# Jdbc_streaming filter plugin v5.1.10 [v5.1.10-plugins-filters-jdbc_streaming]

* A component of the [jdbc integration plugin](integration-jdbc-index.md)
* Integration version: v5.1.10
* Released on: 2021-12-16
* [Changelog](https://github.com/logstash-plugins/logstash-integration-jdbc/blob/v5.1.10/CHANGELOG.md)

For other versions, see the [overview list](filter-jdbc_streaming-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2045]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-jdbc). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2023]

This filter executes a SQL query and store the result set in the field specified as `target`. It will cache the results locally in an LRU cache with expiry.

For example, you can load a row based on an id in the event.

```
filter {
  jdbc_streaming {
    jdbc_driver_library => "/path/to/mysql-connector-java-5.1.34-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydatabase"
    jdbc_user => "me"
    jdbc_password => "secret"
    statement => "select * from WORLD.COUNTRY WHERE Code = :code"
    parameters => { "code" => "country_code"}
    target => "country_details"
  }
}
```

## Prepared Statements [v5.1.10-plugins-filters-jdbc_streaming-prepared_statements]

Using server side prepared statements can speed up execution times as the server optimises the query plan and execution.

Not all JDBC accessible technologies will support prepared statements.

With the introduction of Prepared Statement support comes a different code execution path and some new settings. Most of the existing settings are still useful but there are several new settings for Prepared Statements to read up on.

Use the boolean setting `use_prepared_statements` to enable this execution mode.

Use the `prepared_statement_name` setting to specify a name for the Prepared Statement, this identifies the prepared statement locally and remotely and it should be unique in your config and on the database.

Use the `prepared_statement_bind_values` array setting to specify the bind values. Typically, these values are indirectly extracted from your event, i.e. the string in the array refers to a field name in your event. You can also use constant values like numbers or strings but ensure that any string constants (e.g. a locale constant of "en" or "de") is not also an event field name. It is a good idea to use the bracketed field reference syntax for fields and normal strings for constants, e.g. `prepared_statement_bind_values => ["[src_ip]", "tokyo"],`.

There are 3 possible parameter schemes. Interpolated, field references and constants. Use interpolation when you are prefixing, suffixing or concatenating field values to create a value that exists in your database, e.g. "%{username}@%{domain}" → "<alice@example.org>", "%{distance}km" → "42km". Use field references for exact field values e.g. "\[srcip]" → "192.168.1.2". Use constants when a database column holds values that slice or categorise a number of similar records e.g. language translations.

A boolean setting `prepared_statement_warn_on_constant_usage`, defaulting to true, controls whether you will see a WARN message logged that warns when constants could be missing the bracketed field reference syntax. If you have set your field references and constants correctly you should set `prepared_statement_warn_on_constant_usage` to false. This setting and code checks should be deprecated in a future major Logstash release.

The `statement` (or `statement_path`) setting still holds the SQL statement but to use bind variables you must use the `?` character as a placeholder in the exact order found in the `prepared_statement_bind_values` array. Some technologies may require connection string properties to be set, see MySQL example below.

Example:

```
filter {
  jdbc_streaming {
    jdbc_driver_library => "/path/to/mysql-connector-java-5.1.34-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydatabase?cachePrepStmts=true&prepStmtCacheSize=250&prepStmtCacheSqlLimit=2048&useServerPrepStmts=true"
    jdbc_user => "me"
    jdbc_password => "secret"
    statement => "select * from WORLD.COUNTRY WHERE Code = ?"
    use_prepared_statements => true
    prepared_statement_name => "lookup_country_info"
    prepared_statement_bind_values => ["[country_code]"]
    target => "country_details"
  }
}
```

## Jdbc_streaming Filter Configuration Options [v5.1.10-plugins-filters-jdbc_streaming-options]

This plugin supports the following configuration options plus the [Common options](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`cache_expiration`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-cache_expiration) | [number](/lsr/value-types.md#number) | No |
| [`cache_size`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-cache_size) | [number](/lsr/value-types.md#number) | No |
| [`default_hash`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-default_hash) | [hash](/lsr/value-types.md#hash) | No |
| [`jdbc_connection_string`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_connection_string) | [string](/lsr/value-types.md#string) | Yes |
| [`jdbc_driver_class`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_driver_class) | [string](/lsr/value-types.md#string) | Yes |
| [`jdbc_driver_library`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_driver_library) | a valid filesystem path | No |
| [`jdbc_password`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_password) | [password](/lsr/value-types.md#password) | No |
| [`jdbc_user`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_user) | [string](/lsr/value-types.md#string) | No |
| [`jdbc_validate_connection`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_validate_connection) | [boolean](/lsr/value-types.md#boolean) | No |
| [`jdbc_validation_timeout`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-jdbc_validation_timeout) | [number](/lsr/value-types.md#number) | No |
| [`parameters`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-parameters) | [hash](/lsr/value-types.md#hash) | No |
| [`prepared_statement_bind_values`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_bind_values) | [array](/lsr/value-types.md#array) | No |
| [`prepared_statement_name`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_name) | [string](/lsr/value-types.md#string) | No |
| [`prepared_statement_warn_on_constant_usage`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_warn_on_constant_usage) | [boolean](/lsr/value-types.md#boolean) | No |
| [`sequel_opts`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-sequel_opts) | [hash](/lsr/value-types.md#hash) | No |
| [`statement`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-statement) | [string](/lsr/value-types.md#string) | Yes |
| [`tag_on_default_use`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-tag_on_default_use) | [array](/lsr/value-types.md#array) | No |
| [`tag_on_failure`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-tag_on_failure) | [array](/lsr/value-types.md#array) | No |
| [`target`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-target) | [string](/lsr/value-types.md#string) | Yes |
| [`use_cache`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-use_cache) | [boolean](/lsr/value-types.md#boolean) | No |
| [`use_prepared_statements`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-use_prepared_statements) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-common-options) for a list of options supported by all filter plugins.

### `cache_expiration` [v5.1.10-plugins-filters-jdbc_streaming-cache_expiration]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `5.0`

The minimum number of seconds any entry should remain in the cache. Defaults to 5 seconds.

A numeric value. You can use decimals for example: `cache_expiration => 0.25`. If there are transient jdbc errors, the cache will store empty results for a given parameter set and bypass the jbdc lookup. This will merge the default\_hash into the event until the cache entry expires. Then the jdbc lookup will be tried again for the same parameters. Conversely, while the cache contains valid results, any external problem that would cause jdbc errors will not be noticed for the cache\_expiration period.

### `cache_size` [v5.1.10-plugins-filters-jdbc_streaming-cache_size]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `500`

The maximum number of cache entries that will be stored. Defaults to 500 entries. The least recently used entry will be evicted.

### `default_hash` [v5.1.10-plugins-filters-jdbc_streaming-default_hash]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Define a default object to use when lookup fails to return a matching row. Ensure that the key names of this object match the columns from the statement.

### `jdbc_connection_string` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_connection_string]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC connection string

### `jdbc_driver_class` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_driver_class]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC driver class to load, for example "oracle.jdbc.OracleDriver" or "org.apache.derby.jdbc.ClientDriver"

### `jdbc_driver_library` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_driver_library]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

JDBC driver library path to third party driver library.

### `jdbc_password` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

JDBC password

### `jdbc_user` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC user

### `jdbc_validate_connection` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_validate_connection]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Connection pool configuration. Validate connection before use.

### `jdbc_validation_timeout` [v5.1.10-plugins-filters-jdbc_streaming-jdbc_validation_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3600`

Connection pool configuration. How often to validate a connection (in seconds).

### `parameters` [v5.1.10-plugins-filters-jdbc_streaming-parameters]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Hash of query parameter, for example `{ "id" => "id_field" }`.

### `prepared_statement_bind_values` [v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_bind_values]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

Array of bind values for the prepared statement. Use field references and constants. See the section on [prepared\_statements](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-prepared_statements) for more info.

### `prepared_statement_name` [v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_name]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `""`

Name given to the prepared statement. It must be unique in your config and in the database. You need to supply this if `use_prepared_statements` is true.

### `prepared_statement_warn_on_constant_usage` [v5.1.10-plugins-filters-jdbc_streaming-prepared_statement_warn_on_constant_usage]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

A flag that controls whether a warning is logged if, in `prepared_statement_bind_values`, a String constant is detected that might be intended as a field reference.

### `sequel_opts` [v5.1.10-plugins-filters-jdbc_streaming-sequel_opts]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

General/Vendor-specific Sequel configuration options

An example of an optional connection pool configuration max\_connections - The maximum number of connections the connection pool

examples of vendor-specific options can be found in this documentation page: <https://github.com/jeremyevans/sequel/blob/master/doc/opening_databases.rdoc>

### `statement` [v5.1.10-plugins-filters-jdbc_streaming-statement]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Statement to execute. To use parameters, use named parameter syntax, for example "SELECT \* FROM MYTABLE WHERE ID = :id".

### `tag_on_default_use` [v5.1.10-plugins-filters-jdbc_streaming-tag_on_default_use]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_jdbcstreamingdefaultsused"]`

Append values to the `tags` field if no record was found and default values were used.

### `tag_on_failure` [v5.1.10-plugins-filters-jdbc_streaming-tag_on_failure]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_jdbcstreamingfailure"]`

Append values to the `tags` field if sql error occurred.

### `target` [v5.1.10-plugins-filters-jdbc_streaming-target]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define the target field to store the extracted result(s). Field is overwritten if exists.

### `use_cache` [v5.1.10-plugins-filters-jdbc_streaming-use_cache]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Enable or disable caching, boolean true or false. Defaults to true.

### `use_prepared_statements` [v5.1.10-plugins-filters-jdbc_streaming-use_prepared_statements]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

When set to `true`, enables prepare statement usage

## Common options [v5.1.10-plugins-filters-jdbc_streaming-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v5-1-10-plugins-filters-jdbc_streaming.md#v5.1.10-plugins-filters-jdbc_streaming-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v5.1.10-plugins-filters-jdbc_streaming-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      jdbc_streaming {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v5.1.10-plugins-filters-jdbc_streaming-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      jdbc_streaming {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      jdbc_streaming {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v5.1.10-plugins-filters-jdbc_streaming-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.1.10-plugins-filters-jdbc_streaming-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jdbc\_streaming filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      jdbc_streaming {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v5.1.10-plugins-filters-jdbc_streaming-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v5.1.10-plugins-filters-jdbc_streaming-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      jdbc_streaming {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      jdbc_streaming {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v5.1.10-plugins-filters-jdbc_streaming-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      jdbc_streaming {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      jdbc_streaming {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
