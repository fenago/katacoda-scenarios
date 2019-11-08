Finally, we'll talk about mode. This doesn't really come up too often in practice, but you can't talk about mean and median without talking about mode. All mode means, is the most common value in a dataset.

Let's go back to my example of the number of kids in each house.

```
0, 2, 3, 2, 1, 0, 0, 2, 0
```

How many of each value are there:

```
0: 4, 1: 1, 2: 3, 3: 1
```

The MODE is 0

If I just look at what number occurs most frequently, it turns out to be 0, and the mode therefore of this data is 0. The most common number of children in a given house in this neighborhood is no kids, and that's all that means.

Now this is actually a pretty good example of continuous versus discrete data, because this only really works with discrete data. If I have a continuous range of data then I can't really talk about the most common value that occurs, unless I quantize that somehow into discrete values. So we've already run into one example here where the data type matters.

**Note:** Mode is usually only relevant to discrete numerical data, and not to continuous data.

A lot of real-world data tends to be continuous, so maybe that's why I don't hear too much about mode, but we see it here for completeness.

There you have it: mean, median, and mode in a nutshell. Kind of the most basic statistics stuff you can possibly do, but I hope you gained a little refresher there in the importance of choosing between median and mean. They can tell very different stories, and yet people tend to equate them in their heads, so make sure you're being a responsible data scientist and representing data in a way that conveys the meaning you're trying to represent. If you're trying to display a typical value, often the median is a better choice than the mean because of outliers, so remember that. Let's move on.