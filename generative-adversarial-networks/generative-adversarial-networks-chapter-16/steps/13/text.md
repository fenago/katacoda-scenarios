We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_16/01_train_wgan.py` to view file.

#### Run Code

Now, run the python code by running: `python 01_train_wgan.py`{{execute}}

Running the example is quick, taking approximately 10 minutes on modern hardware without
a GPU. First, the loss of the critic and generator models is reported to the console each iteration
of the training loop. Specifically, c1 is the loss of the critic on real examples, c2 is the loss of
the critic in generated samples, and g is the loss of the generator trained via the critic. The c1
scores are inverted as part of the loss function; this means if they are reported as negative, then
they are really positive, and if they are reported as positive, they are really negative. The sign
of the c2 scores is unchanged.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.
