
Finally, we need to train the discriminator model. This involves repeatedly retrieving samples
of real images and samples of generated images and updating the model for a fixed number of
iterations. We will ignore the idea of epochs for now (e.g. complete passes through the training
dataset) and fit the discriminator model for a fixed number of batches. The model will learn to
discriminate between real and fake (randomly generated) images rapidly, therefore not many
batches will be required before it learns to discriminate perfectly.
The train discriminator() function implements this, using a batch size of 128 images,
where 64 are real and 64 are fake each iteration. We update the discriminator separately for
real and fake examples so that we can calculate the accuracy of the model on each sample prior
to the update. This gives insight into how the discriminator model is performing over time.

```
# train the discriminator model
def train_discriminator(model, dataset, n_iter=20, n_batch=128):
half_batch = int(n_batch / 2)
# manually enumerate epochs
for i in range(n_iter):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update discriminator on real samples
_, real_acc = model.train_on_batch(X_real, y_real)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(half_batch)
# update discriminator on fake samples
_, fake_acc = model.train_on_batch(X_fake, y_fake)
# summarize performance
print('>%d real=%.0f%% fake=%.0f%%' % (i+1, real_acc*100, fake_acc*100))
```

Tying all of this together, the complete example of training an instance of the discriminator
model on real and randomly generated (fake) images is listed below.