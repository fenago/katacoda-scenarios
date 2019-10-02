



Task 6: Typed UDAF

Finally, let us write and use a Typeds UDAF. The Typed UDAF is used on Datasets where we assign the schema using the case class making it type safe. Let us write a Typed UDAF which calculates the average of ratings as we did in the previous couple of tasks. The methods which we have used in the untyped UDAF are different than the methods in Typed UDAF.

Step 1: We shall be using the same file ratings_head.csv which we have used in the previous task. Let us use the average UDAF which we are about to implement to calculate the average of all the ratings.
 

ratings_head.csv - http://bit.ly/2X3r2wb

Please make sure this file is available in IdeaProjects/Spark/chapter_9 folder.
