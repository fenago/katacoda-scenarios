**Step 3:** We can now create a new RDD from the existing RDD. For example, let us count the number of ratings in the ratings RDD we created in the previous step.
 
RDD op.

IntelliJ D/l & Ins
Configure IntelliJ

scala> val count_ratings = ratings.count

 
As you can see from the screenshot above, the count of the total records (ratings) present in the RDD has been returned as a new RDD called count_ratings.
