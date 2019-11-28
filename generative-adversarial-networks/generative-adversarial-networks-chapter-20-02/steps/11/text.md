We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_17/06_train_sgan.py` to view file.

#### Run Code

Now, run the python code by running: `python 06_train_sgan.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.
At the start of the run, the size of the training dataset is summarized, as is the supervised
subset, confirming our configuration. The performance of each model is summarized at the end
of each update, including the loss and accuracy of the supervised discriminator model (c), the
loss of the unsupervised discriminator model on real and generated examples (d), and the loss
of the generator model updated via the composite model (g). The loss for the supervised model
will shrink to a small value close to zero and accuracy will hit 100%, which will be maintained
for the entire run. The loss of the unsupervised discriminator and generator should remain at
modest values throughout the run if they are kept in equilibrium.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.

```
(60000, 28, 28, 1) (60000,)
(100, 28, 28, 1) (100,)
n_epochs=20, n_batch=100, 1/2=50, b/e=600, steps=12000
>1, c[2.305,6], d[0.096,2.399], g[0.095]
>2, c[2.298,18], d[0.089,2.399], g[0.095]
>3, c[2.308,10], d[0.084,2.401], g[0.095]
>4, c[2.304,8], d[0.080,2.404], g[0.095]
>5, c[2.254,18], d[0.077,2.407], g[0.095]
...
```
