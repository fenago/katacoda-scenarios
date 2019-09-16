After the function app is created in Azure, you can use the func azure functionapp publish Core Tools command to deploy your project code to Azure. In these examples, replace <APP_NAME> with the name of your app from the previous step.

`func azure functionapp publish <APP_NAME>`{{copy}}


You'll see output similar to the following, which has been truncated for readability:

```
Getting site publishing info...
...

Preparing archive...
Uploading content...
Upload completed successfully.
Deployment completed successfully.
Syncing triggers...
Functions in myfunctionapp:
    HttpTrigger - [httpTrigger]
        Invoke url: https://myfunctionapp.azurewebsites.net/api/httptrigger?code=cCr8sAxfBiow548FBDLS1....
```

` the Invoke url value for your HttpTrigger, which you can now use to test your function in Azure. The URL contains a code query string value that is your function key. This key makes it difficult for others to call your HTTP trigger endpoint in Azure.