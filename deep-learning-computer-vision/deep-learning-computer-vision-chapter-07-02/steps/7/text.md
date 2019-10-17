We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_07/04_standardization_keras.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_standardization_keras.py`{{execute}}


Running the example first reports the mean and standard deviation of pixel values in the
train and test datasets. The data generator is then configured for feature-wise standardization
and the statistics are calculated on the training dataset, matching what we would expect when
the statistics are calculated manually. A single batch of 64 standardized images is then retrieved
and we can confirm that the mean and standard deviation of this small sample is close to the
expected standard Gaussian. The test is then repeated on the entire training dataset and we
can confirm that the mean is indeed a very small value close to 0.0 and the standard deviation
is a value very close to 1.0. 

**Note:** your statistics may vary slightly due to a different random batch of images being selected.

```
Statistics train=33.318 (78.567), test=33.791 (79.172)
Data Generator mean=33.318, std=78.567
(64, 28, 28, 1) 0.010656365 1.01076797.7. Extensions 71
(60000, 28, 28, 1) -3.4560264e-07 0.9999998
```

Example output from feature-wise standardization on the MNIST dataset.



