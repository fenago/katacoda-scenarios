You must have an Azure Cosmos DB account that uses the SQL API before you create the trigger.

Sign in to the [Azure portal](https://portal.azure.com).

Select Create a **resource** > **Databases** > **Azure Cosmos DB**.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/2/create.JPG)


On the Create Azure Cosmos DB Account page, enter the basic settings for the new Azure Cosmos account.

Setting	| Value | Description
--- | --- | ---
`Subscription` | `Subscription name` | Select the Azure subscription that you want to use for this Azure Cosmos account.
`Resource Group` | `Resource group name` | Select a resource group, or select Create new, then enter a unique name for the new resource group.
`Account Name` | `Enter a unique name` | Enter a name to identify your Azure Cosmos account. Because documents.azure.com is appended to the ID that you provide to create your URI, use a unique ID.
`Location` | `Select the region closest to your users` | Select a geographic location to host your Azure Cosmos DB account. Use the location that is closest to your users to give them the fastest access to the data.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/2/review.JPG)

Select **Review + create**. You can skip the Network and Tags sections.

Review the account settings, and then select Create. It takes a few minutes to create the account. Wait for the portal page to display Your deployment is complete.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/2/deployment.JPG)

Select **Go to resource** to go to the Azure Cosmos DB account page.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/2/deployment.JPG)
