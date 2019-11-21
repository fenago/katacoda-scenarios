We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_19/04_inference_acgan.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_inference_acgan.py`{{execute}}

Running the example, in this case, generates 100 very plausible photos of sneakers.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-19-02/steps/12/1.PNG)

It may be fun to experiment with other class values. For example, below are 100 generated
coats (n class=4). Most of the images are coats, although there are a few pants in there,
showing that the latent space is partially, but not completely, class-conditional.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-19-02/steps/12/2.PNG)
