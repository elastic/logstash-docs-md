---
navigation_title: "v4.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.1-plugins-inputs-twitter.html
---

# Twitter input plugin v4.0.1 [v4.0.1-plugins-inputs-twitter]

* Plugin version: v4.0.1
* Released on: 2019-07-11
* [Changelog](https://github.com/logstash-plugins/logstash-input-twitter/blob/v4.0.1/CHANGELOG.md)

For other versions, see the [overview list](input-twitter-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_1002]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-twitter). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_995]

Ingest events from the Twitter Streaming API.

## Twitter Input Configuration Options [v4.0.1-plugins-inputs-twitter-options]

This plugin supports the following configuration options plus the [Common options](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`consumer_key`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-consumer_key) | [string](/lsr/value-types.md#string) | Yes |
| [`consumer_secret`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-consumer_secret) | [password](/lsr/value-types.md#password) | Yes |
| [`follows`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-follows) | [array](/lsr/value-types.md#array) | No |
| [`full_tweet`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-full_tweet) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ignore_retweets`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-ignore_retweets) | [boolean](/lsr/value-types.md#boolean) | No |
| [`keywords`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-keywords) | [array](/lsr/value-types.md#array) | No |
| [`languages`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-languages) | [array](/lsr/value-types.md#array) | No |
| [`locations`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-locations) | [string](/lsr/value-types.md#string) | No |
| [`oauth_token`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-oauth_token) | [string](/lsr/value-types.md#string) | Yes |
| [`oauth_token_secret`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-oauth_token_secret) | [password](/lsr/value-types.md#password) | Yes |
| [`proxy_address`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-proxy_address) | [string](/lsr/value-types.md#string) | No |
| [`proxy_port`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-proxy_port) | [number](/lsr/value-types.md#number) | No |
| [`rate_limit_reset_in`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-rate_limit_reset_in) | [number](/lsr/value-types.md#number) | No |
| [`use_proxy`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-use_proxy) | [boolean](/lsr/value-types.md#boolean) | No |
| [`use_samples`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-use_samples) | [boolean](/lsr/value-types.md#boolean) | No |

Also see [Common options](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-common-options) for a list of options supported by all input plugins.

### `consumer_key` [v4.0.1-plugins-inputs-twitter-consumer_key]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Your Twitter App’s consumer key

Don’t know what this is? You need to create an "application" on Twitter, see this url: <https://dev.twitter.com/apps/new>

### `consumer_secret` [v4.0.1-plugins-inputs-twitter-consumer_secret]

* This is a required setting.
* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Your Twitter App’s consumer secret

If you don’t have one of these, you can create one by registering a new application with Twitter: <https://dev.twitter.com/apps/new>

### `follows` [v4.0.1-plugins-inputs-twitter-follows]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

A comma separated list of user IDs, indicating the users to return statuses for in the Twitter stream. See <https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters> for more details.

### `full_tweet` [v4.0.1-plugins-inputs-twitter-full_tweet]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Record full tweet object as given to us by the Twitter Streaming API.

### `ignore_retweets` [v4.0.1-plugins-inputs-twitter-ignore_retweets]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Lets you ignore the retweets coming out of the Twitter API. Default ⇒ false

### `keywords` [v4.0.1-plugins-inputs-twitter-keywords]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Any keywords to track in the Twitter stream. For multiple keywords, use the syntax \["foo", "bar"]. There’s a logical OR between each keyword string listed and a logical AND between words separated by spaces per keyword string. See <https://dev.twitter.com/streaming/overview/request-parameters#track> for more details.

The wildcard "\*" option is not supported. To ingest a sample stream of all tweets, the use\_samples option is recommended.

### `languages` [v4.0.1-plugins-inputs-twitter-languages]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

A list of BCP 47 language identifiers corresponding to any of the languages listed on Twitter’s advanced search page will only return tweets that have been detected as being written in the specified languages.

### `locations` [v4.0.1-plugins-inputs-twitter-locations]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

A comma-separated list of longitude, latitude pairs specifying a set of bounding boxes to filter tweets by. See <https://dev.twitter.com/streaming/overview/request-parameters#locations> for more details.

### `oauth_token` [v4.0.1-plugins-inputs-twitter-oauth_token]

* This is a required setting.
* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Your oauth token.

To get this, login to Twitter with whatever account you want, then visit <https://dev.twitter.com/apps>

Click on your app (used with the consumer\_key and consumer\_secret settings) Then at the bottom of the page, click *Create my access token* which will create an oauth token and secret bound to your account and that application.

### `oauth_token_secret` [v4.0.1-plugins-inputs-twitter-oauth_token_secret]

* This is a required setting.
* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting.

Your oauth token secret.

To get this, login to Twitter with whatever account you want, then visit <https://dev.twitter.com/apps>

Click on your app (used with the consumer\_key and consumer\_secret settings) Then at the bottom of the page, click *Create my access token* which will create an oauth token and secret bound to your account and that application.

### `proxy_address` [v4.0.1-plugins-inputs-twitter-proxy_address]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"127.0.0.1"`

Location of the proxy, by default the same machine as the one running this LS instance

### `proxy_port` [v4.0.1-plugins-inputs-twitter-proxy_port]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `3128`

Port where the proxy is listening, by default 3128 (squid)

### `rate_limit_reset_in` [v4.0.1-plugins-inputs-twitter-rate_limit_reset_in]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `300`

Duration in seconds to wait before retrying a connection when twitter responds with a 429 TooManyRequests In some cases the *x-rate-limit-reset* header is not set in the response and \<error>.rate\_limit.reset\_in is nil. If this occurs then we use the integer specified here. The default is 5 minutes.

### `use_proxy` [v4.0.1-plugins-inputs-twitter-use_proxy]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

When to use a proxy to handle the connections

### `use_samples` [v4.0.1-plugins-inputs-twitter-use_samples]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Returns a small random sample of all public statuses. The tweets returned by the default access level are the same, so if two different clients connect to this endpoint, they will see the same tweets. If set to true, the keywords, follows, locations, and languages options will be ignored. Default ⇒ false

## Common options [v4.0.1-plugins-inputs-twitter-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v4-0-1-plugins-inputs-twitter.md#v4.0.1-plugins-inputs-twitter-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v4.0.1-plugins-inputs-twitter-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v4.0.1-plugins-inputs-twitter-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v4.0.1-plugins-inputs-twitter-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v4.0.1-plugins-inputs-twitter-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 twitter inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  twitter {
    id => "my_plugin_id"
  }
}
```

### `tags` [v4.0.1-plugins-inputs-twitter-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v4.0.1-plugins-inputs-twitter-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
