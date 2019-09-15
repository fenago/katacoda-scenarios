Sign in with credentials on the command line
Provide your Azure user credentials on the command line.

 Note

This approach doesn't work with Microsoft accounts or accounts that have two-factor authentication enabled.

Azure CLI

Copy

Try It
az login -u <username> -p <password>
 Important

If you want to avoid displaying your password on console and are using az login interactively, use the read -s command under bash.

bash

Copy
read -sp "Azure password: " AZ_PASS && echo && az login -u <username> -p $AZ_PASS
Under PowerShell, use the Get-Credential cmdlet.

PowerShell

Copy
$AzCred = Get-Credential -UserName <username>
az login -u $AzCred.UserName -p $AzCred.GetNetworkCredential().Password