We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_08/01_load_dataset.py` to view file.

#### Run Code
Running the example first creates an instance of the `ImageDataGenerator` with all of the
default configuration. Next, three iterators are created, one for each of the train, validation,
and test binary classification datasets. As each iterator is created, we can see debug messages
reporting the number of images and classes discovered and prepared. Finally, we test out the
train iterator that would be used to fit a model. The first batch of images is retrieved and we
can confirm that the batch contains two images, as only two images were available. We can also
confirm that the images were loaded and forced to the square dimensions of 256 rows and 256
columns of pixels and the pixel data was not scaled and remains in the range [0, 255].

Now, run the python code by running: `python 01_load_dataset.py`{{execute}}

```
Found 2 images belonging to 2 classes.
Found 2 images belonging to 2 classes.
Found 2 images belonging to 2 classes.
Batch shape=(2, 256, 256, 3), min=0.000, max=255.000
```

Example output loading a dataset from directory with Keras.