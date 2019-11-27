
Then the conditional probabilities for each of the 1,000 image classes can be predicted for
the images.

```
...
# predict class probabilities for images
yhat = model.predict(images)
```

The inception score can then be calculated directly on the NumPy array of probabilities as
we did in the previous section. Before we do that, we must split the conditional probabilities
into groups, controlled by a n split argument and set to the default of 10 as was used in the
original paper.

```
...
n_part = floor(images.shape[0] / n_split)
```
