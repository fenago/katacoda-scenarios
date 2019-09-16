
In the Azure CLI, you use the az functionapp config appsettings set command to create and modify the app setting. The following command disables a function named QueueTrigger by creating an app setting named AzureWebJobs.QueueTrigger.Disabled set it to true.

`az functionapp config appsettings set --name <myFunctionApp> \
--resource-group <myResourceGroup> \
--settings AzureWebJobs.QueueTrigger.Disabled=true`{{copy}}

To **re-enable** the function, rerun the same command with a value of false.

`az functionapp config appsettings set --name <myFunctionApp> \
--resource-group <myResourceGroup> \
--settings AzureWebJobs.QueueTrigger.Disabled=false`{{copy}}
