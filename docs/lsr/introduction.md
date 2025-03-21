# Logstash Plugins [introduction]

Some sort of intro goes here.


## String [string] 

A string must be a single character sequence. Note that string values are enclosed in quotes, either double or single.


## Array [array] 

This type is now mostly deprecated in favor of using a standard type like `string` with the plugin defining the `:list => true` property for better type checking. It is still needed to handle lists of hashes or mixed types where type checking is not desired.


## Number [number] 

Numbers must be valid numeric values (floating point or integer).


## Boolean [boolean] 

A boolean must be either `true` or `false`. Note that the `true` and `false` keywords are not enclosed in quotes.


## Password [password] 

A password is a string with a single value that is not logged or printed.


## Path [path] 

A path is a string that represents a valid operating system path.


## Hash [hash] 

A hash is a collection of key value pairs specified in the format `"field1" => "value1"`. Note that multiple key value entries are separated by spaces rather than commas.


## URI [uri] 

A URI can be anything from a full URL like *http://elastic.co/* to a simple identifier like *foobar*. If the URI contains a password such as *http://user:pass@example.net* the password portion of the URI will not be logged or printed.


## Bytes [bytes] 

A bytes field is a string field that represents a valid unit of bytes. It is a convenient way to declare specific sizes in your plugin options. Both SI (k M G T P E Z Y) and Binary (Ki Mi Gi Ti Pi Ei Zi Yi) units are supported. Binary units are in base-1024 and SI units are in base-1000. This field is case-insensitive and accepts space between the value and the unit. If no unit is specified, the integer string represents the number of bytes.


## CFR [logstash-config-field-references] 

words


## Event API [event-api] 

words

