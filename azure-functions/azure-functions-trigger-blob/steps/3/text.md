1. Expand your function app and click the **+** button next to Functions. If this is the first function in your function app, select In-portal then Continue. Otherwise, go to step three.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/3/1.png)

2. Choose **More templates** then Finish and view templates.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/3/2.png)

3. In the search field, type blob and then choose the Blob trigger template.

4. If prompted, select **Install** to install the Azure Storage extension any dependencies in the function app. After installation succeeds, select **Continue**.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/3/4.png)

5. Use the settings as specified in the table below the image.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-blob/steps/3/5.png)


Setting | Suggested value | Description
--- | --- | ---
`Name` |	`Unique in your function app` |	Name of this blob triggered function.
`Path` |	`samples-workitems/{name}` |	Location in Blob storage being monitored. The file name of the blob is passed in the binding as the name parameter.
`Storage account connection` |	`AzureWebJobsStorage` |	You can use the storage account connection already being used by your function app, or create a new one.

6. Click **Create** to create your function.

Next, you connect to your Azure Storage account and create the samples-workitems container.
