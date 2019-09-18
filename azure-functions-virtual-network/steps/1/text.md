In this scenario, you learn how Azure Functions allows you to build highly scalable APIs. Azure Functions comes with a collection of built-in HTTP triggers and bindings, which make it easy to author an endpoint in a variety of languages, including Node.JS, C#, and more. In this article, you will customize an HTTP trigger to handle specific actions in your API design. You will also prepare for growing your API by integrating it with Azure Functions Proxies and setting up mock APIs. All of this is accomplished on top of the Functions serverless compute environment, so you don't have to worry about scaling resources - you can just focus on your API logic.

#### Prerequisites

Open the Azure portal. To do this, sign in to https://portal.azure.com with your Azure account.


It's important that you understand IP addressing and subnetting. You can start with this article that covers the basics of addressing and subnetting.


First, you create a function app in the Premium plan. This plan provides serverless scale while supporting virtual network integration.

1. Go to the Azure portal.

2. Select + Create a resource on the left hand side, then choose Function app.

3. For Hosting plan, choose App Service plan, then select App Service plan/Location.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/1/1.png)

4. Select Create new, type an App Service plan name, choose a Location in a region near you or near other services your functions access, and then select Pricing tier.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/1/2.png)

5. Choose the EP1 (elastic Premium) plan, then select Apply.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/1/3.png)
