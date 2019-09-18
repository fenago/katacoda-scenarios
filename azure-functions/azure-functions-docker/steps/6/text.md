The following command starts the function app. The app runs using the same Azure Functions runtime that is in Azure. The start command varies, depending on your project language.
`npm install && npm start `{{execute}}

#### Typescript

You can access typescript azure function by opening following link in the browser. Update the query string `?name=<yourname>` and execute the request.

https://[[HOST_SUBDOMAIN]]-7071-[[KATACODA_HOST]].environments.katacoda.com/api/MyHttpTrigger?name={update}

Now that you have run your function locally, you can create the function app and other required resources in Azure.

**Important:** Use `Ctrl` + `C` to stop the function app.
