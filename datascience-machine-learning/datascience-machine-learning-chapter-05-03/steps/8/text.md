Here's an example of doing that with SVC: basically, we have sepal width and sepal length projected down to two dimensions so we can actually visualize it:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-03/steps/6/1.jpg)

With different kernels you might get different results. SVC with a linear kernel will produce something very much as you see in the preceding image. You can use polynomial kernels or fancier kernels that might project down to curves in two dimensions as shown in the image. You can do some pretty fancy classification this way.

These have increasing computational costs, and they can produce more complex relationships. But again, it's a case where too much complexity can yield misleading results, so you need to be careful and actually use train/test when appropriate. Since we are doing supervised learning, you can actually do train/test and find the right model that works, or maybe use an ensemble approach.

You need to arrive at the right kernel for the task at hand. For things like polynomial SVC, what's the right degree polynomial to use? Even things like linear SVC will have different parameters associated with them that you might need to optimize for. This will make more sense with a real example, so let's dive into some actual Python code and see how it works!

