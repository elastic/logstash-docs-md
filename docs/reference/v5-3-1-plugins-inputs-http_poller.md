---
navigation_title: "v5.3.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v5.3.1-plugins-inputs-http_poller.html
---

# Http_poller input plugin v5.3.1 [v5.3.1-plugins-inputs-http_poller]


* Plugin version: v5.3.1
* Released on: 2022-06-14
* [Changelog](https://github.com/logstash-plugins/logstash-input-http_poller/blob/v5.3.1/CHANGELOG.md)

For other versions, see the [overview list](input-http_poller-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_509]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http_poller). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_503]

This Logstash input plugin allows you to call an HTTP API, decode the output of it into event(s), and send them on their merry way. The idea behind this plugins came from a need to read springboot metrics endpoint, instead of configuring jmx to monitor my java application memory/gc/ etc.


## Example [_example_6]

Reads from a list of urls and decodes the body of the response with a codec. The config should look like this:

```ruby
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

```ruby
openssl s_client -showcerts -connect MYURL:MYPORT </dev/null 2>/dev/null|openssl x509 -outform PEM > downloaded_cert.pem; keytool -import -alias test -file downloaded_cert.pem -keystore downloaded_truststore.jks
```

The above snippet will create two files `downloaded_cert.pem` and `downloaded_truststore.jks`. You will be prompted to set a password for the `jks` file during this process. To configure logstash use a config like the one that follows.

```ruby
 http_poller {
   urls => {
     myurl => "https://myhostname:1234"
   }
   truststore => "/path/to/downloaded_truststore.jks"
   truststore_password => "mypassword"
   schedule => { cron => "* * * * * UTC"}
 }
```


## Event Metadata and the Elastic Common Schema (ECS) [v5.3.1-plugins-inputs-http_poller-ecs_metadata]

This input will add metadata about the HTTP connection itself to each event.

When ECS compatibility is disabled, metadata was added to a variety of non-standard top-level fields, which has the potential to create confusion and schema conflicts downstream.

With ECS Compatibility Mode, we can ensure a pipeline maintains access to this metadata throughout the event’s lifecycle without polluting the top-level namespace.

Here’s how ECS compatibility mode affects output.

|  ECS disabled |  ECS v1 | Availability | Description |
| --- | --- | --- | --- |
|  [@metadata][host] |  [@metadata][input][http_poller][request][host][hostname] | *Always* | *Hostname* |
|  [@metadata][code] |  [@metadata][input][http_poller][response][status_code] | *When server responds a valid status code* | *HTTP response code* |
|  [@metadata][response_headers] |  [@metadata][input][http_poller][response][headers] | *When server responds with headers* | *HTTP headers of the response* |
|  [@metadata][response_message] |  [@metadata][input][http_poller][response][status_message] | *When server responds with status line* | *message of status line of HTTP headers* |
|  [@metadata][runtime_seconds] |  [@metadata][input][http_poller][response][elapsed_time_ns] | *When server responds a valid status code* | *elapsed time of calling endpoint. ECS v1 shows in nanoseconds.* |
|  [http_request_failure][runtime_seconds] |  [event][duration] | *When server throws exception* | *elapsed time of calling endpoint. ECS v1 shows in nanoseconds.* |
|  [@metadata][times_retried] |  [@metadata][input][http_poller][request][retry_count] | *When the poller calls server successfully* | *retry count from http client library* |
|  [@metadata][name] / [http_request_failure][name] |  [@metadata][input][http_poller][request][name] | *Always* | *The key of `urls` from poller config* |
|  [@metadata][request] / [http_request_failure][request] |  [@metadata][input][http_poller][request][original] | *Always* | *The whole object of `urls` from poller config* |
|  [http_request_failure][error] |  [error][message] | *When server throws exception* | *Error message* |
|  [http_request_failure][backtrace] |  [error][stack_trace] | *When server throws exception* | *Stack trace of error* |
|  -- |  [url][full] | *When server throws exception* | *The URL of the endpoint* |
|  -- |  [http][request][method] | *When server throws exception* | *HTTP request method* |
|  -- |  [host][hostname] | *When server throws exception* | *Hostname* |


## Http_poller Input Configuration Options [v5.3.1-plugins-inputs-http_poller-options]

This plugin supports the following configuration options plus the [Common options](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`automatic_retries`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-automatic_retries) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`cacert`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-cacert) | a valid filesystem path | No |
| [`client_cert`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-client_cert) | a valid filesystem path | No |
| [`client_key`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-client_key) | a valid filesystem path | No |
| [`connect_timeout`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-connect_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`cookies`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-cookies) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ecs_compatibility`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-ecs_compatibility) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`follow_redirects`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-follow_redirects) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`keepalive`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-keepalive) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`keystore`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-keystore) | a valid filesystem path | No |
| [`keystore_password`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`keystore_type`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-keystore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metadata_target`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-metadata_target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`password`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`pool_max`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-pool_max) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`pool_max_per_route`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-pool_max_per_route) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`proxy`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-proxy) | <<,>> | No |
| [`request_timeout`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-request_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`retry_non_idempotent`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-retry_non_idempotent) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`schedule`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-schedule) | [hash](logstash://reference/configuration-file-structure.md#hash) | Yes |
| [`socket_timeout`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-socket_timeout) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`ssl_supported_protocols`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-ssl_supported_protocols) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`ssl_verification_mode`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-ssl_verification_mode) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`target`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`truststore`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-truststore) | a valid filesystem path | No |
| [`truststore_password`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`truststore_type`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-truststore_type) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`urls`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-urls) | [hash](logstash://reference/configuration-file-structure.md#hash) | Yes |
| [`user`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-user) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`validate_after_inactivity`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-validate_after_inactivity) | [number](logstash://reference/configuration-file-structure.md#number) | No |

Also see [Common options](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-common-options) for a list of options supported by all input plugins.

 

### `automatic_retries` [v5.3.1-plugins-inputs-http_poller-automatic_retries]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1`

How many times should the client retry a failing URL. We highly recommend NOT setting this value to zero if keepalive is enabled. Some servers incorrectly end keepalives early requiring a retry! Note: if `retry_non_idempotent` is set only GET, HEAD, PUT, DELETE, OPTIONS, and TRACE requests will be retried.


### `cacert` [v5.3.1-plugins-inputs-http_poller-cacert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If you need to use a custom X.509 CA (.pem certs) specify the path to that here


### `client_cert` [v5.3.1-plugins-inputs-http_poller-client_cert]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If you’d like to use a client certificate (note, most people don’t want this) set the path to the x509 cert here


### `client_key` [v5.3.1-plugins-inputs-http_poller-client_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If you’re using a client certificate specify the path to the encryption key here


### `connect_timeout` [v5.3.1-plugins-inputs-http_poller-connect_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Timeout (in seconds) to wait for a connection to be established. Default is `10s`


### `cookies` [v5.3.1-plugins-inputs-http_poller-cookies]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Enable cookie support. With this enabled the client will persist cookies across requests as a normal web browser would. Enabled by default


### `ecs_compatibility` [v5.3.1-plugins-inputs-http_poller-ecs_compatibility]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are:

    * `disabled`: unstructured data added at root level
    * `v1`: uses `error`, `url` and `http` fields that are compatible with Elastic Common Schema


Controls this plugin’s compatibility with the [Elastic Common Schema (ECS)][Elastic Common Schema (ECS)\]\(([^:]+)://reference/index.md)). See [Event Metadata and the Elastic Common Schema (ECS)](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-ecs_metadata) for detailed information.

Example output:

**Sample output: ECS disabled**

```text
{
    "http_poller_data" => {
        "@version" => "1",
        "@timestamp" => 2021-01-01T00:43:22.388Z,
        "status" => "UP"
    },
    "@version" => "1",
    "@timestamp" => 2021-01-01T00:43:22.389Z,
}
```

**Sample output: ECS enabled**

```text
{
    "http_poller_data" => {
        "status" => "UP",
        "@version" => "1",
        "event" => {
            "original" => "{\"status\":\"UP\"}"
        },
        "@timestamp" => 2021-01-01T00:40:59.558Z
    },
    "@version" => "1",
    "@timestamp" => 2021-01-01T00:40:59.559Z
}
```

**Sample error output: ECS enabled**

```text
{
    "@timestamp" => 2021-07-09T09:53:48.721Z,
    "@version" => "1",
    "host" => {
        "hostname" => "MacBook-Pro"
    },
    "http" => {
        "request" => {
            "method" => "get"
        }
    },
    "event" => {
        "duration" => 259019
    },
    "error" => {
        "stack_trace" => nil,
        "message" => "Connection refused (Connection refused)"
    },
    "url" => {
        "full" => "http://localhost:8080/actuator/health"
    },
    "tags" => [
        [0] "_http_request_failure"
    ]
}
```


### `follow_redirects` [v5.3.1-plugins-inputs-http_poller-follow_redirects]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Should redirects be followed? Defaults to `true`


### `keepalive` [v5.3.1-plugins-inputs-http_poller-keepalive]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Turn this on to enable HTTP keepalive support. We highly recommend setting `automatic_retries` to at least one with this to fix interactions with broken keepalive implementations.


### `keystore` [v5.3.1-plugins-inputs-http_poller-keystore]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If you need to use a custom keystore (`.jks`) specify that here. This does not work with .pem keys!


### `keystore_password` [v5.3.1-plugins-inputs-http_poller-keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Specify the keystore password here. Note, most .jks files created with keytool require a password!


### `keystore_type` [v5.3.1-plugins-inputs-http_poller-keystore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"JKS"`

Specify the keystore type here. One of `JKS` or `PKCS12`. Default is `JKS`


### `metadata_target` [v5.3.1-plugins-inputs-http_poller-metadata_target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"@metadata"`

If you’d like to work with the request/response metadata. Set this value to the name of the field you’d like to store a nested hash of metadata.


### `password` [v5.3.1-plugins-inputs-http_poller-password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Password to be used in conjunction with [`user`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-user) for HTTP authentication.


### `pool_max` [v5.3.1-plugins-inputs-http_poller-pool_max]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `50`

Max number of concurrent connections. Defaults to `50`


### `pool_max_per_route` [v5.3.1-plugins-inputs-http_poller-pool_max_per_route]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `25`

Max number of concurrent connections to a single host. Defaults to `25`


### `proxy` [v5.3.1-plugins-inputs-http_poller-proxy]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

If you’d like to use an HTTP proxy . This supports multiple configuration syntaxes:

1. Proxy host in form: `http://proxy.org:1234`
2. Proxy host in form: `{host => "proxy.org", port => 80, scheme => 'http', user => 'username@host', password => 'password'}`
3. Proxy host in form: `{url =>  'http://proxy.org:1234', user => 'username@host', password => 'password'}`


### `request_timeout` [v5.3.1-plugins-inputs-http_poller-request_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `60`

Timeout (in seconds) for the entire request.


### `retry_non_idempotent` [v5.3.1-plugins-inputs-http_poller-retry_non_idempotent]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

If `automatic_retries` is enabled this will cause non-idempotent HTTP verbs (such as POST) to be retried.


### `schedule` [v5.3.1-plugins-inputs-http_poller-schedule]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

Schedule of when to periodically poll from the urls Format: A hash with + key: "cron" | "every" | "in" | "at" + value: string Examples: a) { "every" ⇒ "1h" } b) { "cron" ⇒ "* * * * * UTC" } See: rufus/scheduler for details about different schedule options and value string format


### `socket_timeout` [v5.3.1-plugins-inputs-http_poller-socket_timeout]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10`

Timeout (in seconds) to wait for data on the socket. Default is `10s`


### `ssl_supported_protocols` [v5.3.1-plugins-inputs-http_poller-ssl_supported_protocols]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Allowed values are: `'TLSv1.1'`, `'TLSv1.2'`, `'TLSv1.3'`
* Default depends on the JDK being used. With up-to-date Logstash, the default is `['TLSv1.2', 'TLSv1.3']`. `'TLSv1.1'` is not considered secure and is only provided for legacy applications.

List of allowed SSL/TLS versions to use when establishing a connection to the HTTP endpoint.

For Java 8 `'TLSv1.3'` is supported  only since **8u262** (AdoptOpenJDK), but requires that you set the `LS_JAVA_OPTS="-Djdk.tls.client.protocols=TLSv1.3"` system property in Logstash.

::::{note}
If you configure the plugin to use `'TLSv1.1'` on any recent JVM, such as the one packaged with Logstash, the protocol is disabled by default and needs to be enabled manually by changing `jdk.tls.disabledAlgorithms` in the **$JDK_HOME/conf/security/java.security** configuration file. That is, `TLSv1.1` needs to be removed from the list.
::::



### `ssl_verification_mode` [v5.3.1-plugins-inputs-http_poller-ssl_verification_mode]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Supported values are: `full`, `none`
* Default value is `full`

Controls the verification of server certificates. The `full` option verifies that the provided certificate is signed by a trusted authority (CA) and also that the server’s hostname (or IP address) matches the names identified within the certificate.

The `none` setting performs no verification of the server’s certificate. This mode disables many of the security benefits of SSL/TLS and should only be used after cautious consideration. It is primarily intended as a temporary diagnostic mechanism when attempting to resolve TLS errors. Using `none`  in production environments is strongly discouraged.


### `target` [v5.3.1-plugins-inputs-http_poller-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Define the target field for placing the received data. If this setting is omitted, the data will be stored at the root (top level) of the event.

::::{tip}
When ECS is enabled, set `target` in the codec (if the codec has a `target` option). Example: `codec => json { target => "TARGET_FIELD_NAME" }`
::::



### `truststore` [v5.3.1-plugins-inputs-http_poller-truststore]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

If you need to use a custom truststore (`.jks`) specify that here. This does not work with .pem certs!


### `truststore_password` [v5.3.1-plugins-inputs-http_poller-truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Specify the truststore password here. Note, most .jks files created with keytool require a password!


### `truststore_type` [v5.3.1-plugins-inputs-http_poller-truststore_type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"JKS"`

Specify the truststore type here. One of `JKS` or `PKCS12`. Default is `JKS`


### `urls` [v5.3.1-plugins-inputs-http_poller-urls]

* This is a required setting.
* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

A Hash of urls in this format : `"name" => "url"`. The name and the url will be passed in the outputted event.

The values in urls can be either:

* a string url (which will be issued as an HTTP GET).
* a sub-hash containing many useful keys provided by the Manticore backend:

    * url: the String url
    * method: (optional) the HTTP method to use (defaults to GET)
    * user: (optional) the HTTP Basic Auth user. The user must be under an auth sub-hash for Manticore, but this plugin also accepts it either way.
    * password: (optional) the HTTP Basic Auth password. The password must be under an auth sub-hash for Manticore, but this plugin accepts it either way.
    * headers: a hash containing key-value pairs of headers.
    * body: a string (supported only on POST and PUT requests)
    * possibly other options mentioned in the [Manticore docs](https://www.rubydoc.info/github/cheald/manticore/Manticore/Client#http-instance_method). Note that Manticore options that are not explicitly documented above are not thoroughly tested and therefore liable to break in unexpected ways if we replace the backend.


**Notes:**

* Passwords specified as a part of `urls` are prone to exposure in plugin log output. The plugin does not declare them as passwords, and therefore doesn’t wrap them in leak-reducing wrappers as we do elsewhere.
* We don’t guarantee that boolean-type options like Manticore’s `follow_redirects` are supported correctly. The strings `true` or `false` may get passed through, and in ruby any string is "truthy."
* Our implementation of this plugin precludes the ability to specify auth[:eager] as anything other than true


### `user` [v5.3.1-plugins-inputs-http_poller-user]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Username to use with HTTP authentication for ALL requests. Note that you can also set this per-URL. If you set this you must also set the [`password`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-password) option.


### `validate_after_inactivity` [v5.3.1-plugins-inputs-http_poller-validate_after_inactivity]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `200`

How long to wait before checking for a stale connection to determine if a keepalive request is needed. Consider setting this value lower than the default, possibly to 0, if you get connection errors regularly.

This client is based on Apache Commons' HTTP implementation. Here’s how the [Apache Commons documentation](https://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/impl/conn/PoolingHttpClientConnectionManager.md#setValidateAfterInactivity(int)) describes this option: "Defines period of inactivity in milliseconds after which persistent connections must be re-validated prior to being leased to the consumer. Non-positive value passed to this method disables connection validation. This check helps detect connections that have become stale (half-closed) while kept inactive in the pool."



## Common options [v5.3.1-plugins-inputs-http_poller-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`codec`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`tags`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-tags) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`type`](v5-3-1-plugins-inputs-http_poller.md#v5.3.1-plugins-inputs-http_poller-type) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `add_field` [v5.3.1-plugins-inputs-http_poller-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

Add a field to an event


### `codec` [v5.3.1-plugins-inputs-http_poller-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"json"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v5.3.1-plugins-inputs-http_poller-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v5.3.1-plugins-inputs-http_poller-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http_poller inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
input {
  http_poller {
    id => "my_plugin_id"
  }
}
```


### `tags` [v5.3.1-plugins-inputs-http_poller-tags]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.


### `type` [v5.3.1-plugins-inputs-http_poller-type]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
