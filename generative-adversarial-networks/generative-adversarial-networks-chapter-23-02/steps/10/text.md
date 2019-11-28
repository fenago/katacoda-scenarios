
The generate fake samples() function below uses the generator model and a batch of real
source images to generate an equivalent batch of target images for the discriminator. These are
returned with the label class = 0 to indicate to the discriminator that they are fake.

```
# generate a batch of images, returns images and targets
def generate_fake_samples(g_model, samples, patch_shape):
# generate fake instance
X = g_model.predict(samples)
# create 'fake' class labels (0)
y = zeros((len(X), patch_shape, patch_shape, 1))
return X, y
```

Typically, GAN models do not converge; instead, an equilibrium is found between the
generator and discriminator models. As such, we cannot easily judge when training should stop.
Therefore, we can save the model and use it to generate sample image-to-image translations
periodically during training, such as every 10 training epochs. We can then review the generated images at the end of training and use the image quality to choose a final model. The
summarize performance() function implements this, taking the generator model at a point
during training and using it to generate a number, in this case three, of translations of randomly
selected images in the dataset. The source, generated image, and expected target are then
plotted as three rows of images and the plot saved to file. Additionally, the model is saved to an
H5 formatted file that makes it easier to load later. Both the image and model filenames include
the training iteration number, allowing us to easily tell them apart at the end of training.

```
# generate samples and save as a plot and save the model
def summarize_performance(step, g_model, dataset, n_samples=3):
# select a sample of input images
[X_realA, X_realB], _ = generate_real_samples(dataset, n_samples, 1)
# generate a batch of fake samples
X_fakeB, _ = generate_fake_samples(g_model, X_realA, 1)
# scale all pixels from [-1,1] to [0,1]
X_realA = (X_realA + 1) / 2.0
X_realB = (X_realB + 1) / 2.0
X_fakeB = (X_fakeB + 1) / 2.0
# plot real source images23.4. How to Develop and Train a Pix2Pix Model 494
for i in range(n_samples):
pyplot.subplot(3, n_samples, 1 + i)
pyplot.axis('off')
pyplot.imshow(X_realA[i])
# plot generated target image
for i in range(n_samples):
pyplot.subplot(3, n_samples, 1 + n_samples + i)
pyplot.axis('off')
pyplot.imshow(X_fakeB[i])
# plot real target image
for i in range(n_samples):
pyplot.subplot(3, n_samples, 1 + n_samples*2 + i)
pyplot.axis('off')
pyplot.imshow(X_realB[i])
# save plot to file
filename1 = 'plot_%06d.png' % (step+1)
pyplot.savefig(filename1)
pyplot.close()
# save the generator model
filename2 = 'model_%06d.h5' % (step+1)
g_model.save(filename2)
print('>Saved: %s and %s' % (filename1, filename2))
```
