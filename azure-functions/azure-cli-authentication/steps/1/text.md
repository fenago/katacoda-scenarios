The Azure command-line interface (CLI) is Microsoft's cross-platform command-line experience for managing Azure resources. The Azure CLI is designed to be easy to learn and get started with, but powerful enough to be a great tool for building custom automation to use Azure resources.

#### Install Azure CLI
Let's install azure cli using a script which runs all of the installation commands in one step. Run it by using curl and pipe directly to bash, or download the script to a file and inspect it before running.
`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`{{execute}}

You can verify that azure CLI was installed successfully by running:
`az --version`{{execute}}