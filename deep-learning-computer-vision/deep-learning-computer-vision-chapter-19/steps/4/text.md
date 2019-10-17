The Fashion-MNIST dataset is proposed as a more challenging replacement dataset for the
MNIST dataset. It is a dataset comprised of 60,000 small square 28 × 28 pixel grayscale images
of items of 10 types of clothing, such as shoes, t-shirts, dresses, and more. The mapping of all
0-9 integers to class labels is listed below.
- 0: T-shirt/top
- 1: Trouser
- 2: Pullover
- 3: Dress
- 4: Coat
- 5: Sandal
- 6: Shirt
- 7: Sneaker
- 8: Bag
- 9: Ankle boot

It is a more challenging classification problem than MNIST and top results are achieved by
deep learning convolutional neural networks with a classification accuracy of about 90% to 95%
on the hold out test dataset. The example below loads the Fashion-MNIST dataset using the
Keras API and creates a plot of the first nine images in the training dataset.

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_19/01_load_dataset.py` to view file.

#### Run Code
**Note:** It will take some time to complete.

Now, run the python code by running: `python 01_load_dataset.py`{{execute}}

Running the example loads the Fashion-MNIST train and test dataset and prints their shape.
We can see that there are 60,000 examples in the training dataset and 10,000 in the test dataset
and that images are indeed square with 28 × 28 pixels.
