---
navigation_title: "Logstash Plugins"
mapped_pages:
---

# Logstash Plugins [introduction]

Logstash has a rich collection of input, filter, codec, and output plugins.
Check out the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins) to see which plugins are supported at various levels.

The plugins make up your Logstash pipeline.

* [**Integration plugins**](plugin-integrations.md) combine related plugins—inputs, outputs, and sometimes filters and codecs—into one package.

* [**Input plugins**](input-plugins.md) enable a specific source of events to be read by Logstash.

* [**Filter plugins**](filter-plugins.md) perform intermediary processing on an event. Filters are often applied conditionally depending on the characteristics of the event.

* [**Codec plugins**](codec-plugins.md) change the data representation of an event.
Codecs are essentially stream filters that can operate as part of an input or output.

* [**Output plugins**](output-plugins.md) send event data to a particular destination.
Outputs are the final stage in the Logstash event pipeline.


