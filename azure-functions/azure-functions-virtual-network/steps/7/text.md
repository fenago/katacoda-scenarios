With VNet Integration enabled, you can create a proxy in your function app to forward requests to the VM running in the virtual network.

- In your function app, select **Proxies** > +, then use the proxy settings in the table below the image:
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-virtual-network/steps/7/1.png)

Setting | Suggested value | Description
--- | --- | ---
`Name` | `	Plant` | The name can be any value. It's used to identify the proxy.
`Route Template` | `/plant` | Route that maps to a VM resource.
`Backend URL` |  *Mentioned Below* | Replace `<YOUR_VM_IP>` with the IP address of your WordPress VM that you created earlier. This mapping returns a single file from the site.

**Backend URL:** `http://<YOUR_VM_IP>/wp-content/themes/twentyseventeen/assets/images/header.jpg`

- Select **Create** to add the proxy to your function app.