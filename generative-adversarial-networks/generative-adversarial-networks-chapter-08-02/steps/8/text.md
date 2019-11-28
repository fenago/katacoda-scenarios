We now have everything we need to train and evaluate a GAN on the CIFAR-10 photographs of
small objects dataset. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_08/08_complete_example.py` to view file.

#### Run Code

Now, run the python code by running: `python 08_complete_example.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.
The chosen configuration results in the stable training of both the generative and discriminative model. The model performance is reported every batch, including the loss of both the
discriminative (d) and generative (g) models.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.
