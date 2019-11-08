
Ready? Here we go!

- The first moment works out to just be the mean of the data that you're looking at. That's it. The first moment is the mean, the average. It's that simple.
- The second moment is the variance. That's it. The second moment of the dataset is the same thing as the variance value. It might seem a little bit creepy that these things kind of fall out of the math naturally, but think about it. The variance is really based on the square of the differences from the mean, so coming up with a mathematical way of saying that variance is related to mean isn't really that much of a stretch, right. It's just that simple.
- Now when we get to the third and fourth moments, things get a little bit trickier, but they're still concepts that are easy to grasp. The third moment is called skew, and it is basically a measure of how lopsided a distribution is.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/9/5.png)

You can see in these two examples above that, if I have a longer tail on the left, now then that is a negative skew, and if I have a longer tail on the right then, that's a positive skew. The dotted lines show what the shape of a normal distribution would look like without skew. The dotted line out on the left side then I end up with a negative skew, or on the other side, a positive skew in that example. OK, so that's all skew is. It's basically stretching out the tail on one side or the other, and it is a measure of how lopsided, or how skewed a distribution is.

- The fourth moment is called kurtosis. Wow, that's a fancy word! All that really is, is how thick is the tail and how sharp is the peak. So again, it's a measure of the shape of the data distribution. Here's an example:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/9/6.png)

You can see that the higher peak values have a higher kurtosis value. The topmost curve has a higher kurtosis than the bottommost curve. It's a very subtle difference, but a difference nonetheless. It basically measures how peaked your data is.

Let's review all that: the first moment is mean, the second moment is variance, the third moment is skew, and the fourth moment is kurtosis. We already know what mean and variance are. Skew is how lopsided the data is, how stretched out one of the tails might be. Kurtosis is how peaked, how squished together the data distribution is.
