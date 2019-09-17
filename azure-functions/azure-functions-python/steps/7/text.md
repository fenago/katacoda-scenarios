**Note:** Command below will run in terminal 2 (It will open automatically on executing command). 

`curl http://localhost:7071/api/HttpTrigger?name=Azure`{{execute T2}}

The function should execute and return **Hello Azure!**. 

You can access python azure function by opening following link in the browser.
https://[[HOST_SUBDOMAIN]]-7071-[[KATACODA_HOST]].environments.katacoda.com/api/HttpTrigger?name=Azure


**Important:**
- Interface will keep switching back to terminal 1 because function app is running there after executing above command, you can manually switch by clicking `terminal 2`.
- Use `Ctrl` + `C` to stop the function app.