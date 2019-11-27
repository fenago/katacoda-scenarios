Now that we have trained the generator and discriminator models, we can make use of them. In
the case of the semi-supervised GAN, we are less interested in the generator model and more
interested in the supervised model. Reviewing the results for the specific run, we can select a
specific saved model that is known to have good performance on the test dataset. In this case,
the model saved after 12 training epochs, or 7,200 updates, that had a classification accuracy of
about 95.432% on the training dataset. We can load the model directly via the load model()
Keras function.

```
# load the model
model = load_model('c_model_7200.h5')
```

Once loaded, we can evaluate it on the entire training dataset again to confirm the finding,
then evaluate it on the holdout test dataset. Recall, the feature extraction layers expect the
input images to have the pixel values scaled to the range [-1,1], therefore, this must be performed
before any images are provided to the model. The complete example of loading the saved
semi-supervised classifier model and evaluating it in the complete MNIST dataset is listed below.

```
# example of loading the classifier model and generating images
from numpy import expand_dims
from keras.models import load_model
from keras.datasets.mnist import load_data
# load the model
model = load_model('c_model_7200.h5')
# load the dataset
(trainX, trainy), (testX, testy) = load_data()
# expand to 3d, e.g. add channels
trainX = expand_dims(trainX, axis=-1)
testX = expand_dims(testX, axis=-1)
# convert from ints to floats
trainX = trainX.astype('float32')
testX = testX.astype('float32')
# scale from [0,255] to [-1,1]
trainX = (trainX - 127.5) / 127.5
testX = (testX - 127.5) / 127.5
# evaluate the model
_, train_acc = model.evaluate(trainX, trainy, verbose=0)
print('Train Accuracy: %.3f%%' % (train_acc * 100))
_, test_acc = model.evaluate(testX, testy, verbose=0)
print('Test Accuracy: %.3f%%' % (test_acc * 100))
```
