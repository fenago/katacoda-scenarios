We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_12/03_inception_score_keras.py` to view file.

#### Run Code

Now, run the python code by running: `python 03_inception_score_keras.py`{{execute}}

Running the example first defines the 50 fake images, then calculates the inception score on
each batch and reports the expected inception score of 1.0, with a standard deviation of 0.0.

**Note:** the first time the InceptionV3 model is used, Keras will download the model weights
and save them into the ∼/.keras/models/ directory on your workstation. The weights are
about 100 megabytes and may take a moment to download depending on the speed of your
internet connection.

```
loaded (50, 299, 299, 3)
score 1.0 0.0
```
