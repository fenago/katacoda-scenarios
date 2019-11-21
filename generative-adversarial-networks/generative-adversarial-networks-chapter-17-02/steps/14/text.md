Next, the generator model must be updated to take the class label. This has the effect
of making the point in the latent space conditional on the provided class label. As in the
discriminator, the class label is passed through an embedding layer to map it to a unique
50-element vector and is then passed through a fully connected layer with a linear activation
before being resized. In this case, the activations of the fully connected layer are resized
into a single 7 × 7 feature map. This is to match the 7 × 7 feature map activations of the
unconditional generator model. The new 7 × 7 feature map is added as one more channel to
the existing 128, resulting in 129 feature maps that are then upsampled as in the prior model.

The define generator() function below implements this, again parameterizing the number of
classes as we did with the discriminator model.

```
# define the standalone generator model
def define_generator(latent_dim, n_classes=10):
# label input
in_label = Input(shape=(1,))
# embedding for categorical input
li = Embedding(n_classes, 50)(in_label)
# linear multiplication
n_nodes = 7 * 7
li = Dense(n_nodes)(li)
# reshape to additional channel
li = Reshape((7, 7, 1))(li)
# image generator input
in_lat = Input(shape=(latent_dim,))
# foundation for 7x7 image
n_nodes = 128 * 7 * 7
gen = Dense(n_nodes)(in_lat)
gen = LeakyReLU(alpha=0.2)(gen)
gen = Reshape((7, 7, 128))(gen)
# merge image gen and label input
merge = Concatenate()([gen, li])
# upsample to 14x14
gen = Conv2DTranspose(128, (4,4), strides=(2,2), padding='same')(merge)
gen = LeakyReLU(alpha=0.2)(gen)
# upsample to 28x28
gen = Conv2DTranspose(128, (4,4), strides=(2,2), padding='same')(gen)
gen = LeakyReLU(alpha=0.2)(gen)
# output
out_layer = Conv2D(1, (7,7), activation='tanh', padding='same')(gen)
# define model
model = Model([in_lat, in_label], out_layer)
return model
```

To help understand the new model architecture, the image below provides a plot of the new
conditional generator model. In this case, you can see the 100-element point in latent space as
input and subsequent resizing (left) and the new class label input and embedding layer (right),
then the concatenation of the two sets of feature maps (center). The remainder of the model is
the same as the unconditional case

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-17-02/steps/13/2.PNG)