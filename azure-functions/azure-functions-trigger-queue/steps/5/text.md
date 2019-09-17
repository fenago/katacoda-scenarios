1. Back in the Azure portal, browse to your function, expand the Logs at the bottom of the page, and make sure that log streaming isn't paused.

2. In Storage Explorer, expand your storage account, Queues, and myqueue-items, then click Add message.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/5/1.png)

3. Type your "Hello World!" message in Message text and click OK.

4. Wait for a few seconds, then go back to your function logs and verify that the new message has been read from the queue.

    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-queue/steps/5/4.png)

5. Back in Storage Explorer, click Refresh and verify that the message has been processed and is no longer in the queue.