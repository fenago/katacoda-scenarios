In this step, we will setup VScode editor and clone repository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

**Note:** You can also run all these commands in the katacoda terminal instead of vscode terminal.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/fenago/HLFADV.git`{{copy}}

#### Permissions
Now, move in the directory which contains scripts to install the Fabric Samples and binaries, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/setup && chmod 755 *.sh`{{copy}}

The supplied commands in the next steps MUST be run from your orderer sub-directory of the **HLFADV** repository clone.