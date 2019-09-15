Uninstall

Uninstall with apt-get remove:

bash

Copy
sudo apt-get remove -y azure-cli
If you don't plan to reinstall the CLI, remove the Azure CLI repository information:

bash

Copy
sudo rm /etc/apt/sources.list.d/azure-cli.list
Remove the signing key:

bash

Copy
sudo rm /etc/apt/trusted.gpg.d/microsoft.asc.gpg
Remove any unneeded packages:

bash

Copy
sudo apt autoremove