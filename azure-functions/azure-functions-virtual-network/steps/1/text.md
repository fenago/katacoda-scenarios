In this scenario, you will learn how to use Azure Functions to connect to resources in an Azure virtual network. you'll create a function that has access to both the internet and to a VM running WordPress in virtual network.

- Create a function app in the Premium plan
- Deploy a WordPress site to VM in a virtual network
- Connect the function app to the virtual network
- Create a function proxy to access WordPress resources
- Request a WordPress file from inside the virtual network

**Note:** This scenario creates a function app in the Premium plan. This hosting plan is currently in preview. For more information, see Premium plan.

#### Topology
The following diagram shows the architecture of the solution that you create:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/1/1.png)

Functions running in the Premium plan have the same hosting capabilities as web apps in Azure App Service, which includes the VNet Integration feature.

