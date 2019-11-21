Finally, the composite GAN model requires updating. The new GAN model will take a point
in latent space as input and a class label and generate a prediction of whether input was real or
fake, as before. Using the functional API to design the model, it is important that we explicitly
connect the image generated output from the generator as well as the class label input, both as
input to the discriminator model. This allows the same class label input to flow down into the
generator and down into the discriminator. The define gan() function below implements the
conditional version of the GAN.

```
# define the combined generator and discriminator model, for updating the generator
def define_gan(g_model, d_model):
# make weights in the discriminator not trainable
d_model.trainable = False
# get noise and label inputs from generator model
gen_noise, gen_label = g_model.input
# get image output from the generator model
gen_output = g_model.output
# connect image output and label input from generator as inputs to discriminator
gan_output = d_model([gen_output, gen_label])
# define gan model as taking noise and label and outputting a classification
model = Model([gen_noise, gen_label], gan_output)
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt)
return model
```

The plot below summarizes the composite GAN model. Importantly, it shows the generator
model in full with the point in latent space and class label as input, and the connection of the
output of the generator and the same class label as input to the discriminator model (last box
at the bottom of the plot) and the output of a single class label classification of real or fake

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-17-02/steps/13/3.PNG)