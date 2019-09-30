Step 6: We can also extract the keys and values to separate RDDs as shown below.

val RDDKeys = flattened.keys

RDDKeys.collect.foreach(println)


Similarly, we can extract the values using the code below.

val RDDValues = flattened.values

RDDValues.collect.foreach(println)

 

Task 4 is complete!
