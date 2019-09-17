
1. Expand the new taskCollection collection in Data Explorer, choose Documents, then select New Document.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/6/1.JPG)

2. Replace the contents of the new document with the following content, then choose Save.
    <pre class="file" data-target="clipboard">
    {
        "id": "task1",
        "category": "general",
        "description": "some task"
    }
    </pre>

3. Switch to the first browser tab that contains your function in the portal. Expand the function logs and verify that the new document has triggered the function. See that the task1 document ID value is written to the logs.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-cosmosdb/steps/6/3.png)

4. (Optional) Go back to your document, make a change, and click Update. Then, go back to the function logs and verify that the update has also triggered the function.