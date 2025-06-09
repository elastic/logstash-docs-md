---
navigation_title: "v0.0.19"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.0.19-plugins-codecs-nmap.html
---

# Nmap codec plugin v0.0.19 [v0.0.19-plugins-codecs-nmap]

* Plugin version: v0.0.19
* Released on: 2017-06-23
* [Changelog](https://github.com/logstash-plugins/logstash-codec-nmap/blob/v0.0.19/CHANGELOG.md)

For other versions, see the [overview list](codec-nmap-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2427]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-nmap). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2405]

This codec is used to parse [namp](https://nmap.org/) output data which is serialized in XML format. Nmap ("Network Mapper") is a free and open source utility for network discovery and security auditing. For more information on nmap, see <https://nmap.org/>.

This codec can only be used for decoding data.

Event types are listed below

`nmap_scan_metadata`: An object containing top level information about the scan, including how many hosts were up, and how many were down. Useful for the case where you need to check if a DNS based hostname does not resolve, where both those numbers will be zero. `nmap_host`: One event is created per host. The full data covering an individual host, including open ports and traceroute information as a nested structure. `nmap_port`: One event is created per host/port. This duplicates data already in `nmap_host`: This was put in for the case where you want to model ports as separate documents in Elasticsearch (which Kibana prefers). `nmap_traceroute_link`: One of these is output per traceroute *connection*, with a `from` and a `to` object describing each hop. Note that traceroute hop data is not always correct due to the fact that each tracing ICMP packet may take a different route. Also very useful for Kibana visualizations.

## Nmap Codec Configuration Options [v0.0.19-plugins-codecs-nmap-options]

| Setting | Input type | Required |
| :- | :- | :- |
| [`emit_hosts`](v0-0-19-plugins-codecs-nmap.md#v0.0.19-plugins-codecs-nmap-emit_hosts) | [boolean](/lsr/value-types.md#boolean) | No |
| [`emit_ports`](v0-0-19-plugins-codecs-nmap.md#v0.0.19-plugins-codecs-nmap-emit_ports) | [boolean](/lsr/value-types.md#boolean) | No |
| [`emit_scan_metadata`](v0-0-19-plugins-codecs-nmap.md#v0.0.19-plugins-codecs-nmap-emit_scan_metadata) | [boolean](/lsr/value-types.md#boolean) | No |
| [`emit_traceroute_links`](v0-0-19-plugins-codecs-nmap.md#v0.0.19-plugins-codecs-nmap-emit_traceroute_links) | [boolean](/lsr/value-types.md#boolean) | No |

### `emit_hosts` [v0.0.19-plugins-codecs-nmap-emit_hosts]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Emit all host data as a nested document (including ports + traceroutes) with the type *nmap\_fullscan*

### `emit_ports` [v0.0.19-plugins-codecs-nmap-emit_ports]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Emit each port as a separate document with type *nmap\_port*

### `emit_scan_metadata` [v0.0.19-plugins-codecs-nmap-emit_scan_metadata]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Emit scan metadata

### `emit_traceroute_links` [v0.0.19-plugins-codecs-nmap-emit_traceroute_links]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Emit each hop\_tuple of the traceroute with type *nmap\_traceroute\_link*
