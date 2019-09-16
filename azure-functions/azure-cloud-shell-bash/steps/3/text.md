Create a resource group
Create a new resource group in WestUS named "MyRG".

Azure CLI

`

Try It
az group create --location westus --name MyRG


You will get following output:

```
{
  "id": "/subscriptions/<id>/resourceGroups/MyRG",
  "location": "westus",
  "managedBy": null,
  "name": "MyRG",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": null
}
```
