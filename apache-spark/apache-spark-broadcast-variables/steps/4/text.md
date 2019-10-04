Let us now look at another type of Distributed Shared Variable called the Broadcast variable. Let us use our movies dataset which we have been using throughout this course and find out the number of ratings for each movie. We shall be using the movies.csv file and ratings.csv file during this task. We shall broadcast the movies.csv file to look up with the movie Id in ratings.csv file.

**Step 1:** We will be needing two files for this lab exercise. Please download and save this files to IdeaProjects/Spark/chapter_6 folder, if not saved already.

ratings.csv - http://bit.ly/2QmnAH9

This file contains four columns: userId, movieID, rating and timestamp.

movies.csv - http://bit.ly/2EJj0Os

This file contains three columns: movieID, movieName and genre.
