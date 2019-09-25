In this step, we will setup VScode editor and clone respository.

Click **IDE Editor** tab to open Visual Studio and click _Terminal_ > _New Terminal_ to open the VSCode integrated terminal which wil be used to run commands.

Next, clone the following repository by copying & executing following command in the vscode terminal.
`git clone https://github.com/athertahir/kafka.git`{{execute}}

#### Permissions
Now, move in the directory which contains scripts to install kafka, copy and execute the command. We also need to change permission to execute the script using **chmod**.
`cd kafka/setup && chmod 755 *.sh`{{execute T1}} 

`./install.sh && ./start.sh && cd ../Chapter03/monedero`{{execute T1}} 

**Note:**
- The supplied commands in the next steps MUST be run from your `Chapter03/monedero` sub-directory of the **kafka** repository clone. 
- Final code was already cloned from github for this scenario. You can just understand the application code in the next steps and run it using the instructions.