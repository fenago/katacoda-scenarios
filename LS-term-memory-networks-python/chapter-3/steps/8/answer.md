<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
from keras.preprocessing.sequence import pad_sequences
# define sequences
sequences = [
	[5, 10, 15, 20],
	   [10, 20, 30],
            [20,30],
               [10]
	]
# truncate sequence
truncated= pad_sequences(sequences, maxlen=2, truncating='post')
print(truncated)
</pre>

