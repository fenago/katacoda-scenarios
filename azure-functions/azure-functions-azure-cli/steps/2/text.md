#### Install Core Tools
Run following command to install Azure functions core tools.
`npm install -g azure-functions-core-tools`{{execute T1}}

#### Azure CLI

```apt-get update
yes | apt-get install ca-certificates curl apt-transport-https lsb-release gnupg

curl -sL https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor | \
    tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null

AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
    tee /etc/apt/sources.list.d/azure-cli.list

apt-get update
yes | apt-get install azure-cli```{{execute}}


Run the Azure CLI with the az command `az --version`{{execute T1}}