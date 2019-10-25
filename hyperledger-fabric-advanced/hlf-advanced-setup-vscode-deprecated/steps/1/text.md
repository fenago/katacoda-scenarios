In this step, we will setup VScode editor and clone repository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/fenago/HLFADV.git`{{copy}}

#### Permissions
Now, move in the directory which contains scripts to install all the prerequisites and the Fabric Samples and binaries, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd HLFADV/setup && chmod 755 *.sh`{{copy}}

#### Install prerequisites
We have to install following on the platform(s) on which you’ll be developing blockchain applications and/or operating Hyperledger Fabric.

1. Golang
2. Docker
3. Docker Compose
4. JQ Utility
5. Fabric Binaries and Samples
6. CA Server Setup

**Note:**
The supplied commands in the next steps MUST be run from your setup sub-directory of the **HLFADV** repository clone.