The user defined aggregate functions (UDAF) can be classified into two types. 

- Typed user defined aggregate function
- Untyped user defined aggregate function


The Typed user defined aggregate function is applied to Datasets where we get the structure (schema) of rows using the case class, while the Untyped user defined aggregate function is applied to DataFrames.

Please use the built-in functions over UDFs whenever you can. The built-in functions are an efficient way to perform operations. UDFs should only be used when they are absolutely required.
