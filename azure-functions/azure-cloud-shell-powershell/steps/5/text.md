By entering into the StorageAccounts directory, you can easily navigate all your storage resources

```
PS Azure:\MySubscriptionName\StorageAccounts\MyStorageAccountName\Files> dir
```

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-cloud-shell-powershell/steps/5/1.JPG)


With the connection string, you can use the following command to mount the Azure Files share.

`net use <DesiredDriveLetter>: \\<MyStorageAccountName>.file.core.windows.net\<MyFileShareName> <AccountKey> /user:Azure\<MyStorageAccountName>`{{copy}}


You can also navigate the directories under the Azure Files share as follows:

```
PS Azure:\MySubscriptionName\StorageAccounts\MyStorageAccountName\Files> cd .\MyFileShare1\
PS Azure:\MySubscriptionName\StorageAccounts\MyStorageAccountName\Files\MyFileShare1> dir

Mode  Name
----  ----
+     TestFolder
.     hello.ps1
```
