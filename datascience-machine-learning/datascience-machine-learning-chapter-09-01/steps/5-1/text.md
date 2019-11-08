Spark actually has many different components that it's built up of. So there is a Spark Core that lets you do pretty much anything you can dream up just using Spark Core functions alone, but there are these other things built on top of Spark that are also useful.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/3/2.png)

- **Spark Streaming:** Spark Streaming is a library that lets you actually process data in real time. Data can be flowing into a server continuously, say, from weblogs, and Spark Streaming can help you process that data in real time as you go, forever.
- **Spark SQL:** This lets you actually treat data as a SQL database, and actually issue SQL queries on it, which is kind of cool if you're familiar with SQL already.
- **MLlib:** This is what we're going to be focusing on in this section. It is actually a machine learning library that lets you perform common machine learning algorithms, with Spark underneath the hood to actually distribute that processing across a cluster. You can perform machine learning on much larger Datasets than you could have otherwise.
- **GraphX:** This is not for making pretty charts and graphs. It refers to graph in the network theory sense. Think about a social network; that's an example of a graph. GraphX just has a few functions that let you analyze the properties of a graph of information.
