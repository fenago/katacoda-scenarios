
**Step 5:** Let us now specify the data type of return value using the dataType method. Since the average which returns is of type Double, we specify the DoubleType as shown below.

```
def dataType: DataType = DoubleType
```

**Step 6:** Next, we need to specify if the function always returns the same output on identical input using deterministic method. This is true  by default.

```
def deterministic: Boolean = true
```

The program at this point should look like the screenshot shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_022.png)