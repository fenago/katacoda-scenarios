<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# matplotlib crash course


# basic line plot
import matplotlib.pyplot as plt
import numpy
array = numpy.array([10, 20, 30, 40])
plt.plot(array)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()


# basic scatter plot
import matplotlib.pyplot as plt
import numpy
a = numpy.array([10, 20, 30, 60])
b = numpy.array([20, 40, 60, 120])
plt.scatter(a,b)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

</pre>

