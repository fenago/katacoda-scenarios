In the start folder, use the Azure Functions Core Tools to initialize a Python function app.
`func init --worker-runtime python`{{execute T1}}

A function app can contain one or more Azure Functions. Open the `start` folder in **vscode** editor by clicking `IDE Editor` located next to the terminal and examine the contents.

- **local.settings.json:** Contains application settings used for local development
- **host.json:** Contains settings for the Azure Functions host and extensions
- **requirements.txt:** Contains Python packages required by this application