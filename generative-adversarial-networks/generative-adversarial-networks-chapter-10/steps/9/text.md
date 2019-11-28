
Next, we need to use the points in the latent space as input to the generator in order to
generate new images. The generate fake samples() function below implements this, taking
the generator model and size of the latent space as arguments, then generating points in the
latent space and using them as input to the generator model. The function returns the generated
images and their corresponding class label for the discriminator model, specifically class = 0 to
indicate they are fake or generated.

```
# use the generator to generate n fake examples, with class labels
def generate_fake_samples(generator, latent_dim, n_samples):
# generate points in latent space
x_input = generate_latent_points(latent_dim, n_samples)
# predict outputs
X = generator.predict(x_input)
# create class labels
y = zeros((n_samples, 1))
return X, y
```

We need to record the performance of the model. Perhaps the most reliable way to evaluate
the performance of a GAN is to use the generator to generate images, and then review and
subjectively evaluate them. The summarize performance() function below takes the generator
model at a given point during training and uses it to generate 100 images in a 10 × 10 grid that
are then plotted and saved to file. The model is also saved to file at this time, in case we would
like to use it later to generate more images.

```
# generate samples and save as a plot and save the model
def summarize_performance(step, g_model, latent_dim, n_samples=100):
# prepare fake examples
X, _ = generate_fake_samples(g_model, latent_dim, n_samples)
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
pyplot.savefig('results_baseline/generated_plot_%03d.png' % (step+1))
pyplot.close()
# save the generator model
g_model.save('results_baseline/model_%03d.h5' % (step+1))
```
