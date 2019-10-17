We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_24/01_save_model.py` to view file.

#### Run Code

Now, run the python code by running: `python 01_save_model.py`{{execute}}

Running the example may take a little more than **three** minute to execute. As the weight file is loaded, you will see debug information reported about what was loaded, output by the WeightReader class.

```
loading weights of convolution #99
loading weights of convolution #100
loading weights of convolution #101
loading weights of convolution #102
loading weights of convolution #103
loading weights of convolution #104
loading weights of convolution #105
```

At the end of the run, the `model.h5` file is saved in your current working directory with
approximately the same size as the original weight file (237MB), but ready to be loaded and
used directly as a Keras model.

