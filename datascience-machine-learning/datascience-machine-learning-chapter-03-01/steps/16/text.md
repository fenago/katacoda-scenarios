Finally, let's look at box-and-whisker plots. Remember in the previous chapter, when we talked about percentiles I touched on this a little bit.

Again, with a box-and-whisker plot, the box represents the two inner quartiles where 50% of your data resides. Conversely, another 25% resides on either side of that box; the whiskers (dotted lines in our example) represent the range of the data except for outliers.

We define outliers in a box-and-whisker plot as anything beyond 1.5 times the interquartile range, or the size of the box. So, we take the size of the box times 1.5, and up to that point on the dotted whiskers, we call those parts outer quartiles. But anything outside of the outer quartiles is considered an outlier, and that's what the lines beyond the outer quartiles represent. That's where we are defining outliers based on our definition with the box-and-whisker plot.

Some points to remember about box-and-whisker plots:

- They are useful for visualizing the spread and skew of data
- The line in the middle of the box represents the median of the data, and the box represents the bounds of the 1st and 3rd quartiles
- Half of the data exists within the box
- The "whiskers" indicate the range of the data-except for outliers, which are plotted outside the whiskers.
- Outliers are 1.5 times or more the interquartile range.

Now, just to give you an example here, we have created a fake dataset. The following example creates uniformly distributed random numbers between -40 and 60, plus a few outliers above 100 and below -100:

```
uniformSkewed = np.random.rand(100) * 100 - 40 
high_outliers = np.random.rand(10) * 50 + 100 
low_outliers = np.random.rand(10) * -50 - 100 
data = np.concatenate((uniformSkewed, high_outliers, low_outliers)) 
plt.boxplot(data) 
plt.show() 
```

In the code, we have a uniform random distribution of data (uniformSkewed). Then we added a few outliers on the high end (high_outliers) and a few negative outliers (low_outliers) as well. Then we concatenated these lists together and created a single dataset from these three different sets that we created using NumPy. We then took that combined dataset of uniform data and a few outliers and we plotted using plt.boxplot(), and that's how you get a box-and-whisker plot. Call show() to visualize it, and there you go.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-03-01/steps/2/15.png)

You can see that the graph is showing the box that represents the inner 50% of all data, and then we have these outlier lines where we can see little crosses (they may be circles in your version) for each individual outlier that lies in that range.