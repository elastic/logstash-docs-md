---
navigation_title: "v1.1.0"
mapped_pages:
  - https://www.elastic.co/guide/en/logstash-versioned-plugins/current/v1.1.0-plugins-filters-math.html
---

# Math filter plugin v1.1.0 [v1.1.0-plugins-filters-math]

* Plugin version: v1.1.0
* Released on: 2018-06-29
* [Changelog](https://github.com/logstash-plugins/logstash-filter-math/blob/v1.1.0/CHANGELOG.md)

For other versions, see the [overview list](filter-math-index.md).

To learn more about Logstash, see the [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html).

## Getting help [_getting_help_2098]

For questions about the plugin, open a topic in the [Discuss](http://discuss.elastic.co) forums. For bugs or feature requests, open an issue in [Github](https://github.com/logstash-plugins/logstash-filter-math). For the list of Elastic supported plugins, please consult the [Elastic Support Matrix](https://www.elastic.co/support/matrix#matrix_logstash_plugins).

## Description [_description_2076]

This filter performs simple arithmetic calculations on Numeric or Logstash Timestamp values taken from fields in an event.

The following example shows how multiple steps can be calculated. Imagine you have two fields that represent distances in kilometers and you need to add them together and multiply the result by 1000 to get total distance in meters.

```
filter {
  math {
    calculate => [
      [ "add", "[walk1_distance]", "[walk2_distance]", "MEM[0]" ], <1>
      [ "multiply", MEM[0], 1000, "[total_distance_m]" ] <2>
    ]
  }
}
```

1. This calculation adds the two field’s values together and stores the result in a memory register.

2. This calculation multiplies the value in the memory register with a literal numeric value.

Here’s a full example that takes outside and inside air temperatures in degrees Fahrenheit and calculates the difference in Celsius. The arithmetic equivalent is:

`delta_in_c = round( ((inside - 32) * 5 / 9) - ((outside - 32) * 5 / 9) )`

```
input {
  generator {
    message => '{"sensor":"temperature-1", "inside": 71.24, "outside": 61.7 }'
    count => 1
  }
}

filter {
  json {
    source => "message"
  }
  if "_jsonparsefailure" not in [tags]  {
    math {
      calculate => [
        [ "fdiv", 5, 9, "MEM[0]" ],
        [ "subtract", "[outside]", 32, "MEM[1]" ],
        [ "multiply", "MEM[1]", "MEM[0]", "MEM[1]" ],
        [ "subtract", "[inside]", 32, "MEM[2]" ],
        [ "multiply", "MEM[2]", "MEM[0]", "MEM[2]" ],
        [ "subtract", "MEM[2]", "MEM[1]", "MEM[3]" ],
        [ "round", "MEM[3]", 1, "[delta_in_c]" ]
      ]
    }
  }
}

output {
  stdout {
    codec => rubydebug
  }
}
```

The resulting event looks like this.

```
{
        "inside" => 71.24,
    "@timestamp" => 2018-06-23T13:25:22.298Z,
        "sensor" => "temperature-1",
    "delta_in_c" => 5.3,
       "message" => "{\"sensor\":\"temperature-1\", \"inside\": 71.24, \"outside\": 61.7 }",
      "@version" => "1",
      "sequence" => 0,
          "host" => "Elastics-MacBook-Pro.local",
       "outside" => 61.7
}
```

## Math Filter Configuration Options [v1.1.0-plugins-filters-math-options]

This plugin supports the following configuration options plus the [Common options](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-common-options) described later.

| Setting | Input type | Required |
| :- | :- | :- |
| [`calculate`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-calculate) | [array](/lsr/value-types.md#array) of [array](/lsr/value-types.md#array) | Yes |

Also see [Common options](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-common-options) for a list of options supported by all filter plugins.

### `calculate` [v1.1.0-plugins-filters-math-calculate]

* This is a required setting.
* Value type is [array](/lsr/value-types.md#array) of [array](/lsr/value-types.md#array)s
* There is no default value for this setting.

The calculation to be performed. As can be seen from the example above by using multiple inner arrays one can perform calculation with multiple steps or multiple distinct calculations on a single event.

Each inner array **must have 4 elements**

The first element must be the operator. Valid operators are:

| Operation | Representations |
| :- | :- |
| Add | *+*, *add*, *plus* |
| Subtract | *-*, *sub*, *subtract* |
| Multiply | *\**, *mpx*, *times*, *multiply* |
| Round | *round* |
| Power | *\*\**, *^*, *to the power of* |
| Divide | */*, *div*, *divide* |
| Modulo | *mod*, *modulo* |
| FloatDivide | *fdiv*, *float divide* |

You may use any of the representations to refer to an operator. For instance, long hand representation maybe more clear to read when you or a co-worker looks at your config some months later.

The second element is the left hand side operand. It can be a field, a literal or a memory register. If referring to a memory register, ensure that it has been set to a value in a previous calculation.

A literal can be a float or an integer. Exponent expressions, e.g. `10e+3` are not supported.

The third element is the right hand side operand. It can be a field, a literal or a memory register.

The fourth element is the "target". It is where the result is stored and can be a memory register or a field in your event. It cannot be a literal.

You will get a warning if the target of the last calculation is a memory register because the final result will not be added to the event.

### Valid Values [_valid_values_2]

For a calculation to continue, any operand taken from a field in the event must be `Numeric` or a `Logstash Timestamp` and not nil. Timestamps are converted to floating point seconds since the UNIX epoch (Jan, 1 1970 00:00:00 UTC) before being operated on.

### Operators [_operators_2]

The operators `Divide`, `FloatDivide` and `Modulo` have a divide by zero check before the operation is executed.\
The `Power` operator has a check for a negative number being raised to a fractional power as this results in a Complex number that can’t be stored in an event or serialized to JSON.\
The `Round` operator can convert integers to floats `round(42, 1) -> 42.0` and floats to integers (rounding up or down) `round(0.75, 0) -> 1`.

### Memory Registers [_memory_registers_2]

You can choose not to use memory registers and store intermediate results in fields instead but then you may need to remove the fields later.\
Memory registers are implemented as a sparse array and the integer between the square brackets is a zero based direct index into the array. For example, `MEM[5]`, 5 is a reference to the 6th element in the array. The array is cleared for each event, this means that you can’t leave a value behind for a later event to use. Each math filter will have its own memory register array so you can’t share values between math filters in the same pipeline or across pipelines.

Use the bracketed notation e.g. `[fieldname]` to better distinguish fields from memory register references.

### Debugging [_debugging_2]

There is some logging of the calculation progress at the debug logging level.\
This is an excerpt from the full example at the top of this page:

```
[DEBUG][logstash.filters.math    ] executing {"function"=>"float_divide", "left_field"=>"operand 1: 5", "right_field"=>"operand 2: 9", "target"=>"register 0: 'MEM[0]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"float_divide", "target"=>"register 0: 'MEM[0]'", "result"=>0.5555555555555556}
[DEBUG][logstash.filters.math    ] executing {"function"=>"subtract", "left_field"=>"event operand 1: '[outside]'", "right_field"=>"operand 2: 32", "target"=>"register 1: 'MEM[1]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"subtract", "target"=>"register 1: 'MEM[1]'", "result"=>#<BigDecimal:2c16adee,'0.297E2',3(4)>}
[DEBUG][logstash.filters.math    ] executing {"function"=>"multiply", "left_field"=>"register operand 1: 'MEM[1]'", "right_field"=>"register operand 2: 'MEM[0]'", "target"=>"register 1: 'MEM[1]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"multiply", "target"=>"register 1: 'MEM[1]'", "result"=>#<BigDecimal:76bc6a4c,'0.1650000000000000132E2',19(20)>}
[DEBUG][logstash.filters.math    ] executing {"function"=>"subtract", "left_field"=>"event operand 1: '[inside]'", "right_field"=>"operand 2: 32", "target"=>"register 2: 'MEM[2]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"subtract", "target"=>"register 2: 'MEM[2]'", "result"=>#<BigDecimal:6761cedc,'0.3924E2',4(8)>}
[DEBUG][logstash.filters.math    ] executing {"function"=>"multiply", "left_field"=>"register operand 1: 'MEM[2]'", "right_field"=>"register operand 2: 'MEM[0]'", "target"=>"register 2: 'MEM[2]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"multiply", "target"=>"register 2: 'MEM[2]'", "result"=>#<BigDecimal:5b03b20a,'0.21800000000000001744E2',20(24)>}
[DEBUG][logstash.filters.math    ] executing {"function"=>"subtract", "left_field"=>"register operand 1: 'MEM[2]'", "right_field"=>"register operand 2: 'MEM[1]'", "target"=>"register 3: 'MEM[3]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"subtract", "target"=>"register 3: 'MEM[3]'", "result"=>#<BigDecimal:2e0e043,'0.5300000000000000424E1',19(20)>}
[DEBUG][logstash.filters.math    ] executing {"function"=>"round", "left_field"=>"register operand 1: 'MEM[3]'", "right_field"=>"operand 2: 1", "target"=>"event result: '[delta_in_c]'"}
[DEBUG][logstash.filters.math    ] calculation result stored {"function"=>"round", "target"=>"event result: '[delta_in_c]'", "result"=>#<BigDecimal:5415cc0,'0.53E1',2(4)>}
```

## Common options [v1.1.0-plugins-filters-math-common-options]

These configuration options are supported by all filter plugins:

| Setting | Input type | Required |
| :- | :- | :- |
| [`add_field`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-add_field) | [hash](/lsr/value-types.md#hash) | No |
| [`add_tag`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-add_tag) | [array](/lsr/value-types.md#array) | No |
| [`enable_metric`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-enable_metric) | [boolean](/lsr/value-types.md#boolean) | No |
| [`id`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-id) | [string](/lsr/value-types.md#string) | No |
| [`periodic_flush`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-periodic_flush) | [boolean](/lsr/value-types.md#boolean) | No |
| [`remove_field`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-remove_field) | [array](/lsr/value-types.md#array) | No |
| [`remove_tag`](v1-1-0-plugins-filters-math.md#v1.1.0-plugins-filters-math-remove_tag) | [array](/lsr/value-types.md#array) | No |

### `add_field` [v1.1.0-plugins-filters-math-add_field]

* Value type is [hash](/lsr/value-types.md#hash)
* Default value is `{}`

If this filter is successful, add any arbitrary fields to this event. Field names can be dynamic and include parts of the event using the `%{field}`.

Example:

```
    filter {
      math {
        add_field => { "foo_%{somefield}" => "Hello world, from %{host}" }
      }
    }
```

```
    # You can also add multiple fields at once:
    filter {
      math {
        add_field => {
          "foo_%{somefield}" => "Hello world, from %{host}"
          "new_field" => "new_static_value"
        }
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add field `foo_hello` if it is present, with the value above and the `%{host}` piece replaced with that value from the event. The second example would also add a hardcoded field.

### `add_tag` [v1.1.0-plugins-filters-math-add_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, add arbitrary tags to the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      math {
        add_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also add multiple tags at once:
    filter {
      math {
        add_tag => [ "foo_%{somefield}", "taggedy_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would add a tag `foo_hello` (and the second example would of course add a `taggedy_tag` tag).

### `enable_metric` [v1.1.0-plugins-filters-math-enable_metric]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `true`

Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

### `id` [v1.1.0-plugins-filters-math-id]

* Value type is [string](/lsr/value-types.md#string)
* There is no default value for this setting.

Add a unique `ID` to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 math filters. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```
    filter {
      math {
        id => "ABC"
      }
    }
```

### `periodic_flush` [v1.1.0-plugins-filters-math-periodic_flush]

* Value type is [boolean](/lsr/value-types.md#boolean)
* Default value is `false`

Call the filter flush method at regular interval. Optional.

### `remove_field` [v1.1.0-plugins-filters-math-remove_field]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary fields from this event. Fields names can be dynamic and include parts of the event using the %{field} Example:

```
    filter {
      math {
        remove_field => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple fields at once:
    filter {
      math {
        remove_field => [ "foo_%{somefield}", "my_extraneous_field" ]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the field with name `foo_hello` if it is present. The second example would remove an additional, non-dynamic field.

### `remove_tag` [v1.1.0-plugins-filters-math-remove_tag]

* Value type is [array](/lsr/value-types.md#array)
* Default value is `[]`

If this filter is successful, remove arbitrary tags from the event. Tags can be dynamic and include parts of the event using the `%{field}` syntax.

Example:

```
    filter {
      math {
        remove_tag => [ "foo_%{somefield}" ]
      }
    }
```

```
    # You can also remove multiple tags at once:
    filter {
      math {
        remove_tag => [ "foo_%{somefield}", "sad_unwanted_tag"]
      }
    }
```

If the event has field `"somefield" == "hello"` this filter, on success, would remove the tag `foo_hello` if it is present. The second example would remove a sad, unwanted tag as well.
