
Another example is from Netflix, as shown in the following image (the following image is a screenshot from Netflix):

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/3/2.png)

They have various features that try to recommend new movies or other movies you haven't seen yet, based on the movies that you liked or watched in the past as well, and they break that down by genre. They have kind of a different spin on things, where they try to identify the genres or the types of movies that they think you're enjoying the most and they then show you more results from those genres. So, that's another example of a recommender system in action.

The whole point of it is to help you discover things you might not know about before, so it's pretty cool. You know, it gives individual movies, or books, or music, or whatever, a chance to be discovered by people who might not have heard about them before. So, you know, not only is it cool technology, it also kind of levels the playing field a little bit, and helps new items get discovered by the masses. So, it plays a very important role in today's society, at least I'd like to think so! There are few ways of doing this, and we'll look at the main ones in this scenario.

User-based collaborative filtering
First, let's talk about recommending stuff based on your past behavior. One technique is called user-based collaborative filtering, and here's how it works:

**Note:**

Collaborative filtering, by the way, is just a fancy name for saying recommending stuff based on the combination of what you did and what everybody else did, okay? So, it's looking at your behavior and comparing that to everyone else's behavior, to arrive at the things that might be interesting to you that you haven't heard of yet.

The idea here is we build up a matrix of everything that every user has ever bought, or viewed, or rated, or whatever signal of interest that you want to base the system on. So basically, we end up with a row for every user in our system, and that row contains all the things they did that might indicate some sort of interest in a given product. So, picture a table, I have users for the rows, and each column is an item, okay? That might be a movie, a product, a web page, whatever; you can use this for many different things.
I then use that matrix to compute the similarity between different users. So, I basically treat each row of this as a vector and I can compute the similarity between each vector of users, based on their behavior.
Two users who liked mostly the same things would be very similar to each other and I can then sort this by those similarity scores. If I can find all the users similar to you based on their past behavior, I can then find the users most similar to me, and recommend stuff that they liked that I didn't look at yet.
Let's look at a real example, and it'll make a little bit more sense:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/3/3.png)

Let's say that this nice lady in the preceding image watched Star Wars and The Empire Strikes Back and she loved them both. So, we have a user vector, of this lady, giving a 5-star rating to Star Wars and The Empire Strikes Back.

Let's also say Mr. Edgy Mohawk Man comes along and he only watched Star Wars. That's the only thing he's seen, he doesn't know about The Empire Strikes Back yet, somehow, he lives in some strange universe where he doesn't know that there are actually many, many Star Wars movies, growing every year in fact.

We can of course say that this guy's actually similar to this other lady because they both enjoyed Star Wars a lot, so their similarity score is probably fairly good and we can say, okay, well, what has this lady enjoyed that he hasn't seen yet? And, The Empire Strikes Back is one, so we can then take that information that these two users are similar based on their enjoyment of Star Wars, find that this lady also liked The Empire Strikes Back, and then present that as a good recommendation for Mr. Edgy Mohawk Man.

We can then go ahead and recommend The Empire Strikes Back to him and he'll probably love it, because in my opinion, it's actually a better film! But I'm not going to get into geek wars with you here.

