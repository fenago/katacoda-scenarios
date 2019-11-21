
We are also interested in the behavior of loss during training. As such, we can record loss in
lists across each training iteration, then create and save a line plot of the learning dynamics of the
models. Creating and saving the plot of learning curves is implemented in the plot history()
function.

```
# create a line plot of loss for the gan and save to file
def plot_history(d1_hist, d2_hist, g_hist):
pyplot.plot(d1_hist, label='dloss1')
pyplot.plot(d2_hist, label='dloss2')
pyplot.plot(g_hist, label='gloss')
pyplot.legend()
filename = 'plot_line_plot_loss.png'
pyplot.savefig(filename)
pyplot.close()
print('Saved %s' % (filename))
```

Finally, we can define the main training loop via the train() function. The function takes
the defined models and dataset as arguments and parameterizes the number of training epochs
and batch size as default function arguments. Each training loop involves first generating a
half-batch of real and fake samples and using them to create one batch worth of weight updates
to the discriminator. Next, the generator is updated via the composite model, providing the real
(y=1) target as the expected output for the model. The loss is reported each training iteration,
and the model performance is summarized in terms of a plot of generated images at the end of
every epoch. The plot of learning curves is created and saved at the end of the run.