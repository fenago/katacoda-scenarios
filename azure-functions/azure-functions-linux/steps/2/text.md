#### Install Core Tools
Run following command to install Azure functions core tools.
`npm install -g azure-functions-core-tools`{{execute T1}}

#### Azure CLI
Verify the Azure CLI version with the az command `az --version`{{execute T1}}

#### Install .Net Sdk
`wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb`{{execute T1}}

`dpkg -i packages-microsoft-prod.deb`{{execute T1}}

`apt-get install apt-transport-https`{{execute T1}}

`apt-get update`{{execute T1}}

`yes | apt-get install dotnet-sdk-2.2`{{execute T1}}
