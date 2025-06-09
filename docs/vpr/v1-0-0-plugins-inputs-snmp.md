---
navigation_title: "v1.0.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.0.0-plugins-inputs-snmp.html
---

# SNMP input plugin v1.0.0 [v1.0.0-plugins-inputs-snmp]

* Plugin version: v1.0.0
* Released on: 2018-10-24
* [Changelog](https://github.com/logstash-plugins/logstash-input-snmp/blob/v1.0.0/CHANGELOG.md)

For other versions, see the [overview list](input-snmp-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_871]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-input-snmp). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_864]

The SNMP input polls network devices using Simple Network Management Protocol (SNMP) to gather information related to the current state of the devices operation.

## Importing MIBs [v1.0.0-plugins-inputs-snmp-import-mibs]

This plugin already includes the IETF MIBs (management information bases) and these do not need to be imported.

Any other MIB will need to be manually imported to provide mapping of the numeric OIDs to MIB field names in the resulting event.

To import a MIB, the OSS [libsmi library](https://www.ibr.cs.tu-bs.de/projects/libsmi/) is required. libsmi is available and installable on most operating systems.

To import a MIB, you need to first convert the ASN.1 MIB file into a `.dic` file using the libsmi `smidump` command line utility.

Example (using `RFC1213-MIB` file)

```
$ smidump --level=1 -k -f python RFC1213-MIB > RFC1213-MIB.dic
```

Note that the resulting file as output by `smidump` must have the `.dic` extension.

## SNMP Input Configuration Options [v1.0.0-plugins-inputs-snmp-options]

This plugin supports the following configuration options plus the [Common options](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`auth_pass`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-auth_pass) | [password](/lsr/value-types.md#password) | No |
| [`auth_protocol`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-auth_protocol) | [string](/lsr/value-types.md#string), one of `["md5", "sha", "sha2", "hmac128sha224", "hmac192sha256", "hmac256sha384", "hmac384sha512"]` | No |
| [`get`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-get) | [array](/lsr/value-types.md#array) | No |
| [`hosts`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-hosts) | [array](/lsr/value-types.md#array) | No |
| [`interval`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-interval) | [number](/lsr/value-types.md#number) | No |
| [`mib_paths`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-mib_paths) | [path](/lsr/value-types.md#path) | No |
| [`oid_root_skip`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-oid_root_skip) | [boolean](/lsr/value-types.md#boolean) | No |
| [`priv_pass`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-priv_pass) | [password](/lsr/value-types.md#password) | No |
| [`priv_protocol`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-priv_protocol) | [string](/lsr/value-types.md#string), one of `["des", "3des", "aes", "aes128", "aes192", "aes256"]` | No |
| [`security_level`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-security_level) | [string](/lsr/value-types.md#string), one of `["noAuthNoPriv", "authNoPriv", "authPriv"]` | No |
| [`security_name`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-security_name) | [string](/lsr/value-types.md#string) | No |
| [`walk`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-walk) | [array](/lsr/value-types.md#array) | No |

Also see [Common options](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-common-options) for a list of options supported by all input plugins.

### `get` [v1.0.0-plugins-inputs-snmp-get]

Use the `get` option to query for scalar values for the given OID(s). One or more OID(s) are specified as an array of strings of OID(s).

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting

Example

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.3.0", "1.3.6.1.2.1.1.5.0"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public"}]
  }
}
```

### `hosts` [v1.0.0-plugins-inputs-snmp-hosts]

The `hosts` option specifies the list of hosts to query the configured `get` and `walk` options.

Each host definition is a hash and must define the `host` key and value. `host` must use the format `{tcp|udp}:{ip address}/{port}`, for example `host => "udp:127.0.0.1/161"`

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting

Each host definition can optionally include the following keys and values:

* `community` the community string, default is `public`.
* `version` `1`, `2c` or `3`, default is `2c`.
* `retries` is the number of retries in case of failure, default is `2`.
* `timeout` is the timeout in milliseconds with a default value of `1000`.

**Specifying all hosts options**

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public" version => "2c"  retries => 2  timeout => 1000}]
  }
}
```

**Specifying multiple hosts**

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public"}, {host => "udp:192.168.0.1/161" community => "private"}]
  }
}
```

### `interval` [v1.0.0-plugins-inputs-snmp-interval]

The `interval` option specifies the polling interval in seconds.

* Value type is [number](/lsr/value-types.md#number)
* Default value is `30`

### `mib_paths` [v1.0.0-plugins-inputs-snmp-mib_paths]

The `mib_paths` option specifies the location of one or more imported MIB files. The value can be either a dir path containing the imported MIB `.dic` files or a file path to a single MIB `.dic` file.

* Value type is [path](/lsr/value-types.md#path)
* There is no default value for this setting

This plugin includes the IETF MIBs. If you require other MIBs, you need to import them. See [Importing MIBs](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-import-mibs).

### `oid_root_skip` [v1.0.0-plugins-inputs-snmp-oid_root_skip]

The `oid_root_skip` option specifies the number of OID root digits to ignore in event field name. For example, in a numeric OID like "1.3.6.1.2.1.1.1.0" the first 5 digits could be ignored by setting `oid_root_skip => 5` which would result in a field name "1.1.1.0". Similarly when a MIB is used an OID such "1.3.6.1.2.mib-2.system.sysDescr.0" would become "mib-2.system.sysDescr.0"

* Value type is [number](/lsr/value-types.md#number)
* Default value is `0`

### `walk` [v1.0.0-plugins-inputs-snmp-walk]

Use the `walk` option to retrieve the subtree of information for the given OID(s). One or more OID(s) are specified as an array of strings of OID(s).

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting

Queries the subtree of information starting at the given OID(s).

Example

```
  snmp {
    walk => ["1.3.6.1.2.1.1"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public"}]
  }
}
```

## SNMPv3 Authentication Options [_snmpv3_authentication_options_45]

A **single user** can be configured and will be used for all defined SNMPv3 hosts. Multiple snmp input declarations will be needed if multiple SNMPv3 users are required. These options are required only if you are using SNMPv3.

### `auth_pass` [v1.0.0-plugins-inputs-snmp-auth_pass]

The `auth_pass` option specifies the SNMPv3 authentication passphrase or password

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting

### `auth_protocol` [v1.0.0-plugins-inputs-snmp-auth_protocol]

The `auth_protocol` option specifies the SNMPv3 authentication protocol or type

* Value can be any of: `md5`, `sha`, `sha2`, `hmac128sha224`, `hmac192sha256`, `hmac256sha384`, `hmac384sha512`
* There is no default value for this setting

### `priv_pass` [v1.0.0-plugins-inputs-snmp-priv_pass]

The `priv_pass` option specifies the SNMPv3 encryption password

* Value type is [password](/lsr/value-types.md#password)
* There is no default value for this setting

### `priv_protocol` [v1.0.0-plugins-inputs-snmp-priv_protocol]

The `priv_protocol` option specifies the SNMPv3 privacy/encryption protocol

* Value can be any of: `des`, `3des`, `aes`, `aes128`, `aes192`, `aes256`
* There is no default value for this setting

### `security_name` [v1.0.0-plugins-inputs-snmp-security_name]

The `security_name` option specifies the SNMPv3 security name or user name

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting

### `security_level` [v1.0.0-plugins-inputs-snmp-security_level]

The `security_level` option specifies the SNMPv3 security level between Authentication, No Privacy; Authentication, Privacy; or no Authentication, no Privacy

* Value can be any of: `noAuthNoPriv`, `authNoPriv`, `authPriv`
* There is no default value for this setting

## More configuration examples [_more_configuration_examples_12]

**Using both `get` and `walk` in the same poll cycle for each host(s)**

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.3.0", "1.3.6.1.2.1.1.5.0"]
    walk => ["1.3.6.1.2.1.1"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public"}]
  }
}
```

**Specifying all global options**

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0"]
    hosts => [{host => "udp:127.0.0.1/161"}]

    mib_paths => ["path/to/converted/mibfile.dic"]
    oid_root_skip => 0
    interval => 30
  }
}
```

## Polled host information [_polled_host_information_23]

All the polled host information is stored in the event `@metadata`:

* `[@metadata][host_protocol]` : `udp` or `tcp`
* `[@metadata][host_address]` : host address for example `127.0.0.1`
* `[@metadata][host_port]` : host port (for example `161`)
* `[@metadata][host_community]` : community string for example `public`

By default, a `host` field is added to the event with the `[@metadata][host_address]` value.

```
config :add_field, :validate => :hash, :default => { "host" => "%{[@metadata][host_address]}" }
```

You can customize the format and content of the `host` field by specifying an alternate `add_field`.

Example

```
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0"]
    hosts => [{host => "udp:127.0.0.1/161"}]

    add_field => {host => "%{[@metadata][host_protocol]}:%{[@metadata][host_address]}/%{[@metadata][host_port]},%{[@metadata][host_community]}"}
  }
}
```

## Common options [v1.0.0-plugins-inputs-snmp-common-options]

These configuration options are supported by all input plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`codec`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-codec) | [codec](/lsr/value-types.md#codec) | No |
| [`enable_metric`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-id) | [string](/lsr/value-types.md#string) | No |
| [`tags`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-tags) | [array](/lsr/value-types.md#array) | No |
| [`type`](v1-0-0-plugins-inputs-snmp.md#v1.0.0-plugins-inputs-snmp-type) | [string](/lsr/value-types.md#string) | No |

### `add_field` [v1.0.0-plugins-inputs-snmp-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

Add a field to an event

### `codec` [v1.0.0-plugins-inputs-snmp-codec]

* Value type is [codec](/lsr/value-types.md#codec)
* Default value is `"plain"`

The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

### `enable_metric` [v1.0.0-plugins-inputs-snmp-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.0.0-plugins-inputs-snmp-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 snmp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
input {
  snmp {
    id => "my_plugin_id"
  }
}
```

### `tags` [v1.0.0-plugins-inputs-snmp-tags]

* Value type is [array](/lsr/value-types.md#array)
* There is no default value for this setting.

Add any number of arbitrary tags to your event.

This can help with processing later.

### `type` [v1.0.0-plugins-inputs-snmp-type]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a `type` field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.
