

**Step 3:** Next, let us convert the collection to dataset using the toDS method and rename the column as numbers using the withColumnRenamed method. The default column name when you create a dataset is value. Hence we change the default column name to numbers.

```
val numDS = num.toDS().withColumnRenamed("value", "numbers").cache()
```

**Step 4:** now that we have our dataset, let us apply some of the collection functions. First, let us use the array_contains function to check if the collection contains the element we require.

```
val contains = numDS.where(array_contains($"numbers", 5))
```

We use the array_contains function inside the where method to check if the column numbers contains the number 5. This function takes the column name as the first argument and the element as second. We can also pass more than one element as second argument enclosed in a collection as shown in the example below.

```
val eg = numDS.where(array_contains($"numbers", Array(7,8))
```

Let us check the result using the show method.

```
contains.show()
```

The result is as shown in the screenshot below. Since we used the where method, we are only shown the collection which contains the number 5.

 
