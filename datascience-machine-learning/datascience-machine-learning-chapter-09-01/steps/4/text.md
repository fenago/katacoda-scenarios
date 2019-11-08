
**It's scalable**

How is Spark scalable? Well, let's get a little bit more specific here in how it all works.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/3/1.png)

The way it works is, you write a driver program, which is just a little script that looks just like any other Python script really, and it uses the Spark library to actually write your script with. Within that library, you define what's called a Spark Context, which is sort of the root object that you work within when you're developing in Spark.

From there, the Spark framework kind of takes over and distributes things for you. So if you're running in standalone mode on your own computer, like we're going to be doing in these upcoming sections, it all just stays there on your computer, obviously. However, if you are running on a cluster manager, Spark can figure that out and automatically take advantage of it. Spark actually has its own built-in cluster manager, you can actually use it on its own without even having Hadoop installed, but if you do have a Hadoop cluster available to you, it can use that as well.

Hadoop is more than MapReduce; there's actually a component of Hadoop called YARN that separates out the entire cluster management piece of Hadoop. Spark can interface with YARN to actually use that to optimally distribute the components of your processing amongst the resources available to that Hadoop cluster.

Within a cluster, you might have individual executor tasks that are running. These might be running on different computers, or they might be running on different cores of the same computer. They each have their own individual cache and their own individual tasks that they run. The driver program, the Spark Context and the cluster manager work together to coordinate all this effort and return the final result back to you.

The beauty of it is, all you have to do is write the initial little script, the driver program, which uses a Spark Context to describe at a high level the processing you want to do on this data. Spark, working together with the cluster manager that you're using, figures out how to spread that out and distribute it so you don't have to worry about all those details. Well, if it doesn't work, obviously, you might have to do some troubleshooting to figure out if you have enough resources available for the task at hand, but, in theory, it's all just magic.
