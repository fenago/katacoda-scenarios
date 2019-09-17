Run the following command from the command line to create a function app project in the MyFunctionProj folder of the current local directory. A GitHub repo is also created in MyFunctionProj.
`func init MyFunctionProj`{{execute}}

When prompted, select a worker runtime **node** > **javascript** from the following language choices:

- **dotnet:** creates a .NET class library project (.csproj).
- **node:** creates a Node.js-based project. Choose either javascript or typescript.
- **python:** for a Python project, please instead complete Create an HTTP triggered function in Azure.
- **powershell:** for a PowerShell project, please instead complete Create your first PowerShell function in Azure.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-azure-cli/steps/3/1.JPG)
	
After the project is created, use the following command to navigate to the new MyFunctionProj project folder.
`cd MyFunctionProj`{{execute}}