It is possible to write code to manually load image data and return data ready for modeling.
This would include walking the directory structure for a dataset, loading image data, and
returning the input (pixel arrays) and output (class integer). Thankfully, we don’t need to
write this code. Instead, we can use the ImageDataGenerator class provided by Keras. The
main benefit of using this class to load the data is that images are loaded for a single dataset in
batches, meaning that it can be used for loading both small datasets as well as very large image
datasets with thousands or millions of images.

Instead of loading all images into memory, it will load just enough images into memory for
the current and perhaps the next few mini-batches when training and evaluating a deep learning
model. I refer to this as progressive loading (or lazy loading), as the dataset is progressively
loaded from file, retrieving just enough data for what is needed immediately. Two additional
benefits of the using the ImageDataGenerator class is that it can also automatically scale pixel
values of images and it can automatically generate augmented versions of images. We will
leave these topics for discussion in another tutorial (see Chapter 9) and instead focus on how
to use the ImageDataGenerator class to load image data from file. The pattern for using the
ImageDataGenerator class is used as follows:
1. Construct and configure an instance of the ImageDataGenerator class.
2. Retrieve an iterator by calling the flow from directory() function.
3. Use the iterator in the training or evaluation of a model.
