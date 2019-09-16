Expand your new function app, then select the + button next to Functions, choose In-portal, and select Continue.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/2/4.png)

Choose WebHook + API and then select Create.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/2/5.png)

A function is created using a language-specific template for an HTTP triggered function.

Now, you can run the new function by sending an HTTP request.

#### Test the function
In your new function, click </> Get function URL at the top right, select default (Function key), and then click Copy.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/2/6.png)

Paste the function URL into your browser's address bar. Add the query string value &name=<yourname> to the end of this URL and press the Enter key on your keyboard to execute the request. You should see the response returned by the function displayed in the browser.

The following example shows the response in the browser:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/2/7.png)

The request URL includes a key that is required, by default, to access your function over HTTP.