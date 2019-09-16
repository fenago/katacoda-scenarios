
Use apt-get upgrade to update the CLI package.
`sudo apt-get update && yes | sudo apt-get upgrade`{{execute}} 

**Note:** This command upgrades all of the installed packages on your system that have not had a dependency change. To upgrade the CLI only, use apt-get install.

`sudo apt-get update && sudo apt-get install --only-upgrade -y azure-cli`{{execute}} 