az login --service-principal -u <app-url> -p <password-or-cert> --tenant <tenant>
 **Important:**

If you want to avoid displaying your password on console and are using az login interactively, use the read -s command under bash.

read -sp "Azure password: " AZ_PASS && echo && az login --service-principal -u <app-url> -p $AZ_PASS --tenant <tenant>


Under PowerShell, use the Get-Credential cmdlet.

$AzCred = Get-Credential -UserName <app-url>
az login --service-principal -u $AzCred.UserName -p $AzCred.GetNetworkCredential().Password --tenant <tenant>