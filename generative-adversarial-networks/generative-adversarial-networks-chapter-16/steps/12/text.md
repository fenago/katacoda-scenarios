Now that all of the functions have been defined, we can create the models, load the dataset,
and begin the training process.

```
...
# size of the latent space
latent_dim = 50
# create the critic16.5. How to Train a Wasserstein GAN Model 320
critic = define_critic()
# create the generator
generator = define_generator(latent_dim)
# create the gan
gan_model = define_gan(generator, critic)
# load image data
dataset = load_real_samples()
print(dataset.shape)
# train model
train(generator, critic, gan_model, dataset, latent_dim)
```
