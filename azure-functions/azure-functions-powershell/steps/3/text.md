A Functions project is the equivalent of a function app in Azure. It can have multiple functions that all share the same local and hosting configurations.

In the lab environment, run the following command, choosing **powershell** as your worker runtime. You can do it by typing **4** when prompted to select language.

`func init MyFunctionProj`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-powershell/steps/3/1.JPG)


A folder named MyFunctionProj is created, which contains the following three files:

- **local.settings.json:** is used to store app settings and connection strings when running locally. This file doesn't get published to Azure.
- **requirements.txt:**contains the list of packages to be installed on publishing to Azure.
- **host.json:**  contains global configuration options that affect all functions in a function app. This file does get published to Azure.

Navigate to the new MyFunctionProj folder:
`cd MyFunctionProj`{{execute}}

