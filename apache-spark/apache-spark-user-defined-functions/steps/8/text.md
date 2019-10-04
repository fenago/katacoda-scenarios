
**Step 5:** Let us now apply UDF inside the Spark SQL query. You may either choose to create a new Scala object to apply the UDF inside Spark SQL query or within this section. 

We have used the same Scala object to apply the UDF using Spark SQL.

**Step 6:** Let us now define a function to decrease the rating by 0.5 using the def keyword. Please define this function outside the main function as shown in the screenshot below
 
```
def decrUDF2(input: Double): Double = {

  input - 0.5
}
```

 