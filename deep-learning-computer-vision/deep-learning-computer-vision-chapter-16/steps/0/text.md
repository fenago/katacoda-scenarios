Pooling can be used to downsample the content of feature maps, reducing their width and height
whilst maintaining their salient features. A problem with deep convolutional neural networks is
that the number of feature maps often increases with the depth of the network. This problem
can result in a dramatic increase in the number of parameters and computation required when
larger filter sizes are used, such as 5 x 5 and 7 x 7.
To address this problem, a 1 x 1 convolutional layer can be used that offers a channel-wise
pooling, often called feature map pooling or a projection layer. This simple technique can be
used for dimensionality reduction, decreasing the number of feature maps whilst retaining their
salient features. It can also be used directly to create a one-to-one projection of the feature
maps to pool features across channels or to increase the number of feature maps, such as after
traditional pooling layers. In this tutorial, you will discover how to use 1 x 1 filters to control
the number of feature maps in a convolutional neural network. After completing this tutorial,
you will know:
- The 1 x 1 filter can be used to create a linear projection of a stack of feature maps.
- The projection created by a 1 x 1 filter can act like channel-wise pooling and be used for
dimensionality reduction.
- The projection created by a 1 x 1 filter can also be used directly or be used to increase
the number of feature maps in a model.
Let’s get started.
