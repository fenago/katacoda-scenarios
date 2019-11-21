
We are nearly ready to define the training of the models. The discriminator models are
updated directly on real and generated images, although in an effort to further manage how
quickly the discriminator models learn, a pool of fake images is maintained. The paper defines
an image pool of 50 generated images for each discriminator model that is first populated
and probabilistically either adds new images to the pool by replacing an existing image or
uses a generated image directly. We can implement this as a Python list of images for each
discriminator and use the update image pool() function below to maintain each pool list.

```
# update image pool for fake images
def update_image_pool(pool, images, max_size=50):
selected = list()
for image in images:
if len(pool) < max_size:
# stock the pool
pool.append(image)
selected.append(image)
elif random() < 0.5:
# use image, but don't add it to the pool
selected.append(image)
else:
# replace an existing image and use replaced image
ix = randint(0, len(pool))
selected.append(pool[ix])
pool[ix] = image
return asarray(selected)
```
