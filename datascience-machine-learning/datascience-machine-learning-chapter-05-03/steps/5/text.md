
Now these are all very complicated techniques that I can't really get into in the scope of this book, but at the end of the day, it's hard to outperform just the simple techniques that we've already talked about. A few of the complex techniques are listed here:

- **Bayes optical classifier:** In theory, there's something called the Bayes Optimal Classifier that will always be the best, but it's impractical, because it's computationally prohibitive to do it.
- **Bayesian parameter averaging:** Many people have tried to do variations of the Bayes Optimal Classifier to make it more practical, like the Bayesian Parameter Averaging variation. But it's still susceptible to overfitting and it's often outperformed by bagging, which is the same idea behind random forests; you just resample the data multiple times, run different models, and let them all vote on the final result. Turns out that works just as well, and it's a heck of a lot simpler!
- **Bayesian model combination:** Finally, there's something called Bayesian Model Combination that tries to solve all the shortcomings of Bayes Optimal Classifier and Bayesian Parameter Averaging. But, at the end of the day, it doesn't do much better than just cross validating against the combination of models.

Again, these are very complex techniques that are very difficult to use. In practice, we're better off with the simpler ones that we've talked about in more detail. But, if you want to sound smart and use the word Bayes a lot it's good to be familiar with these techniques at least, and know what they are.

So, that's ensemble learning. Again, the takeaway is that the simple techniques, like bootstrap aggregating, or bagging, or boosting, or stacking, or bucket of models, are usually the right choices. There are some much fancier techniques out there but they're largely theoretical. But, at least you know about them now.

It's always a good idea to try ensemble learning out. It's been proven time and time again that it will produce better results than any single model, so definitely consider it!