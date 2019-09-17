Edit the `src/main.../Function.java` source file in the generated project using **vscode** editor to alter the text returned by your Function app. Change this line:

```
return request.createResponseBuilder(HttpStatus.OK).body("Hello, " + name).build();
```

To the following:

<pre class="file" data-target="clipboard">
return request.createResponseBuilder(HttpStatus.OK).body("Hi, " + name).build();
</pre>

Save the changes. Run mvn clean package and run application by running azure-functions:run from the terminal as before. The function app will be updated :

`mvn clean package  && mvn azure-functions:run`{{execute T1}}

Run following in second terminal to get new response.
`curl -w "\n" http://localhost:7071/api/HttpTrigger-Java -d LocalFunction`{{execute T2}}

#### Output
You should get an updated output:
```
Hi, AzureFunctionsTest
```



