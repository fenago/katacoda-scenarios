Type dir under AllResources directory to view your Azure resources.

Azure PowerShell

Copy

Try It
PS Azure:\MySubscriptionName> dir AllResources
Explore resource groups
You can go to the ResourceGroups directory and inside a specific resource group you can find virtual machines.

PS Azure:\MySubscriptionName> cd ResourceGroups\MyResourceGroup1\Microsoft.Compute\virtualMachines

PS Azure:\MySubscriptionName\ResourceGroups\MyResourceGroup1\Microsoft.Compute\virtualMachines> dir


    Directory: Azure:\MySubscriptionName\ResourceGroups\MyResourceGroup1\Microsoft.Compute\virtualMachines


VMName    Location   ProvisioningState VMSize          OS            SKU             OSVersion AdminUserName  NetworkInterfaceName
------    --------   ----------------- ------          --            ---             --------- -------------  --------------------
TestVm1   westus     Succeeded         Standard_DS2_v2 WindowsServer 2016-Datacenter Latest    AdminUser      demo371
TestVm2   westus     Succeeded         Standard_DS1_v2 WindowsServer 2016-Datacenter Latest    AdminUser      demo271


 Note

You may notice that the second time when you type dir, the Cloud Shell is able to display the items much faster. This is because the child items are cached in memory for a better user experience. However, you can always use dir -Force to get fresh data.