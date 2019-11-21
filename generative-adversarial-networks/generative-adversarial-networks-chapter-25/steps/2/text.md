This tutorial is divided into five parts; they are:
1. What Is the CycleGAN Architecture?
2. How to Implement the CycleGAN Discriminator Model
3. How to Implement the CycleGAN Generator Model
4. How to Implement Composite Models and Loss
5. How to Update Model Weights

#### What Is the CycleGAN Architecture?
The CycleGAN model was described by Jun-Yan Zhu, et al. in their 2017 paper titled Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (introduced
in Chapter 24). The model architecture is comprised of two generator models: one generator
(Generator-A) for generating images for the first domain (Domain-A) and the second generator
(Generator-B) for generating images for the second domain (Domain-B).

- Generator-A → Domain-A
- Generator-B → Domain-B

The generator models perform image translation, meaning that the image generation process
is conditional on an input image, specifically an image from the other domain. Generator-A
takes an image from Domain-B as input and Generator-B takes an image from Domain-A as
input.

- Domain-B → Generator-A → Domain-A
- Domain-A → Generator-B → Domain-B

Each generator has a corresponding discriminator model. The first discriminator model
(Discriminator-A) takes real images from Domain-A and generated images from Generator-A
and predicts whether they are real or fake. The second discriminator model (Discriminator-B)
takes real images from Domain-B and generated images from Generator-B and predicts whether
they are real or fake.

- Domain-A → Discriminator-A → [Real/Fake]
- Domain-B → Generator-A → Discriminator-A → [Real/Fake]
- Domain-B → Discriminator-B → [Real/Fake]
- Domain-A → Generator-B → Discriminator-B → [Real/Fake]
