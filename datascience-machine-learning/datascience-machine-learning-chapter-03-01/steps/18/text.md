Measuring covariance mathematically is a little bit hard, but I'll try to explain it. These are the steps:

- Think of the data sets for the two variables as high-dimensional vectors
- Convert these to vectors of variances from the mean
- Take the dot product (cosine of the angle between them) of the two vectors
- Divide by the sample size

It's really more important that you understand how to use it and what it means. To actually derive it, think of the attributes of the data as high dimensional vectors. What we're going to do on each attribute for each data point is compute the variance from the mean at each point. So now I have these high dimensional vectors where each data point, each person, if you will, corresponds to a different dimension.

I have one vector in this high dimensional space that represents all the variances from the mean for, let's say, age for one attribute. Then I have another vector that represents all the variances from the mean for some other attribute, like income. What I do then is I take these vectors that measure the variances from the mean for each attribute, and I take the dot product between the two. Mathematically, that's a way of measuring the angle between these high dimensional vectors. So if they end up being very close to each other, that tells me that these variances are pretty much moving in lockstep with each other across these different attributes. If I take that final dot product and divide it by the sample size, that's how I end up with the covariance amount.

Now you're never going to have to actually compute this yourself the hard way. We'll see how to do this the easy way in Python, but conceptually, that's how it works.

Now the problem with covariance is that it can be hard to interpret. If I have a covariance that's close to zero, well, I know that's telling me there's not much correlation between these variables at all, but a large covariance implies there is a relationship. But how large is large? Depending on the units I'm using, there might be very different ways of interpreting that data. That's a problem that correlation solves.