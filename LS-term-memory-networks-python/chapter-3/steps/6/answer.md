<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
from keras.preprocessing.sequence import pad_sequences
# define sequences
sequences = [
	[5, 10, 15, 20],
	   [10, 20, 30],
            [20,30],
               [10]
	]
# pad sequence
padded = pad_sequences(sequences, padding='post')
print(padded)
</pre>

