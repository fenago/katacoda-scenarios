Now, obviously there's a lot of information that isn't in this model that might be very important, but the decision tree that we train from this data might actually be useful in doing an initial pass at weeding out some candidates. What we end up with might be a tree that looks like the following:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/14/3.jpg)

So it just turns out that in my totally fabricated data, anyone that did an internship in college actually ended up getting a job offer. So my first decision point is "did this person do an internship or not?" If yes, go ahead and bring them in. In my experience, internships are actually a pretty good predictor of how good a person is. If they have the initiative to actually go out and do an internship, and actually learn something at that internship, that's a good sign.
Do they currently have a job? Well, if they are currently employed, in my very small fake dataset it turned out that they are worth hiring, just because somebody else thought they were worth hiring too. Obviously it would be a little bit more of a nuanced decision in the real world.
If they're not currently employed, do they have less than one prior employer? If yes, this person has never held a job and they never did an internship either. Probably not a good hire decision. Don't hire that person.
But if they did have a previous employer, did they at least go to a top-tier school? If not, it's kind of iffy. If so, then yes, we should hire this person based on the data that we trained on.
Walking through a decision tree
So that's how you walk through the results of a decision tree. It's just like going through a flowchart, and it's kind of awesome that an algorithm can produce this for you. The algorithm itself is actually very simple. Let me explain how the algorithm works.

At each step of the decision tree flowchart, we find the attribute that we can partition our data on that minimizes the entropy of the data at the next step. So we have a resulting set of classifications: in this case hire or don't hire, and we want to choose the attribute decision at that step that will minimize the entropy at the next step.

At each step we want to make all of the remaining choices result in either as many no hires or as many hire decisions as possible. We want to make that data more and more uniform so as we work our way down the flowchart, and we ultimately end up with a set of candidates that are either all hires or all no hires so we can classify into yes/no decisions on a decision tree. So we just walk down the tree, minimize entropy at each step by choosing the right attribute to decide on, and we keep on going until we run out.

There's a fancy name for this algorithm. It's called ID3 (Iterative Dichotomiser 3). It is what's known as a greedy algorithm. So as it goes down the tree, it just picks the attribute that will minimize entropy at that point. Now that might not actually result in an optimal tree that minimizes the number of choices that you have to make, but it will result in a tree that works, given the data that you gave it.

Random forests technique
Now one problem with decision trees is that they are very prone to overfitting, so you can end up with a decision tree that works beautifully for the data that you trained it on, but it might not be that great for actually predicting the correct classification for new people that it hasn't seen before. Decision trees are all about arriving at the right decision for the training data that you gave it, but maybe you didn't really take into account the right attributes, maybe you didn't give it enough of a representative sample of people to learn from. This can result in real problems.

So to combat this issue, we use a technique called random forests, where the idea is that we sample the data that we train on, in different ways, for multiple different decision trees. Each decision tree takes a different random sample from our set of training data and constructs a tree from it. Then each resulting tree can vote on the right result.

Now that technique of randomly resampling our data with the same model is a term called bootstrap aggregating, or bagging. This is a form of what we call ensemble learning, which we'll cover in more detail shortly. But the basic idea is that we have multiple trees, a forest of trees if you will, each that uses a random subsample of the data that we have to train on. Then each of these trees can vote on the final result, and that will help us combat overfitting for a given set of training data.

The other thing random forests can do is actually restrict the number of attributes that it can choose, between at each stage, while it is trying to minimize the entropy as it goes. And we can randomly pick which attributes it can choose from at each level. So that also gives us more variation from tree to tree, and therefore we get more of a variety of algorithms that can compete with each other. They can all vote on the final result using slightly different approaches to arriving at the same answer.

So that's how random forests work. Basically, it is a forest of decision trees where they are drawing from different samples and also different sets of attributes at each stage that it can choose between.

So, with all that, let's go make some decision trees. We'll use random forests as well when we're done, because scikit-learn makes it really really easy to do, as you'll see soon.

