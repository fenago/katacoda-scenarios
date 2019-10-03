The difference between UDF and UADF is that, the UDF performs the user-defined operation on one row at a time and returns the result for each row, while UADF performs the user-defined operation on group of rows on a column. An example of aggregate function is sum, count, average etc. The aggregate functions are followed by groupBy function most of the time.
Steps to implement User Defined function
User defined functions (UDF & UDAF) can be implemented by following these three steps.

- Writing a User Defined Function.
- Registering the User Defined Function in Spark Application.
- Using the User Defined Function in Spark SQL or in the DataFrame API.

