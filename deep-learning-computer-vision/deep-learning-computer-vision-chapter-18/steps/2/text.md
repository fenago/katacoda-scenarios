This tutorial is divided into five parts; they are:
1. What Is Transfer Learning?
2. Transfer Learning for Image Recognition
3. How to Use Pre-Trained Models
4. Models for Transfer Learning
5. Examples of Using Pre-Trained Models


##### What Is Transfer Learning?
Transfer learning generally refers to a process where a model trained on one problem is used
in some way on a second, related problem. In deep learning, transfer learning is a technique
whereby a neural network model is first trained on a problem similar to the problem that is
being solved. One or more layers from the trained model are then used in a new model trained
on the problem of interest.

Transfer learning has the benefit of decreasing the training time for a neural network model
and can result in lower generalization error. The weights in re-used layers may be used as the
starting point for the training process and adapted in response to the new problem. This usage
treats transfer learning as a type of weight initialization scheme. This may be useful when the
first related problem has a lot more labeled data than the problem of interest and the similarity
in the structure of the problem may be useful in both contexts.