
More training, beyond some point, does not mean better quality generated images. In this
case, the results after 10 epochs are low quality, although we can see some difference between
background and foreground with a blob in the middle of each image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-08-02/steps/8/1.PNG)

After 90 or 100 epochs, we are starting to see plausible photographs with blobs that look
like birds, dogs, cats, and horses. The objects are familiar and CIFAR-10-like, but many of
them are not clearly one of the 10 specified classes.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-08-02/steps/8/2.PNG)

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-08-02/steps/8/3.PNG)

The model remains stable over the next 100 epochs, with little improvement in the generated
images. The small photos remain vaguely CIFAR-10 like and focused on animals like dogs, cats,
and birds.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-08-02/steps/8/4.PNG)