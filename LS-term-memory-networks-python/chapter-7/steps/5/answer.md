<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
from math import sin
from math import pi
from math import exp
from matplotlib import pyplot
# create sequence
length = 150
period = 5
decay = 0.1
sequence = [0.5 + 0.5 * sin(2 * pi * i / period) * exp(-decay * i) for i in range(length)]
# plot sequence
pyplot.plot(sequence)
pyplot.show()
</pre>

