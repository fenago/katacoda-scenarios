<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
from math import sin
from math import pi
from matplotlib import pyplot
# create sequence
length = 200
freq = 15
sequence = [sin(2 * pi * freq * (i/float(length))) for i in range(length)]
# plot sequence
pyplot.plot(sequence)
pyplot.show()
</pre>

