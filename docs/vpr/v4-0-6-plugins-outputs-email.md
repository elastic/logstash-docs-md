---
navigation_title: "v4.0.6"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.6-plugins-outputs-email.html
---

# Email output plugin v4.0.6 [v4.0.6-plugins-outputs-email]


* Plugin version: v4.0.6
* Released on: 2017-08-16
* [Changelog](https://github.com/logstash-plugins/logstash-output-email/blob/v4.0.6/CHANGELOG.md)

For other versions, see the [overview list](output-email-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1217]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-email). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1210]

Sends email when an output is received. Alternatively, you may include or exclude the email output execution using conditionals.


## Usage Example [_usage_example_5]

```ruby
output {
  if "shouldmail" in [tags] {
    email {
      to => 'technical@example.com'
      from => 'monitor@example.com'
      subject => 'Alert - %{title}'
      body => "Tags: %{tags}\\n\\Content:\\n%{message}"
      domain => 'mail.example.com'
      port => 25
    }
  }
}
```


## Email Output Configuration Options [v4.0.6-plugins-outputs-email-options]

This plugin supports the following configuration options plus the [Common options](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`address`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-address) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`attachments`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-attachments) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`authentication`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-authentication) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`body`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-body) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`cc`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-cc) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`contenttype`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-contenttype) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`debug`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-debug) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`domain`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-domain) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`from`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-from) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`htmlbody`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-htmlbody) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-password) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`port`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-port) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`replyto`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-replyto) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`subject`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-subject) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`to`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-to) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`use_tls`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-use_tls) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`username`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-username) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`via`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-via) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-common-options) for a list of options supported by all output plugins.

 

### `address` [v4.0.6-plugins-outputs-email-address]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

The address used to connect to the mail server


### `attachments` [v4.0.6-plugins-outputs-email-attachments]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

Attachments - specify the name(s) and location(s) of the files.


### `authentication` [v4.0.6-plugins-outputs-email-authentication]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Authentication method used when identifying with the server


### `body` [v4.0.6-plugins-outputs-email-body]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Body for the email - plain text only.


### `cc` [v4.0.6-plugins-outputs-email-cc]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The fully-qualified email address(es) to include as cc: address(es).

This field also accepts a comma-separated string of addresses, for example: `"me@example.com, you@example.com"`


### `contenttype` [v4.0.6-plugins-outputs-email-contenttype]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"text/html; charset=UTF-8"`

contenttype : for multipart messages, set the content-type and/or charset of the HTML part. NOTE: this may not be functional (KH)


### `debug` [v4.0.6-plugins-outputs-email-debug]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Run the mail relay in debug mode


### `domain` [v4.0.6-plugins-outputs-email-domain]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"localhost"`

The HELO/EHLO domain name used in the greeting message when connecting to a remote SMTP server. Some servers require this name to match the actual hostname of the connecting client.


### `from` [v4.0.6-plugins-outputs-email-from]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"logstash.alert@example.com"`

The fully-qualified email address for the From: field in the email.


### `htmlbody` [v4.0.6-plugins-outputs-email-htmlbody]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

HTML Body for the email, which may contain HTML markup.


### `password` [v4.0.6-plugins-outputs-email-password]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Password to authenticate with the server


### `port` [v4.0.6-plugins-outputs-email-port]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `25`

Port used to communicate with the mail server


### `replyto` [v4.0.6-plugins-outputs-email-replyto]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The fully qualified email address for the Reply-To: field.


### `subject` [v4.0.6-plugins-outputs-email-subject]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `""`

Subject: for the email.


### `to` [v4.0.6-plugins-outputs-email-to]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The fully-qualified email address to send the email to.

This field also accepts a comma-separated string of addresses, for example: `"me@example.com, you@example.com"`

You can also use dynamic fields from the event with the `%{{fieldname}}` syntax.


### `use_tls` [v4.0.6-plugins-outputs-email-use_tls]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Enables TLS when communicating with the server


### `username` [v4.0.6-plugins-outputs-email-username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username to authenticate with the server


### `via` [v4.0.6-plugins-outputs-email-via]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"smtp"`

How Logstash should send the email, either via SMTP or by invoking sendmail.



## Common options [v4.0.6-plugins-outputs-email-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v4-0-6-plugins-outputs-email.md#v4.0.6-plugins-outputs-email-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v4.0.6-plugins-outputs-email-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v4.0.6-plugins-outputs-email-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v4.0.6-plugins-outputs-email-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 email outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  email {
    id => "my_plugin_id"
  }
}
```



