

**Step 7:** Next, there are a couple of methods required to complete our implementation of custom accumulator. Ther are the isZero method and the copy method.

```
def isZero(): Boolean = {
  movieCount.isEmpty
}

def copy() = new CountByMovie
```

The isZero method returns a Boolean by checking if the accumulator value is zero or not. The copy method is used to create a new copy of our accumulator object.

These are the abstract methods which must be implemented in our code as they are defined in the base class. These methods will will be used while aggregating the value in the accumulator.


The error for the class name should be gone now. With this we have successfully implemented our Accumulator V2. We now have to use this custom accumulator in our main program.
