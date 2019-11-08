Fortunately, scikit-learn makes this really easy to do, and it's even easier than doing normal train/test! It's extremely simple to do k-fold cross-validation, so you may as well just do it.

Now, the way this all works in practice is you will have a model that you're trying to tune, and you will have different variations of that model, different parameters you might want to tweak on it, right?

Like, for example, the degree of polynomial for a polynomial fit. So, the idea is to try different values of your model, different variations, measure them all using k-fold cross-validation, and find the one that minimizes error against your test dataset. That's kind of your sweet spot there. In practice, you want to use k-fold cross-validation to measure the accuracy of your model against a test dataset, and just keep refining that model, keep trying different values within it, keep trying different variations of that model or maybe even different models entirely, until you find the technique that reduces error the most, using k-fold cross validation.

Let's go dive into an example and see how it works. We're going to apply this to our Iris dataset again, revisiting SVC, and we'll play with k-fold cross-validation and see how simple it is. Let's actually put k-fold cross-validation and train/test into practice here using some real Python code. You'll see it's actually very easy to use, which is a good thing because this is a technique you should be using to measure the accuracy, the effectiveness of your models in supervised learning.

Please go ahead and open up the `KFoldCrossValidation.ipynb` and follow along if you will. We're going to look at the Iris dataset again; remember we introduced this when we talk about dimensionality reduction?

#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `KFoldCrossValidation.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/KFoldCrossValidation.ipynb
