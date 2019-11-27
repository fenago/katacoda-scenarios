The generator model takes as input a point in the latent space and outputs a single 28 × 28
grayscale image. This is achieved by using a fully connected layer to interpret the point in the
latent space and provide sufficient activations that can be reshaped into many copies (in this case,
128) of a low-resolution version of the output image (e.g. 7 × 7). This is then upsampled two
times, doubling the size and quadrupling the area of the activations each time using transpose
convolutional layers. The model uses best practices such as the LeakyReLU activation, a kernel
size that is a factor of the stride size, and a hyperbolic tangent (Tanh) activation function in
the output layer.
The define generator() function below defines the generator model but intentionally does
not compile it as it is not trained directly, then returns the model. The size of the latent space
is parameterized as a function argument.

```
# define the standalone generator model
def define_generator(latent_dim):
# weight initialization
init = RandomNormal(stddev=0.02)
# define model
model = Sequential()
# foundation for 7x7 image
n_nodes = 128 * 7 * 7
model.add(Dense(n_nodes, kernel_initializer=init, input_dim=latent_dim))
model.add(LeakyReLU(alpha=0.2))
model.add(Reshape((7, 7, 128)))
# upsample to 14x14
model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same',
kernel_initializer=init))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# upsample to 28x28
model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same',
kernel_initializer=init))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# output 28x28x1
model.add(Conv2D(1, (7,7), activation='tanh', padding='same', kernel_initializer=init))
return model
```

