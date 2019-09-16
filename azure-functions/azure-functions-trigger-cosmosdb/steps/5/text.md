Open a second instance of the Azure portal in a new tab in the browser.

On the left side of the portal, expand the icon bar, type cosmos in the search field, and select Azure Cosmos DB.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/5/1.JPG)

Choose your Azure Cosmos DB account, then select the Data Explorer.

In Collections, choose taskDatabase and select New Collection.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/5/4.png)

In Add Collection, use the settings shown in the table below the image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/5/5.png)

Setting	| Suggested value | Description
--- | --- | ---
`Database ID` | `Tasks` | The name for your new database. This must match the name defined in your function binding.
`Collection ID` | `Items` | The name for the new collection. This must match the name defined in your function binding.
`Storage capacity` | `Fixed (10 GB)` | Use the default value. This value is the storage capacity of the database.
`Throughput` | `400 RU` | `	Use the default value. If you want to reduce latency, you can scale up the throughput later.
`Partition key` | `/category` | A partition key that distributes data evenly to each partition. Selecting the correct partition key is important in creating a performant collection.

Click OK to create the Items collection. It may take a short time for the collection to get created.

After the collection specified in the function binding exists, you can test the function by adding documents to this new collection.