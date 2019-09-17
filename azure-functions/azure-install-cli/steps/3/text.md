There are two ways to install the Azure CLI with distributions that support apt: As an all-in-one script that runs the install commands for you, and instructions that you can run as a step-by-step process on your own.

#### Install with one command
We offer and maintain a script which runs all of the installation commands in one step. Run it by using curl and pipe directly to bash, or download the script to a file and inspect it before running.

**Important:** This script is only verified for Ubuntu 16.04+ and Debian 8+. It may not work on other distributions.

`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`{{copy}}

**Note:** We will install azure cli using manual commands in the next step. You can also install cli with the above script.