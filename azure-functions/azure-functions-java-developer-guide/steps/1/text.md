The Azure Functions runtime supports `Java SE 8 LTS (zulu8.31.0.2-jre8.0.181-win_x64)`. This guide contains information about the intricacies of writing Azure Functions with Java.

A Java function is a public method, decorated with the annotation @FunctionName. This method defines the entry for a Java function, and must be unique in a particular package.

You should complete the Functions scenario to create your first function using Maven.

#### Programming model
The concepts of triggers and bindings are fundamental to Azure Functions. Triggers start the execution of your code. Bindings give you a way to pass data to and return data from a function, without having to write custom data access code.