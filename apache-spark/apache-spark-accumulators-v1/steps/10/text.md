**Step 4:** This is the step where we perform the error handling by using an if loop. The condition for if  will check if a record has 4 fields by using the length method.

If there are 4 fields in a record, we simply access each field based on its index and store it in the case class records using the Right object.. If there are less than 4 fields, we pass the record as is using the Left object.


```
if (fields.length == 4)
     {
      val UserId: Int = fields(0).toInt
      val movieId: Int = fields(1).toInt
      val rating: Double = fields(2).toDouble
      val timeStamp: String = fields(3)

	Right (records(userId: Int, movieId: Int, rating: Double, timeStamp: String))
    }
    else{
     	Left(record)
    }
  }
}
```

Please make sure you correctly enter all the opening and closing flower brackets if you encounter an error.

Let us now go back to the previous program counters and refer this object there.

Task is complete!

