
We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_23/03_train_pix2pix.py` to view file.

#### Run Code
Now, run the python code by running: `python 03_train_pix2pix.py`{{execute}}

**Note:** Running the example may take many hours to run on CPU hardware. I recommend
running the example on GPU hardware if possible. If you need help, you can get started
quickly by using an AWS EC2 instance to train the model. See the instructions in Appendix C.
The loss is reported each training iteration, including the discriminator loss on real examples
(d1), discriminator loss on generated or fake examples (d2), and generator loss, which is a
weighted average of adversarial and L1 loss (g). If loss for the discriminator goes to zero and
stays there for a long time, consider re-starting the training run as it is an example of a training
failure.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.

```
>1, d1[0.566] d2[0.520] g[82.266]
>2, d1[0.469] d2[0.484] g[66.813]
>3, d1[0.428] d2[0.477] g[79.520]
>4, d1[0.362] d2[0.405] g[78.143]
>5, d1[0.416] d2[0.406] g[72.452]
...
>109596, d1[0.303] d2[0.006] g[5.792]
>109597, d1[0.001] d2[1.127] g[14.343]
>109598, d1[0.000] d2[0.381] g[11.851]
>109599, d1[1.289] d2[0.547] g[6.901]
>109600, d1[0.437] d2[0.005] g[10.460]
>Saved: plot_109600.png and model_109600.h5
```

Models are saved every 10 epochs and saved to a file with the training iteration number.
Additionally, images are generated every 10 epochs and compared to the expected target images.
These plots can be assessed at the end of the run and used to select a final generator model
based on generated image quality. At the end of the run, will you will have 10 saved model
files and 10 plots of generated images. After the first 10 epochs, map images are generated that
look plausible, although the lines for streets are not entirely straight and images contain some
blurring. Nevertheless, large structures are in the right places with mostly the right colors.