The CycleGAN model was described by Jun-Yan Zhu, et al. in their 2017 paper titled Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks. The benefit of the CycleGAN model is that it can be trained without paired
examples. That is, it does not require examples of photographs before and after the translation
in order to train the model, e.g. photos of the same city landscape during the day and at night.
Instead, the model is able to use a collection of photographs from each domain and extract
and harness the underlying style of images in the collection in order to perform the translation.
The paper provides a good description of the models and training process, although the official
Torch implementation was used as the definitive description for each model and training process
and provides the basis for the model implementations described below.