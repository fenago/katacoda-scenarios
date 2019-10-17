
**Step 6:** Let us now perform some operations with our dataset. The following code below is used to find the total count of each rating.

```
val ratingCount = movies.groupBy("rating").count()
```


We simply use the groupBy function to group all the ratings and then count the number of ratings using the count function. 

Next, let us call the show method to display the result on the console.

```
ratingCount.show()
```

Once the program is finished running, the following result should be shown as output.

 

But this was also achieved using DataFrames. How is Datasets special? Well, we can also write functional style programming with Datasets.
