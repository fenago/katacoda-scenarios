In this scenario, you learn how Azure Functions allows you to build highly scalable APIs. Azure Functions comes with a collection of built-in HTTP triggers and bindings, which make it easy to author an endpoint in a variety of languages, including Node.JS, C#, and more. In this article, you will customize an HTTP trigger to handle specific actions in your API design. You will also prepare for growing your API by integrating it with Azure Functions Proxies and setting up mock APIs. All of this is accomplished on top of the Functions serverless compute environment, so you don't have to worry about scaling resources - you can just focus on your API logic.

#### Prerequisites

Open the Azure portal. To do this, sign in to https://portal.azure.com with your Azure account.

Select the Create a resource button found on the upper left-hand corner of the Azure portal, then select Compute > Function App.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/1/1.png)

Use the function app settings as specified in the table below the image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/1/2.png)

Select **Create** to provision and deploy the function app.

Select the Notification icon in the upper-right corner of the portal and watch for the Deployment succeeded message.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-serverless-api/steps/1/3.png)


Select **Go to resource** to view your new function app. You can also select Pin to dashboard. Pinning makes it easier to return to this function app resource from your dashboard.

Next, you create a function in the new function app.
