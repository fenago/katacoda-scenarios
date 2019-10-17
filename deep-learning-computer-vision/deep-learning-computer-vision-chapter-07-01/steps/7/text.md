We can run the normalization code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_07/02_normalization.py` to view file.

#### Run Normalization Code
Running the example first reports the minimum and maximum pixel value for the train
and test datasets. The MNIST dataset only has a single channel because the images are black
and white (grayscale), but if the images were color, the min and max pixel values would be
calculated across all channels in all images in the training dataset, i.e. there would not be a
separate mean value for each channel.

Now, run the python code by running: `python 02_normalization.py`{{execute}}


The `ImageDataGenerator` does not need to be fit on the training dataset as there is nothing
that needs to be calculated, we have provided the scale factor directly. A single batch of
normalized images is retrieved and we can confirm that the min and max pixel values are zero
and one respectively.

```
Using TensorFlow backend.
Train min=0.000, max=255.000
Test min=0.000, max=255.000
Batches train=938, test=157
Batch shape=(64, 28, 28, 1), min=0.000, max=1.000
```
