Next, we construct our y vector which is assigned what we're trying to predict, that is our Hired column:

```
y = df["Hired"] 
X = df[features] 
clf = tree.DecisionTreeClassifier() 
clf = clf.fit(X,y) 
```

This code extracts the entire Hired column and calls it y. Then it takes all of our columns for the feature data and puts them in something called X. This is a collection of all of the data and all of the feature columns, and X and y are the two things that our decision tree classifier needs.

To actually create the classifier itself, two lines of code: we call tree.DecisionTreeClassifier() to create our classifier, and then we fit it to our feature data (X) and the answers (y)- whether or not people were hired. So, let's go ahead and run that.

Displaying graphical data is a little bit tricky, and I don't want to distract us too much with the details here, so please just consider the following boilerplate code. You don't need to get into how Graph viz works here - and dot files and all that stuff: it's not important to our journey right now. The code you need to actually display the end results of a decision tree is simply:

```
from IPython.display import Image   
from sklearn.externals.six import StringIO   
import pydot  
 
dot_data = StringIO()   
tree.export_graphviz(clf, out_file=dot_data,   
                         feature_names=features)   
graph = pydot.graph_from_dot_data(dot_data.getvalue())   
Image(graph.create_png()) 
```

So let's go ahead and run this.

This is what your output should now look like:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/18/4.jpg)

There we have it! How cool is that?! We have an actual flow chart here.
