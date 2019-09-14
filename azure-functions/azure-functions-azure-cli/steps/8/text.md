Functions uses a general-purpose account in Azure Storage to maintain state and other information about your functions. Create a general-purpose storage account in the resource group you created by using the az storage account create command.

In the following command, substitute a globally unique storage account name where you see the <storage_name> placeholder. Storage account names must be between 3 and 24 characters in length and may contain numbers and lowercase letters only.

`az storage account create --name <storage_name> --location westeurope --resource-group myResourceGroup --sku Standard_LRS`{{copy}}