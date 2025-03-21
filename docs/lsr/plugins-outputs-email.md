---
navigation_title: "email"
---

# Email output plugin [plugins-outputs-email]


* Plugin version: v4.1.3
* Released on: 2023-10-03
* [Changelog](https://github.com/logstash-plugins/logstash-output-email/blob/v4.1.3/CHANGELOG.md)

For other versions, see the [Versioned plugin docs](https://www.elastic.co/guide/en/logstash-versioned-plugins/current/output-email-index.md).

## Getting help [_getting_help_75]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-email). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#logstash_plugins).


## Description [_description_74]

Sends email when an output is received. Alternatively, you may include or exclude the email output execution using conditionals.


## Usage Example [_usage_example]

```ruby
output {
  if "shouldmail" in [tags] {
    email {
      to => 'technical@example.com'
      from => 'monitor@example.com'
      subject => 'Alert - %{title}'
      body => "Tags: %{tags}\\n\\Content:\\n%{message}"
      template_file => "/tmp/email_template.mustache"
      domain => 'mail.example.com'
      port => 25
    }
  }
}
```


## Email Output Configuration Options [plugins-outputs-email-options]

This plugin supports the following configuration options plus the [Common options](plugins-outputs-email.md#plugins-outputs-email-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`address`](plugins-outputs-email.md#plugins-outputs-email-address) | [string](introduction.md#string) | No |
| [`attachments`](plugins-outputs-email.md#plugins-outputs-email-attachments) | [array](introduction.md#array) | No |
| [`authentication`](plugins-outputs-email.md#plugins-outputs-email-authentication) | [string](introduction.md#string) | No |
| [`body`](plugins-outputs-email.md#plugins-outputs-email-body) | [string](introduction.md#string) | No |
| [`cc`](plugins-outputs-email.md#plugins-outputs-email-cc) | [string](introduction.md#string) | No |
| [`bcc`](plugins-outputs-email.md#plugins-outputs-email-bcc) | [string](introduction.md#string) | No |
| [`contenttype`](plugins-outputs-email.md#plugins-outputs-email-contenttype) | [string](introduction.md#string) | No |
| [`debug`](plugins-outputs-email.md#plugins-outputs-email-debug) | [boolean](introduction.md#boolean) | No |
| [`domain`](plugins-outputs-email.md#plugins-outputs-email-domain) | [string](introduction.md#string) | No |
| [`from`](plugins-outputs-email.md#plugins-outputs-email-from) | [string](introduction.md#string) | No |
| [`htmlbody`](plugins-outputs-email.md#plugins-outputs-email-htmlbody) | [string](introduction.md#string) | No |
| [`password`](plugins-outputs-email.md#plugins-outputs-email-password) | [password](introduction.md#password) | No |
| [`port`](plugins-outputs-email.md#plugins-outputs-email-port) | [number](introduction.md#number) | No |
| [`replyto`](plugins-outputs-email.md#plugins-outputs-email-replyto) | [string](introduction.md#string) | No |
| [`subject`](plugins-outputs-email.md#plugins-outputs-email-subject) | [string](introduction.md#string) | No |
| [`to`](plugins-outputs-email.md#plugins-outputs-email-to) | [string](introduction.md#string) | Yes |
| [`use_tls`](plugins-outputs-email.md#plugins-outputs-email-use_tls) | [boolean](introduction.md#boolean) | No |
| [`username`](plugins-outputs-email.md#plugins-outputs-email-username) | [string](introduction.md#string) | No |
| [`via`](plugins-outputs-email.md#plugins-outputs-email-via) | [string](introduction.md#string) | No |
| [`template_file`](plugins-outputs-email.md#plugins-outputs-email-template_file) | [path](introduction.md#path) | No |

Also see [Common options](plugins-outputs-email.md#plugins-outputs-email-common-options) for a list of options supported by all output plugins.

 

### `address` [plugins-outputs-email-address]

* Value type is [string](introduction.md#string)
* Default value is `"localhost"`

The address used to connect to the mail server


### `attachments` [plugins-outputs-email-attachments]

* Value type is [array](introduction.md#array)
* Default value is `[]`

Attachments - specify the name(s) and location(s) of the files.


### `authentication` [plugins-outputs-email-authentication]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

Authentication method used when identifying with the server


### `body` [plugins-outputs-email-body]

* Value type is [string](introduction.md#string)
* Default value is `""`

Body for the email - plain text only.


### `cc` [plugins-outputs-email-cc]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The fully-qualified email address(es) to include as cc: address(es).

This field also accepts a comma-separated string of addresses, for example: `"me@example.com, you@example.com"`


### `bcc` [plugins-outputs-email-bcc]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The fully-qualified email address(es) to include as bcc: address(es).

This field accepts several addresses like cc.


### `contenttype` [plugins-outputs-email-contenttype]

* Value type is [string](introduction.md#string)
* Default value is `"text/html; charset=UTF-8"`

contenttype : for multipart messages, set the content-type and/or charset of the HTML part. NOTE: this may not be functional (KH)


### `debug` [plugins-outputs-email-debug]

* Value type is [boolean](introduction.md#boolean)
* Default value is `false`

Run the mail relay in debug mode


### `domain` [plugins-outputs-email-domain]

* Value type is [string](introduction.md#string)
* Default value is `"localhost"`

The HELO/EHLO domain name used in the greeting message when connecting to a remote SMTP server. Some servers require this name to match the actual hostname of the connecting client.


### `from` [plugins-outputs-email-from]

* Value type is [string](introduction.md#string)
* Default value is `"logstash.alert@example.com"`

The fully-qualified email address for the From: field in the email.


### `htmlbody` [plugins-outputs-email-htmlbody]

* Value type is [string](introduction.md#string)
* Default value is `""`

HTML Body for the email, which may contain HTML markup.


### `password` [plugins-outputs-email-password]

* Value type is [password](introduction.md#password)
* There is no default value for this setting.

Password to authenticate with the server


### `port` [plugins-outputs-email-port]

* Value type is [number](introduction.md#number)
* Default value is `25`

Port used to communicate with the mail server


### `replyto` [plugins-outputs-email-replyto]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The fully qualified email address for the Reply-To: field.


### `subject` [plugins-outputs-email-subject]

* Value type is [string](introduction.md#string)
* Default value is `""`

Subject: for the email.


### `to` [plugins-outputs-email-to]

* This is a required setting.
* Value type is [string](introduction.md#string)
* There is no default value for this setting.

The fully-qualified email address to send the email to.

This field also accepts a comma-separated string of addresses, for example: `"me@example.com, you@example.com"`

You can also use dynamic fields from the event with the `%{{fieldname}}` syntax.


### `use_tls` [plugins-outputs-email-use_tls]

* Value type is [boolean](introduction.md#boolean)
* Default value is `false`

Enables TLS when communicating with the server


### `username` [plugins-outputs-email-username]

* Value type is [string](introduction.md#string)
* There is no default value for this setting.

Username to authenticate with the server


### `via` [plugins-outputs-email-via]

* Value type is [string](introduction.md#string)
* Default value is `"smtp"`

How Logstash should send the email, either via SMTP or by invoking sendmail.


### `template_file` [plugins-outputs-email-template_file]

* Value type is [path](introduction.md#path)
* There is no default value for this setting.

Path of a [Mustache templating]([https://mustache.github.io/](https://mustache.github.io/)) file used for email templating. See example in test fixture. Can be used with `body` to send multi-part emails. Takes precedence over `htmlBody`.



## Common options [plugins-outputs-email-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](plugins-outputs-email.md#plugins-outputs-email-codec) | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](plugins-outputs-email.md#plugins-outputs-email-enable_metric) | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](plugins-outputs-email.md#plugins-outputs-email-id) | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

### `codec` [plugins-outputs-email-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [plugins-outputs-email-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [plugins-outputs-email-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 email outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  email {
    id => "my_plugin_id"
  }
}
```

::::{note} 
Variable substitution in the `id` field only supports environment variables and does not support the use of values from the secret store.
::::




