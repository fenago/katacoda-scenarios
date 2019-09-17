Expand your function app and click the + button next to Functions. If this is the first function in your function app, select In-portal then Continue. Otherwise, go to step three.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/4/1.JPG)

Choose **More templates** then Finish and view templates.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/4/2.JPG)


In the search field, type **cosmos** and then choose the Azure Cosmos DB trigger template.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/4/3.JPG)


If prompted, select Install to install the Azure Cosmos DB extension in the function app. After installation succeeds, select **Continue**.

Configure the new **trigger** with the settings as specified in the table below the image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/4/5.JPG)



Setting	| Suggested value | Description
--- | --- | ---
`Name` | `Default` | Use the default function name suggested by the template.
`Azure Cosmos DB account connection` | `New setting` | Select New, then choose your Subscription, the Database account you created earlier, and Select. This creates an application setting for your account connection. This setting is used by the binding to connection to the database.
`Collection name` | `Items` | Name of collection to be monitored.
`Create lease` | `collection if it doesn't exist` | Checked	The collection doesn't already exist, so create it.
`Database name` | `Tasks` | Name of database with the collection to be monitored.


Click Create to create your Azure Cosmos DB triggered function. After the function is created, the template-based function code is displayed.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/4/6.JPG)

