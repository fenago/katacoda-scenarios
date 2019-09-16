
You can use the deployment service REST APIs to deploy the .zip file to your app in Azure. To deploy, send a POST request to:
`https://<app_name>.scm.azurewebsites.net/api/zipdeploy`

The POST request must contain the `.zip` file in the message body. The deployment credentials for your app are provided in the request by using HTTP BASIC authentication.