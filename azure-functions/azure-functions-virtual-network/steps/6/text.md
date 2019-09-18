With a WordPress site running in a VM in a virtual network, you can now connect your function app to that virtual network.

1. In your new function app, select **Platform features** > **Networking**.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/6/1.png)

2. Under **VNet Integration**, select **Click here to configure**.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/6/2.png)

3. On the virtual network integration page, select **Add VNet (preview)**.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/6/3.png)

4. In **Network Feature Status**, use the settings in the table below the image:
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/6/4.png)

Setting	| Suggested value | Description
--- | --- | ---
`Virtual Network` | `MyResourceGroup-vnet` | This virtual network is the one you created earlier.
`Subnet` | `Create New Subnet` | Create a subnet in the virtual network for your function app to use. VNet Integration must be configured to use an empty subnet. It doesn't matter that your functions use a different subnet than your VM. The virtual network automatically routes traffic between the two subnets.
`Subnet name` | `Function-Net` | `Name of the new subnet.
`Virtual network address block` | `10.10.0.0/16` | Choose the same address block used by the WordPress site. You should only have one address block defined.
`Address range` | `10.10.2.0/24` | The subnet size restricts the total number of instances that your Premium plan function app can scale out to. This example uses a /24 subnet with 254 available host addresses. This subnet is over-provisioned, but easy to calculate.

Select **OK** to add the subnet. Close the VNet Integration and Network Feature Status pages to return to your function app page.

The function app can now access the virtual network where the WordPress site is running. Next, you use Azure Functions Proxies to return a file from the WordPress site.