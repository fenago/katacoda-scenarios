
**Step 5:** Let us now use size function to check the size of each of the collections in our datasets. The size function simply returns the size of the collection similar to the length method.

```
val sizeDS = numDS.select($"numbers", size($"numbers").as("size"))
```

We have used the select method to select the numbers column as first column and size function on numbers column as second column. We have then used the as method to rename the column as size.

After running the show method, the following result is shown as in the screenshot.

```
sizeDS.show()
```

The size is shown as 3 since there are 3 elements in each collection.
