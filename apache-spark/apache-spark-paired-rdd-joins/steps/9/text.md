

**Step 4:** Finally, let us use the lookup(key) function to lookup value for a key in our joined RDD.


```
val look = joined.lookup(25)
println(mappedCol)
```

#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.joins"`{{execute}} 

The result is shown as an ArrayBuffer for all the values of the key.

Task is complete!




