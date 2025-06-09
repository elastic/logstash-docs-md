---
navigation_title: "v1.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.4-plugins-filters-jdbc_static.html
---

# Jdbc_static filter plugin v1.0.4 [v1.0.4-plugins-filters-jdbc_static]

* Plugin version: v1.0.4
* Released on: 2018-06-26
* [Changelog](https://github.com/logstash-plugins/logstash-filter-jdbc_static/blob/v1.0.4/CHANGELOG.md)

For other versions, see the [overview list](filter-jdbc_static-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2016]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-jdbc_static). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_1994]

This filter enriches events with data pre-loaded from a remote database.

This filter is best suited for enriching events with reference data that is static or does not change very often, such as environments, users, and products.

This filter works by fetching data from a remote database, caching it in a local, in-memory [Apache Derby](https://db.apache.org/derby/manuals/#docs_10.14) database, and using lookups to enrich events with data cached in the local database. You can set up the filter to load the remote data once (for static data), or you can schedule remote loading to run periodically (for data that needs to be refreshed).

To define the filter, you specify three main sections: local\_db\_objects, loaders, and lookups.

* **local\_db\_objects**

  Define the columns, types, and indexes used to build the local database structure. The column names and types should match the external database. Define as many of these objects as needed to build the local database structure.

* **loaders**

  Query the external database to fetch the dataset that will be cached locally. Define as many loaders as needed to fetch the remote data. Each loader should fill a table defined by `local_db_objects`. Make sure the column names and datatypes in the loader SQL statement match the columns defined under `local_db_objects`. Each loader has an independent remote database connection.

* **lookups**

  Perform lookup queries on the local database to enrich the events. Define as many lookups as needed to enhance the event from all lookup tables in one pass. Ideally the SQL statement should only return one row. Any rows are converted to Hash objects and are stored in a target field that is an Array.

The following example config fetches data from a remote database, caches it in a local database, and uses lookups to enrich events with data cached in the local database.

\+

```
filter {
  jdbc_static {
    loaders => [ <1>
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
    local_db_objects => [ <2>
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
    local_lookups => [ <3>
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
        target => "user" <4>
      }
    ]
    # using add_field here to add & rename values to the event root
    add_field => { server_name => "%{[server][0][description]}" }
    add_field => { user_firstname => "%{[user][0][firstname]}" } <5>
    add_field => { user_lastname => "%{[user][0][lastname]}" } <6>
    remove_field => ["server", "user"]
    staging_directory => "/tmp/logstash/jdbc_static/import_data"
    loader_schedule => "* */2 * * *"
    jdbc_user => "logstash"
    jdbc_password => "example"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_driver_library => "/tmp/logstash/vendor/postgresql-42.1.4.jar"
    jdbc_connection_string => "jdbc:postgresql://remotedb:5432/ls_test_2"
  }
}
```

1. Queries an external database to fetch the dataset that will be cached locally.

2. Defines the columns, types, and indexes used to build the local database structure. The column names and types should match the external database.

3. Performs lookup queries on the local database to enrich the events.

4. Specifies the event field that will store the looked-up data. If the lookup returns multiple columns, the data is stored as a JSON object within the field.

5. Takes data from the JSON object and stores it in top-level event fields for easier analysis in Kibana.

6. Takes data from the JSON object and stores it in top-level event fields for easier analysis in Kibana.

Here’s a full example:

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
    staging_directory => "/tmp/logstash/jdbc_static/import_data"
    loader_schedule => "*/30 * * * *"
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

Assuming the loader fetches the following data from a Postgres database:

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

The events are enriched with a description of the server based on the value of the IP:

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

## Using this plugin with multiple pipelines [_using_this_plugin_with_multiple_pipelines_47]

Logstash uses a single, in-memory Apache Derby instance as the lookup database engine for the entire JVM. Because each plugin instance uses a unique database inside the shared Derby engine, there should be no conflicts with plugins attempting to create and populate the same tables. This is true regardless of whether the plugins are defined in a single pipeline, or multiple pipelines. However, after setting up the filter, you should watch the lookup results and view the logs to verify correct operation.

## Jdbc_static Filter Configuration Options [v1.0.4-plugins-filters-jdbc_static-options]

This plugin supports the following configuration options plus the [Common options](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`jdbc_connection_string`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-jdbc_connection_string) | [string](/lsr/value-types.md#string) | Yes |
| [`jdbc_driver_class`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-jdbc_driver_class) | [string](/lsr/value-types.md#string) | Yes |
| [`jdbc_driver_library`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-jdbc_driver_library) | a valid filesystem path | No |
| [`jdbc_password`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-jdbc_password) | [password](/lsr/value-types.md#password) | No |
| [`jdbc_user`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-jdbc_user) | [string](/lsr/value-types.md#string) | No |
| [`tag_on_failure`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-tag_on_failure) | [array](/lsr/value-types.md#array) | No |
| [`tag_on_default_use`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-tag_on_default_use) | [array](/lsr/value-types.md#array) | No |
| [`staging_directory`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-staging_directory) | [string](/lsr/value-types.md#string) | No |
| [`loader_schedule`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-loader_schedule) | [string](/lsr/value-types.md#string) | No |
| [`loaders`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-loaders) | [array](/lsr/value-types.md#array) | No |
| [`local_db_objects`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-local_db_objects) | [array](/lsr/value-types.md#array) | No |
| [`local_lookups`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-local_lookups) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-common-options) for a list of options supported by all filter plugins.

### `jdbc_connection_string` [v1.0.4-plugins-filters-jdbc_static-jdbc_connection_string]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC connection string.

### `jdbc_driver_class` [v1.0.4-plugins-filters-jdbc_static-jdbc_driver_class]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC driver class to load, for example, "org.apache.derby.jdbc.ClientDriver".

According to [Issue 43](https://github.com/logstash-plugins/logstash-input-jdbc/issues/43), if you are using the Oracle JDBC driver (ojdbc6.jar), the correct `jdbc_driver_class` is `"Java::oracle.jdbc.driver.OracleDriver"`.

### `jdbc_driver_library` [v1.0.4-plugins-filters-jdbc_static-jdbc_driver_library]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC driver library path to third-party driver library. Use comma separated paths in one string if you need multiple libraries.

If the driver class is not provided, the plugin looks for it in the Logstash Java classpath.

### `jdbc_password` [v1.0.4-plugins-filters-jdbc_static-jdbc_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

JDBC password.

### `jdbc_user` [v1.0.4-plugins-filters-jdbc_static-jdbc_user]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

JDBC user.

### `tag_on_default_use` [v1.0.4-plugins-filters-jdbc_static-tag_on_default_use]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_jdbcstaticdefaultsused"]`

Append values to the `tags` field if no record was found and default values were used.

### `tag_on_failure` [v1.0.4-plugins-filters-jdbc_static-tag_on_failure]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `["_jdbcstaticfailure"]`

Append values to the `tags` field if a SQL error occurred.

### `staging_directory` [v1.0.4-plugins-filters-jdbc_static-staging_directory]

* Value type is [string](/lsr/value-types.md#string)
* Default value is derived from the Ruby temp directory + plugin\_name + "import\_data"
* e.g. `"/tmp/logstash/jdbc_static/import_data"`

The directory used stage the data for bulk loading, there should be sufficient disk space to handle the data you wish to use to enrich events. Previous versions of this plugin did not handle loading datasets of more than several thousand rows well due to an open bug in Apache Derby. This setting introduces an alternative way of loading large recordsets. As each row is received it is spooled to file and then that file is imported using a system *import table* system call.

Append values to the `tags` field if a SQL error occurred.

### `loader_schedule` [v1.0.4-plugins-filters-jdbc_static-loader_schedule]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

You can schedule remote loading to run periodically according to a specific schedule. This scheduling syntax is powered by [rufus-scheduler](https://github.com/jmettraux/rufus-scheduler). The syntax is cron-like with some extensions specific to Rufus (for example, timezone support). For more about this syntax, see [parsing cronlines and time strings](https://github.com/jmettraux/rufus-scheduler#parsing-cronlines-and-time-strings).

Examples:

| | |
| :- | :- |
| `*/30 * * * *` | will execute on the 0th and 30th minute of every hour every day. |
| `* 5 * 1-3 *` | will execute every minute of 5am every day of January through March. |
| `0 * * * *` | will execute on the 0th minute of every hour every day. |
| `0 6 * * * America/Chicago` | will execute at 6:00am (UTC/GMT -5) every day. |

Debugging using the Logstash interactive shell:

```
bin/logstash -i irb
irb(main):001:0> require 'rufus-scheduler'
=> true
irb(main):002:0> Rufus::Scheduler.parse('*/10 * * * *')
=> #<Rufus::Scheduler::CronLine:0x230f8709 @timezone=nil, @weekdays=nil, @days=nil, @seconds=[0], @minutes=[0, 10, 20, 30, 40, 50], @hours=nil, @months=nil, @monthdays=nil, @original="*/10 * * * *">
irb(main):003:0> exit
```

The object returned by the above call, an instance of `Rufus::Scheduler::CronLine` shows the seconds, minutes etc. of execution.

### `loaders` [v1.0.4-plugins-filters-jdbc_static-loaders]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| :- | :- | :- |
| id | string | No |
| table | string | Yes |
| query | string | Yes |
| max\_rows | number | No |
| jdbc\_connection\_string | string | No |
| jdbc\_driver\_class | string | No |
| jdbc\_driver\_library | a valid filesystem path | No |
| jdbc\_password | password | No |
| jdbc\_user | string | No |

**Loader Field Descriptions:**

* id

  An optional identifier. This is used to identify the loader that is generating error messages and log lines.

* table

  The destination table in the local lookup database that the loader will fill.

* query

  The SQL statement that is executed to fetch the remote records. Use SQL aliases and casts to ensure that the record’s columns and datatype match the table structure in the local database as defined in the `local_db_objects`.

* max\_rows

  The default for this setting is 1 million. Because the lookup database is in-memory, it will take up JVM heap space. If the query returns many millions of rows, you should increase the JVM memory given to Logstash or limit the number of rows returned, perhaps to those most frequently found in the event data.

* jdbc\_connection\_string

  If not set in a loader, this setting defaults to the plugin-level `jdbc_connection_string` setting.

* jdbc\_driver\_class

  If not set in a loader, this setting defaults to the plugin-level `jdbc_driver_class` setting.

* jdbc\_driver\_library

  If not set in a loader, this setting defaults to the plugin-level `jdbc_driver_library` setting.

* jdbc\_password

  If not set in a loader, this setting defaults to the plugin-level `jdbc_password` setting.

* jdbc\_user

  If not set in a loader, this setting defaults to the plugin-level `jdbc_user` setting.

### `local_db_objects` [v1.0.4-plugins-filters-jdbc_static-local_db_objects]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash represents a table schema for the local lookups database. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| :- | :- | :- |
| name | string | Yes |
| columns | array | Yes |
| index\_columns | number | No |
| preserve\_existing | boolean | No |

**Local\_db\_objects Field Descriptions:**

* name

  The name of the table to be created in the database.

* columns

  An array of column specifications. Each column specification is an array of exactly two elements, for example `["ip", "varchar(15)"]`. The first element is the column name string. The second element is a string that is an [Apache Derby SQL type](https://db.apache.org/derby/docs/10.14/ref/crefsqlj31068.html). The string content is checked when the local lookup tables are built, not when the settings are validated. Therefore, any misspelled SQL type strings result in errors.

* index\_columns

  An array of strings. Each string must be defined in the `columns` setting. The index name will be generated internally. Unique or sorted indexes are not supported.

* preserve\_existing

  This setting, when `true`, checks whether the table already exists in the local lookup database. If you have multiple pipelines running in the same instance of Logstash, and more than one pipeline is using this plugin, then you must read the important multiple pipeline notice at the top of the page.

### `local_lookups` [v1.0.4-plugins-filters-jdbc_static-local_lookups]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

The array should contain one or more Hashes. Each Hash represents a lookup enhancement. Each Hash is validated according to the table below.

| Setting | Input type | Required |
| :- | :- | :- |
| id | string | No |
| query | string | Yes |
| parameters | hash | Yes |
| target | string | No |
| default\_hash | hash | No |
| tag\_on\_failure | string | No |
| tag\_on\_default\_use | string | No |

**Local\_lookups Field Descriptions:**

* id

  An optional identifier. This is used to identify the lookup that is generating error messages and log lines. If you omit this setting then a default id is used instead.

* query

  A SQL SELECT statement that is executed to achieve the lookup. To use parameters, use named parameter syntax, for example `"SELECT * FROM MYTABLE WHERE ID = :id"`.

* parameters

  A key/value Hash or dictionary. The key (LHS) is the text that is substituted for in the SQL statement `SELECT * FROM sensors WHERE reference = :p1`. The value (RHS) is the field name in your event. The plugin reads the value from this key out of the event and substitutes that value into the statement, for example, `parameters => { "p1" => "ref" }`. Quoting is automatic - you do not need to put quotes in the statement. Only use the field interpolation syntax on the RHS if you need to add a prefix/suffix or join two event field values together to build the substitution value. For example, imagine an IOT message that has an id and a location, and you have a table of sensors that have a column of `id-loc_id`. In this case your parameter hash would look like this: `parameters => { "p1" => "%{[id]}-%{[loc_id]}" }`.

* target

  An optional name for the field that will receive the looked-up data. If you omit this setting then the `id` setting (or the default id) is used. The looked-up data, an array of results converted to Hashes, is never added to the root of the event. If you want to do this, you should use the `add_field` setting. This means that you are in full control of how the fields/values are put in the root of the event, for example, `add_field => { user_firstname => "%{[user][0][firstname]}" }` - where `[user]` is the target field, `[0]` is the first result in the array, and `[firstname]` is the key in the result hash.

* default\_hash

  An optional hash that will be put in the target field array when the lookup returns no results. Use this setting if you need to ensure that later references in other parts of the config actually refer to something.

* tag\_on\_failure

  An optional string that overrides the plugin-level setting. This is useful when defining multiple lookups.

* tag\_on\_default\_use

  An optional string that overrides the plugin-level setting. This is useful when defining multiple lookups.

## Common options [v1.0.4-plugins-filters-jdbc_static-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-0-4-plugins-filters-jdbc_static.md#v1.0.4-plugins-filters-jdbc_static-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.0.4-plugins-filters-jdbc_static-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      jdbc_static {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
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

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.0.4-plugins-filters-jdbc_static-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      jdbc_static {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      jdbc_static {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.0.4-plugins-filters-jdbc_static-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.4-plugins-filters-jdbc_static-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 jdbc\_static filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      jdbc_static {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.0.4-plugins-filters-jdbc_static-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.0.4-plugins-filters-jdbc_static-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      jdbc_static {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      jdbc_static {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.0.4-plugins-filters-jdbc_static-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      jdbc_static {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      jdbc_static {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
