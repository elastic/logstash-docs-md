---
navigation_title: "v3.0.7"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v3.0.7-plugins-codecs-line.html
---

# Line codec plugin v3.0.7 [v3.0.7-plugins-codecs-line]


* Plugin version: v3.0.7
* Released on: 2017-12-15
* [Changelog](https://github.com/logstash-plugins/logstash-codec-line/blob/v3.0.7/CHANGELOG.md)

For other versions, see the [overview list](codec-line-index.md).

To learn more about Logstash, see the [Logstash Reference](logstash://reference/index.md).

## Getting help [_getting_help_2335]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-codec-line). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).


## Description [_description_2313]

Line-oriented text data.

Decoding behavior: Only whole line events will be emitted.

Encoding behavior: Each event will be emitted with a trailing newline.


## Line Codec Configuration Options [v3.0.7-plugins-codecs-line-options]

| Setting | Input type | Required |
| --- | --- | --- |
| [`charset`](v3-0-7-plugins-codecs-line.md#v3.0.7-plugins-codecs-line-charset) | [string](logstash://reference/configuration-file-structure.md#string), one of `["ASCII-8BIT", "UTF-8", "US-ASCII", "Big5", "Big5-HKSCS", "Big5-UAO", "CP949", "Emacs-Mule", "EUC-JP", "EUC-KR", "EUC-TW", "GB2312", "GB18030", "GBK", "ISO-8859-1", "ISO-8859-2", "ISO-8859-3", "ISO-8859-4", "ISO-8859-5", "ISO-8859-6", "ISO-8859-7", "ISO-8859-8", "ISO-8859-9", "ISO-8859-10", "ISO-8859-11", "ISO-8859-13", "ISO-8859-14", "ISO-8859-15", "ISO-8859-16", "KOI8-R", "KOI8-U", "Shift_JIS", "UTF-16BE", "UTF-16LE", "UTF-32BE", "UTF-32LE", "Windows-31J", "Windows-1250", "Windows-1251", "Windows-1252", "IBM437", "IBM737", "IBM775", "CP850", "IBM852", "CP852", "IBM855", "CP855", "IBM857", "IBM860", "IBM861", "IBM862", "IBM863", "IBM864", "IBM865", "IBM866", "IBM869", "Windows-1258", "GB1988", "macCentEuro", "macCroatian", "macCyrillic", "macGreek", "macIceland", "macRoman", "macRomania", "macThai", "macTurkish", "macUkraine", "CP950", "CP951", "IBM037", "stateless-ISO-2022-JP", "eucJP-ms", "CP51932", "EUC-JIS-2004", "GB12345", "ISO-2022-JP", "ISO-2022-JP-2", "CP50220", "CP50221", "Windows-1256", "Windows-1253", "Windows-1255", "Windows-1254", "TIS-620", "Windows-874", "Windows-1257", "MacJapanese", "UTF-7", "UTF8-MAC", "UTF-16", "UTF-32", "UTF8-DoCoMo", "SJIS-DoCoMo", "UTF8-KDDI", "SJIS-KDDI", "ISO-2022-JP-KDDI", "stateless-ISO-2022-JP-KDDI", "UTF8-SoftBank", "SJIS-SoftBank", "BINARY", "CP437", "CP737", "CP775", "IBM850", "CP857", "CP860", "CP861", "CP862", "CP863", "CP864", "CP865", "CP866", "CP869", "CP1258", "Big5-HKSCS:2008", "ebcdic-cp-us", "eucJP", "euc-jp-ms", "EUC-JISX0213", "eucKR", "eucTW", "EUC-CN", "eucCN", "CP936", "ISO2022-JP", "ISO2022-JP2", "ISO8859-1", "ISO8859-2", "ISO8859-3", "ISO8859-4", "ISO8859-5", "ISO8859-6", "CP1256", "ISO8859-7", "CP1253", "ISO8859-8", "CP1255", "ISO8859-9", "CP1254", "ISO8859-10", "ISO8859-11", "CP874", "ISO8859-13", "CP1257", "ISO8859-14", "ISO8859-15", "ISO8859-16", "CP878", "MacJapan", "ASCII", "ANSI_X3.4-1968", "646", "CP65000", "CP65001", "UTF-8-MAC", "UTF-8-HFS", "UCS-2BE", "UCS-4BE", "UCS-4LE", "CP932", "csWindows31J", "SJIS", "PCK", "CP1250", "CP1251", "CP1252", "external", "locale"]` | No |
| [`delimiter`](v3-0-7-plugins-codecs-line.md#v3.0.7-plugins-codecs-line-delimiter) | [string](logstash://reference/configuration-file-structure.md#string) | No |
| [`format`](v3-0-7-plugins-codecs-line.md#v3.0.7-plugins-codecs-line-format) | [string](logstash://reference/configuration-file-structure.md#string) | No |

 

### `charset` [v3.0.7-plugins-codecs-line-charset]

* Value can be any of: `ASCII-8BIT`, `UTF-8`, `US-ASCII`, `Big5`, `Big5-HKSCS`, `Big5-UAO`, `CP949`, `Emacs-Mule`, `EUC-JP`, `EUC-KR`, `EUC-TW`, `GB2312`, `GB18030`, `GBK`, `ISO-8859-1`, `ISO-8859-2`, `ISO-8859-3`, `ISO-8859-4`, `ISO-8859-5`, `ISO-8859-6`, `ISO-8859-7`, `ISO-8859-8`, `ISO-8859-9`, `ISO-8859-10`, `ISO-8859-11`, `ISO-8859-13`, `ISO-8859-14`, `ISO-8859-15`, `ISO-8859-16`, `KOI8-R`, `KOI8-U`, `Shift_JIS`, `UTF-16BE`, `UTF-16LE`, `UTF-32BE`, `UTF-32LE`, `Windows-31J`, `Windows-1250`, `Windows-1251`, `Windows-1252`, `IBM437`, `IBM737`, `IBM775`, `CP850`, `IBM852`, `CP852`, `IBM855`, `CP855`, `IBM857`, `IBM860`, `IBM861`, `IBM862`, `IBM863`, `IBM864`, `IBM865`, `IBM866`, `IBM869`, `Windows-1258`, `GB1988`, `macCentEuro`, `macCroatian`, `macCyrillic`, `macGreek`, `macIceland`, `macRoman`, `macRomania`, `macThai`, `macTurkish`, `macUkraine`, `CP950`, `CP951`, `IBM037`, `stateless-ISO-2022-JP`, `eucJP-ms`, `CP51932`, `EUC-JIS-2004`, `GB12345`, `ISO-2022-JP`, `ISO-2022-JP-2`, `CP50220`, `CP50221`, `Windows-1256`, `Windows-1253`, `Windows-1255`, `Windows-1254`, `TIS-620`, `Windows-874`, `Windows-1257`, `MacJapanese`, `UTF-7`, `UTF8-MAC`, `UTF-16`, `UTF-32`, `UTF8-DoCoMo`, `SJIS-DoCoMo`, `UTF8-KDDI`, `SJIS-KDDI`, `ISO-2022-JP-KDDI`, `stateless-ISO-2022-JP-KDDI`, `UTF8-SoftBank`, `SJIS-SoftBank`, `BINARY`, `CP437`, `CP737`, `CP775`, `IBM850`, `CP857`, `CP860`, `CP861`, `CP862`, `CP863`, `CP864`, `CP865`, `CP866`, `CP869`, `CP1258`, `Big5-HKSCS:2008`, `ebcdic-cp-us`, `eucJP`, `euc-jp-ms`, `EUC-JISX0213`, `eucKR`, `eucTW`, `EUC-CN`, `eucCN`, `CP936`, `ISO2022-JP`, `ISO2022-JP2`, `ISO8859-1`, `ISO8859-2`, `ISO8859-3`, `ISO8859-4`, `ISO8859-5`, `ISO8859-6`, `CP1256`, `ISO8859-7`, `CP1253`, `ISO8859-8`, `CP1255`, `ISO8859-9`, `CP1254`, `ISO8859-10`, `ISO8859-11`, `CP874`, `ISO8859-13`, `CP1257`, `ISO8859-14`, `ISO8859-15`, `ISO8859-16`, `CP878`, `MacJapan`, `ASCII`, `ANSI_X3.4-1968`, `646`, `CP65000`, `CP65001`, `UTF-8-MAC`, `UTF-8-HFS`, `UCS-2BE`, `UCS-4BE`, `UCS-4LE`, `CP932`, `csWindows31J`, `SJIS`, `PCK`, `CP1250`, `CP1251`, `CP1252`, `external`, `locale`
* Default value is `"UTF-8"`

The character encoding used in this input. Examples include `UTF-8` and `cp1252`

This setting is useful if your log files are in `Latin-1` (aka `cp1252`) or in another character set other than `UTF-8`.

This only affects "plain" format logs since json is `UTF-8` already.


### `delimiter` [v3.0.7-plugins-codecs-line-delimiter]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* Default value is `"\n"`

Change the delimiter that separates lines


### `format` [v3.0.7-plugins-codecs-line-format]

* Value type is [string](logstash://reference/configuration-file-structure.md#string)
* There is no default value for this setting.

Set the desired text format for encoding.



