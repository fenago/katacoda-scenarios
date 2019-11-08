Another thing that you need to really internalize is that variance is your enemy when you're running an A/B test.

A very common mistake people make who don't know what they're doing with data science is that they will put up a test on a web page, blue button versus orange button, whatever it is, run it for a week, and take the mean amount spent from each of those groups. They then say "oh look! The people with the blue button on average spent a dollar more than the people with the orange button; blue is awesome, I love blue, I'm going to put blue all over the website now!"

But, in fact, all they might have been seeing was just a random variation in purchases. They didn't have a big enough sample because people don't tend to purchase a lot. You get a lot of views but you probably don't have a lot of purchases on your website in comparison, and it's probably a lot of variance in those purchase amounts because different products cost different amounts.

So, you could very easily end up making the wrong decision that ends up costing your company money in the long run, instead of earning your company money if you don't understand the effect of variance on these results. We'll talk about some principal ways of measuring and accounting for that later in the chapter.

**Note:**

You need to make sure that your business owners understand that this is an important effect that you need to quantify and understand before making business decisions following an A/B test or any experiment that you run on the web.

Now, sometimes you need to choose a conversion metric that has less variance. It could be that the numbers on your website just mean that you would have to run an experiment for years in order to get a significant result based on something like revenue or amount spent.

Sometimes if you're looking at more than one metric, such as order amount or order quantity, that has less variance associated with it, you might see a signal on order quantity before you see a signal on revenue, for example. At the end of the day, it ends up being a judgment call. If you see a significant lift in order quantities and maybe a not-so-significant lift in revenue, then you have to say "well, I think there might be something real and beneficial going on here."

However, the only thing that statistics and data size can tell you, are probabilities that an effect is real. It's up to you to decide whether or not it's real at the end of the day. So, let's talk about how to do this in more detail.

The key takeaway here is, just looking at the differences in means isn't enough. When you're trying to evaluate the results of an experiment, you need to take the variance into account as well.

