---
navigation_title: "v3.0.5"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.5-plugins-inputs-http.html
---

# Http input plugin v3.0.5 [v3.0.5-plugins-inputs-http]

* Plugin version: v3.0.5
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-input-http/blob/v3.0.5/CHANGELOG.md)

For other versions, see the [overview list](input-http-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_522]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-http). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_516]

Using this input you can receive single or multiline events over http(s). Applications can send an HTTP POST request with a body to the endpoint started by this input and Logstash will convert it into an event for subsequent processing. Users can pass plain text, JSON, or any formatted data and use a corresponding codec with this input. For Content-Type `application/json` the `json` codec is used, but for all other data formats, `plain` codec is used.

This input can also be used to receive webhook requests to integrate with other services and applications. By taking advantage of the vast plugin ecosystem available in Logstash you can trigger actionable events right from your application.

## Security [_security_46]

This plugin supports standard HTTP basic authentication headers to identify the requester. You can pass in a username, password combination while sending data to this input

You can also setup SSL and send data securely over https, with an option of validating the client’s certificate. Currently, the certificate setup is through [Java Keystore format](https://docs.oracle.com/cd/E19509-01/820-3503/ggfen/index.html)

## Http Input Configuration Options [v3.0.5-plugins-inputs-http-options]

This plugin supports the following configuration options plus the [Common options](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`additional_codecs`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-additional_codecs) | [hash](/lsr/value-types.md#hash) | No |
| [`host`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-host) | [string](/lsr/value-types.md#string) | No |
| [`keystore`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-keystore) | a valid filesystem path | No |
| [`keystore_password`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-keystore_password) | [password](/lsr/value-types.md#password) | No |
| [`password`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-password) | [password](/lsr/value-types.md#password) | No |
| [`port`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-port) | [number](/lsr/value-types.md#number) | No |
| [`response_headers`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-response_headers) | [hash](/lsr/value-types.md#hash) | No |
| [`ssl`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-ssl) | [boolean](/lsr/value-types.md#boolean) | No |
| [`threads`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-threads) | [number](/lsr/value-types.md#number) | No |
| [`user`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-user) | [string](/lsr/value-types.md#string) | No |
| [`verify_mode`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-verify_mode) | [string](/lsr/value-types.md#string), one of `["none", "peer", "force_peer"]` | No |

Also see [Common options](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-common-options) for a list of options supported by all input plugins.

### `additional_codecs` [v3.0.5-plugins-inputs-http-additional_codecs]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"application/json"=>"json"}`

Apply specific codecs for specific content types. The default codec will be applied only after this list is checked and no codec for the request’s content-type is found

### `host` [v3.0.5-plugins-inputs-http-host]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"0.0.0.0"`

Codec used to decode the incoming data. This codec will be used as a fall-back if the content-type is not found in the "additional\_codecs" hash The host or ip to bind

### `keystore` [v3.0.5-plugins-inputs-http-keystore]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

The JKS keystore to validate the client’s certificates

### `keystore_password` [v3.0.5-plugins-inputs-http-keystore_password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Set the truststore password

### `password` [v3.0.5-plugins-inputs-http-password]

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Password for basic authorization

### `port` [v3.0.5-plugins-inputs-http-port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `8080`

The TCP port to bind to

### `response_headers` [v3.0.5-plugins-inputs-http-response_headers]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{"Content-Type"=>"text/plain"}`

specify a custom set of response headers

### `ssl` [v3.0.5-plugins-inputs-http-ssl]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

SSL Configurations

Enable SSL

### `threads` [v3.0.5-plugins-inputs-http-threads]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `4`

Maximum number of threads to use

### `user` [v3.0.5-plugins-inputs-http-user]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Username for basic authorization

### `verify_mode` [v3.0.5-plugins-inputs-http-verify_mode]

* Value can be any of: `none`, `peer`, `force_peer`
* Default value is `"none"`

Set the client certificate verification method. Valid methods: none, peer, force\_peer

## Common options [v3.0.5-plugins-inputs-http-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v3-0-5-plugins-inputs-http.md#v3.0.5-plugins-inputs-http-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v3.0.5-plugins-inputs-http-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v3.0.5-plugins-inputs-http-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v3.0.5-plugins-inputs-http-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v3.0.5-plugins-inputs-http-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 http inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  http {
    id => "my_plugin_id"
  }
}
```

### `tags` [v3.0.5-plugins-inputs-http-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v3.0.5-plugins-inputs-http-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
