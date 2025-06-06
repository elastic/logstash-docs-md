---
navigation_title: "v3.3.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.3.0-plugins-inputs-http_poller.html
---

# Http_poller [v3.3.0-plugins-inputs-http_poller]

* Plugin version: v3.3.0
* Released on: 2017-05-08
* [Changelog](https://github.com/logstash-plugins/logstash-input-http_poller/blob/v3.3.0/CHANGELOG.md)

For other versions, see the [overview list](input-http_poller-index.md "Versioned http_poller input plugin docs").

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

### Getting help [_getting_help_546]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http_poller). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

### Description [_description_540]

This Logstash input plugin allows you to call an HTTP API, decode the output of it into event(s), and send them on their merry way. The idea behind this plugins came from a need to read springboot metrics endpoint, instead of configuring jmx to monitor my java application memory/gc/ etc.

### Example [_example_24]

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
   interval => 30
 }
```

### Http_poller Input Configuration Options [v3.3.0-plugins-inputs-http_poller-options]

This plugin supports the following configuration options plus the [Common options](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-common-options "Common options") described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`user`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-user "user") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | no |
| [`password`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-password "password") | [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password) | No |
| [`automatic_retries`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-automatic_retries "automatic_retries") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`cacert`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-cacert "cacert") | a valid filesystem path | No |
| [`client_cert`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-client_cert "client_cert") | a valid filesystem path | No |
| [`client_key`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-client_key "client_key") | a valid filesystem path | No |
| [`connect_timeout`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-connect_timeout "connect_timeout") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`cookies`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-cookies "cookies") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`follow_redirects`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-follow_redirects "follow_redirects") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`keepalive`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-keepalive "keepalive") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`keystore`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-keystore "keystore") | a valid filesystem path | No |
| [`keystore_password`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-keystore_password "keystore_password") | [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password) | No |
| [`keystore_type`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-keystore_type "keystore_type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`metadata_target`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-metadata_target "metadata_target") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`pool_max`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-pool_max "pool_max") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`pool_max_per_route`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-pool_max_per_route "pool_max_per_route") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`proxy`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-proxy "proxy") | <<,>> | No |
| [`request_timeout`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-request_timeout "request_timeout") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`retry_non_idempotent`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-retry_non_idempotent "retry_non_idempotent") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`schedule`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-schedule "schedule") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`socket_timeout`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-socket_timeout "socket_timeout") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |
| [`ssl_certificate_validation`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-ssl_certificate_validation "ssl_certificate_validation") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`target`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-target "target") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`truststore`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-truststore "truststore") | a valid filesystem path | No |
| [`truststore_password`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-truststore_password "truststore_password") | [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password) | No |
| [`truststore_type`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-truststore_type "truststore_type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`urls`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-urls "urls") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | Yes |
| [`validate_after_inactivity`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-validate_after_inactivity "validate_after_inactivity") | [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number) | No |

Also see [Common options](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-common-options "Common options") for a list of options supported by all input plugins.

 

#### `user` [v3.3.0-plugins-inputs-http_poller-user]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Username to use with HTTP authentication for ALL requests. Note that you can also set this per-URL. If you set this you must also set the `password` option.

#### `password` [v3.3.0-plugins-inputs-http_poller-password]

* Value type is [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password)
* There is no default value for this setting.

Password to be used in conjunction with the username for HTTP authentication.

#### `automatic_retries` [v3.3.0-plugins-inputs-http_poller-automatic_retries]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `1`

How many times should the client retry a failing URL. We highly recommend NOT setting this value to zero if keepalive is enabled. Some servers incorrectly end keepalives early requiring a retry! Note: if `retry_non_idempotent` is set only GET, HEAD, PUT, DELETE, OPTIONS, and TRACE requests will be retried.

#### `cacert` [v3.3.0-plugins-inputs-http_poller-cacert]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

If you need to use a custom X.509 CA (.pem certs) specify the path to that here

#### `client_cert` [v3.3.0-plugins-inputs-http_poller-client_cert]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

If you’d like to use a client certificate (note, most people don’t want this) set the path to the x509 cert here

#### `client_key` [v3.3.0-plugins-inputs-http_poller-client_key]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

If you’re using a client certificate specify the path to the encryption key here

#### `connect_timeout` [v3.3.0-plugins-inputs-http_poller-connect_timeout]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `10`

Timeout (in seconds) to wait for a connection to be established. Default is `10s`

#### `cookies` [v3.3.0-plugins-inputs-http_poller-cookies]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Enable cookie support. With this enabled the client will persist cookies across requests as a normal web browser would. Enabled by default

#### `follow_redirects` [v3.3.0-plugins-inputs-http_poller-follow_redirects]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Should redirects be followed? Defaults to `true`

#### `interval` (DEPRECATED) [v3.3.0-plugins-inputs-http_poller-interval]

* DEPRECATED WARNING: This configuration item is deprecated and may not be available in future versions.
* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* There is no default value for this setting.

How often (in seconds) the urls will be called DEPRECATED. Use *schedule* option instead. If both interval and schedule options are specified, interval option takes higher precedence

#### `keepalive` [v3.3.0-plugins-inputs-http_poller-keepalive]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Turn this on to enable HTTP keepalive support. We highly recommend setting `automatic_retries` to at least one with this to fix interactions with broken keepalive implementations.

#### `keystore` [v3.3.0-plugins-inputs-http_poller-keystore]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

If you need to use a custom keystore (`.jks`) specify that here. This does not work with .pem keys!

#### `keystore_password` [v3.3.0-plugins-inputs-http_poller-keystore_password]

* Value type is [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password)
* There is no default value for this setting.

Specify the keystore password here. Note, most .jks files created with keytool require a password!

#### `keystore_type` [v3.3.0-plugins-inputs-http_poller-keystore_type]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"JKS"`

Specify the keystore type here. One of `JKS` or `PKCS12`. Default is `JKS`

#### `metadata_target` [v3.3.0-plugins-inputs-http_poller-metadata_target]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"@metadata"`

If you’d like to work with the request/response metadata. Set this value to the name of the field you’d like to store a nested hash of metadata.

#### `pool_max` [v3.3.0-plugins-inputs-http_poller-pool_max]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `50`

Max number of concurrent connections. Defaults to `50`

#### `pool_max_per_route` [v3.3.0-plugins-inputs-http_poller-pool_max_per_route]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `25`

Max number of concurrent connections to a single host. Defaults to `25`

#### `proxy` [v3.3.0-plugins-inputs-http_poller-proxy]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

If you’d like to use an HTTP proxy . This supports multiple configuration syntaxes:

1. Proxy host in form: `http://proxy.org:1234`
2. Proxy host in form: `{host => "proxy.org", port => 80, scheme => 'http', user => 'username@host', password => 'password'}`
3. Proxy host in form: `{url => 'http://proxy.org:1234', user => 'username@host', password => 'password'}`

#### `request_timeout` [v3.3.0-plugins-inputs-http_poller-request_timeout]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `60`

This module makes it easy to add a very fully configured HTTP client to logstash based on \[Manticore]\(<https://github.com/cheald/manticore>). For an example of its usage see <https://github.com/logstash-plugins/logstash-input-http_poller> Timeout (in seconds) for the entire request

#### `retry_non_idempotent` [v3.3.0-plugins-inputs-http_poller-retry_non_idempotent]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `false`

If `automatic_retries` is enabled this will cause non-idempotent HTTP verbs (such as POST) to be retried.

#### `schedule` [v3.3.0-plugins-inputs-http_poller-schedule]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* There is no default value for this setting.

Schedule of when to periodically poll from the urls Format: A hash with + key: "cron" | "every" | "in" | "at" + value: string Examples: a) { "every" ⇒ "1h" } b) { "cron" ⇒ "\* \* \* \* \* UTC" } See: rufus/scheduler for details about different schedule options and value string format

#### `socket_timeout` [v3.3.0-plugins-inputs-http_poller-socket_timeout]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `10`

Timeout (in seconds) to wait for data on the socket. Default is `10s`

#### `ssl_certificate_validation` [v3.3.0-plugins-inputs-http_poller-ssl_certificate_validation]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Set this to false to disable SSL/TLS certificate validation Note: setting this to false is generally considered insecure!

#### `target` [v3.3.0-plugins-inputs-http_poller-target]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Define the target field for placing the received data. If this setting is omitted, the data will be stored at the root (top level) of the event.

#### `truststore` [v3.3.0-plugins-inputs-http_poller-truststore]

* Value type is [path](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#path)
* There is no default value for this setting.

If you need to use a custom truststore (`.jks`) specify that here. This does not work with .pem certs!

#### `truststore_password` [v3.3.0-plugins-inputs-http_poller-truststore_password]

* Value type is [password](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#password)
* There is no default value for this setting.

Specify the truststore password here. Note, most .jks files created with keytool require a password!

#### `truststore_type` [v3.3.0-plugins-inputs-http_poller-truststore_type]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* Default value is `"JKS"`

Specify the truststore type here. One of `JKS` or `PKCS12`. Default is `JKS`

#### `urls` [v3.3.0-plugins-inputs-http_poller-urls]

* This is a required setting.
* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* There is no default value for this setting.

A Hash of urls in this format : `"name" => "url"`. The name and the url will be passed in the outputed event

#### `validate_after_inactivity` [v3.3.0-plugins-inputs-http_poller-validate_after_inactivity]

* Value type is [number](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#number)
* Default value is `200`

How long to wait before checking if the connection is stale before executing a request on a connection using keepalive. # You may want to set this lower, possibly to 0 if you get connection errors regularly Quoting the Apache commons docs (this client is based Apache Commmons): *Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool.* See [these docs for more info](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.html#setValidateAfterInactivity\(int\))

### Common options [v3.3.0-plugins-inputs-http_poller-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-add_field "add_field") | [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash) | No |
| [`codec`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-codec "codec") | [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec) | No |
| [`enable_metric`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-enable_metric "enable_metric") | [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean) | No |
| [`id`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-id "id") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |
| [`tags`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-tags "tags") | [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array) | No |
| [`type`](v3-3-0-plugins-inputs-http_poller.md#v3.3.0-plugins-inputs-http_poller-type "type") | [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string) | No |

#### `add_field` [v3.3.0-plugins-inputs-http_poller-add_field]

* Value type is [hash](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#hash)
* Default value is `{}`

Add a field to an event

#### `codec` [v3.3.0-plugins-inputs-http_poller-codec]

* Value type is [codec](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

#### `enable_metric` [v3.3.0-plugins-inputs-http_poller-enable_metric]

* Value type is [boolean](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

#### `id` [v3.3.0-plugins-inputs-http_poller-id]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http\_poller inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  http_poller {
    id => "my_plugin_id"
  }
}
```

#### `tags` [v3.3.0-plugins-inputs-http_poller-tags]

* Value type is [array](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

#### `type` [v3.3.0-plugins-inputs-http_poller-type]

* Value type is [string](https://www.elastic.co/guide/en/logstash/current/configuration-file-structure.html#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
