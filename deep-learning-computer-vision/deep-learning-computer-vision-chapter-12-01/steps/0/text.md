The convolutional layer in convolutional neural networks systematically applies filters to an
input and creates output feature maps. Although the convolutional layer is very simple, it is
capable of achieving sophisticated and impressive results. Nevertheless, it can be challenging to
develop an intuition for how the shape of the filters impacts the shape of the output feature map
and how related configuration hyperparameters such as padding and stride should be configured.
In this tutorial, you will discover an intuition for filter size, the need for padding, and stride in
convolutional neural networks. After completing this tutorial, you will know:

- How filter size or kernel size impacts the shape of the output feature map.
- How the filter size creates a border effect in the feature map and how it can be overcome
with padding.
- How the stride of the filter on the input image can be used to downsample the size of the
output feature map.
Let’s get started.
