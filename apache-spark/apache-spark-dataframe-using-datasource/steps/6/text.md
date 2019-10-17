


**Step 5:** We now have successfully created a dataFrame named users. Let us now print it to console along with the schema.

```
   users.printSchema()

   users.show()
 }

}
```

We call printSchema method to display the inferred schema and show method to display our dataFrame. Please note that when you use show method, only first 20 records in the dataFrame are shown. You can pass an integer for number of records in the show method. For example, to show 40 records you can use something like this users.show(40)

 

The show method is an action and so this the point where the DAG is actually executed. 

