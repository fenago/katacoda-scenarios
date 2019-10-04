Let us write and use a Typeds UDAF. The Typed UDAF is used on Datasets where we assign the schema using the case class making it type safe. Let us write a Typed UDAF which calculates the average of ratings as we did in the previous couple of tasks. The methods which we have used in the untyped UDAF are different than the methods in Typed UDAF.

**Step 1:** We shall be using the ratings_head.csv. Let us use the average UDAF which we are about to implement to calculate the average of all the ratings.
 
ratings_head.csv - http://bit.ly/2X3r2wb

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_9` to view file.