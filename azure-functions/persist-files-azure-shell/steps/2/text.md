When you use basic settings and select only a subscription, Cloud Shell creates three resources on your behalf in the supported region that's nearest to you:

- Resource group: `cloud-shell-storage-<region>`
- Storage account: `cs<uniqueGuid>`
- File share: `cs-<user>-<domain>-com-<uniqueGuid>`

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/2/mount.png)

The file share mounts as clouddrive in your $Home directory.

**Note:**
- This is a one-time action, and the file share mounts automatically in subsequent sessions. You might not get the prompt if you already have setup cloud shell.
- For security, each user should provision their own storage account. For role-based access control (RBAC), users must have contributor access or above at the storage account level.

The file share also contains a `5-GB` image that is created for you which automatically persists data in your $Home directory. This applies for both Bash and PowerShell.