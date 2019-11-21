
Plots of generated images are saved at the end of every epoch or after every 1,187 training
iterations and the iteration number is used in the filename.

```
AtoB_generated_plot_001187.png
AtoB_generated_plot_002374.png
...
BtoA_generated_plot_001187.png
BtoA_generated_plot_002374.png
```

Models are saved after training iterations, and again
the iteration number is used in the filenames.

```
g_model_AtoB_053415.h5
g_model_AtoB_059350.h5
...
g_model_BtoA_053415.h5
g_model_BtoA_059350.h5
```

The plots of generated images can be used to choose a model and more training iterations
may not necessarily mean better quality generated images. Horses to Zebras translation starts to become reliable after about 50 epochs.