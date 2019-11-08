Using MLlib is usually pretty straightforward, there are just some library functions you need to call. It does introduce a few new data types; however, that you need to know about,and one is the vector.

**The vector data type**

Remember when we were doing movie similarities and movie recommendations earlier in the book? An example of a vector might be a list of all the movies that a given user rated. There are two types of vector, sparse and dense. Let's look at an example of those. There are many, many movies in the world, and a dense vector would actually represent data for every single movie, whether or not a user actually watched it. So, for example, let's say I have a user who watched Toy Story, obviously I would store their rating for Toy Story, but if they didn't watch the movie Star Wars, I would actually store the fact that there is not a number for Star Wars. So, we end up taking up space for all these missing data points with a dense vector. A sparse vector only stores the data that exists, so it doesn't waste any memory space on missing data, OK. So, it's a more compact form of representing a vector internally, but obviously that introduces some complexity while processing. So, it's a good way to save memory if you know that your vectors are going to have a lot of missing data in them.

**LabeledPoint data type**

There's also a LabeledPoint data type that comes up, and that's just what it sounds like, a point that has some sort of label associated with it that conveys the meaning of this data in human readable terms.

**Rating data type**

Finally, there is a Rating data type that you'll encounter if you're using recommendations with MLlib. This data type can take in a rating that represents a 1-5 or 1-10, whatever star rating a person might have, and use that to inform product recommendations automatically.

So, I think you finally have everything you need to get started, let's dive in and actually look at some real MLlib code and run it, and then it will make a lot more sense.

