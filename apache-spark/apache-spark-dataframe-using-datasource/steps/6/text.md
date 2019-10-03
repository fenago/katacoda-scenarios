


**Step 5:** We now have successfully created a dataFrame named users. Let us now print it to console along with the schema.

   users.printSchema()

   users.show()
 }

}

We call printSchema method to display the inferred schema and show method to display our dataFrame. Please note that when you use show method, only first 20 records in the dataFrame are shown. You can pass an integer for number of records in the show method. For example, to show 40 records you can use something like this users.show(40)

 

The show method is an action and so this the point where the DAG is actually executed. 

**Step 6:** Let us run this program and check the output. You should see the schema as shown below.


 
As you can see, the schema been correctly discovered by Spark for each and every column in the dataFrame. Please note that if a column has values of more than one data type, Spark will infer it as String.
The output of dataFrame users is as shown below.

 



 

As you can see from the screenshot above, the header is displayed correctly along with the records.
