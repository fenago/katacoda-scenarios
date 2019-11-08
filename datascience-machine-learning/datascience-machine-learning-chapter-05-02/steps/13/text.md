
Now mathematically, it's a little bit more involved than that, so when I actually compute a number for entropy, it's computed using the following expression:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/12/1.jpg)

So for every different class that I have in my data, I'm going to have one of these p terms, p1, p2, and so on and so forth through pn, for n different classes that I might have. The p just represents the proportion of the data that is that class. And if you actually plot what this looks like for each term- pi* ln * pi, it'll look a little bit something like the following graph:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/12/2.jpg)

You add these up for each individual class. For example, if the proportion of the data, that is, for a given class is 0, then the contribution to the overall entropy is 0. And if everything is that class, then again the contribution to the overall entropy is 0 because in either case, if nothing is this class or everything is this class, that's not really contributing anything to the overall entropy.

It's the things in the middle that contribute entropy of the class, where there's some mixture of this classification and other stuff. When you add all these terms together, you end up with an overall entropy for the entire dataset. So mathematically, that's how it works out, but again, the concept is very simple. It's just a measure of how disordered your dataset, how same or different the things in your data are.

