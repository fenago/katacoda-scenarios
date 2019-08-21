The configtxgen command allows users to create and inspect channel config related artifacts. The content of the generated artifacts is dictated by the contents of configtx.yaml.

Open `fabric-setup.sh` by clicking `HLFADV` > `setup` folder in vscode **Explorer** to view the contents of the bash script. Copy & execute `./fabric-setup.sh`{{copy}} the command to download and install configtxgen utility.

#### Validate
You can verify configtxgen is installed on your System by running `configtxgen --version`{{copy}} command.

**Note**: configtxgen looks for at path `FABRIC_CFG_PATH` for `configtx.yaml`. If unset, the tool searches the current folder for the yaml file.

In the next steps, we will use configtxgen utility for generating Channel Tx.

