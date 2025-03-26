---
navigation_title: "v4.0.2"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v4.0.2-plugins-integrations-snmp.html
---

# SNMP Integration Plugin v4.0.2 [v4.0.2-plugins-integrations-snmp]


* Plugin version: v4.0.2
* Released on: 2024-05-20
* [Changelog](https://github.com/logstash-plugins/logstash-integration-snmp/blob/v4.0.2/CHANGELOG.md)

For other versions, see the [overview list](integration-snmp-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_130]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-integration-snmp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

::::{warning}
This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


::::{admonition} Technical Preview
The new `integration-snmp` plugin, and its component plugins--`input-snmp` and `input-snmptrap`--are available in *Technical Preview* and can be installed on the latest Logstash 7.x and 8.x versions.

Current 1.x versions of the `input-snmp` plugin are bundled with {{ls}} by default, and will soon be replaced by the snmp input plugin contained in this integration. (If you want to opt into the Technical Preview for the `integration-snmp` plugin, run `bin/logstash-plugin install logstash-integration-snmp`.)

Be aware of [behavioral and mapping differences](v4-0-2-plugins-integrations-snmp.md#v4.0.2-plugins-integrations-snmp-migration) between current stand-alone plugins and the new versions included in the `integration-snmp`. The information in this topic can help.

::::



## Description [_description_130]

The SNMP integration plugin includes:

* [SNMP input plugin](/lsr/plugins-inputs-snmp.md)
* [Snmptrap input plugin](/lsr/plugins-inputs-snmptrap.md)

The new the `logstash-integration-snmp` plugin combines the `logstash-input-snmp` and `logstash-input-snmptrap` plugins into one integrated plugin that encompasses the capabilities of both. This integrated plugin package provides better alignment in snmp processing, better resource managenment, easier package maintenance, and a smaller installation footprint.

In this section, we’ll cover:

* [Migrating to `logstash-integration-snmp` from individual plugins](v4-0-2-plugins-integrations-snmp.md#v4.0.2-plugins-integrations-snmp-migration)
* [Importing MIBs](v4-0-2-plugins-integrations-snmp.md#v4.0.2-plugins-integrations-snmp-import-mibs)


## Migrating to `logstash-integration-snmp` from individual plugins [v4.0.2-plugins-integrations-snmp-migration]

You’ll retain and expand the functionality of existing stand-alone plugins, but in a more compact, integrated package. In this section, we’ll note mapping and behavioral changes, and explain how to preserve current behavior if needed.

### Migration notes: `logstash-input-snmp` [v4.0.2-plugins-integrations-snmp-migration-input-snmp]

As a component of the new `logstash-integration-snmp` plugin, the `logstash-input-snmp` plugin offers the same capabilities as the stand-alone [logstash-input-snmp](https://github.com/logstash-plugins/logstash-input-snmp).

You might need to address some behavior changes depending on the use-case and how the ingested data is being handled through the pipeline.


### Changes to mapping and error logging: `logstash-input-snmp` [v4.0.2-plugins-integrations-snmp-input-snmp-mapping]

* **No such instance errors** are mapped as `error: no such instance currently exists at this OID string` instead of `noSuchInstance`.
* **No such object errors** are mapped as `error: no such object currently exists at this OID string` instead of `noSuchObject`.
* **End of MIB view errors** are mapped as `error: end of MIB view` instead of `endOfMibView`.
* An **unknown variable type** falls back to the `string` representation instead of logging an error as it did in with the stand-alone `logstash-input-snmp`. This change should not affect existing pipelines, unless they have custom error handlers that rely on specific error messages.


### Migration notes: `logstash-input-snmptrap` [v4.0.2-plugins-integrations-snmp-migration-input-snmptrap]

As a component of the new `logstash-integration-snmp` plugin, the `logstash-input-snmptrap` plugin offers *almost the same capabilities* as the stand-alone [logstash-input-snmp](https://github.com/logstash-plugins/logstash-input-snmp) plugin.

You might need to address some behavior changes depending on your use case and how the ingested data is being handled through the pipeline.


### Changes to mapping and error logging: `logstash-input-snmptrap` [v4.0.2-plugins-integrations-snmp-input-snmptrap-mapping]

* The **PDU variable bindings** are mapped into the {{ls}} event using the defined data type. By default, the stand-alone `logstash-input-snmptrap` plugin converts all of the data to `string`, ignoring the original type. If this behavior is not what you want, you can use a filter to retain the original type.
* **SNMP `TimeTicks` variables** are mapped as `Long` timestamps instead of formatted date string (`%d days, %02d:%02d:%02d.%02d`).
* **`null` variables values** are mapped using the string `null` instead of `Null` (upper-case N).
* **No such instance errors** are mapped as `error: no such instance currently exists at this OID string` instead of `noSuchInstance`.
* **No such object errors** are mapped as `error: no such object currently exists at this OID string` instead of `noSuchObject`.
* **End of MIB view errors** are mapped as `error: end of MIB view` instead of `endOfMibView`.
* The previous generation (stand-alone) input-snmptrap plugin formatted the **`message` field** as a ruby-snmp `SNMP::SNMPv1_Trap` object representation.

    ```sh
    <SNMP::SNMPv1_Trap:0x6f1a7a4 @varbind_list=[#<SNMP::VarBind:0x2d7bcd8f @value="teststring", @name=[1.11.12.13.14.15]>], @timestamp=#<SNMP::TimeTicks:0x1af47e9d @value=55>, @generic_trap=6,  @enterprise=[1.2.3.4.5.6], @source_ip="127.0.0.1", @agent_addr=#<SNMP::IpAddress:0x29a4833e @value="test">, @specific_trap=99>
    ```

    The new integrated `input-snmptrap` plugin uses JSON to format **`message` field**.

    ```json
    {"error_index":0, "variable_bindings":{"1.3.6.1.6.3.1.1.4.1.0":"SNMPv2-MIB::coldStart", "1.3.6.1.2.1.1.3.0":0}, "error_status":0, "type":"TRAP", "error_status_text":"Success", "community":"public", "version":"2c", "request_id":1436216872}
    ```



### Maintain maximum compatibility with previous implementation [v4.0.2-plugins-integrations-snmp-input-snmptrap-compat]

If needed, you can configure the new `logstash-integration-snmp` plugin to maintain maximum compatibility with the previous (stand-alone) version of the [input-snmp](https://github.com/logstash-plugins/logstash-input-snmp) plugin.

```ruby
input {
   snmptrap {
    use_provided_mibs => false
    oid_mapping_format => 'ruby_snmp'
    oid_map_field_values => true
   }
}
```



## Importing MIBs [v4.0.2-plugins-integrations-snmp-import-mibs]

The SNMP plugins already include the IETF MIBs (management information bases) and these do not need to be imported. To disable the bundled MIBs set the `use_provided_mibs` option to `false`.

Any other MIB will need to be manually imported to provide mapping of the numeric OIDs to MIB field names in the resulting event.

To import a MIB, the OSS [libsmi library](https://www.ibr.cs.tu-bs.de/projects/libsmi/) is required. libsmi is available and installable on most operating systems.

To import a MIB, you need to first convert the ASN.1 MIB file into a `.dic` file using the libsmi `smidump` command line utility.

**Example (using `RFC1213-MIB` file)**

```sh
$ smidump --level=1 -k -f python RFC1213-MIB > RFC1213-MIB.dic
```

Note that the resulting file as output by `smidump` must have the `.dic` extension.

### Preventing a `failed to locate MIB module` error [v4.0.2-plugins-integrations-snmp-locate-mibs]

The `smidump` function looks for MIB dependencies in its pre-configured paths list. To avoid the `failed to locate MIB module` error, you may need to provide the MIBs locations in your particular environment.

The recommended ways to provide the additional path configuration are:

* an environment variable, or
* a config file to provide the additional path configuration.

See the "MODULE LOCATIONS" section of the [smi_config documentation](https://www.ibr.cs.tu-bs.de/projects/libsmi/smi_config.html#MODULE%20LOCATIONS) for more information.


### Option 1: Use an environment variable [v4.0.2-plugins-integrations-snmp-env-var]

Set the `SMIPATH` env var with the path to your MIBs. Be sure to include a prepended colon (`:`) for the path.

```sh
$ SMIPATH=":/path/to/mibs/" smidump -k -f python CISCO-PROCESS-MIB.mib > CISCO-PROCESS-MIB_my.dic <1>
```

1. Notice the colon that precedes the path definition.



### Option 2: Provide a configuration file [v4.0.2-plugins-integrations-snmp-mib-config]

The other approach is to create a configuration file with the `path` option. For example, you could create a file called `smi.conf`:

```sh
path :/path/to/mibs/
```

And use the config with smidump:

```sh
$ smidump -c smi.conf -k -f python CISCO-PROCESS-MIB.mib > CISCO-PROCESS-MIB_my.dic
```



