
**Step 8:** Let us finally look at lead and lag functions. The lead and lag functions are used to find how much the value of next row is leading or lagging when compared to the current row.

```
val leads = lead($"pay", 1, 0).over(window)
employeeDS.select($"*", leads.as("lead")).show()
```

The lead function takes three arguments. The first is the column name, second is the offset value, which determines the number of rows preceding/succeeding the current row and the third is the default to specify the default value if the offset is outside the scope of the window.

The following output is shown when we run the program.

 

Similarly, there is lag function which calculates the lag.

```
val lags = lag($"pay", 1, 0).over(window)
employeeDS.select($"*", lags.as("lag")).show()
```

The following output is shown when we run the program.

 

Task is complete!




