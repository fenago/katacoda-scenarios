1. In your function, click Integrate, expand Documentation, and copy both Account name and Account key. You use these credentials to connect to the storage account. If you have already connected your storage account, skip to step 4.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/4/1.png)

2. Run the Microsoft Azure Storage Explorer tool, click the connect icon on the left, choose Use a storage account name and key, and click Next.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/4/2.png)

3. Enter the Account name and Account key from step 1, click Next and then Connect.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/4/3.png)

4. Expand the attached storage account, right-click Queues, click Create Queue, type myqueue-items, and then press enter.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/4/4.png)

Now that you have a storage queue, you can test the function by adding a message to the queue.