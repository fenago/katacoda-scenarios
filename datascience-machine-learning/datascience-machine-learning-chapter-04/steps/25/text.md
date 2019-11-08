
I've gone ahead and hosted that file for you on my own domain, and if we run that, it will load it into what's called a DataFrame object that we're referring to as df. Now I can call head() on this DataFrame to just show the first few lines of it:

```
df.head()
```

The following is the output for the preceding code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/10.png)

The actual dataset is much larger. This is just the first few samples. So, this is real data of mileage, make, model, trim, type, doors, cruise, sound and leather.

OK, now we're going to use pandas to split that up into the features that we care about. We're going to create a model that tries to predict the price just based on the mileage, the model, and the number of doors, and nothing else.

```
import statsmodels.api as sm

df['Model_ord'] = pd.Categorical(df.Model).codes
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit()

est.summary() 
```

Now the problem that I run into is that the model is a text, like Century for Buick, and as you recall, everything needs to be a number when I'm doing this sort of analysis. In the code, I use this Categorical() function in pandas to actually convert the set of model names that it sees in the DataFrame into a set of numbers; that is, a set of codes. I'm going to say my input for this model on the x-axis is mileage (Mileage), model converted to an ordinal value (Model_ord), and the number of doors (Doors). What I'm trying to predict on the y-axis is the price (Price).
