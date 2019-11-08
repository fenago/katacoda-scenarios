
That's step one of item-based collaborative filtering-first I find relationships between movies based on the relationships of the people who watched every given pair of movies. It'll make more sense when we go through the following example:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/8/1.png)

For example, let's say that our nice young lady in the preceding image watched Star Wars and The Empire Strikes Back and liked both of them, so rated them both five stars or something. Now, along comes Mr. Edgy Mohawk Man who also watched Star Wars and The Empire Strikes Back and also liked both of them. So, at this point we can say there's a relationship, there is a similarity between Star Wars and The Empire Strikes Back based on these two users who liked both movies.

What we're going to do is look at each pair of movies. We have a pair of Star Wars and Empire Strikes Back, and then we look at all the users that watched both of them, which are these two guys, and if they both liked them, then we can say that they're similar to each other. Or, if they both disliked them we can also say they're similar to each other, right? So, we're just looking at the similarity score of these two users' behavior related to these two movies in this movie pair.

So, along comes Mr. Moustachy Lumberjack Hipster Man and he watches The Empire Strikes Back and he lives in some strange world where he watched The Empire Strikes Back, but had no idea that Star Wars the first movie existed.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/8/2.png)

Well that's fine, we computed a relationship between The Empire Strikes Back and Star Wars based on the behavior of these two people, so we know that these two movies are similar to each other. So, given that Mr. Hipster Man liked The Empire Strikes Back, we can say with good confidence that he would also like Star Wars, and we can then recommend that back to him as his top movie recommendation. Something like the following illustration:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/8/3.png)

You can see that you end up with very similar results in the end, but we've kind of flipped the whole thing on its head. So, instead of focusing the system on relationships between people, we're focusing them on relationships between items, and those relationships are still based on the aggregate behavior of all the people that watch them. But fundamentally, we're looking at relationships between items and not relationships between people. Got it?
