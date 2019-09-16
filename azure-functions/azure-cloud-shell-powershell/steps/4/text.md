Type `dir AllResources`{{copy}} to view your Azure resources.

```
PS Azure:\MySubscriptionName> dir AllResources
```

#### Explore resource groups
You can go to the ResourceGroups directory and inside a specific resource group you can find virtual machines.

`cd ResourceGroups\MyResourceGroup1\Microsoft.Compute\virtualMachines`{{copy}}

`dir`{{copy}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-cloud-shell-powershell/steps/4/1.JPG)

**Note:**
You may notice that the second time when you type dir, the Cloud Shell is able to display the items much faster. This is because the child items are cached in memory for a better user experience. However, you can always use dir -Force to get fresh data.