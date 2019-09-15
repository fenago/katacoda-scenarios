You can update the FUNCTIONS_EXTENSION_VERSION setting in the function app with the az functionapp config appsettings set command.

Azure CLI

Copy

Try It
az functionapp config appsettings set --name <function_app> \
--resource-group <my_resource_group> \
--settings FUNCTIONS_EXTENSION_VERSION=<version>
Replace <function_app> with the name of your function app. Also replace <my_resource_group> with the name of the resource group for your function app. Also, replace <version> with a valid version of the 1.x runtime or ~2 for version 2.x.