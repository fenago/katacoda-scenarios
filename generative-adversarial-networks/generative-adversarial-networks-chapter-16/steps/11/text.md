We are now ready to fit the GAN model. The model is fit for 10 training epochs, which is
arbitrary, as the model begins generating plausible number-7 digits after perhaps the first few
epochs. A batch size of 64 samples is used, and each training epoch involves 6265 64 , or about 97,
batches of real and fake samples and updates to the model. The model is therefore trained for
10 epochs of 97 batches, or 970 iterations. First, the critic model is updated for a half batch of
real samples, then a half batch of fake samples, together forming one batch of weight updates.
This is then repeated n critic (5) times as required by the WGAN algorithm. The generator
is then updated via the composite GAN model. Importantly, the target label is set to -1 or real
for the generated samples. This has the effect of updating the generator toward getting better
at generating real samples on the next batch.

The train() function below implements this, taking the defined models, dataset, and size
of the latent dimension as arguments and parameterizing the number of epochs and batch size
with default arguments. The generator model is saved at the end of training. The performance
of the critic and generator models is reported each iteration. Sample images are generated and
saved every epoch, and line plots of model performance are created and saved at the end of the
run.

```
# train the generator and critic
def train(g_model, c_model, gan_model, dataset, latent_dim, n_epochs=10, n_batch=64,
n_critic=5):
# calculate the number of batches per training epoch
bat_per_epo = int(dataset.shape[0] / n_batch)
# calculate the number of training iterations
n_steps = bat_per_epo * n_epochs
# calculate the size of half a batch of samples
half_batch = int(n_batch / 2)
# lists for keeping track of loss
c1_hist, c2_hist, g_hist = list(), list(), list()
# manually enumerate epochs
for i in range(n_steps):
# update the critic more than the generator
c1_tmp, c2_tmp = list(), list()
for _ in range(n_critic):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update critic model weights
c_loss1 = c_model.train_on_batch(X_real, y_real)
c1_tmp.append(c_loss1)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
# update critic model weights
c_loss2 = c_model.train_on_batch(X_fake, y_fake)
c2_tmp.append(c_loss2)
# store critic loss
c1_hist.append(mean(c1_tmp))
c2_hist.append(mean(c2_tmp))
# prepare points in latent space as input for the generator
X_gan = generate_latent_points(latent_dim, n_batch)
# create inverted labels for the fake samples
y_gan = -ones((n_batch, 1))
# update the generator via the critic's error
g_loss = gan_model.train_on_batch(X_gan, y_gan)
g_hist.append(g_loss)
# summarize loss on this batch
print('>%d, c1=%.3f, c2=%.3f g=%.3f' % (i+1, c1_hist[-1], c2_hist[-1], g_loss))
# evaluate the model performance every 'epoch'
if (i+1) % bat_per_epo == 0:
summarize_performance(i, g_model, latent_dim)
# line plots of loss
plot_history(c1_hist, c2_hist, g_hist)
```
