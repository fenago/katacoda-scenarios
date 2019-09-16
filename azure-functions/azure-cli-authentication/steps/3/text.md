Provide your Azure user credentials on the command line.

**Note:** This approach doesn't work with Microsoft accounts or accounts that have two-factor authentication enabled.

`az login -u <username> -p <password>`{{copy}}

**Important:** If you want to avoid displaying your password on console and are using az login interactively, use the read -s command under bash.

`read -sp "Azure password: " AZ_PASS && echo && az login -u <username> -p $AZ_PASS`{{copy}}

#### Powershell
Under PowerShell, use the Get-Credential cmdlet.

```
$AzCred = Get-Credential -UserName <username>

az login -u $AzCred.UserName -p $AzCred.GetNetworkCredential().Password
```
