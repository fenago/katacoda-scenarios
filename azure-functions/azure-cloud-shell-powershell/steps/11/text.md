#### List available commands
Under Azure drive, type `Get-AzCommand`{{copy}} to get context-specific Azure commands.

Alternatively, you can always use Get-Command *az* -Module Az.* to find out the available Azure commands.

#### Install custom modules
You can run Install-Module to install modules from the PowerShell Gallery.

#### Get-Help
Type Get-Help to get information about PowerShell in Azure Cloud Shell.
`Get-Help`{{copy}}

For a specific command, you can still do Get-Help followed by a cmdlet.
`Get-Help Get-AzVM`{{copy}}