In this section, we will develop a conditional GAN for the Fashion-MNIST dataset by updating
the unconditional GAN developed in the previous section. The best way to design models in
Keras to have multiple inputs is by using the Functional API, as opposed to the Sequential API
used in the previous section. We will use the functional API to re-implement the discriminator,
generator, and the composite model. Starting with the discriminator model, a new second input
is defined that takes an integer for the class label of the image. This has the effect of making
the input image conditional on the provided class label.

The class label is then passed through an Embedding layer with the size of 50. This means
that each of the 10 classes for the Fashion-MNIST dataset (0 through 9) will map to a different
50-element vector representation that will be learned by the discriminator model. The output
of the embedding is then passed to a fully connected layer with a linear activation. 

Importantly,
the fully connected layer has enough activations that can be reshaped into one channel of a
28×28 image. The activations are reshaped into single 28×28 activation map and concatenated
with the input image. This has the effect of looking like a two-channel input image to the
next convolutional layer. The define discriminator() below implements this update to
the discriminator model. The parameterized shape of the input image is also used after the
embedding layer to define the number of activations for the fully connected layer to reshape its
output. The number of classes in the problem is also parameterized in the function and set.

```
# define the standalone discriminator model
def define_discriminator(in_shape=(28,28,1), n_classes=10):
# label input
in_label = Input(shape=(1,))
# embedding for categorical input
li = Embedding(n_classes, 50)(in_label)
# scale up to image dimensions with linear activation
n_nodes = in_shape[0] * in_shape[1]
li = Dense(n_nodes)(li)
# reshape to additional channel
li = Reshape((in_shape[0], in_shape[1], 1))(li)
# image input
in_image = Input(shape=in_shape)
# concat label as a channel
merge = Concatenate()([in_image, li])
# downsample
fe = Conv2D(128, (3,3), strides=(2,2), padding='same')(merge)
fe = LeakyReLU(alpha=0.2)(fe)
# downsample
fe = Conv2D(128, (3,3), strides=(2,2), padding='same')(fe)
fe = LeakyReLU(alpha=0.2)(fe)
# flatten feature maps
fe = Flatten()(fe)
# dropout
fe = Dropout(0.4)(fe)
# output
out_layer = Dense(1, activation='sigmoid')(fe)
# define model
model = Model([in_image, in_label], out_layer)
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
return model
```

In order to make the architecture clear, below is a plot of the discriminator model. The plot
shows the two inputs: first the class label that passes through the embedding (left) and the
image (right), and their concatenation into a two-channel 28×28 image or feature map (middle).
The rest of the model is the same as the discriminator designed in the previous section.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-17-02/steps/13/1.PNG)
