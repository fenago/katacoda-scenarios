Before we get to Bagging, let’s take a quick look at an important foundation technique called
the bootstrap. The bootstrap is a powerful statistical method for estimating a quantity from a
data sample. This is easiest to understand if the quantity is a descriptive statistic such as a
mean or a standard deviation. Let’s assume we have a sample of 100 values (x) and we’d like to
get an estimate of the mean of the sample. We can calculate the mean directly from the sample
as:

We know that our sample is small and that our mean has error in it. We can improve the
estimate of our mean using the bootstrap procedure:
1. Create many (e.g. 1000) random subsamples of our dataset with replacement (meaning
we can select the same value multiple times).
2. Calculate the mean of each subsample.
3. Calculate the average of all of our collected means and use that as our estimated mean for
the data.

For example, let’s say we used 3 resamples and got the mean values 2.3, 4.5 and 3.3. Taking
the average of these we could take the estimated mean of the data to be 3.367. This process
can be used to estimate other quantities like the standard deviation and even quantities used in
machine learning algorithms, like learned coefficients.