**Median**

Median is a little bit different. The way you compute the median of the dataset is by sorting all the values (in either ascending or descending order), and taking the one that ends up in the middle.

So, for example, let's use the same dataset of children in my neighborhood

```
0, 2, 3, 2, 1, 0, 0, 2, 0
```

I would sort it numerically, and I can take the number that's slap dab in the middle of the data, which turns out to be 1.

```
0, 0, 0, 0, 1, 2, 2, 2, 3
```

Again, all I do is take the data, sort it numerically, and take the center point.

**Note:** If you have an even number of data points, then the median might actually fall in between two data points. It wouldn't be clear which one is actually the middle. In that case, all you do is, take the average of the two that do fall in the middle and consider that number as the median.

**The factor of outliers**

Now in the preceding example of the number of kids in each household, the median and the mean were pretty close to each other because there weren't a lot of outliers. We had 0, 1, 2, or 3 kids, but we didn't have some wacky family that had 100 kids. That would have really skewed the mean, but it might not have changed the median too much. That's why the median is often a very useful thing to look at and often overlooked.

**Note:** Median is less susceptible to outliers than the mean.

People have a tendency to mislead people with statistics sometimes. I'm going to keep pointing this out throughout the book wherever I can.

For example, you can talk about the mean or average household income in the United States,and that actual number from last year when I looked it up was $72,000 or so, but that doesn't really provide an accurate picture of what the typical American makes. That is because, if you look at the median income, it's much lower at $51,939. Why is that? Well, because of income inequality. There are a few very rich people in America, and the same is true in a lot of countries as well. America's not even the worst, but you know those billionaires, those super-rich people that live on Wall Street or Silicon Valley or some other super-rich place, they skew the mean. But there's so few of them that they don't really affect the median so much.

This is a great example of where the median tells a much better story about the typical person or data point in this example than the mean does. Whenever someone talks about the mean, you have to think about what does the data distribution looks like. Are there outliers that might be skewing that mean? And if the answer is potentially yes, you should also ask for the median, because often, that provides more insight than the mean or the average.
