In this scenario, we will describes how to deploy your function app project files to Azure from a .zip (compressed) file. You learn how to do a push deployment, both by using Azure CLI and by using the REST APIs. Azure Functions Core Tools also uses these deployment APIs when publishing a local project to Azure.

The **.zip deployment API** takes the contents of a .zip file and extracts the contents into the wwwroot folder of your function app. This .zip file deployment uses the same Kudu service that powers continuous integration-based deployments, including:

- Deletion of files that were left over from earlier deployments.
- Deployment customization, including running deployment scripts.
- Deployment logs.
- Syncing function triggers in a Consumption plan function app.