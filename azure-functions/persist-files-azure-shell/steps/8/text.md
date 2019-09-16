You can unmount a file share that's mounted to Cloud Shell at any time. Since Cloud Shell requires a mounted file share to be used, you will be prompted to create and mount another file share on the next session.

1. Run `clouddrive unmount`.
2. Acknowledge and confirm prompts.

Your file share will continue to exist unless you delete it manually. Cloud Shell will no longer search for this file share on subsequent sessions. To view more details, run `clouddrive unmount -h`{{copy}} as shown here:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/7/1.png)

**Warning:** Although running this command will not delete any resources, manually deleting a resource group, storage account, or file share that's mapped to Cloud Shell erases your $Home directory disk image and any files in your file share. This action cannot be undone.