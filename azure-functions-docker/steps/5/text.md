The following command creates an HTTP-triggered function named MyHttpTrigger.
`func new --name MyHttpTrigger --template "HttpTrigger"`{{execute}}

When the command executes, you see something like the following output:

```
The function "MyHttpTrigger" was created successfully from the "HttpTrigger" template.
```

**Note:** You can have a look at the `index.js` file in **vscode** editor by clicking `IDE editor` tab and navigating to `MyFunctionProj` > `MyHttpTrigger` folder. Refresh vscode explorer if you don't see new folder.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-azure-cli/steps/5/1.JPG)

Use `Ctrl` + `C` to stop the function app.
