<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# numpy crash course

# define an array
import numpy
listing = [10, 20, 30, 40]
array = numpy.array(listing)
print(array)
print(array.shape)

# access values
import numpy
listing = [[10, 20, 30, 40], [30, 40, 50,60], [100, 200, 300,400]]
array = numpy.array(listing)
print(array)
print(array.shape)
print("First row: %s" % array[1])
print("Last row: %s" % array[-1])
print("Specific row and col: %s" % array[1, 3])
print("Whole col: %s" % array[:, 2])

# arithmetic
import numpy
first_array = numpy.array([20, 20, 20, 60])
second_array = numpy.array([30, 30, 30, 90])
print("Addition: %s" % (first_array + second_array))
print("Multiplication: %s" % (first_array * second_array))



</pre>
