Implementing the calculation of the FID score in Python with NumPy arrays is straightforward.

First, let’s define a function that will take a collection of activations for real and generated
images and return the FID score. The calculate fid() function listed below implements
the procedure. Here, we implement the FID calculation almost directly. It is worth noting
that the official implementation in TensorFlow implements elements of the calculation in a
slightly different order, likely for efficiency, and introduces additional checks around the matrix
square root to handle possible numerical instabilities. I recommend reviewing the official
implementation and extending the implementation below to add these checks if you experience
problems calculating the FID on your own datasets.

```
# calculate frechet inception distance
def calculate_fid(act1, act2):
# calculate mean and covariance statistics
mu1, sigma1 = act1.mean(axis=0), cov(act1, rowvar=False)
mu2, sigma2 = act2.mean(axis=0), cov(act2, rowvar=False)
# calculate sum squared difference between means
ssdiff = numpy.sum((mu1 - mu2)**2.0)
# calculate sqrt of product between cov
covmean = sqrtm(sigma1.dot(sigma2))
# check and correct imaginary numbers from sqrt
if iscomplexobj(covmean):
covmean = covmean.real
# calculate score
fid = ssdiff + trace(sigma1 + sigma2 - 2.0 * covmean)
return fid
```
