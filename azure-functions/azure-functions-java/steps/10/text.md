The deploy process to Azure Functions uses account credentials from the Azure CLI. Sign in with the Azure CLI before continuing.

#### Azure CLI
`az login`{{execute T1}}

Deploy your code into a new Function app using the azure-functions:deploy Maven target. This performs a Zip Deploy with Run From Package mode enabled.

`mvn azure-functions:deploy`{{execute T1}}

When the deploy is complete, you see the URL you can use to access your Azure function app:

```
[INFO] Successfully deployed Function App with package.
[INFO] Deleting deployment package from Azure Storage...
[INFO] Successfully deleted deployment package fabrikam-function-20170920120101928.20170920143621915.zip
[INFO] Successfully deployed Function App at https://fabrikam-function-20170920120101928.azurewebsites.net
[INFO] ------------------------------------------------------------------------
```

Test the function app running on Azure using cURL. You'll need to change the URL from the sample below to match the deployed URL for your own function app.

**Note:**
Make sure you set the Access rights to Anonymous. When you choose the default level of Function, you are required to present the function key in requests to access your function endpoint.

`curl -w "\n" https://fabrikam-function-<update-me>.azurewebsites.net/api/HttpTrigger-Java -d AzureFunctions`{{copy}}

Output

```
Hello AzureFunctions!
```
