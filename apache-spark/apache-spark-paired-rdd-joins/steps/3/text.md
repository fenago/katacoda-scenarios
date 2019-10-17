So far we have been working on single paired RDDs. In this task let us look at two paired RDDs by performing joins.

**Step 1:** Download the ratings.csv file from the URL below. This file contains four columns: userId, movieID, rating and timestamp.

ratings.csv - http://bit.ly/2QmnAH9

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_5` to view file.

**Step 2:** Download the movies.csv file from the URL below. This file contains three columns: movieID, movieName and genre.

movies.csv - http://bit.ly/2EJj0Os

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_5` to view file.

We shall join these datasets based on the movieID.