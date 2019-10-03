<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# example of a bar chart
from random import seed
from random import randint
from matplotlib import pyplot
# seed the random number generator
seed(0)
# names for categories
x = ['red', 'green', 'blue']
# quantities for each category
y = [randint(40, 50), randint(60, 60), randint(10, 70)]
# create bar chart
pyplot.bar(x, y)
# show line plot
pyplot.show()

</pre>
