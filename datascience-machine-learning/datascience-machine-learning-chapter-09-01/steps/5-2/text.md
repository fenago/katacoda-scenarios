I do get some flack sometimes about using Python when I'm teaching people about Apache Spark, but there's a method to my madness. It is true that a lot of people use Scala when they're writing Spark code, because that's what Spark is developed in natively. So, you are incurring a little bit of overhead by forcing Spark to translate your Python code into Scala and then into Java interpreter commands at the end of the day.

However, Python's a lot easier, and you don't need to compile things. Managing dependencies is also a lot easier. You can really focus your time on the algorithms and what you're doing, and less on the minutiae of actually getting it built, and running, and compiling, and all that nonsense. Plus, obviously, this book has been focused on Python so far, and it makes sense to keep using what we've learned and stick with Python throughout these lectures. Here's a quick summary of the pros and cons of the two languages:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/3/3.png)

However, I will say that if you were to do some Spark programming in the real world, there's a good chance people are using Scala. Don't worry about it too much, though, because in Spark the Python and Scala code ends up looking very similar because it's all around the same RDD concept. The syntax is very slightly different, but it's not that different. If you can figure out how to do Spark using Python, learning how to use it in Scala isn't that big of a leap, really. Here's a quick example of the same code in the two languages:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/3/4.png)

So, that's the basic concepts of Spark itself, why it's such a big deal, and how it's so powerful in letting you run machine learning algorithms on very large Datasets, or any algorithm really. Let's now talk in a little bit more detail about how it does that, and the core concept of the Resilient Distributed Dataset.

