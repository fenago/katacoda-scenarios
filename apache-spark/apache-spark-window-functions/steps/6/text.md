

**Step 4:** Now that we have loaded our file, let us first create a window. We shall create a window to partition by the department and order by pay in descending order.

```
val window = Window.partitionBy($"dept").orderBy($"pay".desc)
```

we have called the partitionBy and orderBy method on the Window object to create a window. The partitionBy method creates partitions for each department withing the window and orderBy method will order the rows by pay in descending order.

**Step 5:** Let us first use the rank  function to get the pay for each employee by department in desceinding order. 

```
val ranked = rank().over(window)
```

We have simply called the rank function over the window we created in the previous step using the over method. The rank function allocates increasing integer values to rows based on the column we specified in the orderBy method.

Let us now call the show method on our dataset and add the rank column using the select function.

```
employeeDS.select($"*", ranked.as("rank")).show()
```

You should have the following output when you run this program.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_053.png)

 
