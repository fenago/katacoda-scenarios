<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# q-q plot
from numpy.random import seed
from numpy.random import randn
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 30
# q-q plot
qqplot(data, line='s')
pyplot.show()
</pre>

