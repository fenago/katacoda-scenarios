<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# Load CSV using NumPy

from numpy import loadtxt
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)

#This example can be modified to load the same dataset directly from a 
#URL as follows:
# Load CSV from URL using NumPy

from numpy import loadtxt
from urllib.request import urlopen
url = 'https://goo.gl/bDdBiA'
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)

</pre>
