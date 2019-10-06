In this task let us implement a untyped UDAF. The untyped UDAF is used with DataFrames. UDAFs are a kind of bit complex when compared to UDFs. Let us write a UADF function to calculate the average. The average function is a built-in function available in Spark but let us see this just to understand the process of writing a UADF.

**Step 1:** We shall be using the same file ratings_head.csv which we have used in the previous task. Let us use the average UDAF which we are about to implement to calculate the average rating per user.

ratings_head.csv - http://bit.ly/2X3r2wb

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_9` to view file.