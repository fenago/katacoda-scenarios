**Step 7:** Let us now create a SparkContext object so that we can access all the spark functionality.

```
val sc = new SparkContext("local[*]", "WordCount")
```

We are creating an immutable variable called sc which cotains the SparkContext object. Inside the SparkContext object the first parameter tells Spark if we would want the program to be executed in local or distributed mode. In our case, since we are working locally, we will be using local[*]. The [*] tells Spark to use all the CPU cores available locally in our machine. The next parameter is just the name of our app which is WordCount.
