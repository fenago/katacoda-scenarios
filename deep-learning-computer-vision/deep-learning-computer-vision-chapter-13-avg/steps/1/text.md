Convolutional layers in a convolutional neural network summarize the presence of features in an
input image. A problem with the output feature maps is that they are sensitive to the location
of the features in the input. One approach to address this sensitivity is to downsample the
feature maps. This has the effect of making the resulting downsampled feature maps more
robust to changes in the position of the feature in the image, referred to by the technical phrase
local translation invariance. Pooling layers provide an approach to down sampling feature maps
by summarizing the presence of features in patches of the feature map. Two common pooling
methods are average pooling and max pooling that summarize the average presence of a feature
and the most activated presence of a feature respectively. In this tutorial, you will discover how
the pooling operation works and how to implement it in convolutional neural networks. 

After completing this tutorial, you will know, how to calculate and implement max in a convolutional neural

Let’s get started.