Create a resource group with the az group create. An Azure resource group is a logical container into which Azure resources like function apps, databases, and storage accounts are deployed and managed.

The following example creates a resource group named `myResourceGroup`.

If you are not using Cloud Shell, sign in first using `az login`{{execute}}.

`az group create --name myResourceGroup --location westeurope`{{execute}}

You generally create your resource group and the resources in a region near you.