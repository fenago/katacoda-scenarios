Let us implement a Custom Accumulator which counts the number of times each movie has been rated. We can achieve the same using the map transformation and then applying reduceByKey action. But then this will have the data shuffled across the nodes of the cluster. However, when we use Accumulators, the data is not shuffled across the clusters as each executor processes data locally and has its own local accumulator. The only data shuffled across the cluster will be the count from each local accumulator, which will only be a few bytes. The local count from all the executors is aggregated by the global accumulator in the driver, thus providing the final result.

**Step 1:** Download the ratings.csv file from the URL below. This file contains four columns: userId, movieID, rating and timestamp.

Ratings_head.csv - http://bit.ly/2X3r2wb

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_6` to view file.

