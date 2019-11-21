Semi-supervised learning refers to a problem where a predictive model is required and there
are few labeled examples and many unlabeled examples. The most common example is a
classification predictive modeling problem in which there may be a very large dataset of
examples, but only a small fraction have target labels. The model must learn from the small
set of labeled examples and somehow harness the larger dataset of unlabeled examples in
order to generalize to classifying new examples in the future. The Semi-Supervised GAN, or
sometimes SGAN for short, is an extension of the Generative Adversarial Network architecture
for addressing semi-supervised learning problems.

The discriminator in a traditional GAN is trained to predict whether a given image is real
(from the dataset) or fake (generated), allowing it to learn features from unlabeled images.
The discriminator can then be used via transfer learning as a starting point when developing
a classifier for the same dataset, allowing the supervised prediction task to benefit from the
unsupervised training of the GAN. In the Semi-Supervised GAN, the discriminator model is
updated to predict K + 1 classes, where K is the number of classes in the prediction problem
and the additional class label is added for a new fake class. It involves directly training the
discriminator model for both the unsupervised GAN task and the supervised classification task
simultaneously.

As such, the discriminator is trained in two modes: a supervised and unsupervised mode.
- **Unsupervised Training:** In the unsupervised mode, the discriminator is trained in the
same way as the traditional GAN, to predict whether the example is either real or fake.
- **Supervised Training:** In the supervised mode, the discriminator is trained to predict
the class label of real examples.