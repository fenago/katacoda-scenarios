<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# scikit-learn bootstrap
from sklearn.utils import resample
# data sample
data = [5, 10, 15, 20, 25, 30]
# prepare bootstrap sample
boot = resample(data, replace=True, n_samples=3, random_state=0)
print('Bootstrap Sample: %s' % boot)
# out of bag observations
oob = [x for x in data if x not in boot]
print('OOB Sample: %s' % oob)
</pre>