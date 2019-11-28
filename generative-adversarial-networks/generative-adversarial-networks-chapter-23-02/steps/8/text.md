The define gan() function below
implements this, taking the already-defined generator and discriminator models as arguments
and using the Keras functional API to connect them together into a composite model. Both
loss functions are specified for the two outputs of the model and the weights used for each are
specified in the loss weights argument to the compile() function.

```
# define the combined generator and discriminator model, for updating the generator
def define_gan(g_model, d_model, image_shape):
# make weights in the discriminator not trainable
d_model.trainable = False
# define the source image
in_src = Input(shape=image_shape)
# connect the source image to the generator input
gen_out = g_model(in_src)
# connect the source input and generator output to the discriminator input
dis_out = d_model([in_src, gen_out])
# src image as input, generated image and classification output
model = Model(in_src, [dis_out, gen_out])
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss=['binary_crossentropy', 'mae'], optimizer=opt, loss_weights=[1,100])
return model
```
