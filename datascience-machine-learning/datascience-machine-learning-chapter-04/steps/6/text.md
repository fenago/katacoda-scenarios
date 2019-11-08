There is more than one way to do linear regression. We've talked about ordinary least squares as being a simple way of fitting a line to a set of data, but there are other techniques as well, gradient descent being one of them, and it works best in three-dimensional data. So, it tries to follow the contours of the data for you. It's very fancy and obviously a little bit more computationally expensive, but Python does make it easy for you to try it out if you want to compare it to ordinary least squares.

**Note:**

Using the gradient descent technique can make sense when dealing with 3D data.

Usually though, least squares is a perfectly good choice for doing linear regression, and it's always a legitimate thing to do, but if you do run into gradient descent, you will know that that is just an alternate way of doing linear regression, and it's usually seen in higher dimensional data.
