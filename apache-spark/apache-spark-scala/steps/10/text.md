**Either Monadic Collection**

The Either collection contains two objects called Left and Right object. The way how it works is, we can implement a condition in Either and return Left object in case of errors if the condition in Either is not satisfied and return Right object in case of the condition in Either is satisfied. Left for errors and Right for no errors is just a convention. You can use vice-versa as well.

**Try Monadic Collection**

The Try Monadic Collection is similar to that of Either which contains two objects namely Success and Failure objects. As the name suggests, the Success object returns the value if the condition in Try succeeds else the Failure object is returned with the exception.