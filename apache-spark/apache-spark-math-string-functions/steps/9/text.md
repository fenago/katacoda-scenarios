

Step 4: Let us now use string functions to convert strings from lower case and upper case.

val upCase = quoteDS.select(upper($"value").as("upperCase"))
val lowCase = upCase.select(lower($"upperCase").as("lowerCase"))

Let us use the show method to display the datasets as shown below.

upCase.show()
lowCase.show()


 


