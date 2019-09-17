Back in the Azure portal, browse to your function expand the Logs at the bottom of the page and make sure that log streaming isn't paused.

In Storage Explorer, expand your storage account, Blob containers, and samples-workitems. Click Upload and then Upload files....

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/5/1.png)

In the Upload files dialog box, click the Files field. Browse to a file on your local computer, such as an image file, select it and click Open and then Upload.

Go back to your function logs and verify that the blob has been read.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/5/4.png)

**Note:** When your function app runs in the default Consumption plan, there may be a delay of up to several minutes between the blob being added or updated and the function being triggered. If you need low latency in your blob triggered functions, consider running your function app in an App Service plan.