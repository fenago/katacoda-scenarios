- Navigate back to your frontend function app in the portal.

- In the left-hand navigation, click the plus sign '+' next to "Proxies". Creating a proxy
![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/7/2.png)


Use proxy settings as specified in the table.

Field | Sample value | Description
--- | --- | ---
`Name` | `HelloProxy` | A friendly name used only for management
`Route template` | `/api/remotehello` | Determines what route is used to invoke this proxy
`Backend URL` | `https://%HELLO_HOST%/api/hello` | Specifies the endpoint to which the request should be proxied

**Note:** that Proxies does not provide the /api base path prefix, and this must be included in the route template.

The `%HELLO_HOST%` syntax will reference the app setting you created earlier. The resolved URL will point to your original function.

- Click **Create**.

You can try out your new proxy by copying the Proxy URL and testing it in the browser or with your favorite HTTP client.

- For an anonymous function use:
    * `https://YOURPROXYAPP.azurewebsites.net/api/remotehello?name="Proxies"`
- For a function with authorization use:
    * `https://YOURPROXYAPP.azurewebsites.net/api/remotehello?code=YOURCODE&name="Proxies"`
