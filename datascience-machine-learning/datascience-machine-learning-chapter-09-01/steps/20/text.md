
First, it takes in our list of StringFields ready to convert it into LabeledPoints, where the label is the target value-was this person hired or not? 0 or 1-followed by an array that consists of all the other fields that we care about. So, this is how you create a LabeledPoint that the DecisionTree MLlib class can consume. So, you see in the above code that we're converting years of experience from a string to an integer value, and for all the yes/no fields, we're calling this binary function, that I defined up at the top of the code, but we haven't discussed yet:

```
def binary(YN): 
    if (YN == 'Y'): 
        return 1 
    else: 
        return 0 
```

All it does is convert the character yes to 1, otherwise it returns 0. So, Y will become 1, N will become 0. Similarly, I have a mapEducation function:

```
def mapEducation(degree): 
    if (degree == 'BS'): 
        return 1 
    elif (degree =='MS'): 
        return 2 
    elif (degree == 'PhD'): 
        return 3 
    else: 
        return 0 
```

As we discussed earlier, this simply converts different types of degrees to an ordinal numeric value in exactly the same way as our yes/no fields.

As a reminder, this is the line of code that sent us running through those functions:

```
trainingData = csvData.map(createLabeledPoints)
``` 

At this point, after mapping our RDD using that createLabeledPoints function, we now have a trainingData RDD, and this is exactly what MLlib wants for constructing a decision tree.
