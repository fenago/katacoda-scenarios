The following example uses the cURL tool to deploy a .zip file. Replace the placeholders <username>, <password>, <zip_file_path>, and <app_name>. When prompted by cURL, type in the password.

bash

Copy
curl -X POST -u <deployment_user> --data-binary @"<zip_file_path>" https://<app_name>.scm.azurewebsites.net/api/zipdeploy
This request triggers push deployment from the uploaded .zip file. You can review the current and past deployments by using the https://<app_name>.scm.azurewebsites.net/api/deployments endpoint, as shown in the following cURL example. Again, replace <app_name> with the name of your app and <deployment_user> with the username of your deployment credentials.

bash

Copy
curl -u <deployment_user> https://<app_name>.scm.azurewebsites.net/api/deployments