---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-outputs-cloudwatch.html
---

# Cloudwatch output plugin v3.0.7 [v3.0.7-plugins-outputs-cloudwatch]


* Plugin version: v3.0.7
* Released on: 2017-11-07
* [Changelog](https://github.com/logstash-plugins/logstash-output-cloudwatch/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](output-cloudwatch-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1045]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-output-cloudwatch). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1038]

This output lets you aggregate and send metric data to AWS CloudWatch


## Summary: [_summary_16]

This plugin is intended to be used on a logstash indexer agent (but that is not the only way, see below.)  In the intended scenario, one cloudwatch output plugin is configured, on the logstash indexer node, with just AWS API credentials, and possibly a region and/or a namespace.  The output looks for fields present in events, and when it finds them, it uses them to calculate aggregate statistics.  If the `metricname` option is set in this output, then any events which pass through it will be aggregated & sent to CloudWatch, but that is not recommended.  The intended use is to NOT set the metricname option here, and instead to add a `CW_metricname` field (and other fields) to only the events you want sent to CloudWatch.

When events pass through this output they are queued for background aggregation and sending, which happens every minute by default.  The queue has a maximum size, and when it is full aggregated statistics will be sent to CloudWatch ahead of schedule. Whenever this happens a warning message is written to logstash’s log.  If you see this you should increase the `queue_size` configuration option to avoid the extra API calls.  The queue is emptied every time we send data to CloudWatch.

Note: when logstash is stopped the queue is destroyed before it can be processed. This is a known limitation of logstash and will hopefully be addressed in a future version.


## Details: [_details_16]

There are two ways to configure this plugin, and they can be used in combination: event fields & per-output defaults

Event Field configuration…​ You add fields to your events in inputs & filters and this output reads those fields to aggregate events.  The names of the fields read are configurable via the `field_*` options.

Per-output defaults…​ You set universal defaults in this output plugin’s configuration, and if an event does not have a field for that option then the default is used.

Notice, the event fields take precedence over the per-output defaults.

At a minimum events must have a "metric name" to be sent to CloudWatch. This can be achieved either by providing a default here OR by adding a `CW_metricname` field. By default, if no other configuration is provided besides a metric name, then events will be counted (Unit: Count, Value: 1) by their metric name (either a default or from their `CW_metricname` field)

Other fields which can be added to events to modify the behavior of this plugin are, `CW_namespace`, `CW_unit`, `CW_value`, and `CW_dimensions`.  All of these field names are configurable in this output.  You can also set per-output defaults for any of them. See below for details.

Read more about [AWS CloudWatch](http://aws.amazon.com/cloudwatch/), and the specific of API endpoint this output uses, [PutMetricData](http://docs.amazonwebservices.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.md)


## Cloudwatch Output Configuration Options [v3.0.7-plugins-outputs-cloudwatch-options]

This plugin supports the following configuration options plus the [Common options](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`access_key_id`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-access_key_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`aws_credentials_file`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-aws_credentials_file) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`batch_size`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-batch_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`dimensions`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-dimensions) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`field_dimensions`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-field_dimensions) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field_metricname`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-field_metricname) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field_namespace`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-field_namespace) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field_unit`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-field_unit) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`field_value`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-field_value) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`metricname`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-metricname) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`namespace`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-namespace) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`proxy_uri`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-proxy_uri) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`queue_size`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-queue_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`region`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-region) | [string](logstash://reference/configuration-file-structure.md#string), one of `["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-central-1", "eu-west-1", "eu-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2", "sa-east-1", "us-gov-west-1", "cn-north-1", "ap-south-1", "ca-central-1"]` | No |
| [`secret_access_key`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-secret_access_key) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`session_token`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-session_token) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`timeframe`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-timeframe) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`unit`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-unit) | [string](logstash://reference/configuration-file-structure.md#string), one of `["Seconds", "Microseconds", "Milliseconds", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Bits", "Kilobits", "Megabits", "Gigabits", "Terabits", "Percent", "Count", "Bytes/Second", "Kilobytes/Second", "Megabytes/Second", "Gigabytes/Second", "Terabytes/Second", "Bits/Second", "Kilobits/Second", "Megabits/Second", "Gigabits/Second", "Terabits/Second", "Count/Second", "None"]` | No |
| [`value`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-value) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-common-options) for a list of options supported by all output plugins.

 

### `access_key_id` [v3.0.7-plugins-outputs-cloudwatch-access_key_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

This plugin uses the AWS SDK and supports several ways to get credentials, which will be tried in this order:

1. Static configuration, using `access_key_id` and `secret_access_key` params in logstash plugin config
2. External credentials file specified by `aws_credentials_file`
3. Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
4. Environment variables `AMAZON_ACCESS_KEY_ID` and `AMAZON_SECRET_ACCESS_KEY`
5. IAM Instance Profile (available when running inside EC2)


### `aws_credentials_file` [v3.0.7-plugins-outputs-cloudwatch-aws_credentials_file]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to YAML file containing a hash of AWS credentials. This file will only be loaded if `access_key_id` and `secret_access_key` aren’t set. The contents of the file should look like this:

```ruby
    :access_key_id: "12345"
    :secret_access_key: "54321"
```


### `batch_size` [v3.0.7-plugins-outputs-cloudwatch-batch_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `20`

How many data points can be given in one call to the CloudWatch API


### `dimensions` [v3.0.7-plugins-outputs-cloudwatch-dimensions]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* There is no default value for this setting.

The default dimensions [ name, value, …​ ] to use for events which do not have a `CW_dimensions` field


### `field_dimensions` [v3.0.7-plugins-outputs-cloudwatch-field_dimensions]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"CW_dimensions"`

The name of the field used to set the dimensions on an event metric The field named here, if present in an event, must have an array of one or more key & value pairs, for example…​ `add_field => [ "CW_dimensions", "Environment", "CW_dimensions", "prod" ]` or, equivalently…​ `add_field => [ "CW_dimensions", "Environment" ]` `add_field => [ "CW_dimensions", "prod" ]`


### `field_metricname` [v3.0.7-plugins-outputs-cloudwatch-field_metricname]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"CW_metricname"`

The name of the field used to set the metric name on an event The author of this plugin recommends adding this field to events in inputs & filters rather than using the per-output default setting so that one output plugin on your logstash indexer can serve all events (which of course had fields set on your logstash shippers.)


### `field_namespace` [v3.0.7-plugins-outputs-cloudwatch-field_namespace]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"CW_namespace"`

The name of the field used to set a different namespace per event Note: Only one namespace can be sent to CloudWatch per API call so setting different namespaces will increase the number of API calls and those cost money.


### `field_unit` [v3.0.7-plugins-outputs-cloudwatch-field_unit]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"CW_unit"`

The name of the field used to set the unit on an event metric


### `field_value` [v3.0.7-plugins-outputs-cloudwatch-field_value]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"CW_value"`

The name of the field used to set the value (float) on an event metric


### `metricname` [v3.0.7-plugins-outputs-cloudwatch-metricname]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The default metric name to use for events which do not have a `CW_metricname` field. Beware: If this is provided then all events which pass through this output will be aggregated and sent to CloudWatch, so use this carefully.  Furthermore, when providing this option, you will probably want to also restrict events from passing through this output using event type, tag, and field matching


### `namespace` [v3.0.7-plugins-outputs-cloudwatch-namespace]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"Logstash"`

The default namespace to use for events which do not have a `CW_namespace` field


### `proxy_uri` [v3.0.7-plugins-outputs-cloudwatch-proxy_uri]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

URI to proxy server if required


### `queue_size` [v3.0.7-plugins-outputs-cloudwatch-queue_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `10000`

How many events to queue before forcing a call to the CloudWatch API ahead of `timeframe` schedule Set this to the number of events-per-timeframe you will be sending to CloudWatch to avoid extra API calls


### `region` [v3.0.7-plugins-outputs-cloudwatch-region]

* Value can be any of: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ap-northeast-2`, `sa-east-1`, `us-gov-west-1`, `cn-north-1`, `ap-south-1`, `ca-central-1`
* Default value is `"us-east-1"`

The AWS Region


### `secret_access_key` [v3.0.7-plugins-outputs-cloudwatch-secret_access_key]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Secret Access Key


### `session_token` [v3.0.7-plugins-outputs-cloudwatch-session_token]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The AWS Session token for temporary credential


### `timeframe` [v3.0.7-plugins-outputs-cloudwatch-timeframe]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1m"`

Constants aggregate_key members Units How often to send data to CloudWatch This does not affect the event timestamps, events will always have their actual timestamp (to-the-minute) sent to CloudWatch.

We only call the API if there is data to send.

See the Rufus Scheduler docs for an [explanation of allowed values](https://github.com/jmettraux/rufus-scheduler#the-time-strings-understood-by-rufus-scheduler)


### `unit` [v3.0.7-plugins-outputs-cloudwatch-unit]

* Value can be any of: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`
* Default value is `"Count"`

The default unit to use for events which do not have a `CW_unit` field If you set this option you should probably set the "value" option along with it


### `value` [v3.0.7-plugins-outputs-cloudwatch-value]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"1"`

The default value to use for events which do not have a `CW_value` field If provided, this must be a string which can be converted to a float, for example…​ "1", "2.34", ".5", and "0.67" If you set this option you should probably set the `unit` option along with it



## Common options [v3.0.7-plugins-outputs-cloudwatch-common-options]

These configuration options are supported by all output plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`codec`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-codec) | [codec](logstash://reference/configuration-file-structure.md#codec) | No |
| [`enable_metric`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v3-0-7-plugins-outputs-cloudwatch.md#v3.0.7-plugins-outputs-cloudwatch-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |

### `codec` [v3.0.7-plugins-outputs-cloudwatch-codec]

* Value type is [codec](logstash://reference/configuration-file-structure.md#codec)
* Default value is `"plain"`

The codec used for output data. Output codecs are a convenient method for encoding your data before it leaves the output without needing a separate filter in your Logstash pipeline.


### `enable_metric` [v3.0.7-plugins-outputs-cloudwatch-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance. By default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v3.0.7-plugins-outputs-cloudwatch-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type. For example, if you have 2 cloudwatch outputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
output {
  cloudwatch {
    id => "my_plugin_id"
  }
}
```



