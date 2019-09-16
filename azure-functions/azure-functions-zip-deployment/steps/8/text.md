The following example uses **Publish-AzWebapp** upload the .zip file. Replace the placeholders `<group-name>`, `<app-name>`, and `<zip-file-path>`.

<pre class="file" data-target="clipboard">
Publish-AzWebapp -ResourceGroupName <group-name> -Name <app-name> -ArchivePath <zip-file-path>
</pre>


This request triggers push deployment from the uploaded .zip file.

To review the current and past deployments, run the following commands. Again, replace the <deployment-user>, <deployment-password>, and <app-name> placeholders.

<pre class="file" data-target="clipboard">
$username = "<deployment-user>"

$password = "<deployment-password>"

$apiUrl = "https://<app-name>.scm.azurewebsites.net/api/deployments"

$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $username, $password)))

$userAgent = "powershell/1.0"

Invoke-RestMethod -Uri $apiUrl -Headers @{Authorization=("Basic {0}" -f $base64AuthInfo)} -UserAgent $userAgent -Method GET
</pre>

