Alright, let's actually build some decision trees using Spark and the MLlib library, this is very cool stuff. Wherever you put the course materials for this book, I want you to go to that folder now. Make sure you're completely closed out of Canopy, or whatever environment you're using for Python development, because I want to make sure you're starting it from this directory, OK? And find the SparkDecisionTree script, and double-click that to open up Canopy:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/12/1.png)

Now, up until this point we've been using IPython notebooks for our code, but you can't really use those very well with Spark. With Spark scripts, you need to actually submit them to the Spark infrastructure and run them in a very special way, and we'll see how that works shortly.

#### Exploring decision trees code
So, we are just looking at a raw Python script file now, without any of the usual embellishment of the IPython notebook stuff. let's walk through what's going on in the script.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/12/2.png)

We'll go through it slowly, because this is your first Spark script that you've seen in this book.
