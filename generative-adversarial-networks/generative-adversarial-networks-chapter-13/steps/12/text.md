We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_13/02_fid_keras.py` to view file.

#### Run Code

Now, run the python code by running: `python 02_fid_keras.py`{{execute}}

Running the example first summarizes the shapes of the fabricated images and their rescaled
versions, matching our expectations.

**Note:** the first time the InceptionV3 model is used, Keras will download the model weights
and save them into the ∼/.keras/models/ directory on your workstation. The weights are
about 100 megabytes and may take a moment to download depending on the speed of your
internet connection.13.6. How to Calculate the FID for Real Images 275
The FID score between a given set of images and itself is 0.0, as we expect, and the distance
between the two collections of random images is about 35.

```
Prepared (10, 32, 32, 3) (10, 32, 32, 3)
Scaled (10, 299, 299, 3) (10, 299, 299, 3)
FID (same): -0.000
FID (different): 35.495
```