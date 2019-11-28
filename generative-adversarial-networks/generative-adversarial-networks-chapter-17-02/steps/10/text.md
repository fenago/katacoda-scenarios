We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_17/03_train_unconditional_gan.py` to view file.

#### Run Code

Now, run the python code by running: `python 03_train_unconditional_gan.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.
The loss for the discriminator on real and fake samples, as well as the loss for the generator,
is reported after each batch.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
