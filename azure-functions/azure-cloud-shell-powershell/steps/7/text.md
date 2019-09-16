**Warning:**

Please refer to Troubleshooting remote management of Azure VMs.

Assuming you have a VM, **MyVM1**, let's use `Invoke-AzVMCommand` to invoke a PowerShell script block on the remote machine.

<pre class="file" data-target="clipboard">
Enable-AzVMPSRemoting -Name MyVM1 -ResourceGroupname MyResourceGroup

Invoke-AzVMCommand -Name MyVM1 -ResourceGroupName MyResourceGroup -Scriptblock {Get-ComputerInfo} -Credential (Get-Credential)
</pre>


You can also navigate to the VirtualMachines directory first and run Invoke-AzVMCommand as follows.

```
PS Azure:\> cd MySubscriptionName\ResourceGroups\MyResourceGroup\Microsoft.Compute\virtualMachines
PS Azure:\MySubscriptionName\ResourceGroups\MyResourceGroup\Microsoft.Compute\virtualMachines> Get-Item MyVM1 | Invoke-AzVMCommand -Scriptblock {Get-ComputerInfo} -Credential (Get-Credential)
```

You will see output similar to the following:

```
PSComputerName                         : 65.52.28.207
RunspaceId                             : 2c2b60da-f9b9-4f42-a282-93316cb06fe1
WindowsBuildLabEx                      : 14393.1066.amd64fre.rs1_release_sec.170327-1835
WindowsCurrentVersion                  : 6.3
WindowsEditionId                       : ServerDatacenter
WindowsInstallationType                : Server
WindowsProductId                       : 00376-40000-00000-AA947
WindowsProductName                     : Windows Server 2016 Datacenter
...
```
