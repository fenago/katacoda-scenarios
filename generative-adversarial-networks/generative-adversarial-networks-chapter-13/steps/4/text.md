The FID score is calculated by first loading a pre-trained Inception v3 model. The output layer
of the model is removed and the output is taken as the activations from the last pooling layer, a
global spatial pooling layer. This output layer has 2,048 activations, therefore, each image is
predicted as 2,048 activation features. This is called the coding vector or feature vector for the
image.
A 2,048 feature vector is then predicted for a collection of real images from the problem
domain to provide a reference for how real images are represented. Feature vectors can then be
calculated for synthetic images. The result will be two collections of 2,048 feature vectors for
real and generated images. The FID score is then calculated using the following equation taken
from the paper:

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks\generative-adversarial-networks-chapter-13/steps/4/1.PNG)

The score is referred to as d2, showing that it is a distance and has squared units. The mu1
and mu2 refer to the feature-wise mean of the real and generated images, e.g. 2,048 element
vectors where each element is the mean feature observed across the images. The C1 and C1 are
the covariance matrix for the real and generated feature vectors, often referred to as sigma. The
||mu1 − mu2||2 refers to the sum squared difference between the two mean vectors. Tr refers to
the trace linear algebra operation, e.g. the sum of the elements along the main diagonal of the
square matrix. The square root of a matrix is often also written as M 1 2 , e.g. the matrix to the
power of one half, which has the same effect. This operation can fail depending on the values in
the matrix because the operation is solved using numerical methods. Commonly, some elements
in the resulting matrix may be imaginary, which often can be detected and removed.