<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
from numpy import array
data = array([
    [5.1, 1.1],
    [10.2, 1.9],
    [15.3, 1.8],
    [20.4, 1.7],
    [25.5, 1.6],
    [30.6, 1.5],
    [35.7, 1.4],
    [40.8, 1.3],
    [45.9, 1.2],
    [50.0, 1.1]])
data = data.reshape(1, 20, 1)
print(data.shape)

</pre>
