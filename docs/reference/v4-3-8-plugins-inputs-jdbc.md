---
navigation_title: "v4.3.8"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.3.8-plugins-inputs-jdbc.html
---

# Jdbc input plugin v4.3.8 [v4.3.8-plugins-inputs-jdbc]


* Plugin version: v4.3.8
* Released on: 2018-04-05
* [Changelog](https://github.com/logstash-plugins/logstash-input-jdbc/blob/v4.3.8/CHANGELOG.md)

For other versions, see the [overview list](input-jdbc-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_590]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-jdbc). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_584]

This plugin was created as a way to ingest data in any database with a JDBC interface into Logstash. You can periodically schedule ingestion using a cron syntax (see `schedule` setting) or run the query one time to load data into Logstash. Each row in the resultset becomes a single event. Columns in the resultset are converted into fields in the event.


## Drivers [_drivers_50]

This plugin does not come packaged with JDBC driver libraries. The desired jdbc driver library must be explicitly passed in to the plugin using the `jdbc_driver_library` configuration option.


## Scheduling [_scheduling_93]

Input from this plugin can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ).

Examples:

|     |     |
| --- | --- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).


## State [_state_50]

The plugin will persist the `sql_last_value` parameter in the form of a metadata file stored in the configured `last_run_metadata_path`. Upon query execution, this file will be updated with the current value of `sql_last_value`. Next time the pipeline starts up, this value will be updated by reading from the file. If `clean_run` is set to true, this value will be ignored and `sql_last_value` will be set to Jan 1, 1970, or 0 if `use_column_value` is true, as if no query has ever been executed.


## Dealing With Large Result-sets [_dealing_with_large_result_sets_50]

Many JDBC drivers use the `fetch_size` parameter to limit how many results are pre-fetched at a time from the cursor into the client’s cache before retrieving more results from the result-set. This is configured in this plugin using the `jdbc_fetch_size` configuration option. No fetch size is set by default in this plugin, so the specific driver’s default size will be used.


## Usage: [_usage_50]

Here is an example of setting up the plugin to fetch data from a MySQL database. First, we place the appropriate JDBC driver library in our current path (this can be placed anywhere on your filesystem). In this example, we connect to the *mydb* database using the user: *mysql* and wish to input all rows in the *songs* table that match a specific artist. The following examples demonstrates a possible Logstash configuration for this. The `schedule` option in this example will instruct the plugin to execute this input statement on the minute, every minute.

```ruby
input {
  jdbc {
    jdbc_driver_library => "mysql-connector-java-5.1.36-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydb"
    jdbc_user => "mysql"
    parameters => { "favorite_artist" => "Beethoven" }
    schedule => "* * * * *"
    statement => "SELECT * from songs where artist = :favorite_artist"
  }
}
```


## Configuring SQL statement [_configuring_sql_statement_50]

A sql statement is required for this input. This can be passed-in via a statement option in the form of a string, or read from a file (`statement_filepath`). File option is typically used when the SQL statement is large or cumbersome to supply in the config. The file option only supports one SQL statement. The plugin will only accept one of the options. It cannot read a statement from a file as well as from the `statement` configuration parameter.


## Configuring multiple SQL statements [_configuring_multiple_sql_statements_50]

Configuring multiple SQL statements is useful when there is a need to query and ingest data from different database tables or views. It is possible to define separate Logstash configuration files for each statement or to define multiple statements in a single configuration file. When using multiple statements in a single Logstash configuration file, each statement has to be defined as a separate jdbc input (including jdbc driver, connection string and other required parameters).

Please note that if any of the statements use the `sql_last_value` parameter (e.g. for ingesting only data changed since last run), each input should define its own `last_run_metadata_path` parameter. Failure to do so will result in undesired behaviour, as all inputs will store their state to the same (default) metadata file, effectively overwriting each other’s `sql_last_value`.


## Predefined Parameters [_predefined_parameters_50]

Some parameters are built-in and can be used from within your queries. Here is the list:

|     |     |
| --- | --- |
| sql_last_value | The value used to calculate which rows to query. Before any query is run,this is set to Thursday, 1 January 1970, or 0 if `use_column_value` is true and`tracking_column` is set. It is updated accordingly after subsequent queries are run. |

Example:

```ruby
input {
  jdbc {
    statement => "SELECT id, mycolumn1, mycolumn2 FROM my_table WHERE id > :sql_last_value"
    use_column_value => true
    tracking_column => "id"
    # ... other configuration bits
  }
}
```


## Jdbc Input Configuration Options [v4.3.8-plugins-inputs-jdbc-options]

This plugin supports the following configuration options plus the [Common options](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`clean_run`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-clean_run) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`columns_charset`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-columns_charset) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`connection_retry_attempts`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-connection_retry_attempts) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`connection_retry_attempts_wait_time`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-connection_retry_attempts_wait_time) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jdbc_connection_string`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_connection_string) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_default_timezone`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_default_timezone) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`jdbc_driver_class`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_driver_class) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_driver_library`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_driver_library) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`jdbc_fetch_size`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_fetch_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jdbc_page_size`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_page_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jdbc_paging_enabled`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_paging_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`jdbc_password`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`jdbc_password_filepath`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_password_filepath) | a valid filesystem path | No |
| [`jdbc_pool_timeout`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_pool_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`jdbc_user`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_user) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_validate_connection`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_validate_connection) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`jdbc_validation_timeout`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-jdbc_validation_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`last_run_metadata_path`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-last_run_metadata_path) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`lowercase_column_names`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-lowercase_column_names) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`parameters`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-parameters) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`record_last_run`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-record_last_run) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`schedule`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-schedule) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sequel_opts`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-sequel_opts) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`sql_log_level`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-sql_log_level) | [string](logstash://reference/configuration-file-structure.md#string), one of `["fatal", "error", "warn", "info", "debug"]` | No |
| [`statement`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-statement) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`statement_filepath`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-statement_filepath) | a valid filesystem path | No |
| [`tracking_column`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-tracking_column) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tracking_column_type`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-tracking_column_type) | [string](logstash://reference/configuration-file-structure.md#string), one of `["numeric", "timestamp"]` | No |
| [`use_column_value`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-use_column_value) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |

Also see [Common options](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-common-options) for a list of options supported by all input plugins.

 

### `clean_run` [v4.3.8-plugins-inputs-jdbc-clean_run]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Whether the previous run state should be preserved


### `columns_charset` [v4.3.8-plugins-inputs-jdbc-columns_charset]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

The character encoding for specific columns. This option will override the `:charset` option for the specified columns.

Example:

```ruby
input {
  jdbc {
    ...
    columns_charset => { "column0" => "ISO-8859-1" }
    ...
  }
}
```

this will only convert column0 that has ISO-8859-1 as an original encoding.


### `connection_retry_attempts` [v4.3.8-plugins-inputs-jdbc-connection_retry_attempts]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

Maximum number of times to try connecting to database


### `connection_retry_attempts_wait_time` [v4.3.8-plugins-inputs-jdbc-connection_retry_attempts_wait_time]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0.5`

Number of seconds to sleep between connection attempts


### `jdbc_connection_string` [v4.3.8-plugins-inputs-jdbc-jdbc_connection_string]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC connection string


### `jdbc_default_timezone` [v4.3.8-plugins-inputs-jdbc-jdbc_default_timezone]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Timezone conversion. SQL does not allow for timezone data in timestamp fields.  This plugin will automatically convert your SQL timestamp fields to Logstash timestamps, in relative UTC time in ISO8601 format.

Using this setting will manually assign a specified timezone offset, instead of using the timezone setting of the local machine.  You must use a canonical timezone, **America/Denver**, for example.


### `jdbc_driver_class` [v4.3.8-plugins-inputs-jdbc-jdbc_driver_class]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC driver class to load, for exmaple, "org.apache.derby.jdbc.ClientDriver" NB per [https://github.com/logstash-plugins/logstash-input-jdbc/issues/43](https://github.com/logstash-plugins/logstash-input-jdbc/issues/43) if you are using the Oracle JDBC driver (ojdbc6.jar) the correct `jdbc_driver_class` is `"Java::oracle.jdbc.driver.OracleDriver"`


### `jdbc_driver_library` [v4.3.8-plugins-inputs-jdbc-jdbc_driver_library]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Tentative of abstracting JDBC logic to a mixin for potential reuse in other plugins (input/output) This method is called when someone includes this module Add these methods to the *base* given. JDBC driver library path to third party driver library. In case of multiple libraries being required you can pass them separated by a comma.

If not provided, Plugin will look for the driver class in the Logstash Java classpath.


### `jdbc_fetch_size` [v4.3.8-plugins-inputs-jdbc-jdbc_fetch_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* There is no default value for this setting.

JDBC fetch size. if not provided, respective driver’s default will be used


### `jdbc_page_size` [v4.3.8-plugins-inputs-jdbc-jdbc_page_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `100000`

JDBC page size


### `jdbc_paging_enabled` [v4.3.8-plugins-inputs-jdbc-jdbc_paging_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

JDBC enable paging

This will cause a sql statement to be broken up into multiple queries. Each query will use limits and offsets to collectively retrieve the full result-set. The limit size is set with `jdbc_page_size`.

Be aware that ordering is not guaranteed between queries.


### `jdbc_password` [v4.3.8-plugins-inputs-jdbc-jdbc_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

JDBC password


### `jdbc_password_filepath` [v4.3.8-plugins-inputs-jdbc-jdbc_password_filepath]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

JDBC password filename


### `jdbc_pool_timeout` [v4.3.8-plugins-inputs-jdbc-jdbc_pool_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `5`

Connection pool configuration. The amount of seconds to wait to acquire a connection before raising a PoolTimeoutError (default 5)


### `jdbc_user` [v4.3.8-plugins-inputs-jdbc-jdbc_user]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC user


### `jdbc_validate_connection` [v4.3.8-plugins-inputs-jdbc-jdbc_validate_connection]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Connection pool configuration. Validate connection before use.


### `jdbc_validation_timeout` [v4.3.8-plugins-inputs-jdbc-jdbc_validation_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `3600`

Connection pool configuration. How often to validate a connection (in seconds)


### `last_run_metadata_path` [v4.3.8-plugins-inputs-jdbc-last_run_metadata_path]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"/home/ph/.logstash_jdbc_last_run"`

Path to file with last run time


### `lowercase_column_names` [v4.3.8-plugins-inputs-jdbc-lowercase_column_names]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Whether to force the lowercasing of identifier fields


### `parameters` [v4.3.8-plugins-inputs-jdbc-parameters]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Hash of query parameter, for example `{ "target_id" => "321" }`


### `record_last_run` [v4.3.8-plugins-inputs-jdbc-record_last_run]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Whether to save state or not in [`last_run_metadata_path`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-last_run_metadata_path)


### `schedule` [v4.3.8-plugins-inputs-jdbc-schedule]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Schedule of when to periodically run statement, in Cron format for example: "* * * * *" (execute query every minute, on the minute)

There is no schedule by default. If no schedule is given, then the statement is run exactly once.


### `sequel_opts` [v4.3.8-plugins-inputs-jdbc-sequel_opts]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

General/Vendor-specific Sequel configuration options.

An example of an optional connection pool configuration max_connections - The maximum number of connections the connection pool

examples of vendor-specific options can be found in this documentation page: [https://github.com/jeremyevans/sequel/blob/master/doc/opening_databases.rdoc](https://github.com/jeremyevans/sequel/blob/master/doc/opening_databases.rdoc)


### `sql_log_level` [v4.3.8-plugins-inputs-jdbc-sql_log_level]

* Value can be any of: `fatal`, `error`, `warn`, `info`, `debug`
* Default value is `"info"`

Log level at which to log SQL queries, the accepted values are the common ones fatal, error, warn, info and debug. The default value is info.


### `statement` [v4.3.8-plugins-inputs-jdbc-statement]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

If undefined, Logstash will complain, even if codec is unused. Statement to execute

To use parameters, use named parameter syntax. For example:

```ruby
"SELECT * FROM MYTABLE WHERE id = :target_id"
```

here, ":target_id" is a named parameter. You can configure named parameters with the `parameters` setting.


### `statement_filepath` [v4.3.8-plugins-inputs-jdbc-statement_filepath]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Path of file containing statement to execute


### `tracking_column` [v4.3.8-plugins-inputs-jdbc-tracking_column]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The column whose value is to be tracked if `use_column_value` is set to `true`


### `tracking_column_type` [v4.3.8-plugins-inputs-jdbc-tracking_column_type]

* Value can be any of: `numeric`, `timestamp`
* Default value is `"numeric"`

Type of tracking column. Currently only "numeric" and "timestamp"


### `use_column_value` [v4.3.8-plugins-inputs-jdbc-use_column_value]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

When set to `true`, uses the defined [`tracking_column`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-tracking_column) value as the `:sql_last_value`. When set to `false`, `:sql_last_value` reflects the last time the query was executed.



## Common options [v4.3.8-plugins-inputs-jdbc-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v4-3-8-plugins-inputs-jdbc.md#v4.3.8-plugins-inputs-jdbc-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v4.3.8-plugins-inputs-jdbc-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v4.3.8-plugins-inputs-jdbc-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.3.8-plugins-inputs-jdbc-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.3.8-plugins-inputs-jdbc-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jdbc inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  jdbc {
    id => "my_plugin_id"
  }
}
```


### `tags` [v4.3.8-plugins-inputs-jdbc-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v4.3.8-plugins-inputs-jdbc-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



