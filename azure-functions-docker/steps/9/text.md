You must have a function app to host the execution of your functions. The function app provides an environment for serverless execution of your function code. It lets you group functions as a logic unit for easier management, deployment, and sharing of resources. Create a function app by using the az functionapp create command.

In the following command, substitute a unique function app name where you see the <APP_NAME> placeholder and the storage account name for <STORAGE_NAME>. The <APP_NAME> is used as the default DNS domain for the function app, and so the name needs to be unique across all apps in Azure. You should also set the <language> runtime for your function app, from dotnet (C#) or node (JavaScript).

#### Azure CLI

`az functionapp create --resource-group myResourceGroup --consumption-plan-location westeurope \
--name <APP_NAME> --storage-account  <STORAGE_NAME> --runtime <language>`{{copy}}