---
navigation_title: "v5.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.0.0-plugins-inputs-http_poller.html
---

# Http_poller input plugin v5.0.0 [v5.0.0-plugins-inputs-http_poller]

* Plugin version: v5.0.0
* Released on: 2019-01-30
* [Changelog](https://github.com/logstash-plugins/logstash-input-http_poller/blob/v5.0.0/CHANGELOG.md)

For other versions, see the [overview list](input-http_poller-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_535]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http_poller). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_529]

This Logstash input plugin allows you to call an HTTP API, decode the output of it into event(s), and send them on their merry way. The idea behind this plugins came from a need to read springboot metrics endpoint, instead of configuring jmx to monitor my java application memory/gc/ etc.

## Example [_example_13]

Reads from a list of urls and decodes the body of the response with a codec. The config should look like this:

```
input {
  http_poller {
    urls => {
      test1 => "http://localhost:9200"
      test2 => {
        # Supports all options supported by ruby's Manticore HTTP client
        method => get
        user => "AzureDiamond"
        password => "hunter2"
        url => "http://localhost:9200/_cluster/health"
        headers => {
          Accept => "application/json"
        }
     }
    }
    request_timeout => 60
    # Supports "cron", "every", "at" and "in" schedules by rufus scheduler
    schedule => { cron => "* * * * * UTC"}
    codec => "json"
    # A hash of request metadata info (timing, response headers, etc.) will be sent here
    metadata_target => "http_poller_metadata"
  }
}

output {
  stdout {
    codec => rubydebug
  }
}
```

Using the HTTP poller with custom a custom CA or self signed cert.

If you have a self signed cert you will need to convert your server’s certificate to a valid# `.jks` or `.p12` file. An easy way to do it is to run the following one-liner, substituting your server’s URL for the placeholder `MYURL` and `MYPORT`.

```
openssl s_client -showcerts -connect MYURL:MYPORT </dev/null 2>/dev/null|openssl x509 -outform PEM > downloaded_cert.pem; keytool -import -alias test -file downloaded_cert.pem -keystore downloaded_truststore.jks
```

The above snippet will create two files `downloaded_cert.pem` and `downloaded_truststore.jks`. You will be prompted to set a password for the `jks` file during this process. To configure logstash use a config like the one that follows.

```
 http_poller {
   urls => {
     myurl => "https://myhostname:1234"
   }
   truststore => "/path/to/downloaded_truststore.jks"
   truststore_password => "mypassword"
   schedule => { cron => "* * * * * UTC"}
 }
```

## Http_poller Input Configuration Options [v5.0.0-plugins-inputs-http_poller-options]

This plugin supports the following configuration options plus the [Common options](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`user`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-user) | [string](/lsr/value-types.md#string) | no |
| [`password`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-password) | [password](/lsr/value-types.md#password) | No |
| [`automatic_retries`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-automatic_retries) | [number](/lsr/value-types.md#number) | No |
| [`cacert`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-cacert) | a valid filesystem path | No |
| [`client_cert`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-client_cert) | a valid filesystem path | No |
| [`client_key`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-client_key) | a valid filesystem path | No |
| [`connect_timeout`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-connect_timeout) | [number](/lsr/value-types.md#number) | No |
| [`cookies`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-cookies) | [boolean](/lsr/value-types.md#boolean) | No |
| [`follow_redirects`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-follow_redirects) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keepalive`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-keepalive) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keystore`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-keystore) | a valid filesystem path | No |
| [`keystore_password`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`keystore_type`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-keystore_type) | [string](/lsr/value-types.md#string) | No |
| [`metadata_target`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-metadata_target) | [string](/lsr/value-types.md#string) | No |
| [`pool_max`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-pool_max) | [number](/lsr/value-types.md#number) | No |
| [`pool_max_per_route`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-pool_max_per_route) | [number](/lsr/value-types.md#number) | No |
| [`proxy`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-proxy) | <<,>> | No |
| [`request_timeout`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-request_timeout) | [number](/lsr/value-types.md#number) | No |
| [`retry_non_idempotent`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-retry_non_idempotent) | [boolean](/lsr/value-types.md#boolean) | No |
| [`schedule`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-schedule) | [hash](/lsr/value-types.md#hash) | Yes |
| [`socket_timeout`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-socket_timeout) | [number](/lsr/value-types.md#number) | No |
| [`target`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-target) | [string](/lsr/value-types.md#string) | No |
| [`truststore`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-truststore) | a valid filesystem path | No |
| [`truststore_password`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-truststore_password) | [password](/lsr/value-types.md#password) | No |
| [`truststore_type`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-truststore_type) | [string](/lsr/value-types.md#string) | No |
| [`urls`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-urls) | [hash](/lsr/value-types.md#hash) | Yes |
| [`validate_after_inactivity`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-validate_after_inactivity) | [number](/lsr/value-types.md#number) | No |

Also see [Common options](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-common-options) for a list of options supported by all input plugins.

### `user` [v5.0.0-plugins-inputs-http_poller-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username to use with HTTP authentication for ALL requests. Note that you can also set this per-URL. If you set this you must also set the `password` option.

### `password` [v5.0.0-plugins-inputs-http_poller-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password to be used in conjunction with the username for HTTP authentication.

### `automatic_retries` [v5.0.0-plugins-inputs-http_poller-automatic_retries]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `1`

How many times should the client retry a failing URL. We highly recommend NOT setting this value to zero if keepalive is enabled. Some servers incorrectly end keepalives early requiring a retry! Note: if `retry_non_idempotent` is set only GET, HEAD, PUT, DELETE, OPTIONS, and TRACE requests will be retried.

### `cacert` [v5.0.0-plugins-inputs-http_poller-cacert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom X.509 CA (.pem certs) specify the path to that here

### `client_cert` [v5.0.0-plugins-inputs-http_poller-client_cert]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’d like to use a client certificate (note, most people don’t want this) set the path to the x509 cert here

### `client_key` [v5.0.0-plugins-inputs-http_poller-client_key]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you’re using a client certificate specify the path to the encryption key here

### `connect_timeout` [v5.0.0-plugins-inputs-http_poller-connect_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for a connection to be established. Default is `10s`

### `cookies` [v5.0.0-plugins-inputs-http_poller-cookies]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Enable cookie support. With this enabled the client will persist cookies across requests as a normal web browser would. Enabled by default

### `follow_redirects` [v5.0.0-plugins-inputs-http_poller-follow_redirects]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Should redirects be followed? Defaults to `true`

### `keepalive` [v5.0.0-plugins-inputs-http_poller-keepalive]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Turn this on to enable HTTP keepalive support. We highly recommend setting `automatic_retries` to at least one with this to fix interactions with broken keepalive implementations.

### `keystore` [v5.0.0-plugins-inputs-http_poller-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom keystore (`.jks`) specify that here. This does not work with .pem keys!

### `keystore_password` [v5.0.0-plugins-inputs-http_poller-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the keystore password here. Note, most .jks files created with keytool require a password!

### `keystore_type` [v5.0.0-plugins-inputs-http_poller-keystore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the keystore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `metadata_target` [v5.0.0-plugins-inputs-http_poller-metadata_target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"@metadata"`

If you’d like to work with the request/response metadata. Set this value to the name of the field you’d like to store a nested hash of metadata.

### `pool_max` [v5.0.0-plugins-inputs-http_poller-pool_max]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `50`

Max number of concurrent connections. Defaults to `50`

### `pool_max_per_route` [v5.0.0-plugins-inputs-http_poller-pool_max_per_route]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `25`

Max number of concurrent connections to a single host. Defaults to `25`

### `proxy` [v5.0.0-plugins-inputs-http_poller-proxy]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

If you’d like to use an HTTP proxy . This supports multiple configuration syntaxes:

1. Proxy host in form: `http://proxy.org:1234`
2. Proxy host in form: `{host => "proxy.org", port => 80, scheme => 'http', user => 'username@host', password => 'password'}`
3. Proxy host in form: `{url => 'http://proxy.org:1234', user => 'username@host', password => 'password'}`

### `request_timeout` [v5.0.0-plugins-inputs-http_poller-request_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `60`

Timeout (in seconds) for the entire request.

### `retry_non_idempotent` [v5.0.0-plugins-inputs-http_poller-retry_non_idempotent]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

If `automatic_retries` is enabled this will cause non-idempotent HTTP verbs (such as POST) to be retried.

### `schedule` [v5.0.0-plugins-inputs-http_poller-schedule]

* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

Schedule of when to periodically poll from the urls Format: A hash with + key: "cron" | "every" | "in" | "at" + value: string Examples: a) { "every" ⇒ "1h" } b) { "cron" ⇒ "\* \* \* \* \* UTC" } See: rufus/scheduler for details about different schedule options and value string format

### `socket_timeout` [v5.0.0-plugins-inputs-http_poller-socket_timeout]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `10`

Timeout (in seconds) to wait for data on the socket. Default is `10s`

### `target` [v5.0.0-plugins-inputs-http_poller-target]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Define the target field for placing the received data. If this setting is omitted, the data will be stored at the root (top level) of the event.

### `truststore` [v5.0.0-plugins-inputs-http_poller-truststore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

If you need to use a custom truststore (`.jks`) specify that here. This does not work with .pem certs!

### `truststore_password` [v5.0.0-plugins-inputs-http_poller-truststore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Specify the truststore password here. Note, most .jks files created with keytool require a password!

### `truststore_type` [v5.0.0-plugins-inputs-http_poller-truststore_type]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"JKS"`

Specify the truststore type here. One of `JKS` or `PKCS12`. Default is `JKS`

### `urls` [v5.0.0-plugins-inputs-http_poller-urls]

* This is a required setting.
* Value type is [hash](/lsr/value-types.md#hash)
* There is no default value for this setting.

A Hash of urls in this format : `"name" => "url"`. The name and the url will be passed in the outputed event

### `validate_after_inactivity` [v5.0.0-plugins-inputs-http_poller-validate_after_inactivity]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `200`

How long to wait before checking if the connection is stale before executing a request on a connection using keepalive. # You may want to set this lower, possibly to 0 if you get connection errors regularly Quoting the Apache commons docs (this client is based Apache Commmons): *Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool.* See [these docs for more info](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity\(int\))

## Common options [v5.0.0-plugins-inputs-http_poller-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v5-0-0-plugins-inputs-http_poller.md#v5.0.0-plugins-inputs-http_poller-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v5.0.0-plugins-inputs-http_poller-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v5.0.0-plugins-inputs-http_poller-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v5.0.0-plugins-inputs-http_poller-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v5.0.0-plugins-inputs-http_poller-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http\_poller inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  http_poller {
    id => "my_plugin_id"
  }
}
```

### `tags` [v5.0.0-plugins-inputs-http_poller-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v5.0.0-plugins-inputs-http_poller-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
