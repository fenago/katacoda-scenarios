
Select the **Create a resource** button found on the upper left-hand corner of the Azure portal, then select **Compute** > **Function App**.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-timer/steps/2/create.JPG)

Use the function app settings as specified in the table below the image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-timer/steps/2/settings.JPG)

Setting	| Suggested value | Description
--- | --- | ---
`App name	` | `Globally unique name` | *Name that identifies your new function app.*
`Subscription` |	`Your subscription` | *The subscription under which this new function app is created.*
`Resource Group` |	`myResourceGroup` |	*Name for the new resource group in which to create your function app.*
`OS` |	`Windows` |	*The language options available depend on the OS of the function app. For example, Python requires Linux.*
`Hosting plan` |	`Consumption plan` |	*Hosting plan that defines how resources are allocated to your function app.*
`Location` |	`West Europe` |	*Choose a region near you or near other services your functions access.*
`Runtime stack` |	`Preferred language` |	*Choose a runtime that supports your favorite function programming language. Choose .NET for C# and F# functions.*
`Storage` |	`Globally unique name` |	*Create a storage account used by your function app.*
`Application Insights` |	`Default` |	*Creates an Application Insights resource of the same App name in the nearest supported region.*



#### Create function app
Select **Create** to provision and deploy the function app.

Select the Notification icon in the upper-right corner of the portal and watch for the Deployment succeeded message.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-timer/steps/2/success.JPG)