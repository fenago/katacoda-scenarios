
Let’s take a closer look at each step. The constructor for the ImageDataGenerator contains
many arguments to specify how to manipulate the image data after it is loaded, including
pixel scaling and data augmentation. We do not need any of these features at this stage, so
configuring the ImageDataGenerator is easy.
```
# create a data generator
datagen = ImageDataGenerator()
```

Next, an iterator is required to progressively load images for a single dataset. This requires
calling the flow from directory() function and specifying the dataset directory, such as the
train, test, or validation directory. The function also allows you to configure more details related
to the loading of images. Of note is the target size argument that allows you to load all
images to a specific size, which is often required when modeling. The function defaults to square
images with the size (256, 256).

The function also allows you to specify the type of classification task via the class mode
argument, specifically whether it is ‘binary’ or a multiclass classification ‘categorical’. The
default batch size is 32, which means that 32 randomly selected images from across the classes
in the dataset will be returned in each batch when training. Larger or smaller batches may be
desired. You may also want to return batches in a deterministic order when evaluating a model,
which you can do by setting shuffle to False. The subdirectories of images, one for each
class, are loaded by the flow from directory() function in alphabetical order and assigned
an integer for each class. For example, the subdirectory blue comes before red alphabetically,
therefore the class labels are assigned the integers: blue=0, red=1. This can be changed via
the classes argument in calling flow from directory() when training the model.
There are many other options, and I encourage you to review the API documentation.
We can use the same ImageDataGenerator to prepare separate iterators for separate dataset
directories. This is useful if we would like the same pixel scaling applied to multiple datasets
(e.g. train, test, etc.).

```
# load and iterate training dataset
train_it = datagen.flow_from_directory('data/train/', class_mode='binary', batch_size=64)
# load and iterate validation dataset
val_it = datagen.flow_from_directory('data/validation/', class_mode='binary', batch_size=64)
# load and iterate test dataset
test_it = datagen.flow_from_directory('data/test/', class_mode='binary', batch_size=64)
```
