
#### Azure CLI
You can enable streaming logs by using the Azure CLI. Use the following commands to sign in, choose your subscription, and stream log files:

<pre class="file" data-target="clipboard">

az login
az account list
az account set --subscription <subscriptionNameOrId>

az webapp log tail --resource-group <RESOURCE_GROUP_NAME> --name <FUNCTION_APP_NAME>
</pre>

#### Azure PowerShell
You can enable streaming logs by using Azure PowerShell. For PowerShell, use the following commands to add your Azure account, choose your subscription, and stream log files:

<pre class="file" data-target="clipboard">

Add-AzAccount

Get-AzSubscription

Get-AzSubscription -SubscriptionName "<subscription name>" | Select-AzSubscription

Get-AzWebSiteLog -Name <FUNCTION_APP_NAME> -Tail
</pre>