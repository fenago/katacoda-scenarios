Linux hosting for custom Functions containers supported on Dedicated (App Service) plans and Premium plans. This tutorial uses a Premium plan, which can scale as needed. To learn more about hosting, see Azure Functions hosting plans comparison.

The following example creates a Premium plan named myPremiumPlan in the Elastic Premium 1 pricing tier (--sku EP1), in the West US region (-location WestUS), and in a Linux container **(--is-linux)**.

`az functionapp plan create --resource-group myResourceGroup --name myPremiumPlan \
--location WestUS --number-of-workers 1 --sku EP1 --is-linux`{{copy}}
