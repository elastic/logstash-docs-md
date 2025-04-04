---
navigation_title: "v1.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.0-plugins-filters-jdbc_static.html
---

# Jdbc_static filter plugin v1.0.0 [v1.0.0-plugins-filters-jdbc_static]


* Plugin version: v1.0.0
* Released on: 2018-01-11
* [Changelog](https://github.com/logstash-plugins/logstash-filter-jdbc_static/blob/v1.0.0/CHANGELOG.md)

For other versions, see the [overview list](filter-jdbc_static-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1992]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-jdbc_static). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1970]

This filter is best suited for event enhancement from static or reference data that does not change very often. Examples of these are environments, users and products. Locally there is a database that the enhancement lookups are done against. Remotely there is a database that has the static data. The local db is loaded with data from the remote db once or very periodically. To achieve this three main sections are defined: db_objects, loaders and lookups. The local database is an [Apache Derby](https://db.apache.org/derby/manuals/#docs_10.14) in-memory database.

Db_objects

Define as many of theses as needed to build the local database structure. Define tables, columns and indexes.

Loaders

Define as many loaders as needed to fetch the remote data. Each loader should fill a table created via a db_object. Make sure the column names/datatypes in the loader SQL statement match the columns defined in its corresponding db_object. Each loader has an independent remote database connection.

Lookups

Define as many lookups as needed to enhance the event from all lookup tables in one pass. Ideally the SQL statement should only return one row. Any rows are converted to Hash objects and are stored in a target field that is an Array.

Example config:

```ruby
filter {
  jdbc_static {
    loaders => [
      {
        id => "remote-servers"
        query => "select ip, descr from ref.local_ips order by ip"
        local_table => "servers"
      },
      {
        id => "remote-users"
        query => "select firstname, lastname, userid from ref.local_users order by userid"
        local_table => "users"
      }
    ]
    local_db_objects => [
      {
        name => "servers"
        index_columns => ["ip"]
        columns => [
          ["ip", "varchar(15)"],
          ["descr", "varchar(255)"]
        ]
      },
      {
        name => "users"
        index_columns => ["userid"]
        columns => [
          ["firstname", "varchar(255)"],
          ["lastname", "varchar(255)"],
          ["userid", "int"]
        ]
      }
    ]
    local_lookups => [
      {
        id => "local-servers"
        query => "select descr as description from servers WHERE ip = :ip"
        parameters => {ip => "[from_ip]"}
        target => "server"
      },
      {
        id => "local-users"
        query => "select firstname, lastname from users WHERE userid = :id"
        parameters => {id => "[loggedin_userid]"}
        target => "user"
      }
    ]
    # using add_field here to add & rename values to the event root
    add_field => { server_name => "%{[server][0][description]}" }
    add_field => { user_firstname => "%{[user][0][firstname]}" }
    add_field => { user_lastname => "%{[user][0][lastname]}" }
    remove_field => ["server", "user"]
    jdbc_user => "logstash"
    jdbc_password => "example"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_driver_library => "/tmp/logstash/vendor/postgresql-42.1.4.jar"
    jdbc_connection_string => "jdbc:postgresql://remotedb:5432/ls_test_2"
  }
}
```

Fully worked up example

```
input {
  generator {
    lines => [
      '{"from_ip": "10.2.3.20", "app": "foobar", "amount": 32.95}',
      '{"from_ip": "10.2.3.30", "app": "barfoo", "amount": 82.95}',
      '{"from_ip": "10.2.3.40", "app": "bazfoo", "amount": 22.95}'
    ]
    count => 200
  }
}

filter {
  json {
    source => "message"
  }

  jdbc_static {
    loaders => [
      {
        id => "servers"
        query => "select ip, descr from ref.local_ips order by ip"
        local_table => "servers"
      }
    ]
    local_db_objects => [
      {
        name => "servers"
        index_columns => ["ip"]
        columns => [
          ["ip", "varchar(15)"],
          ["descr", "varchar(255)"]
        ]
      }
    ]
    local_lookups => [
      {
        query => "select descr as description from servers WHERE ip = :ip"
        parameters => {ip => "[from_ip]"}
        target => "server"
      }
    ]
    jdbc_user => "logstash"
    jdbc_password => "logstash??"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_driver_library => "/Users/guy/tmp/logstash-6.0.0/vendor/postgresql-42.1.4.jar"
    jdbc_connection_string => "jdbc:postgresql://localhost:5432/ls_test_2"
  }
}

output {
  stdout {
    codec => rubydebug {metadata => true}
  }
}
```

with this data in a postgres db

```
select * from ref.local_ips order by ip;
    ip     |         descr
-----------+-----------------------
 10.2.3.10 | Authentication Server
 10.2.3.20 | Payments Server
 10.2.3.30 | Events Server
 10.2.3.40 | Payroll Server
 10.2.3.50 | Uploads Server
```

one event

```
{
           "app" => "bazfoo",
      "sequence" => 0,
        "server" => [
        [0] {
            "description" => "Payroll Server"
        }
    ],
        "amount" => 22.95,
    "@timestamp" => 2017-11-30T18:08:15.694Z,
      "@version" => "1",
          "host" => "Elastics-MacBook-Pro.local",
       "message" => "{\"from_ip\": \"10.2.3.40\", \"app\": \"bazfoo\", \"amount\": 22.95}",
       "from_ip" => "10.2.3.40"
}
```


## Using this plugin in multiple pipelines in a Logstash instance [_using_this_plugin_in_multiple_pipelines_in_a_logstash_instance]

::::{important}
As the lookup database engine, an in-memory Apache Derby instance, is a single instance for the whole JVM, each plugin instance whether per pipeline or as multiple plugins in one pipeline will use a unique database inside the shared Derby engine so there should be no conflicts with plugins creating tables and populating them even if the same settings are used. However you should watch the lookup results and the logs initially to verify correct operation.

::::



## Jdbc_static Filter Configuration Options [v1.0.0-plugins-filters-jdbc_static-options]

This plugin supports the following configuration options plus the [Common options](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`jdbc_connection_string`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-jdbc_connection_string) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_driver_class`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-jdbc_driver_class) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`jdbc_driver_library`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-jdbc_driver_library) | a valid filesystem path | No |
| [`jdbc_password`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-jdbc_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`jdbc_user`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-jdbc_user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tag_on_failure`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`tag_on_default_use`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-tag_on_default_use) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`loader_schedule`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-loader_schedule) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`loaders`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-loaders) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`local_db_objects`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-local_db_objects) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`local_lookups`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-local_lookups) | [array](logstash://reference/configuration-file-structure.md#array) | No |

Also see [Common options](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-common-options) for a list of options supported by all filter plugins.

 

### `jdbc_connection_string` [v1.0.0-plugins-filters-jdbc_static-jdbc_connection_string]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC connection string


### `jdbc_driver_class` [v1.0.0-plugins-filters-jdbc_static-jdbc_driver_class]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC driver class to load, for example, "org.apache.derby.jdbc.ClientDriver" NB per [https://github.com/logstash-plugins/logstash-input-jdbc/issues/43](https://github.com/logstash-plugins/logstash-input-jdbc/issues/43) if you are using the Oracle JDBC driver (ojdbc6.jar) the correct `jdbc_driver_class` is `"Java::oracle.jdbc.driver.OracleDriver"`


### `jdbc_driver_library` [v1.0.0-plugins-filters-jdbc_static-jdbc_driver_library]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC driver library path to third party driver library. In case of multiple libraries being required you can pass them separated by a comma.

If not provided, Plugin will look for the driver class in the Logstash Java classpath.


### `jdbc_password` [v1.0.0-plugins-filters-jdbc_static-jdbc_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

JDBC password


### `jdbc_user` [v1.0.0-plugins-filters-jdbc_static-jdbc_user]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

JDBC user


### `tag_on_default_use` [v1.0.0-plugins-filters-jdbc_static-tag_on_default_use]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_jdbcstaticdefaultsused"]`

Append values to the `tags` field if no record was found and default values were used


### `tag_on_failure` [v1.0.0-plugins-filters-jdbc_static-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_jdbcstaticfailure"]`

Append values to the `tags` field if sql error occured


### `loader_schedule` [v1.0.0-plugins-filters-jdbc_static-loader_schedule]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Remote loading can be scheduled to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (e.g. timezone support ). Further documentation describing this syntax can be found [here](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).

Examples:

|     |     |
| --- | --- |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |


### `loaders` [v1.0.0-plugins-filters-jdbc_static-loaders]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| --- | --- | --- |
| id | string | No |
| table | string | Yes |
| query | string | Yes |
| max_rows | number | No |
| jdbc_connection_string | string | No |
| jdbc_driver_class | string | No |
| jdbc_driver_library | a valid filesystem path | No |
| jdbc_password | password | No |
| jdbc_user | string | No |

Loader Field Descriptions
:   id
:   An optional identifier. This is used to identify the loader that is generating error messages and log lines.

table
:   This is the destination table in local lookup db that the loader will fill.

query
:   The SQL statement that is executed to fetch the remove records. Use SQL aliases and casts to ensure that the records columns and datatype match the table structure in the local db as defined in the `local_db_objects`

max_rows
:   The default for this setting is 1 million. As the lookup db is in-memory, it will take up JVM heap space. If the query would return many millions of rows you should increase the JVM memory given to Logstash OR limit the number of rows returned, perhaps to those most frequently found in the event data.

jdbc_connection_string
:   If not set in a loader, this setting defaults to the plugin level `jdbc_connection_string` setting.

jdbc_driver_class
:   If not set in a loader, this setting defaults to the plugin level `jdbc_driver_class` setting.

jdbc_driver_library
:   If not set in a loader, this setting defaults to the plugin level `jdbc_driver_library` setting.

jdbc_password
:   If not set in a loader, this setting defaults to the plugin level `jdbc_password` setting.

jdbc_user
:   If not set in a loader, this setting defaults to the plugin level `jdbc_user` setting.



### `local_db_objects` [v1.0.0-plugins-filters-jdbc_static-local_db_objects]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash represents a table schema for the local lookups database. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| --- | --- | --- |
| name | string | Yes |
| columns | array | Yes |
| index_columns | number | No |
| preserve_existing | boolean | No |

Local_db_objects Field Descriptions
:   name
:   The name of the table to be created in the database.

columns
:   An array of column specifications. Each column specification is an array of exactly two elements, for example `["ip", "varchar(15)"]`. The first element is the column name string. The second element is a string that should be an [Apache Derby SQL type](https://db.apache.org/derby/docs/10.14/ref/crefsqlj31068.html). The string content is not checked during settings validation but when the local lookup tables are built any misspelled SQL type strings will give errors.

index_columns
:   An array of strings. Each string must have been defined in the `columns` setting. The index name will be generated internally. Unique or sorted indexes are not supported.

preserve_existing
:   This setting, when `true`, will check whether the table exists in the local lookup database already. If you have multiple pipelines running in the same instance of Logstash and more than one pipeline is using this plugin then you must read the important multiple pipeline notice at the top of the page.



### `local_lookups` [v1.0.0-plugins-filters-jdbc_static-local_lookups]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash represents a lookup enhancement. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| --- | --- | --- |
| id | string | No |
| query | string | Yes |
| parameters | hash | Yes |
| target | string | No |
| default_hash | hash | No |
| tag_on_failure | string | No |
| tag_on_default_use | string | No |

Local_lookups Field Descriptions
:   id
:   An optional identifier. This is used to identify the lookup that is generating error messages and log lines. If you omit this setting then a default id is used instead.

query
:   A SQL SELECT statement that is executed to achieve the lookup. To use parameters, use named parameter syntax, for example "SELECT * FROM MYTABLE WHERE ID = :id"

parameters
:   A key/value Hash or dictionary. The key (LHS) is the text that is substituted for in the SQL statement `SELECT * FROM sensors WHERE reference = :p1`. The value (RHS) is the field name in your event. The plugin reads the value from this key out of the event and substitutes that value into the statement, e.g. `parameters => { "p1" => "ref" }`. Quoting is automatic - you do not need to put quotes in the statement. Only use the field interpolation syntax on the RHS if you need to add a prefix/suffix or join two event field values together to build the substitution value. For example, imagine an IOT message that has an id and a location and you have a table of sensors that have a column of `id-loc_id`, in this case your parameter hash would look like this: `parameters => { "p1" => "%{[id]}-%{[loc_id]}" }`

target
:   An optional name for the field that will receive the looked up data. If you omit this setting then the `id` setting (or the default id) is used. The looked up data, an array of results converted to Hashes, is never added to the root of the event. If you want to do this then you should use the `add_field` setting to achieve this. This means that you are in full control of how the fields/values are put in the root of the event, e.g. `add_field => { user_firstname => "%{[user][0][firstname]}" }` - where `[user]` is the target field `[0]` is the first result in the array and `[firstname]` is the key in the result hash.

default_hash
:   An optional hash that will be put in the target field array when the lookup returns no results. Use this if you need to ensure that later references in other parts of the config actually refer to something.

tag_on_failure
:   An optional string that overrides the plugin level setting. This is useful when defining multiple lookups.

tag_on_default_use
:   An optional string that overrides the plugin level setting. This is useful when defining multiple lookups.




## Common options [v1.0.0-plugins-filters-jdbc_static-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v1-0-0-plugins-filters-jdbc_static.md#v1.0.0-plugins-filters-jdbc_static-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v1.0.0-plugins-filters-jdbc_static-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      jdbc_static {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      jdbc_static {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v1.0.0-plugins-filters-jdbc_static-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      jdbc_static {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      jdbc_static {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v1.0.0-plugins-filters-jdbc_static-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v1.0.0-plugins-filters-jdbc_static-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jdbc_static filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      jdbc_static {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v1.0.0-plugins-filters-jdbc_static-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v1.0.0-plugins-filters-jdbc_static-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      jdbc_static {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      jdbc_static {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v1.0.0-plugins-filters-jdbc_static-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      jdbc_static {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      jdbc_static {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



