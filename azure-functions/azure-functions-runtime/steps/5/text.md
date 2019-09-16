You can also view and set the FUNCTIONS_EXTENSION_VERSION from the Azure CLI.

**Note:** Because other settings may be impacted by the runtime version, you should change the version in the portal. The portal automatically makes the other needed updates, such as Node.js version and runtime stack, when you change runtime versions.

Using the Azure CLI, view the current runtime version with the az functionapp config appsettings set command.

`az functionapp config appsettings list --name <function_app> --resource-group <my_resource_group>`{{copy}}

In this code, replace `<function_app>` with the name of your function app. Also replace `<my_resource_group>` with the name of the resource group for your function app.

You see the **FUNCTIONS_EXTENSION_VERSION** in the following output, which has been truncated for clarity:

```
[
  {
    "name": "FUNCTIONS_EXTENSION_VERSION",
    "slotSetting": false,
    "value": "~2"
  },
  {
    "name": "FUNCTIONS_WORKER_RUNTIME",
    "slotSetting": false,
    "value": "dotnet"
  },
  
  ...
  
  {
    "name": "WEBSITE_NODE_DEFAULT_VERSION",
    "slotSetting": false,
    "value": "8.11.1"
  }
]
```
