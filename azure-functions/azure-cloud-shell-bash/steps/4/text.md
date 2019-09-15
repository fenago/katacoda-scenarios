
Create an Ubuntu VM in your new resource group. The Azure CLI will create SSH keys and set up the VM with them.

Azure CLI

Copy

Try It
az vm create -n myVM -g MyRG --image UbuntuLTS --generate-ssh-keys
 Note

Using --generate-ssh-keys instructs Azure CLI to create and set up public and private keys in your VM and $Home directory. By default keys are placed in Cloud Shell at /home/<user>/.ssh/id_rsa and /home/<user>/.ssh/id_rsa.pub. Your .ssh folder is persisted in your attached file share's 5-GB image used to persist $Home.

Your username on this VM will be your username used in Cloud Shell ($User@Azure:).