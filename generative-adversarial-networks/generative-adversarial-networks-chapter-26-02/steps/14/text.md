
The summarize performance() function below uses a given generator model to generate
translated versions of a few randomly selected source photographs and saves the plot to file.
The source images are plotted on the first row and the generated images are plotted on the
second row. Again, the plot filename includes the training iteration number.

```
# generate samples and save as a plot and save the model
def summarize_performance(step, g_model, trainX, name, n_samples=5):
# select a sample of input images
X_in, _ = generate_real_samples(trainX, n_samples, 0)
# generate translated images
X_out, _ = generate_fake_samples(g_model, X_in, 0)
# scale all pixels from [-1,1] to [0,1]
X_in = (X_in + 1) / 2.0
X_out = (X_out + 1) / 2.0
# plot real images
for i in range(n_samples):
pyplot.subplot(2, n_samples, 1 + i)
pyplot.axis('off')
pyplot.imshow(X_in[i])
# plot translated image
for i in range(n_samples):
pyplot.subplot(2, n_samples, 1 + n_samples + i)
pyplot.axis('off')
pyplot.imshow(X_out[i])
# save plot to file
filename1 = '%s_generated_plot_%06d.png' % (name, (step+1))
pyplot.savefig(filename1)
pyplot.close()
```
