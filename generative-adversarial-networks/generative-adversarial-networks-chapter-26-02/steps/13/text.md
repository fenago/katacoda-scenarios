
Similarly, a sample of generated images is required to update each discriminator model in
each training iteration. The generate fake samples() function below generates this sample
given a generator model and the sample of real images from the source domain. Again, target
values for each generated image are provided with the correct shape of the PatchGAN, indicating
that they are fake or generated (target = 0.0).

```
# generate a batch of images, returns images and targets
def generate_fake_samples(g_model, dataset, patch_shape):
# generate fake instance
X = g_model.predict(dataset)
# create 'fake' class labels (0)
y = zeros((len(X), patch_shape, patch_shape, 1))
return X, y
```

Typically, GAN models do not converge; instead, an equilibrium is found between the
generator and discriminator models. As such, we cannot easily judge whether training should
stop. Therefore, we can save the model and use it to generate sample image-to-image translations
periodically during training, such as every one or five training epochs. We can then review the
generated images at the end of training and use the image quality to choose a final model. The
save models() function below will save each generator model to the current directory in H5
format, including the training iteration number in the filename.

```
# save the generator models to file
def save_models(step, g_model_AtoB, g_model_BtoA):
# save the first generator model
filename1 = 'g_model_AtoB_%06d.h5' % (step+1)
g_model_AtoB.save(filename1)
# save the second generator model
filename2 = 'g_model_BtoA_%06d.h5' % (step+1)
g_model_BtoA.save(filename2)
print('>Saved: %s and %s' % (filename1, filename2))
```
