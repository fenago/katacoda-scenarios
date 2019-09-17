Select the PowerShell environment from the drop-down and you will be in Azure drive (Azure:)

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-cloud-shell-powershell/steps/1/2.png)

#### List clouddrive Azure file shares
The `Get-CloudDrive`{{copy}} cmdlet retrieves the Azure file share information currently mounted by the clouddrive in the Cloud Shell.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/9/1.png)


#### Unmount clouddrive
You can unmount an Azure file share that's mounted to Cloud Shell at any time. If the Azure file share has been removed, you will be prompted to create and mount a new Azure file share at the next session.

The `Dismount-CloudDrive`{{copy}} cmdlet unmounts an Azure file share from the current storage account. Dismounting the clouddrive terminates the current session. The user will be prompted to create and mount a new Azure file share during the next session.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/9/2.png)
