Did you ever wonder how the spam classifier in your e-mail works? How does it know that an e-mail might be spam or not? Well, one popular technique is something called Naive Bayes, and that's an example of a Bayesian method. Let's learn more about how that works. Let's discuss Bayesian methods.

We did talk about Bayes' theorem earlier in this book in the context of talking about how things like drug tests could be very misleading in their results. But you can actually apply the same Bayes' theorem to larger problems, like spam classifiers. So let's dive into how that might work, it's called a Bayesian method.

So just a refresher on Bayes' theorem -remember, the probability of A given B is equal to the overall probability of A times the probability of B given A over the overall probability of B:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/15/1.jpg)

How can we use that in machine learning? I can actually build a spam classifier for that: an algorithm that can analyze a set of known spam e-mails and a known set of non-spam e-mails, and train a model to actually predict whether new e-mails are spam or not. This is a real technique used in actual spam classifiers in the real world.
