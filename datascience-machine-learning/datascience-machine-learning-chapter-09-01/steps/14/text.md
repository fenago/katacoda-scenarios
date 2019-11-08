Now, we'll start by setting up our SparkContext, and giving it a SparkConf, a configuration.

```
conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree") 
```

This configuration object says, I'm going to set the master node to "local", and this means that I'm just running on my own local desktop, I'm not actually running on a cluster at all, and I'm just going to run in one process. I'm also going to give it an app name of "SparkDecisionTree," and you can call that whatever you want, Fred, Bob, Tim, whatever floats your boat. It's just what this job will appear as if you were to look at it in the Spark console later on.

And then we will create our SparkContext object using that configuration:

```
sc = SparkContext(conf = conf) 
```

That gives us an sc object we can use for creating RDDs.
