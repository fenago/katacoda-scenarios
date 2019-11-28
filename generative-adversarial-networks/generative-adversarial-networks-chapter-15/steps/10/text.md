We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_15/01_train_lsgan.py` to view file.

#### Run Code

Now, run the python code by running: `python 01_train_lsgan.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.

Running the example will report the loss of the discriminator on real (d1) and fake (d2)
examples and the loss of the generator via the discriminator on generated examples presented
as real (g). These scores are printed at the end of each training run and are expected to remain
small values throughout the training process. Values of zero for an extended period may indicate
a failure mode and the training process should be restarted.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.

Consider running the example a few times and compare the average performance.

```
>1, d1=9.292, d2=0.153 g=2.530
>2, d1=1.173, d2=2.057 g=0.903
>3, d1=1.347, d2=1.922 g=2.215
>4, d1=0.604, d2=0.545 g=1.846
>5, d1=0.643, d2=0.734 g=1.619
...
```
