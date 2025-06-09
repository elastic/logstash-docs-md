---
mapped_pages:
  - https://www.elastic.co/guide/en/logstash/current/input-plugins.html
---

# Input plugins [input-plugins]

An input plugin enables a specific source of events to be read by Logstash.

For a list of Elastic supported plugins, please consult the [Support Matrix](https://www.elastic.co/support/matrix#show_logstash_plugins).

|     |     |     |
| --- | --- | --- |
| Plugin | Description | Github repository |
| [azure_event_hubs](plugins-inputs-azure_event_hubs.md) | Receives events from Azure Event Hubs | [azure_event_hubs](https://github.com/logstash-plugins/logstash-input-azure_event_hubs) |
| [beats](plugins-inputs-beats.md) | Receives events from the Elastic Beats framework | [logstash-input-beats](https://github.com/logstash-plugins/logstash-input-beats) |
| [cloudwatch](plugins-inputs-cloudwatch.md) | Pulls events from the Amazon Web Services CloudWatch API | [logstash-input-cloudwatch](https://github.com/logstash-plugins/logstash-input-cloudwatch) |
| [couchdb_changes](plugins-inputs-couchdb_changes.md) | Streams events from CouchDB’s `_changes` URI | [logstash-input-couchdb_changes](https://github.com/logstash-plugins/logstash-input-couchdb_changes) |
| [dead_letter_queue](plugins-inputs-dead_letter_queue.md) | read events from Logstash’s dead letter queue | [logstash-input-dead_letter_queue](https://github.com/logstash-plugins/logstash-input-dead_letter_queue) |
| [elastic_agent](plugins-inputs-elastic_agent.md) | Receives events from the Elastic Agent framework | [logstash-input-beats](https://github.com/logstash-plugins/logstash-input-beats) (shared) |
| [elastic_serverless_forwarder](plugins-inputs-elastic_serverless_forwarder.md) | Accepts events from Elastic Serverless Forwarder | [logstash-input-elastic_serverless_forwarder](https://github.com/logstash-plugins/logstash-input-elastic_serverless_forwarder) |
| [elasticsearch](plugins-inputs-elasticsearch.md) | Reads query results from an Elasticsearch cluster | [logstash-input-elasticsearch](https://github.com/logstash-plugins/logstash-input-elasticsearch) |
| [exec](plugins-inputs-exec.md) | Captures the output of a shell command as an event | [logstash-input-exec](https://github.com/logstash-plugins/logstash-input-exec) |
| [file](plugins-inputs-file.md) | Streams events from files | [logstash-input-file](https://github.com/logstash-plugins/logstash-input-file) |
| [ganglia](plugins-inputs-ganglia.md) | Reads Ganglia packets over UDP | [logstash-input-ganglia](https://github.com/logstash-plugins/logstash-input-ganglia) |
| [gelf](plugins-inputs-gelf.md) | Reads GELF-format messages from Graylog2 as events | [logstash-input-gelf](https://github.com/logstash-plugins/logstash-input-gelf) |
| [generator](plugins-inputs-generator.md) | Generates random log events for test purposes | [logstash-input-generator](https://github.com/logstash-plugins/logstash-input-generator) |
| [github](plugins-inputs-github.md) | Reads events from a GitHub webhook | [logstash-input-github](https://github.com/logstash-plugins/logstash-input-github) |
| [google_cloud_storage](plugins-inputs-google_cloud_storage.md) | Extract events from files in a Google Cloud Storage bucket | [logstash-input-google_cloud_storage](https://github.com/logstash-plugins/logstash-input-google_cloud_storage) |
| [google_pubsub](plugins-inputs-google_pubsub.md) | Consume events from a Google Cloud PubSub service | [logstash-input-google_pubsub](https://github.com/logstash-plugins/logstash-input-google_pubsub) |
| [graphite](plugins-inputs-graphite.md) | Reads metrics from the `graphite` tool | [logstash-input-graphite](https://github.com/logstash-plugins/logstash-input-graphite) |
| [heartbeat](plugins-inputs-heartbeat.md) | Generates heartbeat events for testing | [logstash-input-heartbeat](https://github.com/logstash-plugins/logstash-input-heartbeat) |
| [http](plugins-inputs-http.md) | Receives events over HTTP or HTTPS | [logstash-input-http](https://github.com/logstash-plugins/logstash-input-http) |
| [http_poller](plugins-inputs-http_poller.md) | Decodes the output of an HTTP API into events | [logstash-input-http_poller](https://github.com/logstash-plugins/logstash-input-http_poller) |
| [imap](plugins-inputs-imap.md) | Reads mail from an IMAP server | [logstash-input-imap](https://github.com/logstash-plugins/logstash-input-imap) |
| [irc](plugins-inputs-irc.md) | Reads events from an IRC server | [logstash-input-irc](https://github.com/logstash-plugins/logstash-input-irc) |
| [java_generator](plugins-inputs-java_generator.md) | Generates synthetic log events | [core plugin](https://github.com/elastic/logstash/blob/master/logstash-core/src/main/java/org/logstash/plugins/inputs/Generator.java) |
| [java_stdin](plugins-inputs-java_stdin.md) | Reads events from standard input | [core plugin](https://github.com/elastic/logstash/blob/master/logstash-core/src/main/java/org/logstash/plugins/inputs/Stdin.java) |
| [jdbc](plugins-inputs-jdbc.md) | Creates events from JDBC data | [logstash-integration-jdbc](https://github.com/logstash-plugins/logstash-integration-jdbc) |
| [jms](plugins-inputs-jms.md) | Reads events from a Jms Broker | [logstash-input-jms](https://github.com/logstash-plugins/logstash-input-jms) |
| [jmx](plugins-inputs-jmx.md) | Retrieves metrics from remote Java applications over JMX | [logstash-input-jmx](https://github.com/logstash-plugins/logstash-input-jmx) |
| [kafka](plugins-inputs-kafka.md) | Reads events from a Kafka topic | [logstash-integration-kafka](https://github.com/logstash-plugins/logstash-integration-kafka) |
| [kinesis](plugins-inputs-kinesis.md) | Receives events through an AWS Kinesis stream | [logstash-input-kinesis](https://github.com/logstash-plugins/logstash-input-kinesis) |
| [logstash](plugins-inputs-logstash.md) | Reads from Logstash output of another Logstash instance | [logstash-integration-logstash](https://github.com/logstash-plugins/logstash-integration-logstash) |
| [log4j](plugins-inputs-log4j.md) | Reads events over a TCP socket from a Log4j `SocketAppender` object | [logstash-input-log4j](https://github.com/logstash-plugins/logstash-input-log4j) |
| [lumberjack](plugins-inputs-lumberjack.md) | Receives events using the Lumberjack protocol | [logstash-input-lumberjack](https://github.com/logstash-plugins/logstash-input-lumberjack) |
| [meetup](plugins-inputs-meetup.md) | Captures the output of command line tools as an event | [logstash-input-meetup](https://github.com/logstash-plugins/logstash-input-meetup) |
| [pipe](plugins-inputs-pipe.md) | Streams events from a long-running command pipe | [logstash-input-pipe](https://github.com/logstash-plugins/logstash-input-pipe) |
| [puppet_facter](plugins-inputs-puppet_facter.md) | Receives facts from a Puppet server | [logstash-input-puppet_facter](https://github.com/logstash-plugins/logstash-input-puppet_facter) |
| [rabbitmq](plugins-inputs-rabbitmq.md) | Pulls events from a RabbitMQ exchange | [logstash-integration-rabbitmq](https://github.com/logstash-plugins/logstash-integration-rabbitmq) |
| [redis](plugins-inputs-redis.md) | Reads events from a Redis instance | [logstash-input-redis](https://github.com/logstash-plugins/logstash-input-redis) |
| [relp](plugins-inputs-relp.md) | Receives RELP events over a TCP socket | [logstash-input-relp](https://github.com/logstash-plugins/logstash-input-relp) |
| [rss](plugins-inputs-rss.md) | Captures the output of command line tools as an event | [logstash-input-rss](https://github.com/logstash-plugins/logstash-input-rss) |
| [s3](plugins-inputs-s3.md) | Streams events from files in a S3 bucket | [logstash-input-s3](https://github.com/logstash-plugins/logstash-input-s3) |
| [s3-sns-sqs](plugins-inputs-s3-sns-sqs.md) | Reads logs from AWS S3 buckets using sqs | [logstash-input-s3-sns-sqs](https://github.com/cherweg/logstash-input-s3-sns-sqs) |
| [salesforce](plugins-inputs-salesforce.md) | Creates events based on a Salesforce SOQL query | [logstash-input-salesforce](https://github.com/logstash-plugins/logstash-input-salesforce) |
| [snmp](plugins-inputs-snmp.md) | Polls network devices using Simple Network Management Protocol (SNMP) | [logstash-integration-snmp](https://github.com/logstash-plugins/logstash-integration-snmp) |
| [snmptrap](plugins-inputs-snmptrap.md) | Creates events based on SNMP trap messages | [logstash-integration-snmp](https://github.com/logstash-plugins/logstash-integration-snmp) |
| [sqlite](plugins-inputs-sqlite.md) | Creates events based on rows in an SQLite database | [logstash-input-sqlite](https://github.com/logstash-plugins/logstash-input-sqlite) |
| [sqs](plugins-inputs-sqs.md) | Pulls events from an Amazon Web Services Simple Queue Service queue | [logstash-input-sqs](https://github.com/logstash-plugins/logstash-input-sqs) |
| [stdin](plugins-inputs-stdin.md) | Reads events from standard input | [logstash-input-stdin](https://github.com/logstash-plugins/logstash-input-stdin) |
| [stomp](plugins-inputs-stomp.md) | Creates events received with the STOMP protocol | [logstash-input-stomp](https://github.com/logstash-plugins/logstash-input-stomp) |
| [syslog](plugins-inputs-syslog.md) | Reads syslog messages as events | [logstash-input-syslog](https://github.com/logstash-plugins/logstash-input-syslog) |
| [tcp](plugins-inputs-tcp.md) | Reads events from a TCP socket | [logstash-input-tcp](https://github.com/logstash-plugins/logstash-input-tcp) |
| [twitter](plugins-inputs-twitter.md) | Reads events from the Twitter Streaming API | [logstash-input-twitter](https://github.com/logstash-plugins/logstash-input-twitter) |
| [udp](plugins-inputs-udp.md) | Reads events over UDP | [logstash-input-udp](https://github.com/logstash-plugins/logstash-input-udp) |
| [unix](plugins-inputs-unix.md) | Reads events over a UNIX socket | [logstash-input-unix](https://github.com/logstash-plugins/logstash-input-unix) |
| [varnishlog](plugins-inputs-varnishlog.md) | Reads from the `varnish` cache shared memory log | [logstash-input-varnishlog](https://github.com/logstash-plugins/logstash-input-varnishlog) |
| [websocket](plugins-inputs-websocket.md) | Reads events from a websocket | [logstash-input-websocket](https://github.com/logstash-plugins/logstash-input-websocket) |
| [wmi](plugins-inputs-wmi.md) | Creates events based on the results of a WMI query | [logstash-input-wmi](https://github.com/logstash-plugins/logstash-input-wmi) |
| [xmpp](plugins-inputs-xmpp.md) | Receives events over the XMPP/Jabber protocol | [logstash-input-xmpp](https://github.com/logstash-plugins/logstash-input-xmpp) |


























































