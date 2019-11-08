
As an example, let's just figure out the probability of an e-mail being spam given that it contains the word "free". If people are promising you free stuff, it's probably spam! So let's work that out. The probability of an email being spam given that you have the word "free" in that e-mail works out to the overall probability of it being a spam message times the probability of containing the word "free" given that it's spam over the probability overall of being free:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/15/1.jpg)

The numerator can just be thought of as the probability of a message being Spam and containing the word Free. But that's a little bit different than what we're looking for, because that's the odds out of the complete dataset and not just the odds within things that contain the word Free. The denominator is just the overall probability of containing the word Free. Sometimes that won't be immediately accessible to you from the data that you have. If it's not, you can expand that out to the following expression if you need to derive it:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/15/1.jpg)

This gives you the percentage of e-mails that contain the word "free" that are spam, which would be a useful thing to know when you're trying to figure out if it's spam or not.
