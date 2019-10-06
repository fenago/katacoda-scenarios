**Step 5:** Finally, let us look at  substring and trim functons to extract a part of string and trim the whitespaces before and after the string respectively.

`val sub = quoteDS.select(substring($"value", 0, 2).as("firstWord"))`{{execute}}

`val trimmed = sub.select(trim($"firstWord"))`{{execute}}

Let us use the show method to display the datasets as shown below.

```sub.show()
trimmed.show()```{{execute}}

The substring function takes three arguments. The first is the column name from which the sub string to be extracted from. Second and third are the start and positions from which we want to extract the string from.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_050.png)

Here we have extracted the first word and space after it using the substring function. Since our fist word is only a letter, we start from 0 position and end at 2nd position which is the whitespace. Next, we use the trim function to trime the whitespaces before and after. Since there are no whitespaces before, the function will simply trim the whitespace after. You can also use rtrim function to trim only the whitespaces at the end and ltrim function to trim only the whitespaces at the beginning.

Task is complete!

