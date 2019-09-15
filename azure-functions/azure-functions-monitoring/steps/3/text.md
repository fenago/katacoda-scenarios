The Application Settings tab maintains settings that are used by your function app. These settings are stored encrypted, and you must select Show values to see the values in the portal. You can also access application settings by using the Azure CLI.

Portal
To add a setting in the portal, select New application setting and add the new key-value pair.




To review the Application Insights resource being created, select it to expand the Application Insights window. You can change the New resource name or choose a different Location in an Azure geography where you want to store your data.

**Enable Application Insights while creating a function app**

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/3/create.JPG)

When you choose Create, an Application Insights resource is created with your function app, which has the APPINSIGHTS_INSTRUMENTATIONKEY set in application settings. Everything is ready to go.