---
navigation_title: "v6.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v6.0.1-plugins-filters-geoip.html
---

# Geoip filter plugin v6.0.1 [v6.0.1-plugins-filters-geoip]


* Plugin version: v6.0.1
* Released on: 2019-05-01
* [Changelog](https://github.com/logstash-plugins/logstash-filter-geoip/blob/v6.0.1/CHANGELOG.md)

For other versions, see the [overview list](filter-geoip-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1892]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-geoip). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_1870]

The GeoIP filter adds information about the geographical location of IP addresses, based on data from the Maxmind GeoLite2 databases.


## Supported Databases [_supported_databases_25]

This plugin is bundled with [GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2) City database out of the box. From Maxmind’s description — "GeoLite2 databases are free IP geolocation databases comparable to, but less accurate than, MaxMind’s GeoIP2 databases". Please see GeoIP Lite2 license for more details.

[Commercial databases](https://www.maxmind.com/en/geoip2-databases) from Maxmind are also supported in this plugin.

If you need to use databases other than the bundled GeoLite2 City, you can download them directly from Maxmind’s website and use the `database` option to specify their location. The GeoLite2 databases can be [downloaded from here](https://dev.maxmind.com/geoip/geoip2/geolite2).

If you would like to get Autonomous System Number(ASN) information, you can use the GeoLite2-ASN database.


## Details [_details_43]

A `[geoip][location]` field is created if the GeoIP lookup returns a latitude and longitude. The field is stored in [GeoJSON](http://geojson.org/geojson-spec.html) format. Additionally, the default Elasticsearch template provided with the [elasticsearch output](logstash://reference/plugins-outputs-elasticsearch.md) maps the `[geoip][location]` field to an [Elasticsearch Geo_point datatype](elasticsearch://reference/elasticsearch/mapping-reference/geo-point.md).

As this field is a `geo_point` *and* it is still valid GeoJSON, you get the awesomeness of Elasticsearch’s geospatial query, facet and filter functions and the flexibility of having GeoJSON for all other applications (like Kibana’s map visualization).

::::{note}
This product includes GeoLite2 data created by MaxMind, available from [http://www.maxmind.com](http://www.maxmind.com). This database is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Versions 4.0.0 and later of the GeoIP filter use the MaxMind GeoLite2 database and support both IPv4 and IPv6 lookups. Versions prior to 4.0.0 use the legacy MaxMind GeoLite database and support IPv4 lookups only.

::::



## Geoip Filter Configuration Options [v6.0.1-plugins-filters-geoip-options]

This plugin supports the following configuration options plus the [Common options](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`cache_size`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-cache_size) | [number](logstash://reference/configuration-file-structure.md#number) | No |
| [`database`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-database) | a valid filesystem path | No |
| [`default_database_type`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-default_database_type) | `City` or `ASN` | No |
| [`fields`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-fields) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`source`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-source) | [string](logstash://reference/configuration-file-structure.md#string) | Yes |
| [`tag_on_failure`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-tag_on_failure) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`target`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-target) | [string](logstash://reference/configuration-file-structure.md#string) | No |

Also see [Common options](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-common-options) for a list of options supported by all filter plugins.

 

### `cache_size` [v6.0.1-plugins-filters-geoip-cache_size]

* Value type is [number](logstash://reference/configuration-file-structure.md#number)
* Default value is `1000`

GeoIP lookup is surprisingly expensive. This filter uses an cache to take advantage of the fact that IPs agents are often found adjacent to one another in log files and rarely have a random distribution. The higher you set this the more likely an item is to be in the cache and the faster this filter will run. However, if you set this too high you can use more memory than desired. Since the Geoip API upgraded to v2, there is not any eviction policy so far, if cache is full, no more record can be added. Experiment with different values for this option to find the best performance for your dataset.

This MUST be set to a value > 0. There is really no reason to not want this behavior, the overhead is minimal and the speed gains are large.

It is important to note that this config value is global to the geoip_type. That is to say all instances of the geoip filter of the same geoip_type share the same cache. The last declared cache size will *win*. The reason for this is that there would be no benefit to having multiple caches for different instances at different points in the pipeline, that would just increase the number of cache misses and waste memory.


### `database` [v6.0.1-plugins-filters-geoip-database]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

The path to Maxmind’s database file that Logstash should use. The default database is GeoLite2-City. GeoLite2-City, GeoLite2-Country, GeoLite2-ASN are the free databases from Maxmind that are supported. GeoIP2-City, GeoIP2-ISP, GeoIP2-Country are the commercial databases from Maxmind that are supported.

If not specified, this will default to the GeoLite2 City database that ships with Logstash.


### `default_database_type` [v6.0.1-plugins-filters-geoip-default_database_type]

This plugin now includes both the GeoLite2-City and GeoLite2-ASN databases.  If `database` and `default_database_type` are unset, the GeoLite2-City database will be selected.  To use the included GeoLite2-ASN database, set `default_database_type` to `ASN`.

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* The default value is `City`
* The only acceptable values are `City` and `ASN`


### `fields` [v6.0.1-plugins-filters-geoip-fields]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* There is no default value for this setting.

An array of geoip fields to be included in the event.

Possible fields depend on the database type. By default, all geoip fields are included in the event.

For the built-in GeoLite2 City database, the following are available: `city_name`, `continent_code`, `country_code2`, `country_code3`, `country_name`, `dma_code`, `ip`, `latitude`, `longitude`, `postal_code`, `region_name` and `timezone`.


### `source` [v6.0.1-plugins-filters-geoip-source]

* This is a required setting.
* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

The field containing the IP address or hostname to map via geoip. If this field is an array, only the first value will be used.


### `tag_on_failure` [v6.0.1-plugins-filters-geoip-tag_on_failure]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `["_geoip_lookup_failure"]`

Tags the event on failure to look up geo information. This can be used in later analysis.


### `target` [v6.0.1-plugins-filters-geoip-target]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"geoip"`

Specify the field into which Logstash should store the geoip data. This can be useful, for example, if you have `src_ip` and `dst_ip` fields and would like the GeoIP information of both IPs.

If you save the data to a target field other than `geoip` and want to use the `geo_point` related functions in Elasticsearch, you need to alter the template provided with the Elasticsearch output and configure the output to use the new template.

Even if you don’t use the `geo_point` mapping, the `[target][location]` field is still valid GeoJSON.



## Common options [v6.0.1-plugins-filters-geoip-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v6-0-1-plugins-filters-geoip.md#v6.0.1-plugins-filters-geoip-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v6.0.1-plugins-filters-geoip-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      geoip {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      geoip {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v6.0.1-plugins-filters-geoip-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      geoip {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      geoip {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v6.0.1-plugins-filters-geoip-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v6.0.1-plugins-filters-geoip-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 geoip filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      geoip {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v6.0.1-plugins-filters-geoip-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v6.0.1-plugins-filters-geoip-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      geoip {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      geoip {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v6.0.1-plugins-filters-geoip-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      geoip {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      geoip {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



