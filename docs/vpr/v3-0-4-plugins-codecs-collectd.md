---
navigation_title: "v3.0.4"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.4-plugins-codecs-collectd.html
---

# Collectd [v3.0.4-plugins-codecs-collectd]


* Plugin version: v3.0.4
* Released on: 2017-06-06
* [Changelog](https://github.com/logstash-plugins/logstash-codec-collectd/blob/v3.0.4/CHANGELOG.md)

For other versions, see the [overview list](codec-collectd-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2279]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-collectd). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2257]

Read events from the collectd binary protocol over the network via udp. See [https://collectd.org/wiki/index.php/Binary_protocol](https://collectd.org/wiki/index.php/Binary_protocol)

Configuration in your Logstash configuration file can be as simple as:

```ruby
    input {
      udp {
        port => 25826
        buffer_size => 1452
        codec => collectd { }
      }
    }
```

A sample `collectd.conf` to send to Logstash might be:

```xml
    Hostname    "host.example.com"
    LoadPlugin interface
    LoadPlugin load
    LoadPlugin memory
    LoadPlugin network
    <Plugin interface>
        Interface "eth0"
        IgnoreSelected false
    </Plugin>
    <Plugin network>
        <Server "10.0.0.1" "25826">
        </Server>
    </Plugin>
```

Be sure to replace `10.0.0.1` with the IP of your Logstash instance.


## Collectd Codec Configuration Options [v3.0.4-plugins-codecs-collectd-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`authfile`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-authfile) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`nan_handling`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-nan_handling) | [string](logstash://reference/configuration-file-structure.md#string), one of `["change_value", "warn", "drop"]` | No |
| [`nan_tag`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-nan_tag) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`nan_value`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-nan_value) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`prune_intervals`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-prune_intervals) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`security_level`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-security_level) | [string](logstash://reference/configuration-file-structure.md#string), one of `["None", "Sign", "Encrypt"]` | No |
| [`typesdb`](v3-0-4-plugins-codecs-collectd.md#v3.0.4-plugins-codecs-collectd-typesdb) | [array](logstash://reference/configuration-file-structure.md#array) | No |

 

### `authfile` [v3.0.4-plugins-codecs-collectd-authfile]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Path to the authentication file. This file should have the same format as the [AuthFile](http://collectd.org/documentation/manpages/collectd.conf.5.shtml#authfile_filename) in collectd. You only need to set this option if the `security_level` is set to `Sign` or `Encrypt`


### `nan_handling` [v3.0.4-plugins-codecs-collectd-nan_handling]

* Value can be any of: `change_value`, `warn`, `drop`
* Default value is `"change_value"`

What to do when a value in the event is `NaN` (Not a Number)

* change_value (default): Change the `NaN` to the value of the nan_value option and add `nan_tag` as a tag
* warn: Change the `NaN` to the value of the nan_value option, print a warning to the log and add `nan_tag` as a tag
* drop: Drop the event containing the `NaN` (this only drops the single event, not the whole packet)


### `nan_tag` [v3.0.4-plugins-codecs-collectd-nan_tag]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"_collectdNaN"`

The tag to add to the event if a `NaN` value was found Set this to an empty string ('') if you don’t want to tag


### `nan_value` [v3.0.4-plugins-codecs-collectd-nan_value]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `0`

Only relevant when `nan_handeling` is set to `change_value` Change NaN to this configured value


### `prune_intervals` [v3.0.4-plugins-codecs-collectd-prune_intervals]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Prune interval records.  Defaults to `true`.


### `security_level` [v3.0.4-plugins-codecs-collectd-security_level]

* Value can be any of: `None`, `Sign`, `Encrypt`
* Default value is `"None"`

Security Level. Default is `None`. This setting mirrors the setting from the collectd [Network plugin](https://collectd.org/wiki/index.php/Plugin:Network)


### `typesdb` [v3.0.4-plugins-codecs-collectd-typesdb]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

File path(s) to collectd `types.db` to use. The last matching pattern wins if you have identical pattern names in multiple files. If no types.db is provided the included `types.db` will be used (currently 5.4.0).



