Function currying in Scala is used to create partially applied functions. The curried functions are declared with multiple parameter groups with each group enclosed in paranthesis.

For example,

```
def sum(a: Int) (b:Int): Int = {
> a + b
> }
```

There can also be multiple parameters in each parameter group. We can then use this curried function and create partially applied functions.

