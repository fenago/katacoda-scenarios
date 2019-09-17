Setting the consumption-plan-location parameter means that the function app is hosted in a Consumption hosting plan. In this serverless plan, resources are added dynamically as required by your functions and you only pay when functions are running. For more information, see Choose the correct hosting plan.

After the function app has been created, the Azure CLI shows information similar to the following example:
```
{
  "availabilityState": "Normal",
  "clientAffinityEnabled": true,
  "clientCertEnabled": false,
  "containerSize": 1536,
  "dailyMemoryTimeQuota": 0,
  "defaultHostName": "quickstart.azurewebsites.net",
  "enabled": true,
  "enabledHostNames": [
    "quickstart.azurewebsites.net",
    "quickstart.scm.azurewebsites.net"
  ],
   ....
    // Remaining output has been truncated for readability.
}
```


