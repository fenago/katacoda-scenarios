We can select multiple columns using following code:

```
users.select("first_name", "last_name").show()
```

**Important:** You need to uncomment above line in `users.scala` using **vscode** editor before running program again.

We simply call the select method on users dataFrame and pass the required columns as arguments. Then we call the show method as usual.

`sbt "runMain training.users"`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_010.png)

Task is complete!

