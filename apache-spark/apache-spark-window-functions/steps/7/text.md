
**Step 6:** Let us now find the third highest salary from each department.

```
val rankedDS =  employeeDS.select($"*", ranked.as("rank"))
val second = rankedDS.where("rank = 3")
```

Let us now call the show method on our dataset.

```
second.show()
``` 


As you can see we have obtained the third highest salary of employees from each department. Since Admin Offices department had two emplyees with the same pay, they both are ranked as three.
