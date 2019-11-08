
Now the scale I alluded to earlier, that's normalizing the data. One important thing with k-means is that it works best if your data is all normalized. That means everything is at the same scale. So a problem that I have here is that my ages range from 20 to 70, but my incomes range all the way up to 200,000. So these values are not really comparable. The incomes are much larger than the age values. Scale will take all that data and scale it together to a consistent scale so I can actually compare these things as apples to apples, and that will help a lot with your k-means results.

So, once we've actually called fit on our model, we can actually look at the resulting labels that we got. Then we can actually visualize it using a little bit of matplotlib magic. You can see in the code we have a little trick where we assigned the color to the labels that we ended up with converted to some floating point number. That's just a little trick you can use to assign arbitrary colors to a given value. So let's see what we end up with:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/8/1.jpg)

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/8/2.jpg)



It didn't take that long. You see the results are basically what clusters I assigned everything into. We know that our fake data is already pre-clustered, so it seems that it identified the first and second clusters pretty easily. It got a little bit confused beyond that point, though, because our clusters in the middle are actually a little bit mushed together. They're not really that distinct, so that was a challenge for k-means. But regardless, it did come up with some reasonable guesses at the clusters. This is probably an example of where four clusters would more naturally fit the data.
