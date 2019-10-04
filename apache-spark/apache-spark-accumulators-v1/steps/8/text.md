**Step 1:** To implement a record parser, we shall create yet another Scala object and name it recordParser. Please follow the steps associated with creating a new Scala object. No imports are required for this object.

You should end up with the object as shown below.
 


**Step 2:** Let us first create a case class to store all our good records as shown below.

```
case class records(userId: Int, movieId: Int, rating: Double, timeStamp: String)
```
