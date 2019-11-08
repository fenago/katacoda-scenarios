
It will go off and actually execute everything to get that result. So, if I call two different actions on the same RDD, it will actually end up evaluating that RDD twice, and if you want to avoid all of that extra work, you can cache your RDD in order to make sure that it does not recompute it more than once.

By doing that, we make sure these two subsequent operations do the right thing:

```
print ("Counts by value:") 
counts = resultRDD.countByValue() 
print (counts) 
 
print ("Cluster assignments:") 
results = resultRDD.collect() 
print (results) 
```

In order to get an actual result, what we're going to do is use countByValue, and what that will do is give us back an RDD that has how many points are in each cluster. Remember, resultRDD currently has mapped every individual point to the cluster it ended up with, so now we can use countByValue to just count up how many values we see for each given cluster ID. We can then easily print that list out. And we can actually look at the raw results of that RDD as well, by calling collect on it, and that will give me back every single points cluster assignment, and we can print out all of them.
