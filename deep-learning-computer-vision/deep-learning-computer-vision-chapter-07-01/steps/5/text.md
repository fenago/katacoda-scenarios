The ImageDataGenerator class in Keras provides a suite of techniques for scaling pixel values
in your image dataset prior to modeling. The class will wrap your image dataset, then
when requested, it will return images in batches to the algorithm during training, validation,
or evaluation and apply the scaling operations just-in-time. This provides an efficient and
convenient approach to scaling image data when modeling with neural networks.

The usage of the ImageDataGenerator class is as follows.
1. Load your dataset.
2. Configure the ImageDataGenerator (e.g. construct an instance).
3. Calculate image statistics (e.g. call the fit() function).
4. Use the generator to fit the model (e.g. pass the instance to the fit generator()
function).
5. Use the generator to evaluate the model (e.g. pass the instance to the evaluate generator()
function).


The ImageDataGenerator class supports a number of pixel scaling methods, as well as a
range of data augmentation techniques. We will focus on the pixel scaling techniques in this
chapter and leave the data augmentation methods to a later discussion. The
three main types of pixel scaling techniques supported by the ImageDataGenerator class are as
follows:

- **Pixel Normalization:** scale pixel values to the range 0-1.
- **Pixel Centering:** scale pixel values to have a zero mean.
- **Pixel Standardization:** scale pixel values to have a zero mean and unit variance.