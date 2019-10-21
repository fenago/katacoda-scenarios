<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of TensorFlow library
import tensorflow as tf
# declare two symbolic floating-point scalars
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# create a simple symbolic expression using the add function
add = tf.add(a, b)
# bind 3.8 to 'a', 5.2 to 'b', and evaluate 'c'
sess = tf.Session()
binding = {a: 3.8, b: 5.2}
c = sess.run(add, feed_dict=binding)
print(c)
</pre>