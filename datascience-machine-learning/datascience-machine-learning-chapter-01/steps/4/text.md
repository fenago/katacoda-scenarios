
Let's keep going and have some fun. In the next code block down, you'll see the following code, which tries to detect outliers like Donald Trump and remove them from the dataset:

```
def reject_outliers(data): 
    u = np.median(data) 
    s = np.std(data) 
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)] 
    return filtered 
 
filtered = reject_outliers(incomes) 
plt.hist(filtered, 50) 
plt.show()
```

So select the corresponding code block in the notebook, and press the run button again. When you do that, you'll see this graph instead:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/4/1.png)

Now we see a much better histogram that represents the more typical American - now that we've taken out our outlier that was messing things up.

So, at this point, you have everything you need to get started in this course. We have all the data you need, all the scripts, and the development environment for Python and Python notebooks. So, let's rock and roll. Up next we're going to do a little crash course on Python itself, and even if you're familiar with Python, it might be a good little refresher so you might want to watch it regardless. Let's dive in and learn Python.