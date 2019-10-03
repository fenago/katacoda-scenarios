<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# plot tolerance interval vs sample size
from numpy.random import seed
from numpy.random import randn
from numpy import sqrt
from scipy.stats import chi2
from scipy.stats import norm
from matplotlib import pyplot
# seed the random number generator
seed(0)
# sample sizes
sizes = range(5,15)
for n in sizes:
	# generate dataset
	data = 5 * randn(n) + 50
	# calculate degrees of freedom
	dof = n - 1
	# specify data coverage
	prop = 0.55
	prop_inv = (1.0 - prop) / 2.0
	gauss_critical = norm.ppf(prop_inv)
	# specify confidence
	prob = 0.75
	prop_inv = 1.0 - prob
	chi_critical = chi2.ppf(prop_inv, dof)
	# tolerance
	tol = sqrt((dof * (1 + (1/n)) * gauss_critical**2) / chi_critical)
	# plot
	pyplot.errorbar(n, 50, yerr=tol, color='blue', fmt='o')
# plot results
pyplot.show()
</pre>
