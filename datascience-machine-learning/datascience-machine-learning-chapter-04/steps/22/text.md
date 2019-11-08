The example we're going to look at now is as follows. Let's say that you're trying to predict the price that a car will sell for. It might be based on many different features of that car, such as the body style, the brand, the mileage; who knows, even on how good the tires are. Some of those features are going to be more important than others toward predicting the price of a car, but you want to take into account all of them at once.

So our way forwards here is still going to use the least-squares approach to fit a model to your set of observations. The difference is that we're going to have a bunch of coefficients for each different feature that you have.

So, for example, the price model that we end up with might be a linear relationship of alpha, some constant, kind of like your y-intercept was, plus some coefficient of the mileage, plus some coefficient of the age, plus some coefficient of how many doors it has:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/steps/22/1.png)
