There's a simple web app in the frontend folder that consumes the HTTP API in the function app.

#### Update BaseURL
Open **index.html** in he vscode editor and update `apiBaseUrl` by going to line 116 as shown in the following screenshot.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-python-tensorflow/steps/14/baseurl.JPG)

Replace `http://localhost:7071` with the following url:
`https://[[HOST_SUBDOMAIN]]-7071-[[KATACODA_HOST]].environments.katacoda.com`{{copy}}

**Note:** All commands below will run in terminal 2.

Let's change to the frontend folder. Start an HTTP server with Python 3.6.

`cd functions-python-tensorflow-tutorial/frontend/`{{execute T2}}

`python3.6 -m http.server`{{execute T2}}
