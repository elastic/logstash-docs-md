---
navigation_title: "v0.0.1"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v0.0.1-plugins-filters-elastic_integration.html
---

# Elastic Integration filter plugin v0.0.1 [v0.0.1-plugins-filters-elastic_integration]


* Plugin version: v0.0.1
* Released on: 2023-04-14
* [Changelog](https://github.com/elastic/logstash-filter-elastic_integration/blob/v0.0.1/CHANGELOG.md)

For other versions, see the [overview list](filter-elastic_integration-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_1808]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/elastic/logstash-filter-elastic_integration). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

::::{admonition} Elastic Enterprise License
Use of this plugin requires an active Enterprise Elastic License.

::::



## Description [_description_1786]

Using this filter you can process Elastic integrations powered by {{es}} Ingest Node in Logstash.

Once configured to point to an {{es}} cluster, events processed by this filter will first resolve their effective data-stream, and determine from {{es}} which ingest pipeline to run. The ingest pipeline will be run inside Logstash without transmitting the event to {{es}}. Events that are successfully handled by their ingest pipeline will have `[@metadata][target_ingest_pipeline]` set to `+_none+` so that any downstream {{es}} output in the Logstash pipeline will avoid running the event’s default pipeline *again* in {{es}}.

::::{note}
Some multi-pipeline configurations such as logstash-to-logstash over http(s) do not maintain the state of `[@metadata]` fields. In these setups, you may need to explicitly configure your downstream pipeline’s {{es}} output with `+pipeline => "_none"+` to avoid re-running the default pipeline.
::::


Events that *fail* ingest pipeline processing will be tagged with `_ingest_pipeline_failure`, and their `[@metadata][_ingest_pipeline_failure]` will be populated with details as a key/value map.

::::{important}
This plugin requires minimum Java 17 and Logstash 8.7.0 versions.
::::


::::{admonition} Technology Preview
This Elastic Integration filter plugin is part of a *Technology Preview*, which means that both configuration options and implementation details are subject to change in minor releases without being preceded by deprecation warnings.

Before upgrading this plugin or Logstash itself, please pay special attention to the changelogs to avoid being caught by surprise.

::::



## Minimum Configuration [v0.0.1-plugins-filters-elastic_integration-minimum_configuration]

You will need to configure this plugin to connect to {{es}}, and may need to also need to provide local GeoIp databases.

```shell
filter {
  elastic_integration {
    cloud_id   => "YOUR_CLOUD_ID_HERE"
    cloud_auth => "YOUR_CLOUD_AUTH_HERE"
    geoip_database_directory => "/etc/your/geoip-databases"
  }
}
```

Read on for a guide to configuration, or jump to the [complete list of configuration options](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-options).


## Connecting to {{es}} [v0.0.1-plugins-filters-elastic_integration-connecting_to_elasticsearch]

This plugin communicates with {{es}} to identify which ingest pipeline should be run for a given event, and to retrieve the ingest pipeline definitions themselves. You must configure this plugin to point to {{es}} using exactly one of:

* A Cloud Id (see [`cloud_id`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-cloud_id))
* A list of one or more host URLs (see [`hosts`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-hosts))

Communication will be made securely over SSL unless you explicitly configure this plugin otherwise.

You may need to configure how this plugin establishes trust of the server that responds, and will likely need to configure how this plugin presents its own identity or credentials.

### SSL Trust Configuration [_ssl_trust_configuration_24]

When communicating over SSL, this plugin fully-validates the proof-of-identity presented by {{es}} using the system trust store. You can provide an *alternate* source of trust with one of:

* A PEM-formatted list of trusted certificate authorities (see [`ssl_certificate_authorities`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate_authorities))
* A JKS- or PKCS12-formatted Keystore containing trusted certificates (see [`ssl_truststore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_path))

You can also configure which aspects of the proof-of-identity are verified (see [`ssl_verification_mode`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_verification_mode)).


### SSL Identity Configuration [_ssl_identity_configuration_24]

When communicating over SSL, you can also configure this plugin to present a certificate-based proof-of-identity to the {{es}} cluster it connects to using one of:

* A PKCS8 Certificate/Key pair (see [`ssl_certificate`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate))
* A JKS- or PKCS12-formatted Keystore (see [`ssl_keystore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_path))


### Request Identity [_request_identity_24]

You can configure this plugin to present authentication credentials to {{es}} in one of several ways:

* ApiKey: (see [`api_key`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-api_key))
* Cloud Auth: (see [`cloud_auth`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-cloud_auth))
* HTTP Basic Auth: (see [`auth_basic_username`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_username) and [`auth_basic_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_password))

::::{note}
Your request credentials are only as secure as the connection they are being passed over. They provide neither privacy nor secrecy on their own, and can easily be recovered by an adversary when SSL is disabled.
::::




## Supported Ingest Processors [v0.0.1-plugins-filters-elastic_integration-supported_ingest_processors]

This filter can run {{es}} Ingest Node pipelines that are *wholly* comprised of the supported subset of processors. It has access to the Painless and Mustache scripting engines where applicable:

| Source | Processor | Caveats |
| --- | --- | --- |
| Ingest Common | `append` | *none* |
| `bytes` | *none* |
| `communityid` | *none* |
| `convert` | *none* |
| `csv` | *none* |
| `date` | *none* |
| `dateindexname` | *none* |
| `dissect` | *none* |
| `dotexpander` | *none* |
| `drop` | *none* |
| `fail` | *none* |
| `fingerprint` | *none* |
| `foreach` | *none* |
| `grok` | *none* |
| `gsub` | *none* |
| `htmlstrip` | *none* |
| `join` | *none* |
| `json` | *none* |
| `keyvalue` | *none* |
| `lowercase` | *none* |
| `networkdirection` | *none* |
| `pipeline` | resolved pipeline *must* be wholly-composed of supported processors |
| `redact` | *none* |
| `registereddomain` | *none* |
| `remove` | *none* |
| `rename` | *none* |
| `script` | *none* |
| `set` | *none* |
| `sort` | *none* |
| `split` | *none* |
| `trim` | *none* |
| `uppercase` | *none* |
| `uriparts` | *none* |
| `urldecode` | *none* |
| GeoIp | `geoip` | Requires local MaxMind GeoIp databases [`geoip_database_directory`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-geoip_database_directory) |

### Field Mappings [v0.0.1-plugins-filters-elastic_integration-field_mappings]

During execution, the Ingest pipeline works with a temporary mutable *view* of the Logstash event that re-shapes some {{ls}}-reserved fields into their expected IngestDocument field names and object-types. Changes to the IngestDocument will be reflected in the resulting Logstash Event, including safely mapping these reserved fields *back* from the IngestDocument reserved field to the {{ls}} reserved field counterpart.

| {{ls}} Field | IngestDocument Field | Conflict Handling |
| --- | --- | --- |
| `@timestamp` | `_ingest.timestamp` | when ingest processing *also* sets a top-level `@timestamp` field, it will be made available via the Event’s `_@timestamp` field |
| `@version` | `_version` | when ingest processing *also* sets a top-level `@version` field in the source, it will be made available via the Event’s `_@version` field |
| `@metadata` | `@metadata` | when ingest processing replaces the top-level `@metadata` map with an object that is not a string-object map, it will be made available via the Event’s `_@metadata` field. |
| `tags` | `tags` | when ingest processing produces a top-level `tags` field that is not a collection of strings, it will be made available via the event’s `_tags` field. |
| *everything else* | *in-place, as-structured* | only minimal type conversions are done |



## Elastic Integration Filter Configuration Options [v0.0.1-plugins-filters-elastic_integration-options]

This plugin supports the following configuration options plus the [Common options](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-common-options) described later.

| Setting | Input type | Required |
| --- | --- | --- |
| [`api_key`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-api_key) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`auth_basic_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`auth_basic_username`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_username) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`cloud_auth`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-cloud_auth) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`cloud_id`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-cloud_id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`hosts`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-hosts) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_certificate`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_certificate_authorities`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate_authorities) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`ssl_enabled`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_enabled) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`ssl_key`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_key) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_keystore_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_keystore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_key_passphrase`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_key_passphrase) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_truststore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_path) | [path](logstash://reference/configuration-file-structure.md#path) | No |
| [`ssl_truststore_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_password) | [password](logstash://reference/configuration-file-structure.md#password) | No |
| [`ssl_verification_mode`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_verification_mode) | [string](logstash://reference/configuration-file-structure.md#string), one of `["full", "certificate", "none"]` | No |

### `api_key` [v0.0.1-plugins-filters-elastic_integration-api_key]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

The encoded form of an API key that is used to authenticate this plugin to {es}


### `auth_basic_password` [v0.0.1-plugins-filters-elastic_integration-auth_basic_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when request auth is configured with [`auth_basic_username`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_username)

A password when using HTTP Basic Authentication to connect to {{es}}.


### `auth_basic_username` [v0.0.1-plugins-filters-elastic_integration-auth_basic_username]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.
* When present, [`auth_basic_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-auth_basic_password) is also required.

A user name when using HTTP Basic Authentication to connect to {{es}}.


### `cloud_auth` [v0.0.1-plugins-filters-elastic_integration-cloud_auth]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.

Cloud authentication string ("<username>:<password>" format) is an alternative for the `auth_basic_username`/`auth_basic_password` pair and can be obtained from Elastic Cloud web console.


### `cloud_id` [v0.0.1-plugins-filters-elastic_integration-cloud_id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.
* Cannot be combined with `[`ssl_enabled`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_enabled)⇒false`.

Cloud Id, from the Elastic Cloud web console.

When connecting with a Cloud Id, communication to {{es}} is secured with SSL.

For more details, check out the [Logstash-to-Cloud documentation](logstash://reference/connecting-to-cloud.md).


### `hosts` [v0.0.1-plugins-filters-elastic_integration-hosts]

* Value type is a list of [uri](logstash://reference/configuration-file-structure.md#uri)s
* There is no default value for this setting.
* Constraints:

    * When any URL contains a protocol component, all URLs must have the same protocol as each other.
    * `https`-protocol hosts use HTTPS and cannot be combined with [`+ssl_enabled => false+`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_enabled).
    * `http`-protocol hosts use unsecured HTTP and cannot be combined with [`+ssl_enabled => true+`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_enabled).
    * When any URL omits a port component, the default `9200` is used.
    * When any URL contains a path component, all URLs must have the same path as each other.


A non-empty list of {{es}} hosts to connect.

Examples:

```
`"127.0.0.1"`
`["127.0.0.1:9200","127.0.0.2:9200"]`
`["http://127.0.0.1"]`
`["https://127.0.0.1:9200"]`
`["https://127.0.0.1:9200/subpath"]` (If using a proxy on a subpath)
```
When connecting with a list of hosts, communication to {{es}} is secured with SSL unless configured otherwise.

::::{admonition} Disabling SSL is dangerous
:class: warning

The security of this plugin relies on SSL to avoid leaking credentials and to avoid running illegitimate ingest pipeline definitions.

There are two ways to disable SSL:

* Provide a list of `http`-protocol hosts
* Set [`+ssl_enabled => false+`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_enabled)

::::



### `ssl_certificate` [v0.0.1-plugins-filters-elastic_integration-ssl_certificate]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_key`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_key) and [`ssl_key_passphrase`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_key_passphrase) are also required.
* Cannot be combined with configurations that disable SSL

Path to a PEM-encoded certificate or certificate chain with which to identify this plugin to {{es}}.


### `ssl_certificate_authorities` [v0.0.1-plugins-filters-elastic_integration-ssl_certificate_authorities]

* Value type is a list of [path](logstash://reference/configuration-file-structure.md#path)s
* There is no default value for this setting.
* Cannot be combined with configurations that disable SSL
* Cannot be combined with `[`ssl_verification_mode`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_verification_mode)⇒none`.

One or more PEM-formatted files defining certificate authorities.

This setting can be used to *override* the system trust store for verifying the SSL certificate presented by {{es}}.


### `ssl_enabled` [v0.0.1-plugins-filters-elastic_integration-ssl_enabled]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* There is no default value for this setting.

Secure SSL communication to {{es}} is enabled unless:

* it is explicitly disabled with `+ssl_enabled => false+`; OR
* it is implicitly disabled by providing `http`-protocol [`hosts`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-hosts).

Specifying `+ssl_enabled => true+` can be a helpful redundant safeguard to ensure this plugin cannot be configured to use non-ssl communication.


### `ssl_key` [v0.0.1-plugins-filters-elastic_integration-ssl_key]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate)
* Cannot be combined with configurations that disable SSL

A path to a PKCS8-formatted SSL certificate key.


### `ssl_keystore_password` [v0.0.1-plugins-filters-elastic_integration-ssl_keystore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_keystore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_path)
* Cannot be combined with configurations that disable SSL

Password for the [`ssl_keystore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_path)


### `ssl_keystore_path` [v0.0.1-plugins-filters-elastic_integration-ssl_keystore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_keystore_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_keystore_password) is also required.
* Cannot be combined with configurations that disable SSL

A path to a JKS- or PKCS12-formatted keystore with which to identify this plugin to {{es}}.


### `ssl_key_passphrase` [v0.0.1-plugins-filters-elastic_integration-ssl_key_passphrase]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection identity is configured with [`ssl_certificate`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_certificate)
* Cannot be combined with configurations that disable SSL

A password or passphrase of the [`ssl_key`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_key).


### `ssl_truststore_path` [v0.0.1-plugins-filters-elastic_integration-ssl_truststore_path]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.
* When present, [`ssl_truststore_password`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_password) is required.
* Cannot be combined with configurations that disable SSL
* Cannot be combined with `[`ssl_verification_mode`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_verification_mode)⇒none`.

A path to JKS- or PKCS12-formatted keystore where trusted certificates are located.

This setting can be used to *override* the system trust store for verifying the SSL certificate presented by {{es}}.


### `ssl_truststore_password` [v0.0.1-plugins-filters-elastic_integration-ssl_truststore_password]

* Value type is [password](logstash://reference/configuration-file-structure.md#password)
* There is no default value for this setting.
* Required when connection trust is configured with [`ssl_truststore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_path)
* Cannot be combined with configurations that disable SSL

Password for the [`ssl_truststore_path`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-ssl_truststore_path).


### `ssl_verification_mode` [v0.0.1-plugins-filters-elastic_integration-ssl_verification_mode]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.
* Cannot be combined with configurations that disable SSL

Level of verification of the certificate provided by {{es}}.

SSL certificates presented by {{es}} are fully-validated by default.

* Available modes:

    * `none`: performs no validation, implicitly trusting any server that this plugin connects to (insecure)
    * `certificate`: validates the server-provided certificate is signed by a trusted certificate authority and that the server can prove possession of its associated private key (less secure)
    * `full` (default): performs the same validations as `certificate` and also verifies that the provided certificate has an identity claim matching the server we are attempting to connect to (most secure)



### `geoip_database_directory` [v0.0.1-plugins-filters-elastic_integration-geoip_database_directory]

* Value type is [path](logstash://reference/configuration-file-structure.md#path)
* There is no default value for this setting.

When using the GeoIp processor, this plugin does *not* have access to the GeoIp databases that are a part of the {{es}} cluster, and must be configured with locally-available database files.

Databases are registered by file name, and most integrations rely on databases being present named:

* `GeoLite2-ASN.mmdb`
* `GeoLite2-City.mmdb`
* `GeoLite2-Country.mmdb`

This plugin will discover any regular file with the `.mmdb` suffix in the provided directory, and expects the files it finds to be in the MaxMind DB format.

 



## Common options [v0.0.1-plugins-filters-elastic_integration-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| --- | --- | --- |
| [`add_field`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-add_field) | [hash](logstash://reference/configuration-file-structure.md#hash) | No |
| [`add_tag`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-add_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`enable_metric`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-enable_metric) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`id`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-id) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`periodic_flush`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-periodic_flush) | [boolean](logstash://reference/configuration-file-structure.md#boolean) | No |
| [`remove_field`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-remove_field) | [array](logstash://reference/configuration-file-structure.md#array) | No |
| [`remove_tag`](v0-0-1-plugins-filters-elastic_integration.md#v0.0.1-plugins-filters-elastic_integration-remove_tag) | [array](logstash://reference/configuration-file-structure.md#array) | No |

### `add_field` [v0.0.1-plugins-filters-elastic_integration-add_field]

* Value type is [hash](logstash://reference/configuration-file-structure.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{{field}}`.

Example:

```json
    filter {
      elastic_integration {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```json
    # You can also add multiple fields at once:
    filter {
      elastic_integration {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{{host}}` piece replaced with that value from the event. The second example would also add a hardcoded field.


### `add_tag` [v0.0.1-plugins-filters-elastic_integration-add_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      elastic_integration {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also add multiple tags at once:
    filter {
      elastic_integration {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).


### `enable_metric` [v0.0.1-plugins-filters-elastic_integration-enable_metric]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.


### `id` [v0.0.1-plugins-filters-elastic_integration-id]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 elastic_integration filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```json
    filter {
      elastic_integration {
        id => "ABC"
      }
    }
```


### `periodic_flush` [v0.0.1-plugins-filters-elastic_integration-periodic_flush]

* Value type is [boolean](logstash://reference/configuration-file-structure.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.


### `remove_field` [v0.0.1-plugins-filters-elastic_integration-remove_field]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the `%{{field}}` Example:

```json
    filter {
      elastic_integration {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple fields at once:
    filter {
      elastic_integration {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.


### `remove_tag` [v0.0.1-plugins-filters-elastic_integration-remove_tag]

* Value type is [array](logstash://reference/configuration-file-structure.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{{field}}` syntax.

Example:

```json
    filter {
      elastic_integration {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```json
    # You can also remove multiple tags at once:
    filter {
      elastic_integration {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.



