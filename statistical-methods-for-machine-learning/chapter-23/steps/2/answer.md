<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# example of ranking real-valued observations
from numpy.random import rand
from numpy.random import seed
from scipy.stats import rankdata
# seed random number generator
seed(0)
# generate dataset
data = rand(100)
# review first 5 samples
print(data[:5])
# rank data
ranked = rankdata(data)
# review first 5 ranked samples
print(ranked[:5])
</pre>