We will use pandas to read our CSV in, and create a DataFrame object out of it. Let's go ahead and run our code, and we can use the head() function on the DataFrame to print out the first few lines and make sure that it looks like it makes sense.

```
df.head() 
```

Sure enough we have some valid data in the output:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-02/steps/18/1.jpg)

So, for each candidate ID, we have their years of past experience, whether or not they were employed, their number of previous employers, their highest level of education, whether they went to a top-tier school, and whether they did an internship; and finally here, in the Hired column, the answer - where we knew that we either extended a job offer to this person or not.
