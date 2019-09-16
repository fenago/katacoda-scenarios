After the function app is created in Azure, you can use the func azure functionapp publish Core Tools command to deploy your project code to Azure. In these examples, replace <APP_NAME> with the name of your app from the previous step.

`func azure functionapp publish <APP_NAME>`{{copy}}


` the Invoke url value for your HttpTrigger, which you can now use to test your function in Azure. The URL contains a code query string value that is your function key. This key makes it difficult for others to call your HTTP trigger endpoint in Azure.
