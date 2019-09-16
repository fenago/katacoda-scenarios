The .zip file that you use for push deployment must contain all of the files needed to run your function.

**Important:**

When you use .zip deployment, any files from an existing deployment that aren't found in the .zip file are deleted from your function app.

The code for all the functions in a specific function app is located in a root project folder that contains a host configuration file and one or more subfolders. Each subfolder contains the code for a separate function. The folder structure is shown in the following representation:


```
FunctionApp
 | - host.json
 | - Myfirstfunction
 | | - function.json
 | | - ...  
 | - mysecondfunction
 | | - function.json
 | | - ...  
 | - SharedCode
 | - bin
```

In version `2.x` of the Functions runtime, all functions in the function app must share the same language stack.

The `host.json` file contains runtime-specific configurations and is in the root folder of the function app. A bin folder contains packages and other library files that the function app requires. 

A function app includes all of the files and folders in the wwwroot directory. A .zip file deployment includes the contents of the wwwroot directory, but not the directory itself. When deploying a C# class library project, you must include the compiled library files and dependencies in a bin subfolder in your .zip package.

