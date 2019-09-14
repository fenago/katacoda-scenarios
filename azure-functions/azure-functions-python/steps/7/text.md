In the terminal with the Python virtual environment activated, start the function app.

`func start`{{execute T1}}

**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

`curl http://localhost:7071/api/classify?name=Azure`{{execute T2}}

The function should execute and return **Hello Azure!**. Interface will switch back to terminal 1 after executing above command, you can manually click terminal 2 to see response.

**Important:** Use `Ctrl` + `C` to stop the function app.