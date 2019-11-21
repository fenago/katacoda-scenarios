The supervised classification model is evaluated on the entire training dataset at the end of
every training epoch, in this case after every 600 training updates. At this time, the performance
of the model is summarized, showing that it rapidly achieves good skill. This is surprising given
that the model is only trained on 10 labeled examples of each class.

```
...
Classifier Accuracy: 94.640%
Classifier Accuracy: 93.622%
Classifier Accuracy: 91.870%
Classifier Accuracy: 92.525%
Classifier Accuracy: 92.180%
```

The models are also saved at the end of each training epoch and plots of generated images
are also created. The quality of the generated images is good given the relatively small number
of training epochs.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-20-02/steps/12/1.PNG)