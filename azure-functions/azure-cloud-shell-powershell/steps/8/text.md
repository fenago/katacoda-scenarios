You can use Enter-AzVM to interactively log into a VM running in Azure.

Azure PowerShell

`

Try It
PS Azure:\> Enter-AzVM -Name MyVM1 -ResourceGroupName MyResourceGroup -Credential (Get-Credential)
You can also navigate to the VirtualMachines directory first and run Enter-AzVM as follows

PS Azure:\MySubscriptionName\ResourceGroups\MyResourceGroup\Microsoft.Compute\virtualMachines> Get-Item MyVM1 | Enter-AzVM -Credential (Get-Credential)