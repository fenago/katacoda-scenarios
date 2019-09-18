The function needs the connection string to connect to the default storage account. When you're publishing your custom image to a private container account, you should instead set these application settings as environment variables in the Dockerfile using the ENV instruction, or something similar.

In this case, `<storage_name>` is the name of the storage account you created. Get the connection string with the az storage account show-connection-string command. Add these application settings in the function app with the az functionapp config appsettings set command.

`storageConnectionString=$(az storage account show-connection-string \
--resource-group myResourceGroup --name <storage_name> \
--query connectionString --output tsv)`{{copy}}

`az functionapp config appsettings set --name <app_name> \
--resource-group myResourceGroup \
--settings AzureWebJobsDashboard=$storageConnectionString \
AzureWebJobsStorage=$storageConnectionString`{{copy}}

You can now test your functions running on Linux in Azure.