
We are now ready to fit the GAN models. The model is fit for 100 training epochs, which is
arbitrary, as the model begins generating plausible items of clothing after perhaps 20 epochs. A
batch size of 64 samples is used, and each training epoch involves 60000 64 , or about 937, batches
of real and fake samples and updates to the model. The summarize performance() function
is called every 10 epochs, or every (937 × 10) 9,370 training steps. For a given training step,
first the discriminator model is updated for a half batch of real samples, then a half batch of
fake samples, together forming one batch of weight updates. The generator is then updated via
the combined GAN model. Importantly, the class label is set to 1, or real, for the fake samples.
This has the effect of updating the generator toward getting better at generating real samples
on the next batch.

The discriminator and composite model return three loss values from the call to the
train on batch() function. The first value is the sum of the loss values and can be ignored, whereas the second value is the loss for the real/fake output layer and the third value is
the loss for the clothing label classification. The train() function below implements this, taking
the defined models, dataset, and size of the latent dimension as arguments and parameterizing
the number of epochs and batch size with default arguments. The generator model is saved at
the end of training.

```
# train the generator and discriminator
def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=64):
# calculate the number of batches per training epoch
bat_per_epo = int(dataset[0].shape[0] / n_batch)
# calculate the number of training iterations
n_steps = bat_per_epo * n_epochs
# calculate the size of half a batch of samples
half_batch = int(n_batch / 2)
# manually enumerate epochs
for i in range(n_steps):
# get randomly selected 'real' samples
[X_real, labels_real], y_real = generate_real_samples(dataset, half_batch)
# update discriminator model weights
_,d_r1,d_r2 = d_model.train_on_batch(X_real, [y_real, labels_real])
# generate 'fake' examples
[X_fake, labels_fake], y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
# update discriminator model weights
_,d_f,d_f2 = d_model.train_on_batch(X_fake, [y_fake, labels_fake])
# prepare points in latent space as input for the generator
[z_input, z_labels] = generate_latent_points(latent_dim, n_batch)
# create inverted labels for the fake samples
y_gan = ones((n_batch, 1))
# update the generator via the discriminator's error
_,g_1,g_2 = gan_model.train_on_batch([z_input, z_labels], [y_gan, z_labels])
# summarize loss on this batch
print('>%d, dr[%.3f,%.3f], df[%.3f,%.3f], g[%.3f,%.3f]' % (i+1, d_r1,d_r2, d_f,d_f2,
g_1,g_2))
# evaluate the model performance every 'epoch'
if (i+1) % (bat_per_epo * 10) == 0:
summarize_performance(i, g_model, latent_dim)
```
