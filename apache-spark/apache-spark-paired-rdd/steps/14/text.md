You can also sort the result by the key by referring the first element in the sortBy function or simply using the sortByKey function key as shown below.

```
val sorted = avgRatings.sortByKey()
```


**Step 6:** We can also sort the result on either column using the sortBy function as shown below.

```
val sorted = avgRatings.sortBy(x => x._2)
```


The above line is used to sort the second field which is the value (Average rating) in the ascending order by default. The sorted result is as shown below.


However, if you want to sort it in descending order, you can simply use the dash (-) symbol as shown below.

```
val sorted = avgRatings.sortBy(x => -x._2)
```

You will have the results sorted in descending order when you run the program as shown below.


However, if you want to sort it in descending order, you can simply use the dash (-) symbol as shown below.

```
val sorted = avgRatings.sortBy(x => -x._2)
```