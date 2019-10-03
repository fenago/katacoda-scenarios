


######################################################
Task 4: Writing Untyped UDAF

In the previous task, we have implemented a UDF. In this task let is implement a untyped UDAF. The untyped UDAF is used with DataFrames. UDAFs are a kind of bit complex when compared to UDFs. Let us write a UADF function to calculate the average. The average function is a built-in function available in Spark but let us see this just to understand the process of writing a UADF.

While we write a UADF, we need to implement few methods similar to what we did in Lab exercise 5, Task 5 Implementing Custom Accumulators.

**Step 1:** We shall be using the same file ratings_head.csv which we have used in the previous task. Let us use the average UDAF which we are about to implement to calculate the average rating per user.

ratings_head.csv - http://bit.ly/2X3r2wb

Please make sure this file is available in IdeaProjects/Spark/chapter_9 folder.
