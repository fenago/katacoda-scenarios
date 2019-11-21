
Next, a GAN model can be defined that combines both the generator model and the
discriminator model into one larger model. This larger model will be used to train the model
weights in the generator, using the output and error calculated by the discriminator model. The
discriminator model is trained separately, and as such, the model weights are marked as not
trainable in this larger GAN model to ensure that only the weights of the generator model are
updated. This change to the trainability of the discriminator weights only has an effect when
training the combined GAN model, not when training the discriminator standalone.
This larger GAN model takes as input a point in the latent space, uses the generator model
to generate an image which is fed as input to the discriminator model, then is output or classified
as real or fake. The define gan() function below implements this, taking the already-defined
generator and discriminator models as input.

```
# define the combined generator and discriminator model, for updating the generator
def define_gan(generator, discriminator):
# make weights in the discriminator not trainable
discriminator.trainable = False
# connect them
model = Sequential()
# add generator
model.add(generator)
# add the discriminator
model.add(discriminator)
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt)
return model
```
