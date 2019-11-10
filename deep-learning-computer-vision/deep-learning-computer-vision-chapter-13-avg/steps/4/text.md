
The first max pooling operation is applied as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-13-avg/steps/3/2.JPG)

Given the stride of two, the operation is moved along two columns to the left and the max
is calculated:

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-13-avg/steps/3/3.JPG)

Again, the operation is moved along two columns to the left and the max is calculated:

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-13-avg/steps/3/4.JPG)

That’s it for the first line of pooling operations. The result is the first line of the max pooling
operation:
```
[0.0, 3.0, 0.0]
```
