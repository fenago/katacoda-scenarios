
**Step 2:** Let us cast the date column and convert it to date type using the cast function as shown below.

`val casted = datesDS.select($"id", $"name", $"date".cast("date")).cache()`{{execute}} 

Let us print the schema to check if we were able to successfully convert the date column from String type to Date type. Let us also use the show function to view the dataset.

```casted.printSchema()
casted.show()```{{execute}} 

As you can see, we have successfully casted the date column as date type.
