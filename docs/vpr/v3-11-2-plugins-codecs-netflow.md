---
navigation_title: "v3.11.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.11.2-plugins-codecs-netflow.html
---

# Netflow codec plugin v3.11.2 [v3.11.2-plugins-codecs-netflow]


* Plugin version: v3.11.2
* Released on: 2018-02-01
* [Changelog](https://github.com/logstash-plugins/logstash-codec-netflow/blob/v3.11.2/CHANGELOG.md)

For other versions, see the [overview list](codec-netflow-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2375]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-netflow). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2353]

The "netflow" codec is used for decoding Netflow v5/v9/v10 (IPFIX) flows.


## Supported Netflow/IPFIX exporters [_supported_netflowipfix_exporters_21]

This codec supports:

* Netflow v5
* Netflow v9
* IPFIX

The following Netflow/IPFIX exporters are known to work with the most recent version of the netflow codec:

| Netflow exporter | v5 | v9 | IPFIX | Remarks |
| --- | --- | --- | --- | --- |
| Barracuda Firewall |  |  | y |  |
| Cisco ASA |  | y |  |  |
| Cisco ASR 1k |  |  | n | Fails because of duplicate fields |
| Cisco ASR 9k |  | y |  |  |
| Cisco IOS 12.x |  | y |  |  |
| Cisco ISR w/ HSL |  | n |  | Fails because of duplicate fields, see: [https://github.com/logstash-plugins/logstash-codec-netflow/issues/93](https://github.com/logstash-plugins/logstash-codec-netflow/issues/93) |
| Cisco WLC |  | y |  |  |
| Citrix Netscaler |  |  | y | Still some unknown fields, labeled netscalerUnknown<id> |
| fprobe | y |  |  |  |
| Fortigate FortiOS |  | y |  |  |
| Huawei Netstream |  | y |  |  |
| ipt_NETFLOW | y | y | y |  |
| Juniper MX80 | y |  |  | SW > 12.3R8 |
| Mikrotik | y |  | y | [http://wiki.mikrotik.com/wiki/Manual:IP/Traffic_Flow](http://wiki.mikrotik.com/wiki/Manual:IP/Traffic_Flow) |
| nProbe | y | y | y | L7 DPI fields now also supported |
| Nokia BRAS |  |  | y |  |
| OpenBSD pflow | y | n | y | [http://man.openbsd.org/OpenBSD-current/man4/pflow.4](http://man.openbsd.org/OpenBSD-current/man4/pflow.4) |
| Softflowd | y | y | y | IPFIX supported in [https://github.com/djmdjm/softflowd](https://github.com/djmdjm/softflowd) |
| Streamcore Streamgroomer |  | y |  |  |
| Palo Alto PAN-OS |  | y |  |  |
| Ubiquiti Edgerouter X |  | y |  | With MPLS labels |
| VMware VDS |  |  | y | Still some unknown fields |
| YAF |  |  | y | With silk and applabel, but no DPI plugin support |
| vIPtela |  |  | y |  |


## Usage [_usage_159]

Example Logstash configuration that will listen on 2055/udp for Netflow v5,v9 and IPFIX:

```ruby
input {
  udp {
    port  => 2055
    codec => netflow
  }
}
```

For high-performance production environments the configuration below will decode up to 15000 flows/sec from a Cisco ASR 9000 router on a dedicated 16 CPU instance. If your total flowrate exceeds 15000 flows/sec, you should use multiple Logstash instances.

Note that for richer flows from a Cisco ASA firewall this number will be at least 3x lower.

```ruby
input {
  udp {
    port                 => 2055
    codec                => netflow
    receive_buffer_bytes => 16777216
    workers              => 16
  }
```

To mitigate dropped packets, make sure to increase the Linux kernel receive buffer limit:

```
# sysctl -w net.core.rmem_max=$((1024*1024*16))
```

## Netflow Codec Configuration Options [v3.11.2-plugins-codecs-netflow-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`cache_save_path`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-cache_save_path) | a valid filesystem path | No |
| [`cache_ttl`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-cache_ttl) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`include_flowset_id`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-include_flowset_id) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ipfix_definitions`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-ipfix_definitions) | a valid filesystem path | No |
| [`netflow_definitions`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-netflow_definitions) | a valid filesystem path | No |
| [`target`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`versions`](v3-11-2-plugins-codecs-netflow.md#v3.11.2-plugins-codecs-netflow-versions) | [array](logstash://reference/configuration-file-structure.md#array) | No |

 

### `cache_save_path` [v3.11.2-plugins-codecs-netflow-cache_save_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Enables the template cache and saves it in the specified directory. This minimizes data loss after Logstash restarts because the codec doesn’t have to wait for the arrival of templates, but instead reload already received templates received during previous runs.

Template caches are saved as:

* [path](logstash://reference/configuration-file-structure.md#path)/netflow_templates.cache for Netflow v9 templates.
* [path](logstash://reference/configuration-file-structure.md#path)/ipfix_templates.cache for IPFIX templates.


### `cache_ttl` [v3.11.2-plugins-codecs-netflow-cache_ttl]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `4000`

Netflow v9/v10 template cache TTL (seconds)


### `include_flowset_id` [v3.11.2-plugins-codecs-netflow-include_flowset_id]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Only makes sense for ipfix, v9 already includes this Setting to true will include the flowset_id in events Allows you to work with sequences, for instance with the aggregate filter


### `ipfix_definitions` [v3.11.2-plugins-codecs-netflow-ipfix_definitions]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Override YAML file containing IPFIX field definitions

Very similar to the Netflow version except there is a top level Private Enterprise Number (PEN) key added:

```yaml
pen:
id:
- :uintN or :ip4_addr or :ip6_addr or :mac_addr or :string
- :name
id:
- :skip
```

There is an implicit PEN 0 for the standard fields.

See [https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/ipfix.yaml](https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/ipfix.yaml) for the base set.


### `netflow_definitions` [v3.11.2-plugins-codecs-netflow-netflow_definitions]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

Override YAML file containing Netflow field definitions

Each Netflow field is defined like so:

```yaml
id:
- default length in bytes
- :name
id:
- :uintN or :ip4_addr or :ip6_addr or :mac_addr or :string
- :name
id:
- :skip
```

See [https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/netflow.yaml](https://github.com/logstash-plugins/logstash-codec-netflow/blob/master/lib/logstash/codecs/netflow/netflow.yaml) for the base set.


### `target` [v3.11.2-plugins-codecs-netflow-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"netflow"`

Specify into what field you want the Netflow data.


### `versions` [v3.11.2-plugins-codecs-netflow-versions]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[5, 9, 10]`

Specify which Netflow versions you will accept.



