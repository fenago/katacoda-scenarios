**Step 3:** Let us now write a function to parse the records and extract the fields we are interested in. For our program, we are only interested in userId and ratings fields. The function will split a line of input into a tuple of (userId, ratings).

Let us name the function parseRecords.

```
def parseRecords (rows: String): (Int, Float)={
```

This function takes each line of input as an argument and returns a tuple of an integer and a float.
