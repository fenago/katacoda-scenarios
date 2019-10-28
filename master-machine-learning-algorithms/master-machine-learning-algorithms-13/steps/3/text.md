A downside of k-Nearest Neighbors is that you need to hang on to your entire training dataset.
The Learning Vector Quantization algorithm (or LVQ for short) is an artificial neural network
algorithm that allows you choose how many training instances to hang onto and learns exactly
what those instances should look like.

#### LVQ Model Representation
The representation for LVQ is a collection of codebook vectors. LVQ was developed and is best
understood as a classification algorithm. It supports both binary (two-class) and multiclass
classification problems. A codebook vector is a list of numbers that have the same input and
output attributes as your training data. For example, if your problem is a binary classification
with classes 0 and 1, and the inputs width, length height, then a codebook vector would be
comprised of all four attributes: width, length, height and class.
The model representation is a fixed pool of codebook vectors, learned from the training data.
They look like training instances, but the values of each attribute have been adapted based on
the learning procedure. In the language of neural networks, each codebook vector may be called
a neuron, each attribute on a codebook vector is called a weight and the collection of codebook
vectors is called a network.