
We can then test out this function to calculate the inception score for some contrived feature
vectors. Feature vectors will probably contain small positive values and will have a length of
2,048 elements. We can construct two lots of 10 images worth of feature vectors with small
random numbers as follows:

```
...
# define two collections of activations
act1 = random(10*2048)
act1 = act1.reshape((10,2048))
act2 = random(10*2048)
act2 = act2.reshape((10,2048))
```

One test would be to calculate the FID between a set of activations and itself, which we
would expect to have a score of 0.0. We can then calculate the distance between the two sets of
random activations, which we would expect to be a large number.

```
...
# fid between act1 and act1
fid = calculate_fid(act1, act1)
print('FID (same): %.3f' % fid)
# fid between act1 and act2
fid = calculate_fid(act1, act2)
print('FID (different): %.3f' % fid)
```
