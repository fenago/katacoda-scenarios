
We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_13/03_max_pooling.py` to view file.

#### Run Code
Running the example first summarizes the model. We can see, as we might expect by now,
that the output of the max pooling layer will be a single feature map with each dimension
halved, with the shape (3,3). Applying the max pooling results in a new feature map that still
detects the line, although in a downsampled manner.

Now, run the python code by running: `python 03_max_pooling.py`{{execute}}

Example output from manually applying a two-dimensional filter with max pooling.

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-13-avg/steps/5/1.JPG)
