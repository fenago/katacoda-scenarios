Images are comprised of matrices of pixel values. Black and white images are single matrix of
pixels, whereas color images have a separate array of pixel values for each color channel, such as
red, green, and blue. Pixel values are often unsigned integers in the range between 0 and 255.
Although these pixel values can be presented directly to neural network models in their raw
format, this can result in challenges during modeling, such as in slower than expected training
of the model.

Instead, there can be great benefit in preparing the image pixel values prior to modeling,
such as simply scaling pixel values to the range 0-1 to centering and even standardizing the
values. In this tutorial, you will discover how to prepare image data for modeling with deep
learning neural networks. After completing this tutorial, you will know:

- How to normalize pixel values to a range between zero and one.
- How to center pixel values both globally across channels and locally per channel.
- How to standardize pixel values and how to shift standardized pixel values to the positive
domain.

Let’s get started