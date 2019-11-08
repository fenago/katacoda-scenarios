
SVC is actually a very powerful technique; it's real strength is in higher dimensional feature data. Go ahead and play with it. By the way if you want to not just visualize the results, you can use the predict() function on the SVC model, just like on pretty much any model in scikit-learn, to pass in a feature array that you're interested in. If I want to predict the classification for someone making $200,000 a year who was 40 years old, I would use the following code:

```
svc.predict([[200000, 40]])
```

This would put that person in, in our case, cluster number 1:

If I had a someone making $50,000 here who was 65, I would use the following code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-03/steps/9/3.jpg)

```
svc.predict([[50000, 65]])
```

This is what your output should now look like:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-03/steps/9/4.jpg)


That person would end up in cluster number 2, whatever that represents in this example. So,go ahead and play with it.

