Let's figure out what went wrong with our movie similarities there. We went through all this exciting work to compute correlation scores between movies based on their user ratings vectors, and the results we got kind of sucked. So, just to remind you, we looked for movies that are similar to Star Wars using that technique, and we ended up with a bunch of weird recommendations at the top that had a perfect correlation.

And, most of them were very obscure movies. So, what do you think might be going on there? Well, one thing that might make sense is, let's say we have a lot of people watch Star Wars and some other obscure film. We'd end up with a good correlation between these two movies because they're tied together by Star Wars, but at the end of the day, do we really want to base our recommendations on the behavior of one or two people that watch some obscure movie?

Probably not! I mean yes, the two people in the world, or whatever it is, that watch the movie Full Speed, and both liked it in addition to Star Wars, maybe that is a good recommendation for them, but it's probably not a good recommendation for the rest of the world. We need to have some sort of confidence level in our similarities by enforcing a minimum boundary of how many people watched a given movie. We can't make a judgment that a given movie is good just based on the behavior of one or two people.

So, let's try to put that insight into action using the following code:

```
import numpy as np 
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]}) 
movieStats.head() 
```

What we're going to do is try to identify the movies that weren't actually rated by many people and we'll just throw them out and see what we get. So, to do that we're going to take our original ratings DataFrame and we're going to say groupby('title'), again Pandas has all sorts of magic in it. And, this will basically construct a new DataFrame that aggregates together all the rows for a given title into one row.
