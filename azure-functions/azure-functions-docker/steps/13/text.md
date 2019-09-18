The function app manages the execution of your functions in your hosting plan. Create a function app from a Docker Hub image by using the az functionapp create command.

In the following command, substitute a unique function app name where you see the `<app_name>` placeholder and the storage account name for `<storage_name>`. The `<app_name>` is used as the default DNS domain for the function app, and so the name needs to be unique across all apps in Azure. As before, `<docker-id>` is your Docker account name.

`az functionapp create --name <app_name> --storage-account  <storage_name>  --resource-group myResourceGroup \
--plan myPremiumPlan --deployment-container-image-name <docker-id>/mydockerimage:v1.0.0`{{copy}}

The deployment-container-image-name parameter indicates the image hosted on Docker Hub to use to create the function app.