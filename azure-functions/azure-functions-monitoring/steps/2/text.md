For a function app to send data to Application Insights, it needs to know the instrumentation key of an Application Insights resource. The key must be in an app setting named **APPINSIGHTS_INSTRUMENTATIONKEY **.

#### Function app in the portal
When you create your function app in the Azure portal, Application Insights integration is enabled by default. The Application Insights resource has the same name as your function app, and it's created either in the same region or in nearest region.