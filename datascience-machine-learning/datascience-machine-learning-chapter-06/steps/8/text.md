Alright, let's talk about how item-based collaborative filtering works. It's very similar to user-based collaborative filtering, but instead of users, we're looking at items.

So, let's go back to the example of movie recommendations. The first thing we would do is find every pair of movies that is watched by the same person. So, we go through and find every movie that was watched by identical people, and then we measure the similarity of all those people who viewed that movie to each other. So, by this means we can compute similarities between two different movies, based on the ratings of the people who watched both of those movies.

So, let's presume I have a movie pair, okay? Maybe Star Wars and The Empire Strikes Back. I find a list of everyone who watched both of those movies, then I compare their ratings to each other, and if they're similar then I can say these two movies are similar, because they were rated similarly by people who watched both of them. That's the general idea here. That's one way to do it, there's more than one way to do it!

And then I can just sort everything by the movie, and then by the similarity strength of all the similar movies to it, and there's my results for people who liked also liked, or people who rated this highly also rated this highly and so on and so forth. And like I said, that's just one way of doing it.
