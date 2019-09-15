
Update
Use apt-get upgrade to update the CLI package.

bash

Copy
sudo apt-get update && sudo apt-get upgrade
 Note

This command upgrades all of the installed packages on your system that have not had a dependency change. To upgrade the CLI only, use apt-get install.

bash

Copy
sudo apt-get update && sudo apt-get install --only-upgrade -y azure-cli