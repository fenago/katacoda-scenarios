Finally, we can train the generator and discriminator models. The train() function below
implements this, taking the defined generator, discriminator, composite model, and loaded
dataset as input. The number of epochs is set at 100 to keep training times down, although
200 was used in the paper. A batch size of 1 is used as is recommended in the paper. Training
involves a fixed number of training iterations. There are 1,097 images in the training dataset.
One epoch is one iteration through this number of examples, with a batch size of one means
1,097 training steps. The generator is saved and evaluated every 10 epochs or every 10,097
training steps, and the model will run for 100 epochs, or a total of 100,097 training steps.
Each training step involves first selecting a batch of real examples, then using the generator to
generate a batch of matching fake samples using the real source images. The discriminator is
then updated with the batch of real images and then fake images.

Next, the generator model is updated providing the real source images as input and providing
class labels of 1 (real) and the real target images as the expected outputs of the model required
for calculating loss. The generator has two loss scores as well as the weighted sum score returned
from the call to train on batch(). We are only interested in the weighted sum score (the first
value returned) as it is used to update the model weights. Finally, the loss for each update is
reported to the console each training iteration and model performance is evaluated every 10
training epochs.

```
# train pix2pix model
def train(d_model, g_model, gan_model, dataset, n_epochs=100, n_batch=1):
# determine the output square shape of the discriminator
n_patch = d_model.output_shape[1]
# unpack dataset
trainA, trainB = dataset
# calculate the number of batches per training epoch
bat_per_epo = int(len(trainA) / n_batch)23.4. How to Develop and Train a Pix2Pix Model 495
# calculate the number of training iterations
n_steps = bat_per_epo * n_epochs
# manually enumerate epochs
for i in range(n_steps):
# select a batch of real samples
[X_realA, X_realB], y_real = generate_real_samples(dataset, n_batch, n_patch)
# generate a batch of fake samples
X_fakeB, y_fake = generate_fake_samples(g_model, X_realA, n_patch)
# update discriminator for real samples
d_loss1 = d_model.train_on_batch([X_realA, X_realB], y_real)
# update discriminator for generated samples
d_loss2 = d_model.train_on_batch([X_realA, X_fakeB], y_fake)
# update the generator
g_loss, _, _ = gan_model.train_on_batch(X_realA, [y_real, X_realB])
# summarize performance
print('>%d, d1[%.3f] d2[%.3f] g[%.3f]' % (i+1, d_loss1, d_loss2, g_loss))
# summarize model performance
if (i+1) % (bat_per_epo * 10) == 0:
summarize_performance(i, g_model, dataset)
```
