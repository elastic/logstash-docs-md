---
navigation_title: "v3.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.6-plugins-inputs-salesforce.html
---

# Salesforce input plugin v3.0.6 [v3.0.6-plugins-inputs-salesforce]


* Plugin version: v3.0.6
* Released on: 2020-06-30
* [Changelog](https://github.com/logstash-plugins/logstash-input-salesforce/blob/v3.0.6/CHANGELOG.md)

For other versions, see the [overview list](input-salesforce-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_819]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-salesforce). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_812]

This Logstash input plugin allows you to query Salesforce using SOQL and puts the results into Logstash, one row per event. You can configure it to pull entire sObjects or only specific fields.

::::{note}
This input plugin will stop after all the results of the query are processed and will need to be re-run to fetch new results. It does not utilize the streaming API.
::::


In order to use this plugin, you will need to create a new SFDC Application using oauth. More details can be found here: [https://help.salesforce.com/apex/HTViewHelpDoc?id=connected_app_create.htm](https://help.salesforce.com/apex/HTViewHelpDoc?id=connected_app_create.htm)

You will also need a username, password, and security token for your salesforce instance. More details for generating a token can be found here: [https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm](https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm)

In addition to specifying an sObject, you can also supply a list of API fields that will be used in the SOQL query.


## Example [_example_29]

This example prints all the Salesforce Opportunities to standard out

```ruby
input {
  salesforce {
    client_id => 'OAUTH CLIENT ID FROM YOUR SFDC APP'
    client_secret => 'OAUTH CLIENT SECRET FROM YOUR SFDC APP'
    username => 'email@example.com'
    password => 'super-secret'
    security_token => 'SECURITY TOKEN FOR THIS USER'
    sfdc_object_name => 'Opportunity'
  }
}

output {
  stdout {
    codec => rubydebug
  }
}
```


## Salesforce Input Configuration Options [v3.0.6-plugins-inputs-salesforce-options]

This plugin supports the following configuration options plus the [Common options](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_version`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-api_version) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`client_id`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-client_id) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`client_secret`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-client_secret) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`password`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-password) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`security_token`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-security_token) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`sfdc_fields`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-sfdc_fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`sfdc_filters`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-sfdc_filters) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`sfdc_object_name`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-sfdc_object_name) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`to_underscores`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-to_underscores) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`use_test_sandbox`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-use_test_sandbox) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`username`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-username) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |

Also see [Common options](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-common-options) for a list of options supported by all input plugins.

 

### `api_version` [v3.0.6-plugins-inputs-salesforce-api_version]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

By default, this uses the default Restforce API version. To override this, set this to something like "32.0" for example


### `client_id` [v3.0.6-plugins-inputs-salesforce-client_id]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Consumer Key for authentication. You must set up a new SFDC connected app with oath to use this output. More information can be found here: [https://help.salesforce.com/apex/HTViewHelpDoc?id=connected_app_create.htm](https://help.salesforce.com/apex/HTViewHelpDoc?id=connected_app_create.htm)


### `client_secret` [v3.0.6-plugins-inputs-salesforce-client_secret]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Consumer Secret from your oauth enabled connected app


### `password` [v3.0.6-plugins-inputs-salesforce-password]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The password used to login to sfdc


### `security_token` [v3.0.6-plugins-inputs-salesforce-security_token]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The security token for this account. For more information about generting a security token, see: [https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm](https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm)


### `sfdc_fields` [v3.0.6-plugins-inputs-salesforce-sfdc_fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

These are the field names to return in the Salesforce query If this is empty, all fields are returned.


### `sfdc_filters` [v3.0.6-plugins-inputs-salesforce-sfdc_filters]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

These options will be added to the WHERE clause in the SOQL statement. Additional fields can be filtered on by adding field1 = value1 AND field2 = value2 AND…​


### `sfdc_object_name` [v3.0.6-plugins-inputs-salesforce-sfdc_object_name]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The name of the salesforce object you are creating or updating


### `to_underscores` [v3.0.6-plugins-inputs-salesforce-to_underscores]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Setting this to true will convert SFDC’s NamedFields*c to named_fields*c


### `use_test_sandbox` [v3.0.6-plugins-inputs-salesforce-use_test_sandbox]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Set this to true to connect to a sandbox sfdc instance logging in through test.salesforce.com


### `username` [v3.0.6-plugins-inputs-salesforce-username]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

A valid salesforce user name, usually your email address. Used for authentication and will be the user all objects are created or modified by



## Common options [v3.0.6-plugins-inputs-salesforce-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v3-0-6-plugins-inputs-salesforce.md#v3.0.6-plugins-inputs-salesforce-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v3.0.6-plugins-inputs-salesforce-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v3.0.6-plugins-inputs-salesforce-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.6-plugins-inputs-salesforce-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.6-plugins-inputs-salesforce-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 salesforce inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  salesforce {
    id => "my_plugin_id"
  }
}
```


### `tags` [v3.0.6-plugins-inputs-salesforce-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v3.0.6-plugins-inputs-salesforce-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.



