In the terminal with the Python virtual environment activated, start the function app.

`func start`{{execute T1}}

**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

`curl http://localhost:7071/api/classify?name=Azure`{{execute T2}}

The function should execute and return **Hello Azure!**.

**Important:**
- Interface will keep switching back to terminal 1 because function app is running there after executing following command, you can manually switch by clicking `terminal 2`.
- Use `Ctrl` + `C` to stop the function app.
