---
navigation_title: "Filter plugins"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash/current/filter-plugins.html
---

# Filter plugins [filter-plugins]

A filter plugin performs intermediary processing on an event. Filters are often applied conditionally depending on the characteristics of the event.

The following filter plugins are available below. For a list of Elastic supported plugins, please consult the [Support Matrix](https://www.elastic.co/support/matrix#show_logstash_plugins).

| | | |
| :- | :- | :- |
| Plugin | Description | Github repository |
| [age](plugins-filters-age.md) | Calculates the age of an event by subtracting the event timestamp from the current timestamp | [logstash-filter-age](https://github.com/logstash-plugins/logstash-filter-age) |
| [aggregate](plugins-filters-aggregate.md) | Aggregates information from several events originating with a single task | [logstash-filter-aggregate](https://github.com/logstash-plugins/logstash-filter-aggregate) |
| [alter](plugins-filters-alter.md) | Performs general alterations to fields that the `mutate` filter does not handle | [logstash-filter-alter](https://github.com/logstash-plugins/logstash-filter-alter) |
| [bytes](plugins-filters-bytes.md) | Parses string representations of computer storage sizes, such as "123 MB" or "5.6gb", into their numeric value in bytes | [logstash-filter-bytes](https://github.com/logstash-plugins/logstash-filter-bytes) |
| [cidr](plugins-filters-cidr.md) | Checks IP addresses against a list of network blocks | [logstash-filter-cidr](https://github.com/logstash-plugins/logstash-filter-cidr) |
| [cipher](plugins-filters-cipher.md) | Applies or removes a cipher to an event | [logstash-filter-cipher](https://github.com/logstash-plugins/logstash-filter-cipher) |
| [clone](plugins-filters-clone.md) | Duplicates events | [logstash-filter-clone](https://github.com/logstash-plugins/logstash-filter-clone) |
| [csv](plugins-filters-csv.md) | Parses comma-separated value data into individual fields | [logstash-filter-csv](https://github.com/logstash-plugins/logstash-filter-csv) |
| [date](plugins-filters-date.md) | Parses dates from fields to use as the Logstash timestamp for an event | [logstash-filter-date](https://github.com/logstash-plugins/logstash-filter-date) |
| [de\_dot](plugins-filters-de_dot.md) | Computationally expensive filter that removes dots from a field name | [logstash-filter-de\_dot](https://github.com/logstash-plugins/logstash-filter-de_dot) |
| [dissect](plugins-filters-dissect.md) | Extracts unstructured event data into fields using delimiters | [logstash-filter-dissect](https://github.com/logstash-plugins/logstash-filter-dissect) |
| [dns](plugins-filters-dns.md) | Performs a standard or reverse DNS lookup | [logstash-filter-dns](https://github.com/logstash-plugins/logstash-filter-dns) |
| [drop](plugins-filters-drop.md) | Drops all events | [logstash-filter-drop](https://github.com/logstash-plugins/logstash-filter-drop) |
| [elapsed](plugins-filters-elapsed.md) | Calculates the elapsed time between a pair of events | [logstash-filter-elapsed](https://github.com/logstash-plugins/logstash-filter-elapsed) |
| [elastic\_integration](plugins-filters-elastic_integration.md) | Provides additional Logstash processing on data from Elastic integrations | [logstash-filter-elastic\_integration](https://github.com/elastic/logstash-filter-elastic_integration) |
| [elasticsearch](plugins-filters-elasticsearch.md) | Copies fields from previous log events in Elasticsearch to current events | [logstash-filter-elasticsearch](https://github.com/logstash-plugins/logstash-filter-elasticsearch) |
| [environment](plugins-filters-environment.md) | Stores environment variables as metadata sub-fields | [logstash-filter-environment](https://github.com/logstash-plugins/logstash-filter-environment) |
| [extractnumbers](plugins-filters-extractnumbers.md) | Extracts numbers from a string | [logstash-filter-extractnumbers](https://github.com/logstash-plugins/logstash-filter-extractnumbers) |
| [fingerprint](plugins-filters-fingerprint.md) | Fingerprints fields by replacing values with a consistent hash | [logstash-filter-fingerprint](https://github.com/logstash-plugins/logstash-filter-fingerprint) |
| [geoip](plugins-filters-geoip.md) | Adds geographical information about an IP address | [logstash-filter-geoip](https://github.com/logstash-plugins/logstash-filter-geoip) |
| [grok](plugins-filters-grok.md) | Parses unstructured event data into fields | [logstash-filter-grok](https://github.com/logstash-plugins/logstash-filter-grok) |
| [http](plugins-filters-http.md) | Provides integration with external web services/REST APIs | [logstash-filter-http](https://github.com/logstash-plugins/logstash-filter-http) |
| [i18n](plugins-filters-i18n.md) | Removes special characters from a field | [logstash-filter-i18n](https://github.com/logstash-plugins/logstash-filter-i18n) |
| [java\_uuid](plugins-filters-java_uuid.md) | Generates a UUID and adds it to each processed event | [core plugin](https://github.com/elastic/logstash/blob/8.18/logstash-core/src/main/java/org/logstash/plugins/filters/Uuid.java) |
| [jdbc\_static](plugins-filters-jdbc_static.md) | Enriches events with data pre-loaded from a remote database | [logstash-integration-jdbc](https://github.com/logstash-plugins/logstash-integration-jdbc) |
| [jdbc\_streaming](plugins-filters-jdbc_streaming.md) | Enrich events with your database data | [logstash-integration-jdbc](https://github.com/logstash-plugins/logstash-integration-jdbc) |
| [json](plugins-filters-json.md) | Parses JSON events | [logstash-filter-json](https://github.com/logstash-plugins/logstash-filter-json) |
| [json\_encode](plugins-filters-json_encode.md) | Serializes a field to JSON | [logstash-filter-json\_encode](https://github.com/logstash-plugins/logstash-filter-json_encode) |
| [kv](plugins-filters-kv.md) | Parses key-value pairs | [logstash-filter-kv](https://github.com/logstash-plugins/logstash-filter-kv) |
| [memcached](plugins-filters-memcached.md) | Provides integration with external data in Memcached | [logstash-filter-memcached](https://github.com/logstash-plugins/logstash-filter-memcached) |
| [metricize](plugins-filters-metricize.md) | Takes complex events containing a number of metrics and splits these up into multiple events, each holding a single metric | [logstash-filter-metricize](https://github.com/logstash-plugins/logstash-filter-metricize) |
| [metrics](plugins-filters-metrics.md) | Aggregates metrics | [logstash-filter-metrics](https://github.com/logstash-plugins/logstash-filter-metrics) |
| [mutate](plugins-filters-mutate.md) | Performs mutations on fields | [logstash-filter-mutate](https://github.com/logstash-plugins/logstash-filter-mutate) |
| [prune](plugins-filters-prune.md) | Prunes event data based on a list of fields to blacklist or whitelist | [logstash-filter-prune](https://github.com/logstash-plugins/logstash-filter-prune) |
| [range](plugins-filters-range.md) | Checks that specified fields stay within given size or length limits | [logstash-filter-range](https://github.com/logstash-plugins/logstash-filter-range) |
| [ruby](plugins-filters-ruby.md) | Executes arbitrary Ruby code | [logstash-filter-ruby](https://github.com/logstash-plugins/logstash-filter-ruby) |
| [sleep](plugins-filters-sleep.md) | Sleeps for a specified time span | [logstash-filter-sleep](https://github.com/logstash-plugins/logstash-filter-sleep) |
| [split](plugins-filters-split.md) | Splits multi-line messages, strings, or arrays into distinct events | [logstash-filter-split](https://github.com/logstash-plugins/logstash-filter-split) |
| [syslog\_pri](plugins-filters-syslog_pri.md) | Parses the `PRI` (priority) field of a `syslog` message | [logstash-filter-syslog\_pri](https://github.com/logstash-plugins/logstash-filter-syslog_pri) |
| [threats\_classifier](plugins-filters-threats_classifier.md) | Enriches security logs with information about the attacker’s intent | [logstash-filter-threats\_classifier](https://github.com/empow/logstash-filter-threats_classifier) |
| [throttle](plugins-filters-throttle.md) | Throttles the number of events | [logstash-filter-throttle](https://github.com/logstash-plugins/logstash-filter-throttle) |
| [tld](plugins-filters-tld.md) | Replaces the contents of the default message field with whatever you specify in the configuration | [logstash-filter-tld](https://github.com/logstash-plugins/logstash-filter-tld) |
| [translate](plugins-filters-translate.md) | Replaces field contents based on a hash or YAML file | [logstash-filter-translate](https://github.com/logstash-plugins/logstash-filter-translate) |
| [truncate](plugins-filters-truncate.md) | Truncates fields longer than a given length | [logstash-filter-truncate](https://github.com/logstash-plugins/logstash-filter-truncate) |
| [urldecode](plugins-filters-urldecode.md) | Decodes URL-encoded fields | [logstash-filter-urldecode](https://github.com/logstash-plugins/logstash-filter-urldecode) |
| [useragent](plugins-filters-useragent.md) | Parses user agent strings into fields | [logstash-filter-useragent](https://github.com/logstash-plugins/logstash-filter-useragent) |
| [uuid](plugins-filters-uuid.md) | Adds a UUID to events | [logstash-filter-uuid](https://github.com/logstash-plugins/logstash-filter-uuid) |
| [wurfl\_device\_detection](plugins-filters-wurfl_device_detection.md) | Enriches logs with device information such as brand, model, OS | [logstash-filter-wurfl\_device\_detection](https://github.com/WURFL/logstash-filter-wurfl_device_detection) |
| [xml](plugins-filters-xml.md) | Parses XML into fields | [logstash-filter-xml](https://github.com/logstash-plugins/logstash-filter-xml) |
