We need to record the performance of the model. Perhaps the most reliable way to evaluate
the performance of a GAN is to use the generator to generate images, and then review and
subjectively evaluate them. The summarize performance() function below takes the generator
model at a given point during training and uses it to generate 100 images in a 10 × 10 grid,
that are then plotted and saved to file. The model is also saved to file at this time, in case we
would like to use it later to generate more images.

```
# generate samples and save as a plot and save the model
def summarize_performance(step, g_model, latent_dim, n_samples=100):
# prepare fake examples
X, _ = generate_fake_samples(g_model, latent_dim, n_samples)16.5. How to Train a Wasserstein GAN Model 318
# scale from [-1,1] to [0,1]
X = (X + 1) / 2.0
# plot images
for i in range(10 * 10):
# define subplot
pyplot.subplot(10, 10, 1 + i)
# turn off axis
pyplot.axis('off')
# plot raw pixel data
pyplot.imshow(X[i, :, :, 0], cmap='gray_r')
# save plot to file
filename1 = 'generated_plot_%04d.png' % (step+1)
pyplot.savefig(filename1)
pyplot.close()
# save the generator model
filename2 = 'model_%04d.h5' % (step+1)
g_model.save(filename2)
print('>Saved: %s and %s' % (filename1, filename2))
```
