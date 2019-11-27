Next, a GAN model can be defined that combines both the generator model and the critic
model into one larger model. This larger model will be used to train the model weights in the
generator, using the output and error calculated by the critic model. The critic model is trained
separately, and as such, the model weights are marked as not trainable in this larger GAN
model to ensure that only the weights of the generator model are updated. This change to the
trainability of the critic weights only has an effect when training the combined GAN model, not
when training the critic standalone.
This larger GAN model takes as input a point in the latent space, uses the generator model
to generate an image, which is fed as input to the critic model, then scored as real or fake. The
model is fit using RMSProp with the custom wasserstein loss() function. The define gan()
function below implements this, taking the already defined generator and critic models as input.

```
# define the combined generator and critic model, for updating the generator
def define_gan(generator, critic):
# make weights in the critic not trainable
critic.trainable = False
# connect them
model = Sequential()
# add generator
model.add(generator)
# add the critic
model.add(critic)
# compile model
opt = RMSprop(lr=0.00005)
model.compile(loss=wasserstein_loss, optimizer=opt)
return model
```

