Before running this sample, you must have the following:

- Install Azure Functions Core Tools version.
- Install the Azure CLI.
- An active Azure subscription.

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?ref=microsoft.com&utm_source=microsoft.com&utm_medium=docs&utm_campaign=visualstudio) before you begin.

**Note:** Creating an azure account is optional, if you don't want to publish your function on Azure.

#### Install Core Tools on Linux
Run following commands to install Azure functions core tools.
`curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg`{{execute T1}}

`sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg`{{execute T1}}

`sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'`{{execute T1}}

`sudo apt-get update`{{execute T1}}

`yes | sudo apt-get install azure-functions-core-tools`{{execute T1}}

#### Azure CLI
Verify the Azure CLI version with the az command `az --version`{{execute T1}}