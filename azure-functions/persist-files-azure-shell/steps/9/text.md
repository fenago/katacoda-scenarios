List clouddrive Azure file shares
The Get-CloudDrive cmdlet retrieves the Azure file share information currently mounted by the clouddrive in the Cloud Shell.
Running Get-CloudDrive

Unmount clouddrive
You can unmount an Azure file share that's mounted to Cloud Shell at any time. If the Azure file share has been removed, you will be prompted to create and mount a new Azure file share at the next session.

The Dismount-CloudDrive cmdlet unmounts an Azure file share from the current storage account. Dismounting the clouddrive terminates the current session. The user will be prompted to create and mount a new Azure file share during the next session. Running Dismount-CloudDrive