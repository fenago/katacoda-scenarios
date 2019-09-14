A Functions project is the equivalent of a function app in Azure. It can have multiple functions that all share the same local and hosting configurations.

In the virtual environment, run the following command, choosing **python** as your worker runtime.

`func init MyFunctionProj`{{execute}}

A folder named MyFunctionProj is created, which contains the following three files:

- **local.settings.json:** is used to store app settings and connection strings when running locally. This file doesn't get published to Azure.
- **requirements.txt:**contains the list of packages to be installed on publishing to Azure.
- **host.json:**  contains global configuration options that affect all functions in a function app. This file does get published to Azure.

Navigate to the new MyFunctionProj folder:
`cd MyFunctionProj`{{execute}}

