The last concept I want to cover in our Python basics is looping, and we saw a couple of examples of this already, but let's just do another one:

```
for x in range(10):
 print (x),
The output of the previous code is as follows:

```
0 1 2 3 4 5 6 7 8 9
For example, we can use this range operator to automatically define a list of numbers in the range. So if we say for x in range(10), range 10 will produce a list of 0 through 9, and by saying for x in that list, we will iterate through every individual entry in that list and print it out. Again, the comma after the print statement says don't give me a new line, just keep on going. So the output of this ends up being all the elements of that list printed next to each other.

To do something a little bit more complicated, we'll do something similar, but this time we'll show how continue and break work. As in other languages, you can actually choose to skip the rest of the processing for a loop iteration, or actually stop the iteration of the loop prematurely:

```
for x in range(10):
    if (x is 1):
 continue
 if (x > 5):
    break
 print (x),
The output of the above code is as follows:

```
0 2 3 4 5
In this example, we'll go through the values 0 through 9, and if we hit on the number 1, we will continue before we print it out. We'll skip the number 1, basically, and if the number is greater than 5, we'll break the loop and stop the processing entirely. The output that we expect is that we will print out the numbers 0 through 5, unless it's 1, in which case, we'll skip number 1, and sure enough, that's what it does.
