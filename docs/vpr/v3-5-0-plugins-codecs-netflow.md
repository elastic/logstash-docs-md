---
navigation_title: "v3.5.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.5.0-plugins-codecs-netflow.html
---

# Netflow codec plugin v3.5.0 [v3.5.0-plugins-codecs-netflow]

* Plugin version: v3.5.0
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-netflow/blob/v3.5.0/CHANGELOG.md)

For other versions, see the [overview list](codec-netflow-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2423]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-netflow). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2401]

The "netflow" codec is used for decoding Netflow v5/v9/v10 (IPFIX) flows.

## Supported Netflow/IPFIX exporters [_supported_netflowipfix_exporters_35]

The following Netflow/IPFIX exporters are known to work with the most recent version of the netflow codec:

| Netflow exporter | v5 | v9 | IPFIX | Remarks |
| :- | :-: | :-: | :-: | :- |
| Softflowd | y | y | y | IPFIX supported in <https://github.com/djmdjm/softflowd> |
| nProbe | y | y | y | |
| ipt\_NETFLOW | y | y | y | |
| Cisco ASA | | y | | |
| Cisco IOS 12.x | | y | | |
| fprobe | y | | | |
| Juniper MX80 | y | | | SW > 12.3R8 |
| OpenBSD pflow | y | n | y | <http://man.openbsd.org/OpenBSD-current/man4/pflow.4> |
| Mikrotik 6.35.4 | y | | n | <http://wiki.mikrotik.com/wiki/Manual:IP/Traffic_Flow> |
| Ubiquiti Edgerouter X | | y | | With MPLS labels |
| Citrix Netscaler | | | y | Still some unknown fields, labeled netscalerUnknown\<id> |

## Usage [_usage_177]

Example Logstash configuration:

```
input {
  udp {
    host => localhost
    port => 2055
    codec => netflow {
      versions => [5, 9]
    }
    type => netflow
  }
  udp {
    host => localhost
    port => 4739
    codec => netflow {
      versions => [10]
      target => ipfix
   }
   type => ipfix
  }
  tcp {
    host => localhost
    port => 4739
    codec => netflow {
      versions => [10]
      target => ipfix
    }
    type => ipfix
  }
}
```

## Netflow Codec Configuration Options [v3.5.0-plugins-codecs-netflow-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`cache_save_path`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-cache_save_path) | a valid filesystem path | No |
| [`cache_ttl`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-cache_ttl) | [number](/lsr/value-types.md#number) | No |
| [`include_flowset_id`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-include_flowset_id) | [boolean](/lsr/value-types.md#boolean) | No |
| [`ipfix_definitions`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-ipfix_definitions) | a valid filesystem path | No |
| [`netflow_definitions`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-netflow_definitions) | a valid filesystem path | No |
| [`target`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-target) | [string](/lsr/value-types.md#string) | No |
| [`versions`](v3-5-0-plugins-codecs-netflow.md#v3.5.0-plugins-codecs-netflow-versions) | [array](/lsr/value-types.md#array) | No |

### `cache_save_path` [v3.5.0-plugins-codecs-netflow-cache_save_path]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Where to save the template cache This helps speed up processing when restarting logstash (So you don’t have to await the arrival of templates) cache will save as path/netflow\_templates.cache and/or path/ipfix\_templates.cache

### `cache_ttl` [v3.5.0-plugins-codecs-netflow-cache_ttl]

* Value type is [number](/lsr/value-types.md#number)
* Default value is `4000`

Netflow v9/v10 template cache TTL (minutes)

### `include_flowset_id` [v3.5.0-plugins-codecs-netflow-include_flowset_id]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Only makes sense for ipfix, v9 already includes this Setting to true will include the flowset\_id in events Allows you to work with sequences, for instance with the aggregate filter

### `ipfix_definitions` [v3.5.0-plugins-codecs-netflow-ipfix_definitions]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Override YAML file containing IPFIX field definitions

Very similar to the Netflow version except there is a top level Private Enterprise Number (PEN) key added:

```
pen:
id:
- :uintN or :ip4_addr or :ip6_addr or :mac_addr or :string
- :name
id:
- :skip
```

There is an implicit PEN 0 for the standard fields.

See <https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/ipfix.yaml> for the base set.

### `netflow_definitions` [v3.5.0-plugins-codecs-netflow-netflow_definitions]

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting.

Override YAML file containing Netflow field definitions

Each Netflow field is defined like so:

```
id:
- default length in bytes
- :name
id:
- :uintN or :ip4_addr or :ip6_addr or :mac_addr or :string
- :name
id:
- :skip
```

See <https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/netflow.yaml> for the base set.

### `target` [v3.5.0-plugins-codecs-netflow-target]

* Value type is [string](/lsr/value-types.md#string)
* Default value is `"netflow"`

Specify into what field you want the Netflow data.

### `versions` [v3.5.0-plugins-codecs-netflow-versions]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[5, 9, 10]`

Specify which Netflow versions you will accept.
