
Step 9: Let us now use of UDAF we wrote in this task. We have to call the toColumn method on our UDAF and give it a name using the name method as shown below.

val averageRating = averageTypedUDAF.toColumn.name("averageRating")

Let us now use the select method for the UDAF as shown below.

val avg = ds.select(averageRating)

Finally, let us call the show method and run the program.

avg.show()

The output which calculates average of all the ratings is as shown in the screenshot below.
 
 

This completes the Typed UADF task.

Task 6 is complete!


SUMMARY

In this chapter we have looked at User Defined Functions, which is the custom functions Spark. We have learned what UDFs and UDAFs are, why they are required and when they are used. We have also learned Scala programming concepts called function currying and partially applied functions
In the labs, we have had our hands on Scala function currying and partially applied functions. We have then used UDFs and two types of UDAFs to process data.
