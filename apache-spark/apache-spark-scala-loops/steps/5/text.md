**Step 2:** Let us now look at various ways we can print to the console. Using all the above variables we created in the previous step, let us concatenate them all in one string using '+' symbol as shown below.

`println("Printing to console using concatenation: " + name + num + longNum + decimal + decimalf + letter + lieDetector)`{{execute}}


It works but the output is not formatted correctly because we have not used spaces to separate the variables. We can add a white space as a string after each variable but it becomes a lengthy process if we have so many variables.


So, to overcome this we can substitute the variables within a string using an s prefix in the print statement before the double quotes as shown below. Each variable has a `prefix.

`println(s"Printing to console using variable substitution: $name $num $longNum $decimal $decimalf $letter $lieDetector")`{{execute}}
