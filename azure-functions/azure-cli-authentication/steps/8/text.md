
Uninstall with apt-get remove:
`sudo apt-get remove -y azure-cli`{{execute}} 

If you don't plan to reinstall the CLI, remove the Azure CLI repository information:
`sudo rm /etc/apt/sources.list.d/azure-cli.list`{{execute}} 

Remove the signing key:
`sudo rm /etc/apt/trusted.gpg.d/microsoft.asc.gpg`{{execute}} 

Remove any unneeded packages:

`yes | sudo apt autoremove`{{execute}} 