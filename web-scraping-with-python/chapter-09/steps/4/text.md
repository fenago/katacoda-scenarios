re is a standard Python library that's used to deal with Regex. Every default Python installation contains the re library.

`python`{{execute}}

`>>>>` in code represents the use of the Python IDE. It accepts the code or instructions it's given and displays the output on the next line.

Let's begin by importing re using the Python IDE and listing its properties using the dir() function:

`import re`{{execute}}

`print(dir(re)) #listing features from re`{{execute}}

As we can see from the preceding output, there are various functions available in re. We will be using a few of these functions from a content extraction perspective, and we will explain the basics of Regex fundamentals by using examples such as the following:


```sentence = """Brief information about Jobs in Python. Programming and Scripting experience in some language (such as Python R, MATLAB, SAS, Mathematica, Java, C, C++, VB, JavaScript or FORTRAN) is expected. Participants should be comfortable with basic programming concepts like variables, loops, and functions."""```{{execute}}

sentence we declared previously contains brief information regarding Python jobs and job descriptions. We will be using this sentence to explain basic Regex functionalities. 

The `split()` function explodes the string and returns the list of individual words, which are separated by the space character by default. We can also split the string object using re.split(). In this case, split() accepts the Regex pattern to split the sentence, for example, re.split(r'\s+',sentence):


`splitSentence = sentence.split() #split sentence or re.split(r'\s',sentence)`{{execute}}

`print("Length of Sentence: ",len(sentence), '& splitSentence: ',len(splitSentence))`{{execute}}

```
Length of Sentence: 297 & splitSentence: 42
```

`print(splitSentence) #List of words obtained using split()`{{execute}}

```
['Brief', 'information', 'about', 'Jobs', 'in', 'Python.', 'Programming', 'and', 'Scripting', 'experience', 'in', 'some', 'language', '(such', 'as', 'Python', 'R,', 'MATLAB,', 'SAS,', 'Mathematica,', 'Java,', 'C,', 'C++,', 'VB,', 'JavaScript', 'or', 'FORTRAN)', 'is', 'expected.', 'Participants', 'should', 'be', 'comfortable', 'with', 'basic', 'programming', 'concepts', 'like', 'variables,', 'loops,', 'and', 'functions.']
```
