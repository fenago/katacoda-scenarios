To authenticate to servers or VMs using SSH, generate the public-private key pair in Cloud Shell and publish the public key to authorized_keys on the remote machine, such as /home/user/.ssh/authorized_keys.

**Note:** You can create SSH private-public keys using ssh-keygen and publish them to $env:USERPROFILE\.ssh in Cloud Shell.

#### Using SSH
Follow instructions here to create a new VM configuration using Azure PowerShell cmdlets. Before calling into New-AzVM to kick off the deployment, add SSH public key to the VM configuration. The newly created VM will contain the public key in the `~\.ssh\authorized_keys` location, thereby enabling credential-free SSH session to the VM.

<pre class="file" data-target="clipboard">

# Create VM config object - $vmConfig using instructions on linked page above

# Generate SSH keys in Cloud Shell
ssh-keygen -t rsa -b 2048 -f $HOME\.ssh\id_rsa 

# Ensure VM config is updated with SSH keys
$sshPublicKey = Get-Content "$HOME\.ssh\id_rsa.pub"
Add-AzVMSshPublicKey -VM $vmConfig -KeyData $sshPublicKey -Path "/home/azureuser/.ssh/authorized_keys"

# Create a virtual machine
New-AzVM -ResourceGroupName <yourResourceGroup> -Location <vmLocation> -VM $vmConfig

# SSH to the VM
ssh azureuser@MyVM.Domain.Com
</pre>