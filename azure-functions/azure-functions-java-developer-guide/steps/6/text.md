#### Azure portal
In the Azure portal, use the Application Settings tab to add the JAVA_OPTS setting.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-java-developer-guide/steps/6/settings.JPG)

#### Azure CLI
You can use the az functionapp config appsettings set command to set JAVA_OPTS, as in the following example:

```az functionapp config appsettings set --name <APP_NAME> \
--resource-group <RESOURCE_GROUP> \
--settings "JAVA_OPTS=-Djava.awt.headless=true"```{{copy}}

This example enables headless mode. Replace <APP_NAME> with the name of your function app, and <RESOURCE_GROUP> with the resource group.

**Warning:**
In the Consumption plan, you must add the WEBSITE_USE_PLACEHOLDER setting with a value of 0.
This setting does increase the cold start times for Java functions.