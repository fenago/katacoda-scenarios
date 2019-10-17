**Step 2:** Let us now create an RDD using a file from the file system. We shall be using the textFile API to create an RDD from the file system. First, download the file ratings.csv from the URL below and save it to the home/chapter_3 folder. (Please create a folder named chapter_3 in the home folder.)

Ratings.csv - http://bit.ly/2L8IEBS

Each line of this file represents one rating of one movie by one user, and has the following format: userId,movieId,rating,timestamp

`val ratings = sc.textFile("apache-spark/Files/chapter_3/ratings.csv")`{{execute}} 
