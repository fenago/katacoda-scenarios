Create an Azure Functions project
In the start folder, use the Azure Functions Core Tools to initialize a Python function app.

console

Copy
func init --worker-runtime python
A function app can contain one or more Azure Functions. Open the start folder in an editor and examine the contents.

local.settings.json: Contains application settings used for local development
host.json: Contains settings for the Azure Functions host and extensions
requirements.txt: Contains Python packages required by this application