The following command starts the function app. The app runs using the same Azure Functions runtime that is in Azure. The start command varies, depending on your project language.
`func start --build`{{execute}}

**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

`curl http://localhost:7071/api/MyHttpTrigger?name=Azure`{{execute T2}}

The function should execute and return **Hello Azure!**. 

**Important:**
- Interface will keep switching back to terminal 1 because function app is running there after executing following command, you can manually switch by clicking `terminal 2`.
- Use `Ctrl` + `C` to stop the function app in terminal 1.

Now that you have run your function locally, you can create the function app and other required resources in Azure.
