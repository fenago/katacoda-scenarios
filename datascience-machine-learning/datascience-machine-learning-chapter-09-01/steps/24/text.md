
We're going to import the KMeans package from the clustering MLlib package, we're going to import array and random from numpy, because, again, we're free to use whatever you want, this is a Python script at the end of the day, and MLlib often does require numpy arrays as input. We're going to import the sqrt function and the usual boilerplate stuff, we need SparkConf and SparkContext, pretty much every time from pyspark. We're also going to import the scale function from scikit-learn. Again, it's OK to use scikit-learn as long as you make sure its installed in every machine that you're going to be running this job on, and also don't assume that scikit-learn will magically scale itself up just because you're running it on Spark. But, since I'm only using it for the scaling function, it's OK. Alright, let's go ahead and set things up.

I'm going to create a global variable first:

```
K=5 
```

I'm going to run k-means clustering in this example with a K of 5, meaning with five different clusters. I'm then going to go ahead and set up a local SparkConf just running on my own desktop:

```
conf = SparkConf().setMaster("local").setAppName("SparkKMeans") 
sc = SparkContext(conf = conf) 
```

I'm going to set the name of my application to SparkKMeans and create a SparkContext object that I can then use to create RDDs that run on my local machine. We'll skip past the createClusteredData function for now, and go to the first line of code that gets run.

```
data = sc.parallelize(scale(createClusteredData(100, K)))  
```

- The first thing we're going to do is create an RDD by parallelizing in some fake data that I'm creating, and that's what the createClusteredData function does. Basically, I'm telling you to create 100 data points clustered around K centroids, and this is pretty much identical to the code that we looked at when we played with k-means clustering earlier in the book. If you want a refresher, go ahead and look back at that chapter. Basically, what we're going to do is create a bunch of random centroids around which we normally distribute some age and income data. So, what we're doing is trying to cluster people based on their age and income, and we are fabricating some data points to do that. That returns a numpy array of our fake data.
- Once that result comes back from createClusteredData, I'm calling scale on it, and that will ensure that my ages and incomes are on comparable scales. Now, remember the section we studied saying you have to remember about data normalization? This is one of those examples where it is important, so we are normalizing that data with scale so that we get good results from k-means.
- And finally, we parallelize the resulting list of arrays into an RDD using parallelize. Now our data RDD contains all of our fake data. All we have to do, and this is even easier than a decision tree, is call KMeans.train on our training data.

```
clusters = KMeans.train(data, K, maxIterations=10, 
        initializationMode="random") 
```

We pass in the number of clusters we want, our K value, a parameter that puts an upper boundary on how much processing it's going to do; we then tell it to use the default initialization mode of k-means where we just randomly pick our initial centroids for our clusters before we start iterating on them, and back comes the model that we can use. We're going to call that clusters.

Alright, now we can play with that cluster.
