<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Python Crash Course


# Assignment
# ==========

# Strings
data = 'This is my first programme'
print(data[0])
print(len(data))
print(data)

# Numbers
value = 153.5
print(value)
value = 10
print(value)

# Boolean
x = True
y = False
print(x, y)

# Multiple Assignment
x, y, z = 10, 20, 30
print(x, y, z)

# No value
x = None
print(x)



# Flow Control
# ============

# If-Then-Else

value = 55
if value >= 55:
	print('That is slow')
elif value > 100:
	print('That is fast')
else:
	print('This is over speeding')

# For-Loop
for x in range(5):
	print(x)

# While-Loop
x = 1
while x < 5:
	print(x)
	x += 1


# Data Structures
# ===============

# Tuple (cannot change)
array = (5, 10, 15)
print(array)


# Lists
listing = [5, 10, 15]
print("Zeroth Value: %d" % listing[0])
listing.append(4)
print("List Length: %d" % len(listing))
for value in listing:
	print(value)



# Dictionaries

dictionary = {'x': 5, 'y': 10, 'z': 15}
print("X value: %d" % dictionary['x'])
dictionary['x'] = 11
print("X value: %d" % dictionary['x'])
print("Keys: %s" % dictionary.keys())
print("Values: %s" % dictionary.values())
for key in dictionary.keys():
	print(dictionary[key])


# Functions
# ===========

# Sum function
def sumfuc(a, b):
	return a + b

# Test sum function
sumfuc(5, 10)




</pre>