
We are now ready to fit the GAN model. The model is fit for 10 training epochs, which is
arbitrary, as the model begins generating plausible number-8 digits after perhaps the first few
epochs. A batch size of 128 samples is used, and each training epoch involves 5851/128 or about 45
batches of real and fake samples and updates to the model. The model is therefore trained for
10 epochs of 45 batches, or 450 iterations. First, the discriminator model is updated for a half
batch of real samples, then a half batch of fake samples, together forming one batch of weight
updates. The generator is then updated via the composite GAN model. Importantly, the class
label is set to 1, or real, for the fake samples. This has the effect of updating the generator
toward getting better at generating real samples on the next batch.
The train() function below implements this, taking the defined models, dataset, and size of
the latent dimension as arguments and parameterizing the number of epochs and batch size with
default arguments. The generator model is saved at the end of training. The performance of
the discriminator and generator models is reported each iteration. Sample images are generated
and saved every epoch, and line plots of model performance are created and saved at the end of
the run.

```
# train the generator and discriminator
def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=10, n_batch=128):
# calculate the number of batches per epoch
bat_per_epo = int(dataset.shape[0] / n_batch)
# calculate the total iterations based on batch and epoch
n_steps = bat_per_epo * n_epochs
# calculate the number of samples in half a batch
half_batch = int(n_batch / 2)
# prepare lists for storing stats each iteration
d1_hist, d2_hist, g_hist, a1_hist, a2_hist = list(), list(), list(), list(), list()
# manually enumerate epochs
for i in range(n_steps):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update discriminator model weights
d_loss1, d_acc1 = d_model.train_on_batch(X_real, y_real)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
# update discriminator model weights
d_loss2, d_acc2 = d_model.train_on_batch(X_fake, y_fake)
# prepare points in latent space as input for the generator
X_gan = generate_latent_points(latent_dim, n_batch)
# create inverted labels for the fake samples
y_gan = ones((n_batch, 1))
# update the generator via the discriminator's error
g_loss = gan_model.train_on_batch(X_gan, y_gan)
# summarize loss on this batch
print('>%d, d1=%.3f, d2=%.3f g=%.3f, a1=%d, a2=%d' %
(i+1, d_loss1, d_loss2, g_loss, int(100*d_acc1), int(100*d_acc2)))
# record history
d1_hist.append(d_loss1)
d2_hist.append(d_loss2)
g_hist.append(g_loss)
a1_hist.append(d_acc1)
a2_hist.append(d_acc2)
# evaluate the model performance every 'epoch'
if (i+1) % bat_per_epo == 0:
summarize_performance(i, g_model, latent_dim)
plot_history(d1_hist, d2_hist, g_hist, a1_hist, a2_hist)
```
