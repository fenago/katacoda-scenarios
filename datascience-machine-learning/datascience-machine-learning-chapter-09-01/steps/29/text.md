#### Run Code
Now, run the python code by running: `python SparkKMeans.py`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/23/2.png)


It worked, awesome! So remember, the output that we asked for was, first of all, a count of how many points ended up in each cluster. So, this is telling us that cluster 0 had 21 points in it, cluster 1 had 20 points in it, and so on and so forth. It ended up pretty evenly distributed, so that's a good sign.

Next, we printed out the cluster assignments for each individual point, and, if you remember, the original data that fabricated this data did it sequentially, so it's actually a good thing that you see all of the 3s together, and all the 1s together, and all the 4s together, it looks like it started to get a little bit confused with the 0s and 2s, but by and large, it seems to have done a pretty good job of uncovering the clusters that we created the data with originally.

And finally, we computed the WSSSE metric, it came out to 19.97 in this example. So, if you want to play around with this a little bit, I encourage you to do so. You can see what happens to that error metric as you increase or decrease the values of K, and think about why that may be. You can also experiment with what happens if you don't normalize all the data, does that actually affect your results in a meaningful way? Is that actually an important thing to do? And you can also experiment with the maxIterations parameter on the model itself and get a good feel of what that actually does to the final results, and how important it is. So, feel free to mess around with it and experiment away. That's k-means clustering done with MLlib and Spark in a scalable manner. Very cool stuff.
