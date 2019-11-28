We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_19/03_train_acgan.py` to view file.

#### Run Code

Now, run the python code by running: `python 03_train_acgan.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.
The loss is reported each training iteration, including the real/fake and class loss for the
discriminator on real examples (dr), the discriminator on fake examples (df), and the generator
updated via the composite model when generating images (g).

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.

```
>1, dr[0.934,2.967], df[1.310,3.006], g[0.878,3.368]
>2, dr[0.711,2.836], df[0.939,3.262], g[0.947,2.751]
>3, dr[0.649,2.980], df[1.001,3.147], g[0.844,3.226]
>4, dr[0.732,3.435], df[0.823,3.715], g[1.048,3.292]
>5, dr[0.860,3.076], df[0.591,2.799], g[1.123,3.313]
...
```

A total of 10 sample images are generated and 10 models saved over the run. Plots of
generated clothing after 10 iterations already look plausible.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-19-02/steps/10/1.PNG)

The images remain reliable throughout the training process.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-19-02/steps/10/2.PNG)