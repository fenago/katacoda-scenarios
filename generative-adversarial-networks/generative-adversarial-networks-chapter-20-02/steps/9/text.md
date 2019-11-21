
Next, we can define a function to train the models. The defined models and loaded training
dataset are provided as arguments, and the number of training epochs and batch size are
parameterized with default values, in this case 20 epochs and a batch size of 100. The chosen
model configuration was found to overfit the training dataset quickly, hence the relatively smaller
number of training epochs. Increasing the epochs to 100 or more results in much higher-quality
generated images, but a lower-quality classifier model. Balancing these two concerns might
make a fun extension.

First, the labeled subset of the training dataset is selected, and the number of training
steps is calculated. The training process is almost identical to the training of a vanilla GAN
model, with the addition of updating the supervised model with labeled examples. A single
cycle through updating the models involves first updating the supervised discriminator model
with labeled examples, then updating the unsupervised discriminator model with unlabeled real
and generated examples. Finally, the generator model is updated via the composite model.
The shared weights of the discriminator model get updated with 1.5 batches worth of samples,
whereas the weights of the generator model are updated with one batch worth of samples each
iteration. Changing this so that each model is updated by the same amount might improve the
model training process.

```
# train the generator and discriminator
def train(g_model, d_model, c_model, gan_model, dataset, latent_dim, n_epochs=20,
n_batch=100):
# select supervised dataset
X_sup, y_sup = select_supervised_samples(dataset)
print(X_sup.shape, y_sup.shape)
# calculate the number of batches per training epoch
bat_per_epo = int(dataset[0].shape[0] / n_batch)
# calculate the number of training iterations
n_steps = bat_per_epo * n_epochs
# calculate the size of half a batch of samples
half_batch = int(n_batch / 2)
print('n_epochs=%d, n_batch=%d, 1/2=%d, b/e=%d, steps=%d' % (n_epochs, n_batch,
half_batch, bat_per_epo, n_steps))
# manually enumerate epochs
for i in range(n_steps):
# update supervised discriminator (c)
[Xsup_real, ysup_real], _ = generate_real_samples([X_sup, y_sup], half_batch)
c_loss, c_acc = c_model.train_on_batch(Xsup_real, ysup_real)
# update unsupervised discriminator (d)
[X_real, _], y_real = generate_real_samples(dataset, half_batch)20.4. How to Develop a Semi-Supervised GAN for MNIST 440
d_loss1 = d_model.train_on_batch(X_real, y_real)
X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
d_loss2 = d_model.train_on_batch(X_fake, y_fake)
# update generator (g)
X_gan, y_gan = generate_latent_points(latent_dim, n_batch), ones((n_batch, 1))
g_loss = gan_model.train_on_batch(X_gan, y_gan)
# summarize loss on this batch
print('>%d, c[%.3f,%.0f], d[%.3f,%.3f], g[%.3f]' % (i+1, c_loss, c_acc*100, d_loss1,
d_loss2, g_loss))
# evaluate the model performance every so often
if (i+1) % (bat_per_epo * 1) == 0:
summarize_performance(i, g_model, c_model, latent_dim, dataset)
```
