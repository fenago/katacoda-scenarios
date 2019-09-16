With Application Insights integration enabled, you can view telemetry data in the Monitor tab.

1. In the function app page, select a function that has run at least once after Application Insights was configured. Then select the Monitor tab.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/4/1.png)


2. Select **Refresh** periodically, until the list of function invocations appears.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/5/2.png)

    It can take up to `five minutes` for the list to appear while the telemetry client batches data for transmission to the server. (The delay doesn't apply to the Live Metrics Stream. That service connects to the Functions host when you load the page, so logs are streamed directly to the page.)

3. To see the logs for a particular function invocation, select the Date column link for that invocation.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/5/3.png)

    The logging output for that invocation appears in a new page.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/5/4.png)

You can see that both pages have a **Run in Application Insights** link to the Application Insights Analytics query that retrieves the data.
    
![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/5/5.png)

The following query is displayed. You can see that the invocation list is limited to the last 30 days. The list shows no more than 20 rows (where timestamp > ago(30d) | take 20). The invocation details list is for the last 30 days with no limit.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-monitoring/steps/5/6.png)
