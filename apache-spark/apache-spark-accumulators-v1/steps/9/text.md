**Step 3:** Let us now define a parse function which takes input record of type String as argument. The return type is an Either monadic collection which will either return String as Left object or a records case class as Right object.

Do not worry if you do not understand this as of now. All this makes sense when you look at the rest of the code.

```
def parse(record:String):Either[String, records]= {
```

Next, let us declare an array variable of type String and name it fields, so that we can split the incoming records based on a comma. This way, we can access each field indivudually and also we can know the number if fields each record has.

```
val fields: Array[String] = record.split(",")
```

 


