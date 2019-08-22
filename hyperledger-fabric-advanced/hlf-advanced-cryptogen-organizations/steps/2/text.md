We will use the cryptogen tool to generate the cryptographic material (x509 certs and signing keys) for our various network entities. These certificates are representative of identities, and they allow for sign/verify authentication to take place as our entities communicate and transact.

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{execute}} the command to download and install cryptogen utility.

#### Validate
You can verify cryptogen is installed on your System by running `cryptogen version`{{execute}} command.

In the next steps, we will use **showtemplate** command provided using cryptogen utility.

