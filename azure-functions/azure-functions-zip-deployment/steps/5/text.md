You can use Azure CLI to trigger a push deployment. Push deploy a .zip file to your function app by using the az functionapp deployment source config-zip command. To use this command, you must use Azure CLI version 2.0.21 or later. To see what Azure CLI version you are using, use the az --version command.

In the following command, replace the <zip_file_path> placeholder with the path to the location of your .zip file. Also, replace <app_name> with the unique name of your function app.


az functionapp deployment source config-zip  -g myResourceGroup -n \
<app_name> --src <zip_file_path>

This command deploys project files from the downloaded .zip file to your function app in Azure. It then restarts the app. To view the list of deployments for this function app, you must use the REST APIs.

When you're using Azure CLI on your local computer, <zip_file_path> is the path to the .zip file on your computer. You can also run Azure CLI in Azure Cloud Shell. When you use Cloud Shell, you must first upload your deployment .zip file to the Azure Files account that's associated with your Cloud Shell. In that case, <zip_file_path> is the storage location that your Cloud Shell account uses.