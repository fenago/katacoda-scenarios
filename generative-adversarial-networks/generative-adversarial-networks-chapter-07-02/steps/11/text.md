
More training, beyond some point, does not mean better quality generated images. In this
case, the results after 10 epochs are low quality, although we can see that the generator has
learned to generate centered figures in white on a black background (recall we have inverted the
grayscale in the plot).

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks\generative-adversarial-networks-chapter-07-02/steps/8/1.PNG)

After 20 or 30 more epochs, the model begins to generate very plausible MNIST figures,
suggesting that 100 epochs are probably not required for the chosen model configurations.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks\generative-adversarial-networks-chapter-07-02/steps/8/2.PNG)


The generated images after 100 epochs are not greatly different, but I believe I can detect
less blocky-ness in the curves.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks\generative-adversarial-networks-chapter-07-02/steps/8/3.PNG)
