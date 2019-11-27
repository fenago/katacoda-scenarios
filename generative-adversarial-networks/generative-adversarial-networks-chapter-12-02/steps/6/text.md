
We can then enumerate over the conditional probabilities in blocks of n part images or
predictions and calculate the inception score.

```
...
# retrieve p(y|x)
ix_start, ix_end = i * n_part, (i+1) * n_part
p_yx = yhat[ix_start:ix_end]
```

After calculating the scores for each split of conditional probabilities, we can calculate and
return the average and standard deviation inception scores.

```
...
# average across images
is_avg, is_std = mean(scores), std(scores)
```

