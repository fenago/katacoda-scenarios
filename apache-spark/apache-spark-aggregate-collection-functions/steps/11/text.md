
**Step 6:** Let us now use the sort_array function to sort the collection in ascending or descending order.

```
val sorted = numDS.select($"numbers", sort_array($"numbers", false).as("sorted"))
```

The sort_array function takes the column on which we want to perform the sort on as first argument and boolean as second argument. We specify true if we want to sort in the ascending order or false, otherwise.

After running the show method, the following result is shown as in the screenshot.

```
sorted.show()
```
 
#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.collections"`{{execute}} 

Task is complete!

