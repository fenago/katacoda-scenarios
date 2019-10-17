We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_07/03_centering.py` to view file.


#### Run Code
Now, run the python code by running: `python 03_centering.py`{{execute}}


Running the example first reports the mean pixel value for the train and test datasets. The
MNIST dataset only has a single channel because the images are black and white (grayscale),
but if the images were color, the mean pixel values would be calculated across all channels in all
images in the training dataset, i.e. there would not be a separate mean value for each channel.

The ImageDataGenerator is fit on the training dataset and we can confirm that the mean pixel
value matches our own manual calculation. A single batch of centered images is retrieved and
we can confirm that the mean pixel value is a small-ish value close to zero. The test is repeated
using the entire training dataset as the batch size, and in this case, the mean pixel value for the
scaled dataset is a number very close to zero, confirming that centering is having the desired
effect. Note: your statistics may vary slightly due to a different random batch of images being
selected.

```
Means train=33.318, test=33.791
Data Generator Mean: 33.318
(64, 28, 28, 1) 0.09971977
(60000, 28, 28, 1) -1.9512918e-05
```

Example output from feature-wise centering on the MNIST dataset.