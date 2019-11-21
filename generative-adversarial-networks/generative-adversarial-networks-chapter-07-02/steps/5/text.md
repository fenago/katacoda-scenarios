
Now, we need a source of fake images. We don’t have a generator model yet, so instead,
we can generate images comprised of random pixel values, specifically random pixel values
in the range [0,1] like our scaled real images. The generate fake samples() function below
implements this behavior and generates images of random pixel values and their associated class
label of 0, for fake.

```
# generate n fake samples with class labels
def generate_fake_samples(n_samples):
# generate uniform random numbers in [0,1]
X = rand(28 * 28 * n_samples)
# reshape into a batch of grayscale images
X = X.reshape((n_samples, 28, 28, 1))
# generate 'fake' class labels (0)
y = zeros((n_samples, 1))
return X, y
```
