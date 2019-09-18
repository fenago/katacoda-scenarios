Select **OK** to create the virtual network.

Back in the **Networking** tab, choose None for **Public IP**.

Choose the **Management** tab, then in **Diagnostics storage account**, choose the Storage account you created with your function app.

Select **Review + create**. After validation completes, select Create. The VM create process takes a few minutes. The created VM can only access the virtual network.

After the VM is created, choose Go to resource to view the page for your new VM, then choose Networking under Settings.

Verify that there's no **Public IP**. Make a note the Private IP, which you use to connect to the VM from your function app.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/5/1.png)

You now have a WordPress site deployed entirely within your virtual network. This site isn't accessible from the public internet.