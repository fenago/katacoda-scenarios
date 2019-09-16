#### Prerequisites for manual mounting
You can update the file share that's associated with Cloud Shell by using the clouddrive mount command.

If you mount an existing file share, the storage accounts must be located in your select Cloud Shell region. Retrieve the location by running env and checking the `ACC_LOCATION`.

#### `clouddrive mount` command

**Note:** If you're mounting a new file share, a new user image is created for your $Home directory. Your previous $Home image is kept in your previous file share.

Run the clouddrive mount command with the following parameters:
`clouddrive mount -s mySubscription -g myRG -n storageAccountName -f fileShareName`{{copy}}

To view more details, run `clouddrive mount -h`, as shown here:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/persist-files-azure-shell/steps/7/1.png)