<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# split train and test data
from numpy import array
# define array
data = array([
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]])
# separate data
split = 1
train,test = data[:split,:1],data[split:,:2]
print(train)
print(test)
</pre>

