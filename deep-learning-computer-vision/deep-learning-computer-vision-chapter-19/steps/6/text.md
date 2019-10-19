Adding padding to the convolutional operation can often result in better model performance, as
more of the input image of feature maps are given an opportunity to participate or contribute
to the output. By default, the convolutional operation uses ‘valid’ padding, which means that
convolutions are only applied where possible. This can be changed to ‘same’ padding so that
zero values are added around the input such that the output has the same size as the input

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/03_baseline_with_padding.py` to view file.


#### Run Code
**Note:** It will take some time to complete.

Now, run the python code by running: `python 03_baseline_with_padding.py`{{execute}}

