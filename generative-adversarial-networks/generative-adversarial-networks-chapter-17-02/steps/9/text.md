
We are now ready to fit the GAN models. The model is fit for 100 training epochs, which is
arbitrary, as the model begins generating plausible items of clothing after perhaps 20 epochs. A
batch size of 128 samples is used, and each training epoch involves 60000/128 , or about 468 batches
of real and fake samples and updates to the model. First, the discriminator model is updated
for a half batch of real samples, then a half batch of fake samples, together forming one batch of
weight updates. The generator is then updated via the composite GAN model. Importantly, the
class label is set to 1 or real for the fake samples. This has the effect of updating the generator
toward getting better at generating real samples on the next batch. The train() function
below implements this, taking the defined models, dataset, and size of the latent dimension as
arguments and parameterizing the number of epochs and batch size with default arguments.
The generator model is saved at the end of training.

```
# train the generator and discriminator
def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=128):
bat_per_epo = int(dataset.shape[0] / n_batch)
half_batch = int(n_batch / 2)
# manually enumerate epochs
for i in range(n_epochs):
# enumerate batches over the training set
for j in range(bat_per_epo):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update discriminator model weights
d_loss1, _ = d_model.train_on_batch(X_real, y_real)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
# update discriminator model weights
d_loss2, _ = d_model.train_on_batch(X_fake, y_fake)
# prepare points in latent space as input for the generator
X_gan = generate_latent_points(latent_dim, n_batch)
# create inverted labels for the fake samples
y_gan = ones((n_batch, 1))
# update the generator via the discriminator's error
g_loss = gan_model.train_on_batch(X_gan, y_gan)
# summarize loss on this batch
print('>%d, %d/%d, d1=%.3f, d2=%.3f g=%.3f' %
(i+1, j+1, bat_per_epo, d_loss1, d_loss2, g_loss))
# save the generator model
g_model.save('generator.h5')
```

We can then define the size of the latent space, define all three models, and train them on
the loaded Fashion-MNIST dataset.

```
...
# size of the latent space
latent_dim = 100
# create the discriminator
discriminator = define_discriminator()
# create the generator
generator = define_generator(latent_dim)
# create the gan
gan_model = define_gan(generator, discriminator)
# load image data
dataset = load_real_samples()
# train model
train(generator, discriminator, gan_model, dataset, latent_dim)
```
