The clouddrive directory syncs with the Azure portal storage blade. Use this blade to transfer local files to or from your file share. Updating files from within Cloud Shell is reflected in the file storage GUI when you refresh the blade.

Download files
List of local files

In the Azure portal, go to the mounted file share.
Select the target file.
Select the Download button.
Upload files
Local files to be uploaded

Go to your mounted file share.
Select the Upload button.
Select the file or files that you want to upload.
Confirm the upload.
You should now see the files that are accessible in your clouddrive directory in Cloud Shell.

Note: If you need to define a function in a file and call it from the PowerShell cmdlets, then the dot operator must be included. For example: . .\MyFunctions.ps1