We can load the MNIST dataset and summarize the dataset. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_07/01_mnist_dataset.py` to view file.


#### Run Code
Now, run the python code by running: `python 01_mnist_dataset.py`{{execute}}

Running the example first loads the dataset into memory. Then the shape of the train and
test datasets is reported. We can see that all images are 28 by 28 pixels with a single channel
for black-and-white images. There are 60,000 images for the training dataset and 10,000 for the
test dataset. We can also see that pixel values are integer values between 0 and 255 and that
the mean and standard deviation of the pixel values are similar between the two datasets.

```
Train (60000, 28, 28) (60000,)
Test ((10000, 28, 28), (10000,))
Train 0 255 33.318421449829934 78.56748998339798
Test 0 255 33.791224489795916 79.17246322228644
```

We will use this dataset to explore different pixel scaling methods using the ImageDataGenerator
class in Keras.