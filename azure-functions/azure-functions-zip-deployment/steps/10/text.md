
To enable your function app to run from a package, you just add a `WEBSITE_RUN_FROM_PACKAGE` setting to your function app settings. The WEBSITE_RUN_FROM_PACKAGE setting can have one of the following values:

Value |	Description
--- | ---
`1` |	*Recommended for function apps running on Windows. Run from a package file in the d:\home\data\SitePackages folder of your function app. If not deploying with zip deploy, this option requires the folder to also have a file named packagename.txt. This file contains only the name of the package file in folder, without any whitespace.*
`<url>` |	*Location of a specific package file you want to run. When using Blob storage, you should use a private container with a Shared Access Signature (SAS) to enable the Functions runtime to access to the package. You can use the Azure Storage Explorer to upload package files to your Blob storage account.*

The following shows a function app configured to run from a .zip file hosted in Azure Blob storage:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-zip deployment/steps/10/settings.JPG)

**Note:** Currently, only .zip package files are supported.