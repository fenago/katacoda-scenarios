
In addition to image quality, it is a good idea to keep track of the loss and accuracy of the
model over time. The loss and classification accuracy for the discriminator for real and fake
samples can be tracked for each model update, as can the loss for the generator for each update.
These can then be used to create line plots of loss and accuracy at the end of the training run.
The plot history() function below implements this and saves the results to file.

```
# create a line plot of loss for the gan and save to file
def plot_history(d1_hist, d2_hist, g_hist, a1_hist, a2_hist):
# plot loss
pyplot.subplot(2, 1, 1)
pyplot.plot(d1_hist, label='d-real')
pyplot.plot(d2_hist, label='d-fake')
pyplot.plot(g_hist, label='gen')
pyplot.legend()
# plot discriminator accuracy
pyplot.subplot(2, 1, 2)
pyplot.plot(a1_hist, label='acc-real')
pyplot.plot(a2_hist, label='acc-fake')
pyplot.legend()
# save plot to file
pyplot.savefig('results_baseline/plot_line_plot_loss.png')
pyplot.close()
```
