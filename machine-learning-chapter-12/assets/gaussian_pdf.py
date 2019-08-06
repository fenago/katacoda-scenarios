# Example of Gaussian PDF
from math import sqrt
from math import pi
from math import exp


# %%
'''
## Gaussian Probability Density Function
A Gaussian distribution can be summarized using only two numbers: the mean and the
standard deviation. Therefore, with a little math, we can estimate the probability of a given
value. This piece of math is called a Gaussian Probability Distribution Function (or Gaussian
PDF)
'''

# %%
# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent


# %%
'''
Let's test it out to see how it works. Below are some worked examples.
'''

# %%
# Test Gaussian PDF
print(calculate_probability(1.0, 1.0, 1.0))
print(calculate_probability(2.0, 1.0, 1.0))
print(calculate_probability(0.0, 1.0, 1.0))


# %%
'''
Running the example prints the probability of some input values. You can see that when the value is 1
and the mean and standard deviation is 1 our input is the most likely (top of the bell curve) and
has the probability of 0.39. We can see that when we keep the statistics the same and change
the x value to 1 standard deviation either side of the mean value (2 and 0 or the same distance
either side of the bell curve) the probabilities of those input values are the same at 0.24.
'''