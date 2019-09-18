Next, create a preconfigured VM that runs WordPress inside a virtual network (WordPress LEMP7 Max Performance by Jetware). A WordPress VM is used because of its low cost and convenience. This same scenario works with any resource in a virtual network, such as REST APIs, App Service Environments, and other Azure services.

- In the portal, choose + **Create a resource** on the left navigation pane, in the search field type `WordPress LEMP7 Max Performance`{{copy}}, and press Enter.

- Choose **Wordpress LEMP Max Performance** in the search results. Select a software plan of **Wordpress LEMP Max Performance for CentOS** as the Software Plan and select **Create**.

- In the **Basics** tab, use the VM settings as specified in the table below the image:
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/4/1.png)

Setting	| Suggested value | Description
--- | --- | ---
`Subscription` | `Your subscription` | The subscription under which your resources are created.
`Resource group` | `myResourceGroup` | Choose myResourceGroup, or the resource group you created with your function app. Using the same resource group for the function app, WordPress VM, and hosting plan makes it easier to clean up resources when you are done with this tutorial.
`Virtual machine name` | `VNET-Wordpress` | The VM name needs to be unique in the resource group
`Region` | `(Europe) West Europe` | Choose a region near you or near the functions that access the VM.
`Size` | `B1s` | Choose Change size and then select the B1s standard image, which has 1 vCPU and 1 GB of memory.
`Authentication type` | `Password` | To use password authentication, you must also specify a Username, a secure Password, and then Confirm password. For this tutorial, you won't need to sign in to the VM unless you need to troubleshoot.


- Choose the **Networking** tab and under Configure virtual networks select **Create new**.

- In **Create virtual network**, use the settings in the table below the image:
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/4/2.png)


Setting	| Suggested value | Description
--- | --- | ---
`Name` | `myResourceGroup-vnet` | You can use the default name generated for your virtual network.
`Address range` | `10.10.0.0/16` | Use a single address range for the virtual network.
`Subnet name` | `Tutorial-Net` | Name of the subnet.
`Address range (subnet)` | `	10.10.1.0/24` | The subnet size defines how many interfaces can be added to the subnet. This subnet is used by the WordPress site. A /24 subnet provides 254 host addresses.