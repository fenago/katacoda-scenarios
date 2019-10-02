Selecting multiple columns…

users.select("first_name”, “last_name").show()


We simply call the select method on users dataFrame and pass the required columns as arguments. Then we call the show method as usual.

We can load data to Spark using this same method for any format like json, parqet, ORC, Avro, etc. Please check the link in References section for more info.

Task 1 is complete!
