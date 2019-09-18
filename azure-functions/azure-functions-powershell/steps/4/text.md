
To add a function to your project, run the following command:
`func new`{{execute T1}}

Choose the **HTTP trigger** template, type `HttpTrigger`{{copy}} as the name for the function, then press Enter.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-powershell/steps/4/1.JPG)

A subfolder named `HttpTrigger` is created, which contains the following files:

- **function.json:** configuration file that defines the function, trigger, and other bindings. Review this file and see that the value for scriptFile points to the file containing the function, while the invocation trigger and bindings are defined in the bindings array.

- **run.ps1:** script file that is your HTTP triggered function. Review this script and see its content. HTTP data from the trigger is passed to this function using the req named binding parameter.

**Note:** You can have a look at the `run.ps1` file in **vscode** editor by clicking `IDE editor` tab and navigating to `MyFunctionProj` > `HttpTrigger` folder. Refresh vscode explorer if you don't see new folder.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-powershell/steps/4/2.JPG)
