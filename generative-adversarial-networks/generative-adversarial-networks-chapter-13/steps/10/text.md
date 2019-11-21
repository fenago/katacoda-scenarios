
Once resized, the image pixel values will also need to be scaled to meet the expectations
for inputs to the inception model. This can be achieved by calling the preprocess input()
function. We can update our calculate fid() function defined in the previous section to take
the loaded inception model and two NumPy arrays of image data as arguments, instead of
activations. The function will then calculate the activations before calculating the FID score as
before. The updated version of the calculate fid() function is listed below.

```
# calculate frechet inception distance
def calculate_fid(model, images1, images2):
# calculate activations
act1 = model.predict(images1)
act2 = model.predict(images2)
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

We can then test this function with some contrived collections of images, in this case, 10
32 × 32 images with random pixel values in the range [0,255].

```
...
# define two fake collections of images
images1 = randint(0, 255, 10*32*32*3)
images1 = images1.reshape((10,32,32,3))
images2 = randint(0, 255, 10*32*32*3)
images2 = images2.reshape((10,32,32,3))
```
