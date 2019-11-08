
First, we call map to compute the error for each point. Then to get a final total that represents the entire Dataset, we're calling reduce on that result. So, we're doing data.map to compute the error for each point, and then reduce to take all of those errors and add them all together. And that's what the little lambda function does. This is basically a fancy way of saying, "I want you to add up everything in this RDD into one final result." reduce will take the entire RDD, two things at a time, and combine them together using whatever function you provide. The function I'm providing it above is "take the two rows that I'm combining together and just add them up."

If we do that throughout every entry of the RDD, we end up with a final summed-up total. It might seem like a little bit of a convoluted way to just sum up a bunch of values, but by doing it this way we are able to make sure that we can actually distribute this operation if we need to. We could actually end up computing the sum of one piece of the data on one machine, and a sum of a different piece over on another machine, and then take those two sums and combine them together into a final result. This reduce function is saying, how do I take any two intermediate results from this operation, and combine them together?

Again, feel free to take a moment and stare at this a little bit longer if you want it to sink in. Nothing really fancy going on here, but there are a few important points:

- We introduced the use of a cache if you want to make sure that you don't do unnecessary recomputations on an RDD that you're going to use more than once.
- We introduced the use of the reduce function.
- We have a couple of interesting mapper functions as well here, so there's a lot to learn from in this example.

At the end of the day, it will just do k-means clustering, so let's go ahead and run it.
