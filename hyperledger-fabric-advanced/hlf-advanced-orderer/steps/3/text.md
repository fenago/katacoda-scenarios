

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{copy}} the command to download and install configtxgen utility.

#### Validate
You can verify configtxgen is installed on your System by runningfollowing commands.

`configtxgen --version`{{copy}}

`cryptogen --version`{{copy}}

**Note**: configtxgen looks for at path `FABRIC_CFG_PATH` for `configtx.yaml`. If unset, the tool searches the current folder for the yaml file.


Now, move in the directory which contains the bash scripts. We also need to change permission to execute the script using **chmod**.
`cd ../orderer/simple-two-org && chmod 755 *.sh`{{copy}}