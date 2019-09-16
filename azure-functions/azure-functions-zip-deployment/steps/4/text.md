Use the following deployment GET API to download the files from your <function_app> project:

`https://<function_app>.scm.azurewebsites.net/api/zip/site/wwwroot/`{{copy}}

Including `/site/wwwroot/` makes sure your zip file includes only the function app project files and not the entire site. If you are not already signed in to Azure, you will be asked to do so.

You can also download a `.zip` file from a GitHub repository. When you download a GitHub repository as a .zip file, GitHub adds an extra folder level for the branch. This extra folder level means that you can't deploy the .zip file directly as you downloaded it from GitHub. If you're using a GitHub repository to maintain your function app, you should use continuous integration to deploy your app.