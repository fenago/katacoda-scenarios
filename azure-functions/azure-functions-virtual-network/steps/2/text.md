

Open the Azure portal. To do this, sign in to https://portal.azure.com with your Azure account.

**Prerequisites** It's important that you understand IP addressing and subnetting. You can start with this article that covers the basics of [addressing and subnetting](https://support.microsoft.com/en-us/help/164015/understanding-tcp-ip-addressing-and-subnetting-basics) 


First, you create a function app in the Premium plan. This plan provides serverless scale while supporting virtual network integration.

1. Go to the Azure portal.

2. Select + **Create a resource** on the left hand side, then choose Function app.

3. For **Hosting plan**, choose **App Service plan**, then select **App Service plan/Location**.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/2/1.png)

4. Select **Create new**, type an App Service plan name, choose a **Location** in a region near you or near other services your functions access, and then select Pricing tier.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/2/2.png)

5. Choose the **EP1 (elastic Premium)** plan, then select **Apply**.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/2/3.png)
