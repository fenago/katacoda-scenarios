By default, your HTTP-triggered function is configured to accept any HTTP method. There is also a default URL of the form `http://<yourapp>.azurewebsites.net/api/<funcname>?code=<functionkey>`. In this section, you will modify the function to respond only to GET requests against `/api/hello` route instead.

- Navigate to your function in the Azure portal. Select Integrate in the left navigation.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/3/1.png)

- Use the HTTP trigger settings as specified in the table.

Field |	Sample value | Description
--- | --- | ---
`Allowed HTTP methods` | `Selected methods` | *Determines what HTTP methods may be used to invoke this function*
`Selected HTTP methods` | `GET Allows only` |	*selected HTTP methods to be used to invoke this function*
`Route template` |	`/hello` | *Determines what route is used to invoke this function*
`Authorization Level` |	`Anonymous` | *Optional: Makes your function accessible without an API key*

**Note:** that you did not include the /api base path prefix in the route template, as this is handled by a global setting.

- Click **Save**.