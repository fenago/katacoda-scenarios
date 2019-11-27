Tying all of this together, the calculate inception score() function below takes an array
of images with the expected size and pixel values in [0,255] and calculates the average and
standard deviation inception scores using the inception v3 model in Keras.

```
# assumes images have the shape 299x299x3, pixels in [0,255]
def calculate_inception_score(images, n_split=10, eps=1E-16):
# load inception v3 model
model = InceptionV3()
# convert from uint8 to float32
processed = images.astype('float32')
# pre-process raw images for inception v3 model
processed = preprocess_input(processed)
# predict class probabilities for images
yhat = model.predict(processed)
# enumerate splits of images/predictions
scores = list()
n_part = floor(images.shape[0] / n_split)
for i in range(n_split):
# retrieve p(y|x)
ix_start, ix_end = i * n_part, i * n_part + n_part
p_yx = yhat[ix_start:ix_end]
# calculate p(y)
p_y = expand_dims(p_yx.mean(axis=0), 0)
# calculate KL divergence using log probabilities
kl_d = p_yx * (log(p_yx + eps) - log(p_y + eps))
# sum over classes
sum_kl_d = kl_d.sum(axis=1)
# average over images
avg_kl_d = mean(sum_kl_d)
# undo the log
is_score = exp(avg_kl_d)
# store
scores.append(is_score)
# average across images
is_avg, is_std = mean(scores), std(scores)
return is_avg, is_std12.5. How to Implement the Inception Score With Keras 260
```

We can test this function with 50 artificial images with the value 1.0 for all pixels.

```
...
# pretend to load images
images = ones((50, 299, 299, 3))
print('loaded', images.shape)
```

This will calculate the score for each group of five images and the low quality would suggest
that an average inception score of 1.0 will be reported. 

