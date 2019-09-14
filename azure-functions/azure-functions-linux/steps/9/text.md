You must have a function app to host the execution of your functions on Linux. The function app provides a serverless environment for executing your function code. It lets you group functions as a logic unit for easier management, deployment, and sharing of resources. Create a function app running on Linux by using the az functionapp create command.

In the following command, use a unique function app name where you see the <app_name> placeholder and the storage account name for <storage_name>. The <app_name> is also the default DNS domain for the function app. This name needs to be unique across all apps in Azure. You should also set the <language> runtime for your function app, from dotnet (C#), node (JavaScript/TypeScript), or python.

#### Azure CLI

`az functionapp create --resource-group myResourceGroup --consumption-plan-location westus --os-type Linux \
--name <app_name> --storage-account  <storage_name> --runtime <language>`{{copy}}

After the function app has been created, you see the following message:

```
Your serverless Linux function app 'myfunctionapp' has been successfully created.

To active this function app, publish your app content using Azure Functions Core Tools or the Azure portal.
Now, you can publish your project to the new function app in Azure.
```
