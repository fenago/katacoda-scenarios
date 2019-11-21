
The generator model will be fit via the unsupervised discriminator model. We will use the
composite model architecture, common to training the generator model when implemented
in Keras. Specifically, weight sharing is used where the output of the generator model is
passed directly to the unsupervised discriminator model, and the weights of the discriminator
are marked as not trainable. The define gan() function below implements this, taking the
already-defined generator and discriminator models as input and returning the composite model
used to train the weights of the generator model.

```
# define the combined generator and discriminator model, for updating the generator
def define_gan(g_model, d_model):
# make weights in the discriminator not trainable
d_model.trainable = False
# connect image output from generator as input to discriminator
gan_output = d_model(g_model.output)
# define gan model as taking noise and outputting a classification
model = Model(g_model.input, gan_output)
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt)
return model
```
