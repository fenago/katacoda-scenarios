
This tutorial is divided into three parts; they are:
1. Dataset Directory Structure
2. Example Dataset Structure
3. How to Progressively Load Images

#### Dataset Directory Structure
There is a standard way to lay out your image data for modeling. After you have collected
your images, you must sort them first by dataset, such as train, test, and validation, and
second by their class. For example, imagine an image classification problem where we wish to
classify photos of cars based on their color, e.g. red cars, blue cars, etc. First, we have a data/
directory where we will store all of the image data. Next, we will have a data/train/ directory
for the training dataset and a data/test/ for the holdout test dataset. We may also have a
data/validation/ for a validation dataset during training. So far, we have:

```
data/
data/train/
data/test/
data/validation/
```


Under each of the dataset directories, we will have subdirectories, one for each class where
the actual image files will be placed. For example, if we have a binary classification task for
classifying photos of cars as either a red car or a blue car, we would have two classes, red and
blue, and therefore two class directories under each dataset directory. For example:

```
data/
data/train/
data/train/red/
data/train/blue/
data/test/
data/test/red/
data/test/blue/
data/validation/
data/validation/red/
data/validation/blue/
```
