Weak models are added sequentially, trained using the weighted training data. The process
continues until a pre-set number of weak learners have been created (a user parameter) or no
further improvement can be made on the training dataset. Once completed, you are left with a
pool of weak learners each with a stage value.


#### Making Predictions with AdaBoost
Predictions are made by calculating the weighted average of the weak classifiers. For a new input
instance, each weak learner calculates a predicted value as either +1.0 or -1.0. The predicted
values are weighted by each weak learners stage value. The prediction for the ensemble model
is taken as the sum of the weighted predictions. If the sum is positive, then the first class is
predicted, if negative the second class is predicted.

For example, `5` weak classifiers may predict the values 1.0, 1.0, -1.0, 1.0, -1.0. From a
majority vote, it looks like the model will predict a value of 1.0 or the first class. These same 5
weak classifiers may have the stage values 0.2, 0.5, 0.8, 0.2 and 0.9 respectively. Calculating
the weighted sum of these predictions results in an output of -0.8, which would be an ensemble
prediction of -1.0 or the second class.