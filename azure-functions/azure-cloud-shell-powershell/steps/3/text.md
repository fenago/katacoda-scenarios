1. List all your subscriptions from Azure drive

```
PS Azure:\> dir
```

2. `cd` to your preferred subscription

```
PS Azure:\> cd MySubscriptionName
PS Azure:\MySubscriptionName>
```

3. View all your Azure resources under the current subscription.

Type `dir`{{copy}} to list multiple views of your Azure resources.

```
PS Azure:\MySubscriptionName> dir

    Directory: azure:\MySubscriptionName

Mode Name
---- ----
+    AllResources
+    ResourceGroups
+    StorageAccounts
+    VirtualMachines
+    WebApps
```
