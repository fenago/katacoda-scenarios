When you create a function app using the Azure CLI, Visual Studio, or Visual Studio Code, you must create the Application Insights resource. You can then add the instrumentation key from that resource as an application setting in your function app.

Functions makes it easy to add Application Insights integration to a function app from the Azure portal.


1. In the portal, select All services > Function Apps, select your function app, and then select the Application Insights banner at the top of the window
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/4/1.JPG)

2. Create an Application Insights resource by using the settings specified in the table below the image.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/4/2.JPG)


Setting	Suggested value	Description
--- | --- | ---
`Name` | `Unique app name` | *It's easiest to use the same name as your function app, which must be unique in your subscription.
`Location` | `West Europe` | *If possible, use the same region as your function app, or one that's close to that region.*

3. Select **OK**. The Application Insights resource is created in the same resource group and subscription as your function app. After the resource is created, close the Application Insights window.

4. Back in your function app, select Application settings, and then scroll down to Application settings. If you see a setting named **APPINSIGHTS_INSTRUMENTATIONKEY**, Application Insights integration is enabled for your function app running in Azure.

Early versions of Functions used built-in monitoring, which is no longer recommended. When enabling Application Insights integration for such a function app, you must also disable built-in logging.