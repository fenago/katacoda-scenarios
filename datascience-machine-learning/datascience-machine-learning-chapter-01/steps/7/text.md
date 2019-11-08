
In other languages, it's pretty typical to have a bracket or a brace of some sort there to denote that I'm inside a for loop, an if block, or some sort of block of code, but in Python, that's all designated with whitespaces. Tab is actually important in telling Python what's in which block of code:

```
for number in listOfNumbers: 
    print number, 
    if (number % 2 == 0): 
        print ("is even")
    else: 
        print ("is odd") 
         
print ("Hooray! We're all done.")
```

You'll notice that within this for block, we have a tab of one within that entire block, and for every number in listOfNumbers we will execute all of this code that's tabbed in by one Tab stop. We'll print the number, and the comma just means that we're not going to do a new line afterwards. We'll print something else right after it, and if (number % 2 = 0), we'll say it's even. Otherwise, we'll say it's odd, and when we're done, we'll print out All done:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/7/3.png)
