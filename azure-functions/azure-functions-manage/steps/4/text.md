The az functionapp config appsettings list command returns the existing application settings, as in the following example:

```az functionapp config appsettings list --name <FUNCTION_APP_NAME> \
--resource-group <RESOURCE_GROUP_NAME>```{{copy}}

The az functionapp config appsettings set command adds or updates an application setting. The following example creates a setting with a key named **CUSTOM_FUNCTION_APP_SETTING** and a value of **12345**:

```az functionapp config appsettings set --name <FUNCTION_APP_NAME> \
--resource-group <RESOURCE_GROUP_NAME> \
--settings CUSTOM_FUNCTION_APP_SETTING=12345```{{copy}}